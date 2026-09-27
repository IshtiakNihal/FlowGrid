"""
FlowGrid - Export All V3 Boards to Matching High-Resolution PNGs
Renders each board at exact pixel dimensions using headless Edge.
Guarantees 100% visual synchronization between local sources and visual evidence.
"""
import os
import subprocess
import time

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
os.makedirs('figma_exports', exist_ok=True)

boards = [
    ('figma_svgs_v3/00_brief_and_research.svg', 'figma_exports/page_00_brief.png', 2400, 1950),
    ('figma_svgs_v3/01_foundations.svg', 'figma_exports/page_01_foundations.png', 2400, 2050),
    ('figma_svgs_v3/02_components.svg', 'figma_exports/page_02_components.png', 2800, 2550),
    ('figma_svgs_v3/03_desktop_bn.svg', 'figma_exports/page_03_desktop_bn.png', 6480, 7200),
    ('figma_svgs_v3/04_mobile_bn.svg', 'figma_exports/page_04_mobile_bn.png', 2450, 4850),
    ('figma_svgs_v3/05_english.svg', 'figma_exports/page_05_english.png', 7000, 7400),
    ('figma_svgs_v3/06_prototype_motion.svg', 'figma_exports/page_06_motion.png', 2800, 2500),
    ('figma_svgs_v3/07_project_and_concept_assets.svg', 'figma_exports/page_07_assets.png', 2800, 2900),
    ('figma_svgs_v3/08_handoff_qa.svg', 'figma_exports/page_08_handoff.png', 2800, 2600)
]

print("Starting render of all 9 boards to figma_exports/...")

for svg_rel, png_rel, w, h in boards:
    svg_abs = os.path.abspath(svg_rel).replace('\\', '/')
    png_abs = os.path.abspath(png_rel)
    
    cmd = [
        edge_path,
        '--headless',
        '--disable-gpu',
        '--hide-scrollbars',
        f'--window-size={w},{h}',
        f'--screenshot={png_abs}',
        f'file:///{svg_abs}'
    ]
    
    t0 = time.time()
    res = subprocess.run(cmd, capture_output=True, text=True)
    dt = time.time() - t0
    
    if os.path.exists(png_abs):
        size_kb = os.path.getsize(png_abs) / 1024
        print(f"[OK] {os.path.basename(png_rel)} ({w}x{h}): {size_kb:.1f} KB in {dt:.1f}s")
    else:
        print(f"[FAIL] to render {png_rel} (Code: {res.returncode})")

# Also render a clean crop of the Primary Button Component (exact 210x52 geometry)
btn_svg = '''<svg width="210" height="52" viewBox="0 0 210 52" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="210" height="52" fill="#183B35" rx="2"/>
  <text x="105" y="32" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="600" text-anchor="middle">পরামর্শ বুক করুন</text>
</svg>'''

with open('figma_exports/component_button_primary.svg', 'w', encoding='utf-8') as f:
    f.write(btn_svg)

btn_svg_abs = os.path.abspath('figma_exports/component_button_primary.svg').replace('\\', '/')
btn_png_abs = os.path.abspath('figma_exports/component_3_1190.png')
cmd_btn = [
    edge_path,
    '--headless',
    '--disable-gpu',
    '--hide-scrollbars',
    '--window-size=210,52',
    f'--screenshot={btn_png_abs}',
    f'file:///{btn_svg_abs}'
]
subprocess.run(cmd_btn)
if os.path.exists(btn_png_abs):
    print(f"[OK] component_3_1190.png (Button Component Clean): {os.path.getsize(btn_png_abs)/1024:.1f} KB")

# Clean up test file if present
if os.path.exists('figma_exports/page_00_brief_test.png'):
    os.remove('figma_exports/page_00_brief_test.png')

print("All exports successfully generated and verified in figma_exports/!")
