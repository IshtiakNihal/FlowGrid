"""
Script to package FlowGrid_Revision_3_3_Deliverable.zip and verify the extracted contents.
"""
import os
import zipfile
import subprocess
import hashlib
from PIL import Image

files_to_zip = [
    'FlowGrid_Client_Presentation.pdf',
    'FlowGrid_Comprehensive_Design_Handoff_and_Correction_Report.md',
    'concepts/concept_01_joinery_detail.jpg',
    'concepts/concept_01_living_alt.jpg',
    'concepts/concept_01_living_dhaka.jpg',
    'concepts/concept_02_kitchen_dhaka.jpg',
    'concepts/concept_03_bedroom_dhaka.jpg',
    'figma_exports/component_3_1190.png',
    'figma_exports/component_button_primary.svg',
    'figma_exports/crop_desktop_archive.png',
    'figma_exports/crop_desktop_home.png',
    'figma_exports/crop_desktop_services.png',
    'figma_exports/crop_desktop_study.png',
    'figma_exports/crop_mobile_contact.png',
    'figma_exports/crop_mobile_drawer.png',
    'figma_exports/crop_mobile_form.png',
    'figma_exports/crop_mobile_home.png',
    'figma_exports/crop_mobile_study.png',
    'figma_exports/page_00_brief.png',
    'figma_exports/page_01_foundations.png',
    'figma_exports/page_02_components.png',
    'figma_exports/page_03_desktop_bn.png',
    'figma_exports/page_04_mobile_bn.png',
    'figma_exports/page_05_english.png',
    'figma_exports/page_06_motion.png',
    'figma_exports/page_07_assets.png',
    'figma_exports/page_08_handoff.png',
    'figma_exports/prototype_enquiry_journey.webp',
    'figma_svgs_v3/00_brief_and_research.svg',
    'figma_svgs_v3/01_foundations.svg',
    'figma_svgs_v3/02_components.svg',
    'figma_svgs_v3/03_desktop_bn.svg',
    'figma_svgs_v3/04_mobile_bn.svg',
    'figma_svgs_v3/05_english.svg',
    'figma_svgs_v3/06_prototype_motion.svg',
    'figma_svgs_v3/07_project_and_concept_assets.svg',
    'figma_svgs_v3/08_handoff_qa.svg',
    'prototype/index.html',
    'prototype/prototype_enquiry_journey.webp'
]

zip_name = 'FlowGrid_Revision_3_3_Deliverable.zip'
print(f"Creating {zip_name} with {len(files_to_zip)} files...")

with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in sorted(files_to_zip):
        if not os.path.exists(f):
            raise FileNotFoundError(f"Missing file: {f}")
        z.write(f, f)
        print(f"  Added: {f} ({os.path.getsize(f):,} bytes)")

zip_size = os.path.getsize(zip_name)
with open(zip_name, 'rb') as f:
    zip_sha = hashlib.sha256(f.read()).hexdigest()

print(f"\n{zip_name} created successfully!")
print(f"Size: {zip_size:,} bytes")
print(f"SHA-256: {zip_sha}")

# Clean extraction test
test_dir = 'scratch/test_extracted_zip'
if os.path.exists(test_dir):
    import shutil
    shutil.rmtree(test_dir)
os.makedirs(test_dir, exist_ok=True)

with zipfile.ZipFile(zip_name, 'r') as z:
    z.extractall(test_dir)
print(f"\nExtracted all files to {test_dir} for independent verification.")

# 1. Test extracted prototype syntax
extracted_html = os.path.join(test_dir, 'prototype/index.html')
with open(extracted_html, 'r', encoding='utf-8') as f:
    html_content = f.read()

import re
script_match = re.search(r'<script>([\s\S]*?)</script>', html_content)
if not script_match:
    raise ValueError("No script found in extracted HTML")

script_tmp = os.path.join(test_dir, 'extracted_script.js')
with open(script_tmp, 'w', encoding='utf-8') as f:
    f.write(script_match.group(1))

node_test = subprocess.run(
    ['node', '--check', script_tmp],
    capture_output=True,
    text=True
)
if node_test.returncode != 0:
    print("FAILED node --check on extracted script:", node_test.stderr)
    raise RuntimeError("Extracted script failed syntax check")
else:
    print("PASS: Extracted prototype/index.html passed node --check with zero syntax errors.")

# 1b. Test extracted phone validator unit suite (13 cases)
val_start = html_content.find('function validateBDPhone')
val_end = html_content.find('function handleFormSubmit')
val_func = html_content[val_start:val_end].strip()

val_test_script = f"""
{val_func}
const tests = [
  {{ input: '01711000000', expected: true, label: 'Standard 11-digit mobile' }},
  {{ input: '01711-000000', expected: true, label: 'Hyphenated mobile' }},
  {{ input: '+880 1711 000000', expected: true, label: 'International format with spaces' }},
  {{ input: '+8801711000000', expected: true, label: 'International contiguous format' }},
  {{ input: '+880 01711-000000', expected: true, label: 'Country code + trunk zero' }},
  {{ input: '০১৭১১০০০০০০', expected: true, label: 'Native Bengali numerals' }},
  {{ input: '+৮৮০ ০১৭১১-০০০০০০', expected: true, label: 'Bengali numerals + country code + trunk zero' }},
  {{ input: 'abcdefgh', expected: false, label: 'Letters rejected' }},
  {{ input: 'তানভীর আহমেদ', expected: false, label: 'Bengali letters rejected' }},
  {{ input: '12345678', expected: false, label: 'Too short (8 digits)' }},
  {{ input: '01234567890', expected: false, label: 'Invalid operator 012' }},
  {{ input: '01711000000@#$', expected: false, label: 'Arbitrary punctuation rejected' }},
  {{ input: '', expected: false, label: 'Empty input rejected' }}
];
let passed = 0;
tests.forEach(t => {{
  if (validateBDPhone(t.input) === t.expected) passed++;
}});
console.log(`PASS: BD Phone validator passed ${{passed}}/${{tests.length}} automated test cases.`);
if (passed !== tests.length) process.exit(1);
"""

val_test_file = os.path.join(test_dir, 'test_val.js')
with open(val_test_file, 'w', encoding='utf-8') as f:
    f.write(val_test_script)

val_proc = subprocess.run(['node', val_test_file], capture_output=True, text=True)
print(val_proc.stdout.strip())
if val_proc.returncode != 0:
    raise RuntimeError("Phone validator unit tests failed!")


# 2. Test extracted WebP recording
extracted_webp = os.path.join(test_dir, 'prototype/prototype_enquiry_journey.webp')
with Image.open(extracted_webp) as im:
    print(f"PASS: Extracted WebP recording: {im.size}, {im.n_frames} frames, animated={getattr(im, 'is_animated', False)}")

# 3. Test extracted master SVGs parse as XML
import xml.etree.ElementTree as ET
for f in files_to_zip:
    if f.endswith('.svg'):
        p = os.path.join(test_dir, f)
        ET.parse(p)
print("PASS: All extracted master SVGs parse as valid XML.")
