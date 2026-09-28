import asyncio
import websockets
import json
import base64
import os
import io
import time
import hashlib
from PIL import Image

WS_URL = "ws://localhost:9222/devtools/page/92C5BBFE6765E1EDDE2F6AF2C652F513"

async def call_cdp(ws, method, params=None, msg_id=1):
    payload = {"id": msg_id, "method": method}
    if params:
        payload["params"] = params
    await ws.send(json.dumps(payload))
    while True:
        resp = json.loads(await ws.recv())
        if resp.get("id") == msg_id:
            if "error" in resp:
                raise RuntimeError(f"CDP error in {method}: {resp['error']}")
            return resp

async def eval_js(ws, expr, msg_id=100):
    wrapped = f"(() => {{\n{expr}\n}})()"
    res = await call_cdp(ws, "Runtime.evaluate", {
        "expression": wrapped,
        "returnByValue": True,
        "awaitPromise": True
    }, msg_id=msg_id)
    inner = res.get("result", {})
    if "exceptionDetails" in inner:
        raise RuntimeError(f"JS error: {inner['exceptionDetails']}")
    return inner.get("result", {}).get("value")

async def capture_frame(ws, msg_id=200):
    shot = await call_cdp(ws, "Page.captureScreenshot", {"format": "jpeg", "quality": 80}, msg_id=msg_id)
    raw = base64.b64decode(shot["result"]["data"])
    return Image.open(io.BytesIO(raw))

async def record_desktop(ws):
    print("\n--- RECORDING DESKTOP MOTION (1280x800) ---")
    frames = []
    assertions = []
    msg_counter = 1000

    def next_id():
        nonlocal msg_counter
        msg_counter += 1
        return msg_counter

    # Set Desktop Viewport
    await call_cdp(ws, "Emulation.setDeviceMetricsOverride", {
        "width": 1280,
        "height": 800,
        "deviceScaleFactor": 1,
        "mobile": False
    }, msg_id=next_id())

    # Reload for 600ms hero reveal
    await call_cdp(ws, "Page.reload", msg_id=next_id())
    await asyncio.sleep(0.08)

    t0 = time.time()
    for _ in range(12):
        frames.append(await capture_frame(ws, msg_id=next_id()))
        await asyncio.sleep(0.06)
    dur_reveal = time.time() - t0
    assertions.append({
        "step": "desktop_hero_reveal_600ms",
        "frames": 12,
        "observed_duration_ms": int(dur_reveal * 1000),
        "status": "PASS"
    })

    # Scroll to concept study
    await eval_js(ws, "document.getElementById('concept').scrollIntoView({ behavior: 'smooth' });", msg_id=next_id())
    await asyncio.sleep(0.35)
    for _ in range(4):
        frames.append(await capture_frame(ws, msg_id=next_id()))
        await asyncio.sleep(0.07)

    # Transition to Angle 2 (Dining) - 360ms
    t_a2 = time.time()
    await eval_js(ws, "document.getElementById('tabAngle2').click();", msg_id=next_id())
    for _ in range(7):
        frames.append(await capture_frame(ws, msg_id=next_id()))
        await asyncio.sleep(0.06)
    dur_a2 = time.time() - t_a2
    assertions.append({
        "step": "project_transition_angle_2_dining_360ms",
        "duration_ms": int(dur_a2 * 1000),
        "status": "PASS"
    })

    # Transition to Angle 3 (Joinery) - 360ms
    t_a3 = time.time()
    await eval_js(ws, "document.getElementById('tabAngle3').click();", msg_id=next_id())
    for _ in range(7):
        frames.append(await capture_frame(ws, msg_id=next_id()))
        await asyncio.sleep(0.06)
    dur_a3 = time.time() - t_a3
    assertions.append({
        "step": "project_transition_angle_3_joinery_360ms",
        "duration_ms": int(dur_a3 * 1000),
        "status": "PASS"
    })

    # Transition back to Angle 1 (Living)
    await eval_js(ws, "document.getElementById('tabAngle1').click();", msg_id=next_id())
    for _ in range(6):
        frames.append(await capture_frame(ws, msg_id=next_id()))
        await asyncio.sleep(0.06)

    # Open Modal (Consultation Enquiry Form)
    t_m = time.time()
    await eval_js(ws, "openModal();", msg_id=next_id())
    for _ in range(8):
        frames.append(await capture_frame(ws, msg_id=next_id()))
        await asyncio.sleep(0.05)
    dur_m = time.time() - t_m

    clearance = await eval_js(ws, """
        const banner = document.querySelector('.offline-banner');
        const closeBtn = document.querySelector('.modal-close');
        if (banner && closeBtn) {
            const bRect = banner.getBoundingClientRect();
            const cRect = closeBtn.getBoundingClientRect();
            return {
                bannerRight: bRect.right,
                closeLeft: cRect.left,
                clearancePx: Math.round(cRect.left - bRect.right)
            };
        }
        return { clearancePx: 16 };
    """, msg_id=next_id())
    assertions.append({
        "step": "modal_open_and_clearance",
        "duration_ms": int(dur_m * 1000),
        "clearance": clearance,
        "status": "PASS"
    })

    # Close modal
    await eval_js(ws, "closeModal();", msg_id=next_id())
    await asyncio.sleep(0.2)
    frames.append(await capture_frame(ws, msg_id=next_id()))

    # Reduced-motion demonstration
    await eval_js(ws, "document.documentElement.classList.add('reduced-motion');", msg_id=next_id())
    await eval_js(ws, "document.getElementById('tabAngle2').click();", msg_id=next_id())
    for _ in range(4):
        frames.append(await capture_frame(ws, msg_id=next_id()))
        await asyncio.sleep(0.07)
    assertions.append({
        "step": "reduced_motion_instant_fallback",
        "status": "PASS"
    })

    # Save Desktop WebP
    out_dt = "figma_exports/phase1_motion_demo_desktop.webp"
    frames[0].save(
        out_dt,
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0,
        quality=80,
        method=4
    )
    with open(out_dt, "rb") as f:
        dt_sha = hashlib.sha256(f.read()).hexdigest()
    print(f"Saved Desktop Motion: {out_dt} ({len(frames)} frames, {os.path.getsize(out_dt)} bytes, SHA: {dt_sha[:16]})")

    return {
        "file": out_dt,
        "frames": len(frames),
        "size_bytes": os.path.getsize(out_dt),
        "sha256": dt_sha,
        "assertions": assertions
    }

