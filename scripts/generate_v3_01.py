"""
FlowGrid - Page 01: Foundations Generator (v3)
Reconciled contrast ratios, typography hierarchy, 48px touch targets, 0-2px radii.
"""
import os
from svg_utils import wrap_text, escape_xml, validate_svg_file

def generate_board_01():
    w, h = 2400, 2050
    svg = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{w}" height="{h}" fill="#F4F1E8"/>')
    
    # Header Banner
    svg.append('<rect x="80" y="80" width="2240" height="140" fill="#183B35" rx="4"/>')
    svg.append('<text x="120" y="145" fill="#F4F1E8" font-family="\'Bodoni Moda\', serif" font-size="36" font-weight="600">FlowGrid — Design Foundations &amp; System Tokens (v3)</text>')
    svg.append('<text x="120" y="185" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="18">Semantic color tokens, verified contrast metrics, bilingual typography scale, spatial rhythm, and responsive grids</text>')

    # Section 01: Semantic Color Tokens & Reconciled Contrast Ratios
    svg.append('<rect x="80" y="260" width="2240" height="640" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<rect x="80" y="260" width="2240" height="60" fill="#183B35" rx="4 4 0 0"/>')
    svg.append('<text x="110" y="300" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="20" font-weight="600">01. Semantic Color Tokens &amp; Mathematically Verified Contrast Ratios</text>')

    colors = [
        ("surface.page", "#F4F1E8", "Warm Paper", "Primary page surface & warm architectural canvas", "Base Canvas", "N/A"),
        ("text.primary", "#183B35", "Deep Pine Ink", "Headlines, body text, primary button background", "10.84 : 1", "PASS (AAA)"),
        ("text.secondary", "#56645E", "Muted Pine Slate", "Supporting copy, captions, timestamps, input placeholders", "5.50 : 1", "PASS (AA)"),
        ("accent.clay", "#895239", "Terracotta Clay", "Focus rings, category badges, section numbers", "5.58 : 1", "PASS (AA)"),
        ("surface.clean", "#FFFFFF", "Pure White", "Form inputs, card surfaces, modal overlays", "1.15 : 1", "Surface"),
        ("surface.mist", "#DEE7E2", "Soft Mist", "Process steps, table headers; dark footer links (9.69:1 on #183B35)", "9.69 : 1", "PASS (AAA)"),
        ("border.control", "#718178", "Slate Border", "Form input borders, outlined buttons (Non-text UI)", "3.64 : 1", "PASS (UI)"),
        ("status.error", "#9B302B", "Crimson Error", "Form validation error text and error outline states", "6.52 : 1", "PASS (AA)"),
        ("status.success", "#245C43", "Forest Success", "Confirmed receipt banners and success icons (on Mist)", "6.19 : 1", "PASS (AA)"),
        ("action.whatsapp", "#0D5C52", "Dark Forest Teal", "Accessible WhatsApp: 7.87:1 on #FFFFFF, 6.96:1 on #F4F1E8", "7.87 : 1", "PASS (AAA)")
    ]

    for idx, (token, hex_val, name, desc, ratio, comp) in enumerate(colors):
        col = idx % 5
        row = idx // 5
        cx = 110 + col * 440
        cy = 350 + row * 260
        
        svg.append(f'<rect x="{cx}" y="{cy}" width="410" height="230" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
        svg.append(f'<rect x="{cx+15}" y="{cy+15}" width="380" height="70" fill="{hex_val}" stroke="#B8C2BA" stroke-width="0.5" rx="2"/>')
        
        tc = "#FFFFFF" if hex_val in ("#183B35", "#56645E", "#895239", "#9B302B", "#245C43", "#0D5C52") else "#183B35"
        svg.append(f'<text x="{cx+30}" y="{cy+55}" fill="{tc}" font-family="\'Manrope\', sans-serif" font-size="16" font-weight="700">{hex_val}</text>')
        
        svg.append(f'<text x="{cx+15}" y="{cy+110}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="15" font-weight="700">{name}</text>')
        svg.append(f'<text x="{cx+15}" y="{cy+130}" fill="#895239" font-family="monospace" font-size="12">{token}</text>')
        
        td, _ = wrap_text(desc, cx+15, cy+155, 38, 16, "'Manrope', sans-serif", 12, "#56645E")
        svg.append(td)
        
        svg.append(f'<rect x="{cx+15}" y="{cy+195}" width="380" height="24" fill="#FFFFFF" rx="2"/>')
        svg.append(f'<text x="{cx+25}" y="{cy+212}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="12" font-weight="600">Contrast: {ratio}</text>')
        badge_c = "#245C43" if "PASS" in comp else "#56645E"
        svg.append(f'<text x="{cx+380}" y="{cy+212}" fill="{badge_c}" font-family="\'Manrope\', sans-serif" font-size="12" font-weight="700" text-anchor="end">{comp}</text>')

    # Section 02: Bilingual Typography Scale
    svg.append('<rect x="80" y="930" width="1100" height="660" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<rect x="80" y="930" width="1100" height="60" fill="#183B35" rx="4 4 0 0"/>')
    svg.append('<text x="110" y="970" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="20" font-weight="600">02. Bilingual Typography Hierarchy</text>')

    type_levels = [
        ("Hero Display (EN)", "Bodoni Moda 600", "88px / 1.05", "Architecture of everyday calm in Dhaka"),
        ("Hero Display (BN)", "Noto Sans Bengali 600", "56px / 1.35", "দৈনন্দিন জীবনের শান্ত ও সুবিন্যস্ত স্থাপত্য"),
        ("Section Title (EN)", "Bodoni Moda 500", "44px / 1.15", "Resilient joinery for urban apartments"),
        ("Section Title (BN)", "Noto Sans Bengali 600", "36px / 1.40", "টেকসই কাঠের কাজ ও ব্যবহারিক নকশা"),
        ("Body Text (BN)", "Noto Sans Bengali 400", "17px / 1.75", "ঢাকার আধুনিক অ্যাপার্টমেন্টে প্রয়োজনীয় স্থান ও স্টোরেজের ভারসাম্য বজায় রাখা।"),
        ("Body Text (EN)", "Manrope 400", "16px / 1.60", "Balancing spatial elegance, natural light, and heavy cooking demands."),
        ("UI & Controls (Multi)", "Manrope 600 / Noto 600", "15px / 1.50", "পরামর্শ শুরু করুন / Book Consultation (Min 48px hit area)")
    ]

    ty = 1030
    for level, font, size, sample in type_levels:
        svg.append(f'<text x="110" y="{ty}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">{escape_xml(level)} — {escape_xml(font)} ({escape_xml(size)})</text>')
        font_f = "'Bodoni Moda', serif" if "Bodoni" in font else ("'Noto Sans Bengali', sans-serif" if "Noto" in font else "'Manrope', sans-serif")
        font_s = 26 if "Hero" in level else (20 if "Section" in level else 15)
        svg.append(f'<text x="110" y="{ty+30}" fill="#183B35" font-family="{font_f}" font-size="{font_s}">{escape_xml(sample)}</text>')
        svg.append(f'<line x1="110" y1="{ty+48}" x2="1140" y2="{ty+48}" stroke="#DEE7E2" stroke-width="1"/>')
        ty += 78

    # Section 03: Spatial Rhythm & Radii
    svg.append('<rect x="1220" y="930" width="1100" height="660" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<rect x="1220" y="930" width="1100" height="60" fill="#183B35" rx="4 4 0 0"/>')
    svg.append('<text x="1250" y="970" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="20" font-weight="600">03. Spatial System, Radii &amp; Touch Targets</text>')

    spaces = [
        ("4px", "Micro spacing between inline icons and text"),
        ("8px", "Compact padding inside tags and pills"),
        ("12px", "Input internal vertical padding"),
        ("16px", "Standard input horizontal padding, card content padding"),
        ("24px", "Grid gutter, stack spacing between form fields"),
        ("32px", "Medium section spacing, dialog inset"),
        ("48px", "Standard button height, minimum touch target (48x48px)"),
        ("64px", "Desktop module spacing, header separation"),
        ("80px", "Desktop section vertical rhythm, desktop header height"),
        ("128px", "Major architectural page block transition")
    ]
    sy = 1025
    for s_val, s_desc in spaces:
        svg.append(f'<rect x="1250" y="{sy}" width="70" height="24" fill="#DEE7E2" rx="2"/>')
        svg.append(f'<text x="1285" y="{sy+17}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700" text-anchor="middle">{s_val}</text>')
        svg.append(f'<text x="1340" y="{sy+17}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="14">{escape_xml(s_desc)}</text>')
        sy += 36

    svg.append('<rect x="1250" y="1410" width="1040" height="150" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<text x="1270" y="1440" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="16" font-weight="700">Strict Architectural Radius Policy:</text>')
    t_rad, _ = wrap_text("• Media & Photography: 0px (Strict architectural squared edges. Never rounded).\n• Interactive Controls & Inputs: 2px (Subtle tactile softness, never pill-shaped).\n• Modals, Drawers & Cards: 4px (Maximum radius for major spatial panels).\n• Touch Targets: Every interactive element has an active hit area of at least 48 × 48 px.", 1270, 1470, 80, 20, "'Manrope', sans-serif", 13, "#56645E")
    svg.append(t_rad)

    # Section 04: Responsive Layout Grids
    svg.append('<rect x="80" y="1620" width="2240" height="360" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<rect x="80" y="1620" width="2240" height="60" fill="#183B35" rx="4 4 0 0"/>')
    svg.append('<text x="110" y="1660" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="20" font-weight="600">04. Responsive Layout Breakpoints &amp; Fluid Scale</text>')

    bps = [
        ("Desktop Large (1920px)", "12 Columns", "1312px Max Container", "Gutter 32px, Margin Auto", "Wide monitors, luxury portfolio viewing"),
        ("Desktop Primary (1440px)", "12 Columns", "1280px Container", "Gutter 24px, Margin 80px", "Primary master design baseline"),
        ("Tablet Landscape (1024px)", "8 Columns", "960px Container", "Gutter 20px, Margin 32px", "Compact laptops & horizontal tablets"),
        ("Tablet Portrait (768px)", "8 Columns", "Fluid Container", "Gutter 16px, Margin 24px", "iPad and vertical tablet browsing"),
        ("Mobile Primary (390px)", "4 Columns", "350px Fluid Container", "Gutter 12px, Margin 20px", "iPhone 14/15/16 baseline; full depth"),
        ("Mobile Narrow (320px)", "4 Columns", "288px Fluid Container", "Gutter 8px, Margin 16px", "WCAG Reflow compliance minimum")
    ]
    for b_idx, (b_title, b_cols, b_cont, b_gut, b_use) in enumerate(bps):
        bx = 110 + (b_idx % 3) * 740
        by = 1710 + (b_idx // 3) * 125
        svg.append(f'<rect x="{bx}" y="{by}" width="710" height="105" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
        svg.append(f'<text x="{bx+20}" y="{by+28}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="16" font-weight="700">{escape_xml(b_title)}</text>')
        svg.append(f'<text x="{bx+20}" y="{by+54}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600">{escape_xml(b_cols)} · {escape_xml(b_cont)} · {escape_xml(b_gut)}</text>')
        svg.append(f'<text x="{bx+20}" y="{by+80}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">{escape_xml(b_use)}</text>')

    svg.append('</svg>')

    out_path = 'figma_svgs_v3/01_foundations.svg'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    
    valid, err = validate_svg_file(out_path)
    print(f'Board 01: {out_path} -> Valid XML? {valid} ({err})')

if __name__ == '__main__':
    generate_board_01()
