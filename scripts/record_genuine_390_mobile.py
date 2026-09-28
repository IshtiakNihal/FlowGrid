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
            if 'error' in resp:
                raise RuntimeError(f"CDP error in {method}: {resp['error']}")
            return resp

async def eval_js(ws, expr, msg_id=100):
    # Wrap in IIFE to prevent variable collisions across calls
    stripped = expr.strip()
    if not (stripped.startswith('(') and stripped.endswith(')')) and (';' in stripped or '\n' in stripped):
        wrapped = f"(() => {{\n{expr}\n}})()"
    else:
        wrapped = expr
    res = await call_cdp(ws, 'Runtime.evaluate', {
        'expression': wrapped,
        'returnByValue': True,
        'awaitPromise': True
    }, msg_id=msg_id)
    inner = res.get('result', {})
    if 'exceptionDetails' in inner:
        raise RuntimeError(f"JavaScript evaluation failed in:\n{expr}\nException: {inner['exceptionDetails']}")
    return inner.get('result', {}).get('value')

async def press_key(ws, key='Tab', shift=False, msg_id=500):
    modifiers = 8 if shift else 0  # 8 is Shift in CDP
    vk = 9 if key == 'Tab' else (27 if key == 'Escape' else 13)
    await call_cdp(ws, 'Input.dispatchKeyEvent', {
        'type': 'rawKeyDown',
        'key': key,
        'code': key,
        'windowsVirtualKeyCode': vk,
        'nativeVirtualKeyCode': vk,
        'modifiers': modifiers
    }, msg_id=msg_id)
    await call_cdp(ws, 'Input.dispatchKeyEvent', {
        'type': 'keyUp',
        'key': key,
        'code': key,
        'windowsVirtualKeyCode': vk,
        'nativeVirtualKeyCode': vk,
        'modifiers': modifiers
    }, msg_id=msg_id+1)
    await asyncio.sleep(0.08)

async def capture_frame(ws, msg_id=200):
    res = await call_cdp(ws, 'Page.captureScreenshot', {'format': 'png'}, msg_id=msg_id)
    b64_data = res['result']['data']
    raw_bytes = base64.b64decode(b64_data)
    im = Image.open(io.BytesIO(raw_bytes))
    return im

