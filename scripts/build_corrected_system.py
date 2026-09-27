"""
FlowGrid - Corrected Master Generation Script
Generates comprehensive, non-overflowing, fully structured SVG suites for all 9 Figma pages.
Includes full scope: Home, Projects, Case Study, Services, Process, Studio, Contact (all states), Privacy, 404
across Bangla Desktop, Bangla Mobile, and English equivalents.
"""
import os
import base64
import textwrap

os.makedirs('figma_svgs_v2', exist_ok=True)

def get_base64_image(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            data = base64.b64encode(f.read()).decode('utf-8')
            ext = 'jpeg' if path.endswith('.jpg') else 'png'
            return f"data:image/{ext};base64,{data}"
    return ""

img_living_1 = get_base64_image('concepts/concept_01_living_dhaka.jpg')
img_living_2 = get_base64_image('concepts/concept_01_living_alt.jpg')
img_living_3 = get_base64_image('concepts/concept_01_joinery_detail.jpg')
img_kitchen = get_base64_image('concepts/concept_02_kitchen_dhaka.jpg')
img_bedroom = get_base64_image('concepts/concept_03_bedroom_dhaka.jpg')

def svg_text_wrapped(text, x, y, max_chars, line_height, font_family, font_size, fill, font_weight=400, letter_spacing=0):
    lines = textwrap.wrap(text, width=max_chars)
    tspans = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else line_height
        tspans.append(f'<tspan x="{x}" dy="{dy}">{line}</tspan>')
    ls_attr = f' letter-spacing="{letter_spacing}"' if letter_spacing else ''
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{font_family}" font-size="{font_size}" font-weight="{font_weight}"{ls_attr}>' + "".join(tspans) + '</text>'

print("Helper loaded.")