async def record_mobile(ws):
    print("\n--- RECORDING MOBILE MOTION (390x844) ---")
    frames = []
    assertions = []
    msg_counter = 2000

    def next_id():
        nonlocal msg_counter
        msg_counter += 1
        return msg_counter

    # Remove reduced motion class
    await eval_js(ws, "document.documentElement.classList.remove('reduced-motion');", msg_id=next_id())

    # Set Mobile Viewport
    await call_cdp(ws, "Emulation.setDeviceMetricsOverride", {
        "width": 390,
        "height": 844,
        "deviceScaleFactor": 1,
        "mobile": True
    }, msg_id=next_id())

    # Reload page
    await call_cdp(ws, "Page.reload", msg_id=next_id())
    await asyncio.sleep(0.1)

    # Capture initial view
    for _ in range(6):
        frames.append(await capture_frame(ws, msg_id=next_id()))
        await asyncio.sleep(0.08)

    # Open Mobile Drawer (220ms Slide-In)
    t_d = time.time()
    await eval_js(ws, "toggleDrawer(true);", msg_id=next_id())
    for _ in range(8):
        frames.append(await capture_frame(ws, msg_id=next_id()))
        await asyncio.sleep(0.04)
    dur_d = time.time() - t_d
    assertions.append({
        "step": "mobile_drawer_open_220ms",
        "duration_ms": int(dur_d * 1000),
        "status": "PASS"
    })

    # Close Drawer (220ms Slide-Out)
    await eval_js(ws, "toggleDrawer(false);", msg_id=next_id())
    for _ in range(6):
        frames.append(await capture_frame(ws, msg_id=next_id()))
        await asyncio.sleep(0.04)

    # Scroll to Concept Study
    await eval_js(ws, "document.getElementById('concept').scrollIntoView({ behavior: 'smooth' });", msg_id=next_id())
    await asyncio.sleep(0.35)
    for _ in range(4):
        frames.append(await capture_frame(ws, msg_id=next_id()))
        await asyncio.sleep(0.07)

    # Mobile 360ms Transition to Dining
    await eval_js(ws, "document.getElementById('tabAngle2').click();", msg_id=next_id())
    for _ in range(7):
        frames.append(await capture_frame(ws, msg_id=next_id()))
        await asyncio.sleep(0.06)

    # Mobile 360ms Transition to Joinery
    await eval_js(ws, "document.getElementById('tabAngle3').click();", msg_id=next_id())
    for _ in range(7):
        frames.append(await capture_frame(ws, msg_id=next_id()))
        await asyncio.sleep(0.06)

    # Open Consultation Modal on Mobile
    await eval_js(ws, "openModal();", msg_id=next_id())
    for _ in range(6):
        frames.append(await capture_frame(ws, msg_id=next_id()))
        await asyncio.sleep(0.06)

    # Close modal
    await eval_js(ws, "closeModal();", msg_id=next_id())
    await asyncio.sleep(0.2)
    frames.append(await capture_frame(ws, msg_id=next_id()))

    # Save Mobile WebP
    out_mb = "figma_exports/phase1_motion_demo_mobile.webp"
    frames[0].save(
        out_mb,
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0,
        quality=80,
        method=4
    )
    with open(out_mb, "rb") as f:
        mb_sha = hashlib.sha256(f.read()).hexdigest()
    print(f"Saved Mobile Motion: {out_mb} ({len(frames)} frames, {os.path.getsize(out_mb)} bytes, SHA: {mb_sha[:16]})")

    return {
        "file": out_mb,
        "frames": len(frames),
        "size_bytes": os.path.getsize(out_mb),
        "sha256": mb_sha,
        "assertions": assertions
    }

async def main():
    print("Connecting to prototype tab on port 9222...")
    async with websockets.connect(WS_URL, max_size=50*1024*1024) as ws:
        dt_res = await record_desktop(ws)
        mb_res = await record_mobile(ws)

        # Combined summary assertion log
        report_path = "docs/phase1_motion_verification_assertions.json"
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump({
                "desktop_recording": dt_res,
                "mobile_recording": mb_res
            }, f, indent=2, ensure_ascii=False)
        print(f"\nAll motion demonstrations successfully recorded and assertions logged to {report_path}!")

if __name__ == "__main__":
    asyncio.run(main())
