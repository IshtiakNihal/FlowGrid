"""
FlowGrid Design System - SVG Shared Utilities (v3)
Provides safe XML escaping, dynamic text wrapping with height computation,
and self-contained base64 image embedding.
"""
import textwrap
import base64
import os
import re
import xml.etree.ElementTree as ET

def escape_xml(text):
    if not isinstance(text, str):
        text = str(text)
    # Avoid double escaping already escaped entities
    text = re.sub(r'&(?!(amp|lt|gt|quot|apos|#\d+|#x[a-fA-F0-9]+);)', '&amp;', text)
    text = text.replace('<', '&lt;').replace('>', '&gt;')
    return text

def wrap_text(text, x, y, max_chars, line_height, font_family, font_size, fill, font_weight=400, text_anchor="start"):
    """
    Wraps text and returns (svg_text_element, total_height)
    """
    lines = textwrap.wrap(text, width=max_chars)
    if not lines:
        lines = [""]
    tspans = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else line_height
        safe_line = escape_xml(line)
        tspans.append(f'<tspan x="{x}" dy="{dy}">{safe_line}</tspan>')
    
    anchor_attr = f' text-anchor="{text_anchor}"' if text_anchor != "start" else ""
    svg_str = f'<text x="{x}" y="{y}" fill="{fill}" font-family="{font_family}" font-size="{font_size}" font-weight="{font_weight}"{anchor_attr}>' + "".join(tspans) + '</text>'
    total_height = len(lines) * line_height
    return svg_str, total_height

def get_base64_image(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            data = f.read()
        ext = os.path.splitext(path)[1].lower()
        mime = 'image/jpeg' if ext in ('.jpg', '.jpeg') else 'image/png'
        return f"data:{mime};base64,{base64.b64encode(data).decode('utf-8')}"
    return ""

def validate_svg_file(path):
    try:
        ET.parse(path)
        return True, "Valid XML"
    except ET.ParseError as e:
        return False, str(e)