async def run_journey():
    # 0. Compute SHA-256 of the exact prototype being tested in binary mode
    proto_file = r'C:\Nihal\Az_Works\FlowGrid\prototype\index.html'
    with open(proto_file, 'rb') as f:
        tested_html_sha256 = hashlib.sha256(f.read()).hexdigest()
    print(f"Tested prototype/index.html SHA-256: {tested_html_sha256}")

    temp_dir = r'C:\Users\ishti\AppData\Local\Temp\chrome_record_genuine_390_v5'
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
                return {
                    innerWidth: window.innerWidth,
                    innerHeight: window.innerHeight,
                    scrollWidth: document.documentElement.scrollWidth,
                    clientWidth: document.documentElement.clientWidth,
                    matchMedia900: window.matchMedia('(max-width: 900px)').matches,
                    matchMedia480: window.matchMedia('(max-width: 480px)').matches,
                    hasSimClass: document.documentElement.classList.contains('mobile-sim-active'),
                    activeElement: document.activeElement ? (document.activeElement.id || document.activeElement.tagName) : 'none'
                };
            """, msg_id=10)
            assertions['initial_bn_metrics'] = bn_metrics
            print("1. Initial BN Metrics:", bn_metrics)
            assert bn_metrics['innerWidth'] == 390, f"Expected innerWidth 390, got {bn_metrics['innerWidth']}"
            assert bn_metrics['scrollWidth'] == 390, f"Expected scrollWidth 390, got {bn_metrics['scrollWidth']}"
            assert not bn_metrics['hasSimClass'], "Simulator class must be false"
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

            # --- STEP 3: Mobile Off-Canvas Drawer Navigation & Genuine Keyboard Trapping ---
            # 3a. Focus the opening trigger deliberately
            await eval_js(ws, "document.getElementById('btnHamburger').focus();", msg_id=30)
            trig_focus = await eval_js(ws, "document.activeElement.id", msg_id=31)
            assert trig_focus == 'btnHamburger', f"Expected btnHamburger focused, got {trig_focus}"
            print("3a. Focused opening trigger:", trig_focus)

            # Open drawer via click
            await eval_js(ws, "document.getElementById('btnHamburger').click();", msg_id=32)
            await asyncio.sleep(0.2)
            drawer_open = await eval_js(ws, "document.getElementById('mobileDrawer').classList.contains('open')", msg_id=33)
            drawer_focus = await eval_js(ws, "document.activeElement.id", msg_id=34)
            print("3b. Drawer open:", drawer_open, "Initial focus:", drawer_focus)
            assert drawer_open, "Drawer must be open"
            assert drawer_focus == 'drawerCloseBtn', f"Expected drawerCloseBtn, got {drawer_focus}"
            assertions['drawer_initial_focus'] = {
                'expected': 'drawerCloseBtn',
                'actual': drawer_focus,
                'pass': (drawer_focus == 'drawerCloseBtn')
            }
            await sample(6, pause=0.08)

            # 3c. Tab through drawer links using genuine CDP keyboard input
            expected_drawer_tabs = ['drawConcept', 'drawServices', 'drawProcess', 'drawStudio', 'drawContact', 'drawBtnConsult']
            actual_drawer_tabs = []
            tab_step_results = []
            for exp_id in expected_drawer_tabs:
                await press_key(ws, 'Tab', shift=False, msg_id=35)
                cur_focus = await eval_js(ws, "document.activeElement.id", msg_id=36)
                actual_drawer_tabs.append(cur_focus)
                passed = (cur_focus == exp_id)
                tab_step_results.append({'expected': exp_id, 'actual': cur_focus, 'pass': passed})
                assert passed, f"Drawer Tab step mismatch: expected {exp_id}, got {cur_focus}"
                await sample(1, pause=0.05)
            assertions['drawer_tab_sequence'] = tab_step_results
            print("3c. Drawer Tab Sequence:", actual_drawer_tabs)

            # 3d. Forward wrap: Tab from drawBtnConsult wraps to drawerCloseBtn
            await press_key(ws, 'Tab', shift=False, msg_id=37)
            drawer_fwd_wrap = await eval_js(ws, "document.activeElement.id", msg_id=38)
            fwd_pass = (drawer_fwd_wrap == 'drawerCloseBtn')
            assertions['drawer_forward_wrap'] = {
                'expected': 'drawerCloseBtn',
                'actual': drawer_fwd_wrap,
                'pass': fwd_pass
            }
            print("3d. Drawer Forward Wrap Tab ->", drawer_fwd_wrap)
            assert fwd_pass, f"Expected drawerCloseBtn, got {drawer_fwd_wrap}"
            await sample(2, pause=0.06)

            # 3e. Backward wrap: Shift+Tab from drawerCloseBtn wraps to drawBtnConsult
            await press_key(ws, 'Tab', shift=True, msg_id=39)
            drawer_bwd_wrap = await eval_js(ws, "document.activeElement.id", msg_id=40)
            bwd_pass = (drawer_bwd_wrap == 'drawBtnConsult')
            assertions['drawer_shift_tab_wrap'] = {
                'expected': 'drawBtnConsult',
                'actual': drawer_bwd_wrap,
                'pass': bwd_pass
            }
            print("3e. Drawer Shift+Tab Wrap ->", drawer_bwd_wrap)
            assert bwd_pass, f"Expected drawBtnConsult, got {drawer_bwd_wrap}"
            await sample(3, pause=0.08)

            # 3f. Escape key closes drawer and returns focus to opening trigger (btnHamburger)
            await press_key(ws, 'Escape', shift=False, msg_id=41)
            await asyncio.sleep(0.2)
            drawer_open_after_esc = await eval_js(ws, "document.getElementById('mobileDrawer').classList.contains('open')", msg_id=42)
            drawer_esc_focus = await eval_js(ws, "document.activeElement.id", msg_id=43)
            esc_pass = (not drawer_open_after_esc) and (drawer_esc_focus == 'btnHamburger')
            assertions['drawer_escape'] = {
                'closed': not drawer_open_after_esc,
                'focus_return_expected': 'btnHamburger',
                'focus_return_actual': drawer_esc_focus,
                'pass': esc_pass
            }
            print(f"3f. Drawer Escape Result: closed={not drawer_open_after_esc}, focus={drawer_esc_focus}")
            assert not drawer_open_after_esc, "Drawer must be closed after Escape"
            assert drawer_esc_focus == 'btnHamburger', f"Focus must return to btnHamburger, got {drawer_esc_focus}"
            await sample(4, pause=0.08)

            # --- STEP 4: Concept Tab Switching ---
            for tab_id in ['tabAngle2', 'tabAngle3', 'tabAngle1']:
                await eval_js(ws, f"document.getElementById('{tab_id}').click();", msg_id=50)
                await sample(3, pause=0.1)

            # --- STEP 5: Consultation Modal Open & Genuine Keyboard Trapping ---
            # 5a. Focus the opening trigger deliberately
            await eval_js(ws, "document.getElementById('btnHeaderConsult').focus();", msg_id=60)
            modal_trig_focus = await eval_js(ws, "document.activeElement.id", msg_id=61)
            assert modal_trig_focus == 'btnHeaderConsult', f"Expected btnHeaderConsult focused, got {modal_trig_focus}"
            print("5a. Focused opening trigger:", modal_trig_focus)

            # Open modal via click
            await eval_js(ws, "document.getElementById('btnHeaderConsult').click();", msg_id=62)
            await asyncio.sleep(0.2)
            modal_open = await eval_js(ws, "document.getElementById('enquiryModal').classList.contains('open')", msg_id=63)
            modal_initial_focus = await eval_js(ws, "document.activeElement.id", msg_id=64)
            print("5b. Modal open:", modal_open, "Initial focus:", modal_initial_focus)
            assert modal_open, "Modal must be open"
            assert modal_initial_focus == 'inputName', f"Expected inputName, got {modal_initial_focus}"
            assertions['modal_initial_focus'] = {
                'expected': 'inputName',
                'actual': modal_initial_focus,
                'pass': (modal_initial_focus == 'inputName')
            }
            await sample(6, pause=0.1)

            # 5c. Normal backward step: Shift+Tab from inputName moves to modalCloseBtn
            await press_key(ws, 'Tab', shift=True, msg_id=65)
            step_back = await eval_js(ws, "document.activeElement.id", msg_id=66)
            step_back_pass = (step_back == 'modalCloseBtn')
            assertions['modal_shift_tab_step_back'] = {
                'from': 'inputName',
                'expected': 'modalCloseBtn',
                'actual': step_back,
                'pass': step_back_pass
            }
            print("5c. Modal Shift+Tab Step Back (from inputName) ->", step_back)
            assert step_back_pass, f"Expected modalCloseBtn, got {step_back}"
            await sample(2, pause=0.06)

            # 5d. Backward boundary wrap: Shift+Tab from modalCloseBtn wraps to btnSubmitEnquiry
            await press_key(ws, 'Tab', shift=True, msg_id=67)
            modal_bwd_wrap = await eval_js(ws, "document.activeElement.id", msg_id=68)
            modal_bwd_pass = (modal_bwd_wrap == 'btnSubmitEnquiry')
            assertions['modal_backward_boundary_wrap'] = {
                'from': 'modalCloseBtn',
                'expected': 'btnSubmitEnquiry',
                'actual': modal_bwd_wrap,
                'pass': modal_bwd_pass
            }
            print("5d. Modal Shift+Tab Backward Boundary Wrap ->", modal_bwd_wrap)
            assert modal_bwd_pass, f"Expected btnSubmitEnquiry, got {modal_bwd_wrap}"
            await sample(3, pause=0.08)

            # 5e. Forward boundary wrap: Tab from btnSubmitEnquiry wraps to modalCloseBtn
            await press_key(ws, 'Tab', shift=False, msg_id=69)
            modal_fwd_wrap = await eval_js(ws, "document.activeElement.id", msg_id=70)
            modal_fwd_pass = (modal_fwd_wrap == 'modalCloseBtn')
            assertions['modal_forward_boundary_wrap'] = {
                'from': 'btnSubmitEnquiry',
                'expected': 'modalCloseBtn',
                'actual': modal_fwd_wrap,
                'pass': modal_fwd_pass
            }
            print("5e. Modal Tab Forward Boundary Wrap ->", modal_fwd_wrap)
            assert modal_fwd_pass, f"Expected modalCloseBtn, got {modal_fwd_wrap}"
            await sample(2, pause=0.06)

            # 5f. Normal forward step: Tab from modalCloseBtn moves to inputName
            await press_key(ws, 'Tab', shift=False, msg_id=71)
            step_fwd = await eval_js(ws, "document.activeElement.id", msg_id=72)
            step_fwd_pass = (step_fwd == 'inputName')
            assertions['modal_tab_step_forward'] = {
                'from': 'modalCloseBtn',
                'expected': 'inputName',
                'actual': step_fwd,
                'pass': step_fwd_pass
            }
            print("5f. Modal Tab Step Forward ->", step_fwd)
            assert step_fwd_pass, f"Expected inputName, got {step_fwd}"
            await sample(2, pause=0.06)

            # --- STEP 6: Empty Form Validation & Clearance Check ---
            await eval_js(ws, "document.getElementById('btnSubmitEnquiry').click();", msg_id=80)
            await asyncio.sleep(0.15)
            has_error_summary = await eval_js(ws, "document.getElementById('errorSummaryBanner').classList.contains('visible')", msg_id=81)
            err_banner_focus = await eval_js(ws, "document.activeElement.id", msg_id=82)
            err_summary_geom = await eval_js(ws, """
                (() => {
                    const banner = document.getElementById('errorSummaryBanner').getBoundingClientRect();
                    const closeBtn = document.getElementById('modalCloseBtn').getBoundingClientRect();
                    const gap = closeBtn.left - banner.right;
                    return {
                        bannerRight: Math.round(banner.right),
                        closeBtnLeft: Math.round(closeBtn.left),
                        clearanceGap: Math.round(gap),
                        clearanceOk: (banner.right + 8 <= closeBtn.left)
                    };
                })()
            """, msg_id=83)
            assertions['empty_error_summary_visible'] = has_error_summary
            assertions['empty_error_summary_focused'] = err_banner_focus
            assertions['empty_error_summary_geometry'] = err_summary_geom
            print("6. Empty Error Summary Visible:", has_error_summary, "Focused:", err_banner_focus, "Geom:", err_summary_geom)
            assert has_error_summary, "Error summary banner should be visible"
            assert err_banner_focus == 'errorSummaryBanner', f"Expected focus on errorSummaryBanner, got {err_banner_focus}"
            assert err_summary_geom['clearanceOk'], f"Error summary clearance gap < 8px: {err_summary_geom}"
            assert err_summary_geom['clearanceGap'] >= 8, f"Error summary clearance gap must be >= 8px, got {err_summary_geom['clearanceGap']}"
            await sample(6, pause=0.1)

            # --- STEP 7: Invalid Phone Input Validation ---
            await eval_js(ws, """
                document.getElementById('inputName').value = 'তানভীর আহমেদ';
                document.getElementById('inputPhone').value = '01711abcxyz';
                document.getElementById('inputArea').value = 'ধানমন্ডি, ঢাকা';
                document.getElementById('selectType').value = 'residential_full';
                document.getElementById('btnSubmitEnquiry').click();
            """, msg_id=90)
            await asyncio.sleep(0.15)
            phone_invalid_err = await eval_js(ws, "!document.getElementById('errPhone').classList.contains('hidden')", msg_id=91)
            assertions['phone_invalid_err_shown'] = phone_invalid_err
            print("7. Phone Invalid Error Shown:", phone_invalid_err)
            assert phone_invalid_err, "Phone error should be shown for invalid phone"
            await sample(6, pause=0.1)

            # --- STEP 8: Valid Form Entry & stateSubmitting Focus ---
            await eval_js(ws, """
                document.getElementById('inputPhone').value = '০১৭১১০০০০০০';
                document.getElementById('inputNotes').value = 'ধানমন্ডিতে ২৫০০ বর্গফুটের ডুপ্লেক্স অ্যাপার্টমেন্টের জন্য আধুনিক ইন্টেরিয়র আর্কিটেকচার সেবা প্রয়োজন।';
                document.getElementById('btnSubmitEnquiry').click();
            """, msg_id=100)
            await asyncio.sleep(0.15)
            submitting_focus = await eval_js(ws, "document.activeElement.id", msg_id=101)
            assertions['submitting_focus'] = submitting_focus
            print("8. Submitting Focus:", submitting_focus)
            assert submitting_focus == 'stateSubmitting', f"Expected stateSubmitting focused, got {submitting_focus}"
            await sample(6, pause=0.1)

            # Wait for submission timer to finish (900ms)
            await asyncio.sleep(0.95)

            # --- STEP 9: Receipt State Focus ---
            receipt_focus = await eval_js(ws, "document.activeElement.id", msg_id=110)
            assertions['receipt_focus'] = receipt_focus
            print("9. Receipt Focus:", receipt_focus)
            assert receipt_focus == 'btnDone', f"Expected btnDone focused, got {receipt_focus}"
            await sample(8, pause=0.1)

            # --- STEP 10: 'New Enquiry' Button Click & Focus Restoration ---
            await eval_js(ws, "document.getElementById('btnNewEnquiry').click();", msg_id=120)
            await asyncio.sleep(0.15)
            new_enquiry_focus = await eval_js(ws, "document.activeElement.id", msg_id=121)
            assertions['new_enquiry_focus_restored'] = new_enquiry_focus
            print("10. New Enquiry Focus Restored to:", new_enquiry_focus)
            assert new_enquiry_focus == 'inputName', f"Expected inputName focused, got {new_enquiry_focus}"
            await sample(6, pause=0.1)

            # 10b. Close modal via genuine Escape key and verify focus returns to opening trigger (btnHeaderConsult)
            await press_key(ws, 'Escape', shift=False, msg_id=125)
            await asyncio.sleep(0.2)
            modal_open_after_esc = await eval_js(ws, "document.getElementById('enquiryModal').classList.contains('open')", msg_id=126)
            modal_esc_focus = await eval_js(ws, "document.activeElement.id", msg_id=127)
            modal_esc_pass = (not modal_open_after_esc) and (modal_esc_focus == 'btnHeaderConsult')
            assertions['modal_escape'] = {
                'closed': not modal_open_after_esc,
                'focus_return_expected': 'btnHeaderConsult',
                'focus_return_actual': modal_esc_focus,
                'pass': modal_esc_pass
            }
            print(f"10b. Modal Escape Result: closed={not modal_open_after_esc}, focus={modal_esc_focus}")
            assert not modal_open_after_esc, "Modal must be closed after Escape"
            assert modal_esc_focus == 'btnHeaderConsult', f"Focus must return to btnHeaderConsult, got {modal_esc_focus}"
            await sample(4, pause=0.08)

            # --- STEP 11: Switch to English Mode (BN -> EN) ---
            await eval_js(ws, "document.getElementById('langToggle').click();", msg_id=130)
            await asyncio.sleep(0.3)

            en_metrics = await eval_js(ws, """
                return {
                    currentLang: currentLang,
                    innerWidth: window.innerWidth,
                    innerHeight: window.innerHeight,
                    scrollWidth: document.documentElement.scrollWidth,
                    clientWidth: document.documentElement.clientWidth,
                    matchMedia900: window.matchMedia('(max-width: 900px)').matches,
                    hasSimClass: document.documentElement.classList.contains('mobile-sim-active'),
                    hamburgerRight: document.getElementById('btnHamburger').getBoundingClientRect().right,
                    headerWidth: document.querySelector('header').offsetWidth
                };
            """, msg_id=131)
            assertions['en_switch_metrics'] = en_metrics
            print("11. English Metrics (BN -> EN):", en_metrics)
            assert en_metrics['currentLang'] == 'en', "Language must be English"
            assert en_metrics['innerWidth'] == 390, f"Expected innerWidth 390, got {en_metrics['innerWidth']}"
            assert en_metrics['scrollWidth'] == 390, f"Expected scrollWidth 390, got {en_metrics['scrollWidth']}"
            assert en_metrics['hamburgerRight'] <= 390, f"Hamburger clipped! right={en_metrics['hamburgerRight']}"
            await sample(8, pause=0.1)

            # --- STEP 12: English Off-Canvas Drawer ---
            await eval_js(ws, "document.getElementById('btnHamburger').focus();", msg_id=140)
            await eval_js(ws, "document.getElementById('btnHamburger').click();", msg_id=141)
            await asyncio.sleep(0.2)
            en_drawer_focus = await eval_js(ws, "document.activeElement.id", msg_id=142)
            assertions['en_drawer_focus'] = en_drawer_focus
            print("12. English Drawer Focus:", en_drawer_focus)
            assert en_drawer_focus == 'drawerCloseBtn', f"Expected drawerCloseBtn, got {en_drawer_focus}"
            await sample(5, pause=0.08)
            await press_key(ws, 'Escape', shift=False, msg_id=143)
            await asyncio.sleep(0.2)
            en_drawer_esc_focus = await eval_js(ws, "document.activeElement.id", msg_id=144)
            assert en_drawer_esc_focus == 'btnHamburger', f"Expected focus on btnHamburger, got {en_drawer_esc_focus}"

            # --- STEP 13: English Consultation Modal, Receipt & Geometry Check ---
            await eval_js(ws, "document.getElementById('btnHeaderConsult').focus();", msg_id=150)
            await eval_js(ws, "document.getElementById('btnHeaderConsult').click();", msg_id=151)
            await asyncio.sleep(0.2)

            en_modal_geom = await eval_js(ws, """
                const card = document.getElementById('modalCard').getBoundingClientRect();
                return {
                    modalCardRight: card.right,
                    modalCardWidth: card.width,
                    docScrollW: document.documentElement.scrollWidth
                };
            """, msg_id=152)
            assertions['en_modal_geometry'] = en_modal_geom
            print("13. English Modal Geometry:", en_modal_geom)
            assert en_modal_geom['modalCardRight'] <= 390, f"Modal card overflow: {en_modal_geom['modalCardRight']}"
            assert en_modal_geom['docScrollW'] == 390, f"Doc overflow in modal: {en_modal_geom['docScrollW']}"
            await sample(6, pause=0.1)

            # Fill and submit in English
            await eval_js(ws, """
                document.getElementById('inputName').value = 'Nihal Rahman';
                document.getElementById('inputPhone').value = '+880 1711 000000';
                document.getElementById('inputArea').value = 'Gulshan-2, Dhaka';
                document.getElementById('selectType').value = 'residential_full';
                document.getElementById('btnSubmitEnquiry').click();
            """, msg_id=160)
            await asyncio.sleep(1.1)

            en_receipt_geom = await eval_js(ws, """
                const rWrap = document.querySelector('#stateReceipt .receipt-wrap').getBoundingClientRect();
                const notice = document.getElementById('receiptSimNotice').getBoundingClientRect();
                return {
                    receiptWrapRight: rWrap.right,
                    noticeRight: notice.right,
                    docScrollW: document.documentElement.scrollWidth,
                    receiptFocus: document.activeElement.id
                };
            """, msg_id=161)
            assertions['en_receipt_geometry'] = en_receipt_geom
            print("   English Receipt Geometry:", en_receipt_geom)
            assert en_receipt_geom['receiptWrapRight'] <= 390, f"Receipt wrap overflow: {en_receipt_geom['receiptWrapRight']}"
            assert en_receipt_geom['noticeRight'] <= 390, f"Notice overflow: {en_receipt_geom['noticeRight']}"
            assert en_receipt_geom['docScrollW'] == 390, f"Doc overflow in receipt: {en_receipt_geom['docScrollW']}"
            await sample(8, pause=0.1)

            # Close English receipt modal via btnDone and verify focus returns to btnHeaderConsult
            await eval_js(ws, "document.getElementById('btnDone').click();", msg_id=165)
            await asyncio.sleep(0.2)
            en_receipt_closed = await eval_js(ws, "!document.getElementById('enquiryModal').classList.contains('open')", msg_id=166)
            en_done_focus = await eval_js(ws, "document.activeElement.id", msg_id=167)
            assert en_receipt_closed, "Modal must be closed after Done"
            assert en_done_focus == 'btnHeaderConsult', f"Expected focus on btnHeaderConsult, got {en_done_focus}"
            assertions['en_receipt_done_escape'] = {
                'closed': en_receipt_closed,
                'focus_return': en_done_focus,
                'pass': True
            }
            await sample(4, pause=0.08)

            # --- STEP 14: English Offline Modal Fallback & Clearance Check ---
            # Open offline state via demo button with deliberate focus
            await eval_js(ws, "document.getElementById('btnDemoOffline').focus();", msg_id=170)
            await eval_js(ws, "document.getElementById('btnDemoOffline').click();", msg_id=171)
            await asyncio.sleep(0.2)
            en_offline_geom = await eval_js(ws, """
                (() => {
                    const banner = document.querySelector('.offline-banner').getBoundingClientRect();
                    const closeBtn = document.getElementById('modalCloseBtn').getBoundingClientRect();
                    const gap = closeBtn.left - banner.right;
                    return {
                        offlineBannerRight: Math.round(banner.right),
                        closeBtnLeft: Math.round(closeBtn.left),
                        closeBtnRight: Math.round(closeBtn.right),
                        clearanceGap: Math.round(gap),
                        clearanceOk: (banner.right + 8 <= closeBtn.left),
                        docScrollW: document.documentElement.scrollWidth,
                        focus: document.activeElement.id
                    };
                })()
            """, msg_id=172)
            assertions['en_offline_geometry'] = en_offline_geom
            print("14. English Offline Geometry & Clearance:", en_offline_geom)
            assert en_offline_geom['offlineBannerRight'] <= 390, f"Offline banner overflow: {en_offline_geom['offlineBannerRight']}"
            assert en_offline_geom['docScrollW'] == 390, f"Doc overflow in offline: {en_offline_geom['docScrollW']}"
            assert en_offline_geom['clearanceOk'], f"Offline banner clearance gap < 8px: {en_offline_geom}"
            assert en_offline_geom['clearanceGap'] >= 8, f"Offline banner clearance gap must be >= 8px, got {en_offline_geom['clearanceGap']}"
            await sample(8, pause=0.1)

            # Close modal via Escape and verify focus returns to btnDemoOffline
            await press_key(ws, 'Escape', shift=False, msg_id=173)
            await asyncio.sleep(0.2)
            en_offline_closed = await eval_js(ws, "!document.getElementById('enquiryModal').classList.contains('open')", msg_id=174)
            en_offline_esc_focus = await eval_js(ws, "document.activeElement.id", msg_id=175)
            assert en_offline_closed, "Offline modal must be closed after Escape"
            assert en_offline_esc_focus == 'btnDemoOffline', f"Expected focus on btnDemoOffline, got {en_offline_esc_focus}"
            assertions['en_offline_escape'] = {
                'closed': en_offline_closed,
                'focus_return': en_offline_esc_focus,
                'pass': True
            }
            await sample(4, pause=0.08)

            # --- STEP 15: Return to Bengali Mode (EN -> BN) ---
            await eval_js(ws, "document.getElementById('langToggle').click();", msg_id=180)
            await asyncio.sleep(0.3)
            bn_return_metrics = await eval_js(ws, """
                return {
                    currentLang: currentLang,
                    innerWidth: window.innerWidth,
                    scrollWidth: document.documentElement.scrollWidth,
                    clientWidth: document.documentElement.clientWidth
                };
            """, msg_id=181)
            assertions['bn_return_metrics'] = bn_return_metrics
            print("15. Bengali Return Metrics (EN -> BN):", bn_return_metrics)
            assert bn_return_metrics['currentLang'] == 'bn', "Language must be Bengali"
            assert bn_return_metrics['innerWidth'] == 390, f"Expected innerWidth 390, got {bn_return_metrics['innerWidth']}"
            assert bn_return_metrics['scrollWidth'] == 390, f"Expected scrollWidth 390, got {bn_return_metrics['scrollWidth']}"
            await sample(6, pause=0.1)

            # --- STEP 16: Separate System & Manual Reduced Motion Verification ---
            # 16a. Genuine Emulated System Media Query prefers-reduced-motion
            await call_cdp(ws, 'Emulation.setEmulatedMedia', {
                'features': [{'name': 'prefers-reduced-motion', 'value': 'reduce'}]
            }, msg_id=190)
            await asyncio.sleep(0.1)
            sys_reduced_match = await eval_js(ws, "window.matchMedia('(prefers-reduced-motion: reduce)').matches", msg_id=191)
            assertions['system_reduced_motion_mq'] = sys_reduced_match
            print("16. System Prefers Reduced Motion MQ:", sys_reduced_match)
            assert sys_reduced_match, "System media query emulation must match"
            await sample(4, pause=0.1)

            # Clear emulated media
            await call_cdp(ws, 'Emulation.setEmulatedMedia', {'features': []}, msg_id=192)

            # 16b. Separate manual class toggle
            await eval_js(ws, "toggleReducedMotion();", msg_id=193)
            has_motion_class = await eval_js(ws, "document.documentElement.classList.contains('reduced-motion')", msg_id=194)
            assertions['manual_reduced_motion_class'] = has_motion_class
            print("    Manual Reduced Motion Class Toggle:", has_motion_class)
            assert has_motion_class, "Manual toggle class must be set"
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
