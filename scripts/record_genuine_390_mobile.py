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
from PIL import Image

PORT = 9229
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
    temp_dir = r'C:\Users\ishti\AppData\Local\Temp\chrome_record_genuine_390_smooth'
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
    assertions = {}
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

            # Settle layout
            await asyncio.sleep(0.5)

            # Assert Initial Metrics
            metrics = await eval_js(ws, """
                ({
                    innerWidth: window.innerWidth,
                    innerHeight: window.innerHeight,
                    matchMedia900: window.matchMedia('(max-width: 900px)').matches,
                    matchMedia480: window.matchMedia('(max-width: 480px)').matches,
                    hasSimClass: document.documentElement.classList.contains('mobile-sim-active'),
                    activeElement: document.activeElement ? (document.activeElement.id || document.activeElement.tagName) : 'none'
                })
            """, msg_id=10)
            assertions['initial_metrics'] = metrics
            print("Initial Metrics:", metrics)

            async def sample(n=1, pause=0.08):
                nonlocal frame_counter
                for _ in range(n):
                    frame_counter += 1
                    im = await capture_frame(ws, msg_id=frame_counter)
                    frames.append(im)
                    if pause > 0:
                        await asyncio.sleep(pause)

            # Initial view (10 frames ~1s)
            await sample(10, pause=0.1)

            # Scroll down smoothly through mobile layout (25 frames)
            for y in range(0, 750, 30):
                await eval_js(ws, f"window.scrollTo(0, {y});", msg_id=20)
                await sample(1, pause=0.04)
            await sample(5, pause=0.1)

            # Scroll back to top (15 frames)
            for y in range(750, -1, -50):
                await eval_js(ws, f"window.scrollTo(0, {max(0, y)});", msg_id=21)
                await sample(1, pause=0.04)
            await sample(5, pause=0.1)

            # Open Mobile Off-Canvas Drawer (12 frames)
            await eval_js(ws, "document.getElementById('btnHamburger').click();", msg_id=30)
            for _ in range(6):
                await sample(1, pause=0.05)
            drawer_focus = await eval_js(ws, "document.activeElement.id", msg_id=31)
            assertions['drawer_focus'] = drawer_focus
            print("Drawer Focus:", drawer_focus)
            await sample(6, pause=0.1)

            # Cycle Tab focus inside drawer to Services, then Close button (10 frames)
            await eval_js(ws, "document.getElementById('drawServices').focus();", msg_id=32)
            await sample(5, pause=0.1)
            await eval_js(ws, "document.getElementById('drawerCloseBtn').focus();", msg_id=33)
            await sample(5, pause=0.1)

            # Close drawer
            await eval_js(ws, "document.getElementById('drawerCloseBtn').click();", msg_id=34)
            for _ in range(6):
                await sample(1, pause=0.05)
            await sample(4, pause=0.1)

            # Concept Tabs interaction (12 frames)
            for tab_id in ['tabAngle2', 'tabAngle3', 'tabAngle1']:
                await eval_js(ws, f"document.getElementById('{tab_id}').click();", msg_id=40)
                await sample(4, pause=0.1)

            # Open Consultation Modal via Header CTA (10 frames)
            await eval_js(ws, "document.getElementById('btnHeaderConsult').click();", msg_id=50)
            for _ in range(5):
                await sample(1, pause=0.06)
            modal_initial_focus = await eval_js(ws, "document.activeElement.id", msg_id=51)
            assertions['modal_initial_focus'] = modal_initial_focus
            print("Modal Initial Focus:", modal_initial_focus)
            await sample(5, pause=0.1)

            # Test Empty Form Validation (10 frames)
            await eval_js(ws, "document.getElementById('btnSubmitEnquiry').click();", msg_id=60)
            await asyncio.sleep(0.1)
            has_error_summary = await eval_js(ws, "!document.getElementById('errorSummaryBanner').classList.contains('hidden')", msg_id=61)
            assertions['empty_error_summary'] = has_error_summary
            print("Empty Error Summary Shown:", has_error_summary)
            await sample(10, pause=0.1)

            # Test Invalid Phone Input (10 frames)
            await eval_js(ws, """
                document.getElementById('inputName').value = 'তানভীর আহমেদ';
                document.getElementById('inputPhone').value = '01711abcxyz';
                document.getElementById('inputArea').value = 'ধানমন্ডি, ঢাকা';
                document.getElementById('selectType').value = 'residential_full';
                document.getElementById('btnSubmitEnquiry').click();
            """, msg_id=70)
            await asyncio.sleep(0.1)
            phone_invalid_err = await eval_js(ws, "!document.getElementById('errPhone').classList.contains('hidden')", msg_id=71)
            assertions['phone_invalid_err'] = phone_invalid_err
            print("Phone Invalid Error Shown:", phone_invalid_err)
            await sample(10, pause=0.1)

            # Enter Valid Bengali Form Data (10 frames)
            await eval_js(ws, """
                document.getElementById('inputName').value = 'তানভীর আহমেদ';
                document.getElementById('inputPhone').value = '০১৭১১০০০০০০';
                document.getElementById('inputArea').value = 'ধানমন্ডি, ঢাকা';
                document.getElementById('selectType').value = 'residential_full';
                document.getElementById('inputNotes').value = 'ধানমন্ডিতে ২৫০০ বর্গফুটের ডুপ্লেক্স অ্যাপার্টমেন্টের জন্য আধুনিক ইন্টেরিয়র আর্কিটেকচার সেবা প্রয়োজন।';
            """, msg_id=80)
            await sample(10, pause=0.1)

            # Submit Valid Form -> stateSubmitting Focus Check (10 frames)
            await eval_js(ws, "document.getElementById('btnSubmitEnquiry').click();", msg_id=90)
            await asyncio.sleep(0.1)
            submitting_focus = await eval_js(ws, "document.activeElement.id", msg_id=91)
            assertions['submitting_focus'] = submitting_focus
            print("Submitting Focus:", submitting_focus)
            await sample(8, pause=0.1)

            # Settle receipt state (12 frames)
            await asyncio.sleep(0.4)
            receipt_focus = await eval_js(ws, "document.activeElement.id", msg_id=100)
            assertions['receipt_focus'] = receipt_focus
            print("Receipt Focus:", receipt_focus)
            await sample(12, pause=0.1)

            # Click 'New Enquiry' -> Focus Restoration to inputName Check (10 frames)
            await eval_js(ws, "document.getElementById('btnNewEnquiry').click();", msg_id=110)
            await asyncio.sleep(0.15)
            new_enquiry_focus = await eval_js(ws, "document.activeElement.id", msg_id=111)
            assertions['new_enquiry_focus'] = new_enquiry_focus
            print("New Enquiry Focus Restored to:", new_enquiry_focus)
            await sample(10, pause=0.1)

            # Close modal via close button
            await eval_js(ws, "document.getElementById('modalCloseBtn').click();", msg_id=120)
            await sample(6, pause=0.08)

            # Switch Language to English (8 frames)
            await eval_js(ws, "document.getElementById('langToggle').click();", msg_id=130)
            await sample(8, pause=0.1)
            current_lang = await eval_js(ws, "currentLang", msg_id=131)
            assertions['current_lang'] = current_lang
            print("Current Lang:", current_lang)

            # Open English Drawer (8 frames)
            await eval_js(ws, "document.getElementById('btnHamburger').click();", msg_id=140)
            await sample(8, pause=0.1)
            await eval_js(ws, "document.getElementById('drawerCloseBtn').click();", msg_id=141)
            await sample(5, pause=0.08)

            # Offline Simulation State Check (10 frames)
            await eval_js(ws, "toggleOfflineModal();", msg_id=150)
            await asyncio.sleep(0.15)
            offline_focus = await eval_js(ws, "document.activeElement.id", msg_id=151)
            assertions['offline_focus'] = offline_focus
            print("Offline State Focus:", offline_focus)
            await sample(10, pause=0.1)
            await eval_js(ws, "document.getElementById('btnRetryOffline').click();", msg_id=152)
            await sample(6, pause=0.08)
            await eval_js(ws, "closeModal();", msg_id=153)
            await sample(4, pause=0.08)

            # Reduced Motion Tests: Media Query vs Manual Toggle
            await call_cdp(ws, 'Emulation.setEmulatedMedia', {
                'features': [{'name': 'prefers-reduced-motion', 'value': 'reduce'}]
            }, msg_id=160)
            mq_reduced = await eval_js(ws, "window.matchMedia('(prefers-reduced-motion: reduce)').matches", msg_id=161)
            assertions['prefers_reduced_motion_mq'] = mq_reduced
            print("Prefers Reduced Motion MQ:", mq_reduced)

            await eval_js(ws, "toggleReducedMotion();", msg_id=162)
            manual_reduced = await eval_js(ws, "document.documentElement.classList.contains('reduced-motion')", msg_id=163)
            assertions['manual_reduced_motion_class'] = manual_reduced
            print("Manual Reduced Motion Class:", manual_reduced)
            await sample(8, pause=0.1)

            # Final state
            await eval_js(ws, "resetForm();", msg_id=170)
            await sample(5, pause=0.1)

    finally:
        proc.terminate()

    print(f"Captured total {len(frames)} distinct frames. Dimensions: {frames[0].size}")

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
    print(f"Saved animated WebP to {out_proto} and {out_figma}")
    print(f"File Size: {proto_size} bytes, Frames: {len(frames)}, Dimensions: {frames[0].size}")

    report_path = r'C:\Nihal\Az_Works\FlowGrid\docs\genuine_390_verification_assertions.json'
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({
            'frames': len(frames),
            'size_bytes': proto_size,
            'dimensions': list(frames[0].size),
            'assertions': assertions
        }, f, indent=2, ensure_ascii=False)
    print(f"Saved assertions to {report_path}")

asyncio.run(run_journey())
