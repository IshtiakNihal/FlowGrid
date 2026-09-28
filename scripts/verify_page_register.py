"""
Automated verification script to validate that all 46 layout geometries in
Section 2 of FlowGrid_Comprehensive_Design_Handoff_and_Correction_Report.md
match the canvas coordinate rectangles in the master vector SVGs.
"""
import re

with open('figma_svgs_v3/03_desktop_bn.svg', 'r', encoding='utf-8') as f:
    svg3 = f.read()
with open('figma_svgs_v3/04_mobile_bn.svg', 'r', encoding='utf-8') as f:
    svg4 = f.read()
with open('figma_svgs_v3/05_english.svg', 'r', encoding='utf-8') as f:
    svg5 = f.read()

with open('FlowGrid_Comprehensive_Design_Handoff_and_Correction_Report.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract rows from Section 2
rows = re.findall(r'\|\s*(\d+)\s*\|\s*([^|]+)\|\s*(\d+px)\s*\|\s*x:\s*(\d+),\s*y:\s*(\d+)\s*\|\s*(\d+)\s*×\s*(\d+)[^|]*\|\s*([^|]+)\|', text)

print(f"Extracted {len(rows)} layout rows from Section 2 of report.")
if len(rows) != 46:
    raise ValueError(f"Expected 46 rows, found {len(rows)}")

all_match = True
for r in rows:
    num, name, vp, x, y, w, h, ev = r
    n = int(num)
    target_svg = svg3 if n <= 11 else (svg4 if n <= 23 else svg5)
    
    # Check if x, y, width, height appears in svg
    p1 = f'x="{x}" y="{y}" width="{w}" height="{h}"'
    p2 = f'width="{w}" height="{h}" x="{x}" y="{y}"'
    
    found = (p1 in target_svg) or (p2 in target_svg)
    if not found:
        reg = rf'<(?:rect|g|svg)[^>]*(?:x="{x}"[^>]*y="{y}"|y="{y}"[^>]*x="{x}")[^>]*(?:width="{w}"[^>]*height="{h}"|height="{h}"[^>]*width="{w}")'
        m = re.search(reg, target_svg)
        if m:
            found = True
    
    if found:
        print(f"Row {num:>2}: [MATCH] {name.strip():<32} ({x}, {y}, {w}, {h})")
    else:
        print(f"Row {num:>2}: [FAIL] {name.strip():<32} ({x}, {y}, {w}, {h})")
        all_match = False

if all_match:
    print("\nALL 46 LAYOUT ROWS MATCH THE MASTER SVGS 100% PERFECTLY!")
else:
    print("\nSOME ROWS DID NOT MATCH.")
    exit(1)
