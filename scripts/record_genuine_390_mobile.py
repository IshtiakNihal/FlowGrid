import asyncio
import websockets
import json
import urllib.request
import subprocess
import time
import os
import io
import base64
import shutil
import hashlib
from PIL import Image

PORT = 9235
CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
TARGET_URL = 'file:///C:/Nihal/Az_Works/FlowGrid/prototype/index.html'

async def call_cdp(ws, method, params=None, msg_id=1):
    payload = {'id': msg_id, 'method': method}
    if params:
        payload['params'] = params
    await ws.send(json.dumps(payload))
    while True:
        resp = json.loads(await ws.recv())
        if resp.get('id') == msg_id:
            return resp

async def eval_js(ws, expr, msg_id=100):
    res = await call_cdp(ws, 'Runtime.evaluate', {'expression': expr, 'returnByValue': True}, msg_id=msg_id)
    return res.get('result', {}).get('result', {}).get('value')

async def capture_frame(ws, msg_id=200):
    res = await call_cdp(ws, 'Page.captureScreenshot', {'format': 'png'}, msg_id=msg_id)
    b64_data = res['result']['data']
    raw_bytes = base64.b64decode(b64_data)
    im = Image.open(io.BytesIO(raw_bytes))
    return im

async def run_journey():
    # 0. Compute SHA-256 of the exact prototype being tested
    proto_file = r'C:\Nihal\Az_Works\FlowGrid\prototype\index.html'
    with open(proto_file, 'rb') as f:
        tested_html_sha256 = hashlib.sha256(f.read()).hexdigest()
    print(f"Tested prototype/index.html SHA-256: {tested_html_sha256}")

    temp_dir = r'C:\Users\ishti\AppData\Local\Temp\chrome_record_genuine_390_v4'
    os.makedirs(temp_dir, exist_ok=True)
    cmd = [
        CHROME_PATH,
        '--headless=new',
        f'--remote-debugging-port={PORT}',
        f'--user-data-dir={temp_dir}',
        '--hide-scrollbars',
        TARGET_URL
    ]
    proc = subprocess.Popen(cmd)
    frames = []
    assertions = {
        'tested_html_path': 'prototype/index.html',
        'tested_html_sha256': tested_html_sha256,
        'target_viewport': {'width': 390, 'height': 844}
    }
    frame_counter = 1000

    try:
        await asyncio.sleep(2.5)
        req = urllib.request.urlopen(f'http://localhost:{PORT}/json')
        targets = json.loads(req.read())
        target = next(t for t in targets if 'prototype/index.html' in t.get('url', ''))
        ws_url = target['webSocketDebuggerUrl']
        print(f"Connected to CDP at {ws_url}")

        async with websockets.connect(ws_url, max_size=50_000_000) as ws:
            # 1. Enable domains
            await call_cdp(ws, 'Page.enable', msg_id=1)
            await call_cdp(ws, 'DOM.enable', msg_id=2)
            await call_cdp(ws, 'Runtime.enable', msg_id=3)

            # 2. Set genuine 390x844 mobile viewport override
            await call_cdp(ws, 'Emulation.setDeviceMetricsOverride', {
                'width': 390,
                'height': 844,
                'deviceScaleFactor': 1,
                'mobile': True,
                'fitWindow': False
            }, msg_id=4)
            await call_cdp(ws, 'Emulation.setTouchEmulationEnabled', {'enabled': True}, msg_id=5)

            await asyncio.sleep(0.5)

            async def sample(n=1, pause=0.08):
                nonlocal frame_counter
                for _ in range(n):
                    frame_counter += 1
                    im = await capture_frame(ws, msg_id=frame_counter)
                    frames.append(im)
                    if pause > 0:
                        await asyncio.sleep(pause)

            # --- STEP 1: Initial Bengali Mobile Viewport Metrics ---
            bn_metrics = await eval_js(ws, """
                ({
                    innerWidth: window.innerWidth,
                    innerHeight: window.innerHeight,
                    scrollWidth: document.documentElement.scrollWidth,
                    clientWidth: document.documentElement.clientWidth,
                    matchMedia900: window.matchMedia('(max-width: 900px)').matches,
                    matchMedia480: window.matchMedia('(max-width: 480px)').matches,
                    hasSimClass: document.documentElement.classList.contains('mobile-sim-active'),
                    activeElement: document.activeElement ? (document.activeElement.id || document.activeElement.tagName) : 'none'
                })
            """, msg_id=10)
            assertions['initial_bn_metrics'] = bn_metrics
            print("1. Initial BN Metrics:", bn_metrics)
            await sample(6, pause=0.1)

            # --- STEP 2: Smooth Mobile Scroll (Hero & Gallery) ---
            for y in range(0, 600, 40):
                await eval_js(ws, f"window.scrollTo(0, {y});", msg_id=20)
                await sample(1, pause=0.04)
            await sample(4, pause=0.1)
            for y in range(600, -1, -60):
                await eval_js(ws, f"window.scrollTo(0, {max(0, y)});", msg_id=21)
                await sample(1, pause=0.04)
            await sample(4, pause=0.1)

            # --- STEP 3: Mobile Off-Canvas Drawer Navigation & Keyboard Trapping ---
            await eval_js(ws, "document.getElementById('btnHamburger').click();", msg_id=30)
            await asyncio.sleep(0.25)
            drawer_focus = await eval_js(ws, "document.activeElement.id", msg_id=31)
            assertions['drawer_initial_focus'] = drawer_focus
            print("3. Drawer Initial Focus:", drawer_focus)
            await sample(6, pause=0.08)

            # Tab through drawer links
            drawer_tab_order = []
            for btn_id in ['drawConcept', 'drawServices', 'drawProcess', 'drawStudio', 'drawContact']:
                await eval_js(ws, f"document.getElementById('{btn_id}').focus();", msg_id=32)
                drawer_tab_order.append(await eval_js(ws, "document.activeElement.id", msg_id=33))
                await sample(1, pause=0.05)
            assertions['drawer_tab_sequence'] = drawer_tab_order

            # Shift+Tab wrap test: focus drawerCloseBtn then simulate Shift+Tab wrap to last control
            await eval_js(ws, """
                const evt = new KeyboardEvent('keydown', { key: 'Tab', shiftKey: true, bubbles: true });
                document.getElementById('drawerCloseBtn').focus();
                document.dispatchEvent(evt);
            """, msg_id=34)
            drawer_shift_wrap = await eval_js(ws, "document.activeElement.id", msg_id=35)
            assertions['drawer_shift_tab_wrap'] = drawer_shift_wrap
            print("   Drawer Shift+Tab Wrapped To:", drawer_shift_wrap)
            await sample(3, pause=0.08)

            # Escape key closes drawer and returns focus to hamburger button
            await eval_js(ws, """
                const escEvt = new KeyboardEvent('keydown', { key: 'Escape', bubbles: true });
                document.dispatchEvent(escEvt);
            """, msg_id=36)
            await asyncio.sleep(0.2)
            drawer_esc_focus = await eval_js(ws, "document.activeElement.id", msg_id=37)
            assertions['drawer_escape_focus_return'] = drawer_esc_focus
            print("   Drawer Escape Focus Returned To:", drawer_esc_focus)
            await sample(4, pause=0.08)

            # --- STEP 4: Concept Tab Switching ---
            for tab_id in ['tabAngle2', 'tabAngle3', 'tabAngle1']:
                await eval_js(ws, f"document.getElementById('{tab_id}').click();", msg_id=40)
                await sample(3, pause=0.1)

            # --- STEP 5: Consultation Modal Open & Focus ---
            await eval_js(ws, "document.getElementById('btnHeaderConsult').click();", msg_id=50)
            await asyncio.sleep(0.2)
            modal_initial_focus = await eval_js(ws, "document.activeElement.id", msg_id=51)
            assertions['modal_initial_focus'] = modal_initial_focus
            print("5. Modal Initial Focus:", modal_initial_focus)
            await sample(6, pause=0.1)

            # Modal Shift+Tab wrap test: from inputName with Shift+Tab, focus wraps to modalCloseBtn
            await eval_js(ws, """
                const evt = new KeyboardEvent('keydown', { key: 'Tab', shiftKey: true, bubbles: true });
                document.getElementById('inputName').focus();
                document.dispatchEvent(evt);
            """, msg_id=52)
            modal_shift_wrap = await eval_js(ws, "document.activeElement.id", msg_id=53)
            assertions['modal_shift_tab_wrap'] = modal_shift_wrap
            print("   Modal Shift+Tab Wrapped To:", modal_shift_wrap)
            await sample(3, pause=0.08)

            # --- STEP 6: Empty Form Validation ---
            await eval_js(ws, "document.getElementById('btnSubmitEnquiry').click();", msg_id=60)
            await asyncio.sleep(0.15)
            has_error_summary = await eval_js(ws, "!document.getElementById('errorSummaryBanner').classList.contains('hidden')", msg_id=61)
            err_banner_focus = await eval_js(ws, "document.activeElement.id", msg_id=62)
            assertions['empty_error_summary_visible'] = has_error_summary
            assertions['empty_error_summary_focused'] = err_banner_focus
            print("6. Empty Error Summary Visible:", has_error_summary, "Focused:", err_banner_focus)
            await sample(6, pause=0.1)

            # --- STEP 7: Invalid Phone Input Validation ---
            await eval_js(ws, """
                document.getElementById('inputName').value = 'তানভীর আহমেদ';
                document.getElementById('inputPhone').value = '01711abcxyz';
                document.getElementById('inputArea').value = 'ধানমন্ডি, ঢাকা';
                document.getElementById('selectType').value = 'residential_full';
                document.getElementById('btnSubmitEnquiry').click();
            """, msg_id=70)
            await asyncio.sleep(0.15)
            phone_invalid_err = await eval_js(ws, "!document.getElementById('errPhone').classList.contains('hidden')", msg_id=71)
            assertions['phone_invalid_err_shown'] = phone_invalid_err
            print("7. Phone Invalid Error Shown:", phone_invalid_err)
            await sample(6, pause=0.1)

            # --- STEP 8: Valid Form Entry & stateSubmitting Focus ---
            await eval_js(ws, """
                document.getElementById('inputPhone').value = '০১৭১১০০০০০০';
                document.getElementById('inputNotes').value = 'ধানমন্ডিতে ২৫০০ বর্গফুটের ডুপ্লেক্স অ্যাপার্টমেন্টের জন্য আধুনিক ইন্টেরিয়র আর্কিটেকচার সেবা প্রয়োজন।';
                document.getElementById('btnSubmitEnquiry').click();
            """, msg_id=80)
            await asyncio.sleep(0.15)
            submitting_focus = await eval_js(ws, "document.activeElement.id", msg_id=81)
            assertions['submitting_focus'] = submitting_focus
            print("8. Submitting Focus:", submitting_focus)
            await sample(6, pause=0.1)

            # Wait for submission timer to finish (900ms)
            await asyncio.sleep(0.9)

            # --- STEP 9: Receipt State Focus ---
            receipt_focus = await eval_js(ws, "document.activeElement.id", msg_id=90)
            assertions['receipt_focus'] = receipt_focus
            print("9. Receipt Focus:", receipt_focus)
            await sample(8, pause=0.1)

            # --- STEP 10: 'New Enquiry' Button Click & Focus Restoration ---
            await eval_js(ws, "document.getElementById('btnNewEnquiry').click();", msg_id=100)
            await asyncio.sleep(0.15)
            new_enquiry_focus = await eval_js(ws, "document.activeElement.id", msg_id=101)
            assertions['new_enquiry_focus_restored'] = new_enquiry_focus
            print("10. New Enquiry Focus Restored to:", new_enquiry_focus)
            await sample(6, pause=0.1)

            # Close modal via Escape key and verify focus returns to trigger
            await eval_js(ws, """
                const escEvt = new KeyboardEvent('keydown', { key: 'Escape', bubbles: true });
                document.dispatchEvent(escEvt);
            """, msg_id=110)
            await asyncio.sleep(0.15)
            modal_esc_focus = await eval_js(ws, "document.activeElement.id", msg_id=111)
            assertions['modal_escape_focus_return'] = modal_esc_focus
            print("   Modal Escape Focus Returned To:", modal_esc_focus)
            await sample(4, pause=0.08)

            # --- STEP 11: BILINGUAL SWITCH TO ENGLISH (BN -> EN) ---
            await eval_js(ws, "document.getElementById('langToggle').click();", msg_id=120)
            await asyncio.sleep(0.3)
            en_metrics = await eval_js(ws, """
                ({
                    currentLang: currentLang,
                    innerWidth: window.innerWidth,
                    innerHeight: window.innerHeight,
                    scrollWidth: document.documentElement.scrollWidth,
                    clientWidth: document.documentElement.clientWidth,
                    matchMedia900: window.matchMedia('(max-width: 900px)').matches,
                    hasSimClass: document.documentElement.classList.contains('mobile-sim-active'),
                    hamburgerRight: document.getElementById('btnHamburger').getBoundingClientRect().right,
                    headerWidth: document.querySelector('header').offsetWidth
                })
            """, msg_id=121)
            assertions['en_switch_metrics'] = en_metrics
            print("11. English Metrics (BN -> EN):", en_metrics)
            # Assert zero overflow in English
            assert en_metrics['innerWidth'] == 390, f"Expected 390, got {en_metrics['innerWidth']}"
            assert en_metrics['scrollWidth'] == 390, f"Expected scrollWidth 390, got {en_metrics['scrollWidth']}"
            assert en_metrics['hamburgerRight'] <= 390, f"Hamburger right exceeds 390: {en_metrics['hamburgerRight']}"
            await sample(8, pause=0.1)

            # --- STEP 12: English Mobile Drawer Navigation ---
            await eval_js(ws, "document.getElementById('btnHamburger').click();", msg_id=130)
            await asyncio.sleep(0.2)
            en_drawer_focus = await eval_js(ws, "document.activeElement.id", msg_id=131)
            assertions['en_drawer_focus'] = en_drawer_focus
            print("12. English Drawer Focus:", en_drawer_focus)
            await sample(6, pause=0.08)
            await eval_js(ws, "document.getElementById('drawerCloseBtn').click();", msg_id=132)
            await sample(4, pause=0.08)

            # --- STEP 13: English Consultation Modal & Receipt Viewport Check ---
            await eval_js(ws, "document.getElementById('btnHeaderConsult').click();", msg_id=140)
            await asyncio.sleep(0.2)
            en_modal_geom = await eval_js(ws, """
                ({
                    modalCardRight: document.getElementById('modalCard').getBoundingClientRect().right,
                    modalCardWidth: document.getElementById('modalCard').offsetWidth,
                    docScrollW: document.documentElement.scrollWidth
                })
            """, msg_id=141)
            assertions['en_modal_geometry'] = en_modal_geom
            print("13. English Modal Geometry:", en_modal_geom)
            await sample(6, pause=0.1)

            # Submit valid English form
            await eval_js(ws, """
                document.getElementById('inputName').value = 'Tanvir Ahmed';
                document.getElementById('inputPhone').value = '+880 1711 000000';
                document.getElementById('inputArea').value = 'Dhanmondi, Dhaka';
                document.getElementById('selectType').value = 'residential_full';
                document.getElementById('inputNotes').value = 'Modern interior architecture consultation required for duplex apartment.';
                document.getElementById('btnSubmitEnquiry').click();
            """, msg_id=150)
            await asyncio.sleep(0.15)
            assertions['en_submitting_focus'] = await eval_js(ws, "document.activeElement.id", msg_id=151)
            await sample(4, pause=0.1)
            await asyncio.sleep(0.9)

            # English Receipt State Check
            en_receipt_geom = await eval_js(ws, """
                ({
                    receiptWrapRight: document.querySelector('.receipt-wrap').getBoundingClientRect().right,
                    noticeRight: document.getElementById('receiptSimNotice').getBoundingClientRect().right,
                    docScrollW: document.documentElement.scrollWidth,
                    receiptFocus: document.activeElement.id
                })
            """, msg_id=160)
            assertions['en_receipt_geometry'] = en_receipt_geom
            print("   English Receipt Geometry:", en_receipt_geom)
            assert en_receipt_geom['docScrollW'] == 390
            assert en_receipt_geom['noticeRight'] <= 390
            await sample(8, pause=0.1)

            # Close English receipt modal
            await eval_js(ws, "document.getElementById('btnDone').click();", msg_id=170)
            await sample(4, pause=0.08)

            # --- STEP 14: English Offline Modal Demonstration ---
            await eval_js(ws, "toggleOfflineModal();", msg_id=180)
            await asyncio.sleep(0.2)
            en_offline_geom = await eval_js(ws, """
                ({
                    offlineBannerRight: document.querySelector('.offline-banner').getBoundingClientRect().right,
                    docScrollW: document.documentElement.scrollWidth,
                    focus: document.activeElement.id
                })
            """, msg_id=181)
            assertions['en_offline_geometry'] = en_offline_geom
            print("14. English Offline Geometry:", en_offline_geom)
            assert en_offline_geom['docScrollW'] == 390
            assert en_offline_geom['offlineBannerRight'] <= 390
            await sample(6, pause=0.1)
            await eval_js(ws, "closeModal();", msg_id=182)
            await sample(3, pause=0.08)

            # --- STEP 15: BILINGUAL SWITCH BACK TO BENGALI (EN -> BN) ---
            await eval_js(ws, "document.getElementById('langToggle').click();", msg_id=190)
            await asyncio.sleep(0.3)
            bn_return_metrics = await eval_js(ws, """
                ({
                    currentLang: currentLang,
                    innerWidth: window.innerWidth,
                    scrollWidth: document.documentElement.scrollWidth,
                    clientWidth: document.documentElement.clientWidth
                })
            """, msg_id=191)
            assertions['bn_return_metrics'] = bn_return_metrics
            print("15. Bengali Return Metrics (EN -> BN):", bn_return_metrics)
            assert bn_return_metrics['innerWidth'] == 390
            assert bn_return_metrics['scrollWidth'] == 390
            await sample(6, pause=0.1)

            # --- STEP 16: Reduced Motion Testing (Separated) ---
            # Test A: System Media Query Preference via CDP Emulation
            await call_cdp(ws, 'Emulation.setEmulatedMedia', {
                'features': [{'name': 'prefers-reduced-motion', 'value': 'reduce'}]
            }, msg_id=200)
            mq_reduced = await eval_js(ws, "window.matchMedia('(prefers-reduced-motion: reduce)').matches", msg_id=201)
            assertions['system_prefers_reduced_motion_mq'] = mq_reduced
            print("16. System Prefers Reduced Motion MQ:", mq_reduced)

            # Test B: Interactive Manual Toggle Button
            await eval_js(ws, "toggleReducedMotion();", msg_id=202)
            manual_reduced = await eval_js(ws, "document.documentElement.classList.contains('reduced-motion')", msg_id=203)
            assertions['manual_reduced_motion_class'] = manual_reduced
            print("    Manual Reduced Motion Class Toggle:", manual_reduced)
            await sample(6, pause=0.1)

            # Motion specification note (handoff distinction)
            assertions['motion_specifications_status'] = {
                'hero_reveal_600ms_wipe': 'Documented design handoff specification on Board 06 (not implemented prototype feature)',
                'project_expansion_360ms': 'Documented design handoff specification on Board 06 (not implemented prototype feature)'
            }

            # Final state reset
            await eval_js(ws, "resetForm();", msg_id=210)
            await sample(4, pause=0.1)

    finally:
        proc.terminate()

    print(f"\nCaptured total {len(frames)} distinct frames. Dimensions: {frames[0].size}")

    # Output paths
    out_proto = r'C:\Nihal\Az_Works\FlowGrid\prototype\prototype_enquiry_journey.webp'
    out_figma = r'C:\Nihal\Az_Works\FlowGrid\figma_exports\prototype_enquiry_journey.webp'

    # Save animated WebP with 100ms per frame
    frames[0].save(
        out_proto,
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0,
        quality=80,
        method=4
    )

    shutil.copyfile(out_proto, out_figma)

    proto_size = os.path.getsize(out_proto)
    with open(out_proto, 'rb') as f:
        recording_sha256 = hashlib.sha256(f.read()).hexdigest()

    im_saved = Image.open(out_proto)
    decoded_frames = im_saved.n_frames

    print(f"Saved animated WebP to {out_proto} and {out_figma}")
    print(f"File Size: {proto_size} bytes, Decoded Frames: {decoded_frames}, Captured Steps: {len(frames)}, Dimensions: {frames[0].size}")
    print(f"Recording SHA-256: {recording_sha256}")

    # Save comprehensive assertions report
    report_path = r'C:\Nihal\Az_Works\FlowGrid\docs\genuine_390_verification_assertions.json'
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({
            'recording': {
                'file_name': 'prototype_enquiry_journey.webp',
                'frames': decoded_frames,
                'decoded_frames': decoded_frames,
                'captured_steps': len(frames),
                'size_bytes': proto_size,
                'sha256': recording_sha256,
                'dimensions': list(frames[0].size)
            },
            'assertions': assertions
        }, f, indent=2, ensure_ascii=False)
    print(f"Saved assertions to {report_path}")

asyncio.run(run_journey())
