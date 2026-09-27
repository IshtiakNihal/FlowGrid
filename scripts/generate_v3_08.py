"""
FlowGrid - Page 08: Handoff & QA Generator (v3)
Reconciled contrast ratios, explicit pending implementation QA checks,
Core Web Vitals budgets, CSS tokens, and single owner fact confirmation register.
"""
import os
from svg_utils import wrap_text, escape_xml, validate_svg_file

def generate_board_08():
    w, h = 2800, 2600
    svg = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{w}" height="{h}" fill="#F4F1E8"/>')

    # Header Banner
    svg.append('<rect x="80" y="80" width="2640" height="140" fill="#183B35" rx="4"/>')
    svg.append('<text x="120" y="145" fill="#F4F1E8" font-family="\'Bodoni Moda\', serif" font-size="36" font-weight="600">FlowGrid — Developer Handoff, Accessibility QA &amp; Client Action Register (v3)</text>')
    svg.append('<text x="120" y="185" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="18">CSS custom properties, reconciled contrast calculations, explicit frontend implementation checklists, and owner business questionnaire</text>')

    # -------------------------------------------------------------
    # 01. CSS Custom Properties (:root Tokens)
    # -------------------------------------------------------------
    svg.append('<rect x="80" y="260" width="1300" height="740" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<rect x="80" y="260" width="1300" height="60" fill="#183B35" rx="4 4 0 0"/>')
    svg.append('<text x="110" y="300" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="20" font-weight="600">01. Production CSS Custom Properties (:root Design Tokens)</text>')

    svg.append('<rect x="110" y="350" width="1240" height="620" fill="#183B35" rx="4"/>')
    tokens_code = [
        ":root {",
        "  /* Surface & Base Canvas Tokens */",
        "  --fg-surface-page: #F4F1E8;         /* Warm architectural paper */",
        "  --fg-surface-clean: #FFFFFF;        /* Pure white input & card surface */",
        "  --fg-surface-mist: #DEE7E2;         /* Soft mist panels & secondary badges */",
        "",
        "  /* Typography & Ink Color Tokens */",
        "  --fg-text-primary: #183B35;         /* Deep pine ink (10.84:1 contrast ratio) */",
        "  --fg-text-secondary: #56645E;       /* Muted slate caption (5.50:1 contrast ratio) */",
        "  --fg-accent-clay: #895239;          /* Terracotta focus ring & badges (5.58:1) */",
        "",
        "  /* Status & Action Tokens */",
        "  --fg-border-control: #718178;       /* Slate border for inputs (3.64:1 UI target) */",
        "  --fg-status-error: #9B302B;         /* High-contrast validation crimson (6.52:1) */",
        "  --fg-status-success: #245C43;       /* Confirmed forest green (6.19:1 on mist) */",
        "  --fg-action-whatsapp: #0D5C52;      /* Accessible forest teal (6.20:1 with white) */",
        "",
        "  /* Spatial Rhythm & Geometry Tokens */",
        "  --fg-radius-media: 0px;             /* Strict architectural squared edges */",
        "  --fg-radius-control: 2px;           /* Subtle tactile corner softness */",
        "  --fg-radius-panel: 4px;             /* Modals and major spatial containers */",
        "  --fg-touch-min: 48px;               /* Minimum interactive hit area */",
        "}"
    ]
    tcy = 385
    for tline in tokens_code:
        col = "#895239" if tline.startswith("  /*") else ("#F4F1E8" if "{" in tline or "}" in tline else "#DEE7E2")
        svg.append(f'<text x="140" y="{tcy}" fill="{col}" font-family="monospace" font-size="13">{escape_xml(tline)}</text>')
        tcy += 24

    # -------------------------------------------------------------
    # 02. Measured Accessibility Audits & Pending Checks
    # -------------------------------------------------------------
    svg.append('<rect x="1420" y="260" width="1300" height="740" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<rect x="1420" y="260" width="1300" height="60" fill="#183B35" rx="4 4 0 0"/>')
    svg.append('<text x="1450" y="300" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="20" font-weight="600">02. Measured Accessibility Ratios &amp; Implementation Limits</text>')

    # Table of Reconciled Measured Pairs
    svg.append('<rect x="1450" y="340" width="1240" height="310" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<text x="1470" y="370" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="15" font-weight="700">Reconciled Relative Luminance Contrast Checks (WCAG 2.2 sRGB Formula):</text>')

    contrast_rows = [
        ("Deep Pine (#183B35) on Warm Paper (#F4F1E8)", "10.84 : 1", "PASS (AAA) · Commutative in both directions"),
        ("Muted Slate (#56645E) on Warm Paper (#F4F1E8)", "5.50 : 1", "PASS (AA) · Secondary copy & metadata"),
        ("Form Placeholder (#56645E) on White (#FFFFFF)", "6.21 : 1", "PASS (AA) · Replaced failing 1.83:1 placeholder"),
        ("Dark Footer Links (#DEE7E2) on Deep Pine (#183B35)", "9.69 : 1", "PASS (AAA) · Replaced failing 1.94:1 footer links"),
        ("Dark Footer Muted (#C4D1CA) on Deep Pine (#183B35)", "7.76 : 1", "PASS (AAA) · Replaced failing 1.97:1 footer text"),
        ("Terracotta Clay (#895239) on Warm Paper (#F4F1E8)", "5.58 : 1", "PASS (AA) · Category tags & focus rings"),
        ("Validation Crimson (#9B302B) on Warm Paper", "6.52 : 1", "PASS (AA) · Form error message text + icon"),
        ("Forest Green (#245C43) on Soft Mist (#DEE7E2)", "6.19 : 1", "PASS (AA) · Success confirmation banner"),
        ("Dark Forest Teal (#0D5C52) on White (#FFFFFF)", "7.87 : 1", "PASS (AAA) · WhatsApp action (replaces #128C7E 4.14:1)"),
        ("Dark Forest Teal (#0D5C52) on Warm Paper (#F4F1E8)", "6.96 : 1", "PASS (AA) · WhatsApp action on page canvas")
    ]
    cry = 398
    for c_pair, c_rat, c_eval in contrast_rows:
        svg.append(f'<text x="1470" y="{cry}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="12" font-weight="600">{escape_xml(c_pair)}:</text>')
        svg.append(f'<text x="1940" y="{cry}" fill="#895239" font-family="monospace" font-size="12" font-weight="700">{escape_xml(c_rat)}</text>')
        svg.append(f'<text x="2060" y="{cry}" fill="#245C43" font-family="\'Manrope\', sans-serif" font-size="11">{escape_xml(c_eval)}</text>')
        cry += 24

    # Pending Frontend Implementation Verification Block
    svg.append('<rect x="1450" y="665" width="1240" height="315" fill="#DEE7E2" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<text x="1470" y="695" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="15" font-weight="700">Explicit Pending Implementation Checklist (No Overstated Certification):</text>')

    qa_pending = [
        ("WCAG 1.4.12 Text Spacing:", "Pending DOM testing with user-injected stylesheets (1.5x line-height, 0.12em letter spacing, 0.16em word spacing) to guarantee zero clipped Bengali conjuncts or layout overlap."),
        ("WCAG 2.1.1 Keyboard Navigation:", "Pending React/HTML implementation to verify logical DOM tab order, visible focus rings (2px #895239 with 2px offset), and focus trapping inside the mobile navigation drawer."),
        ("WCAG 4.1.3 Status Messages:", "Pending frontend implementation of ARIA live regions (aria-live=\"polite\") for form submission feedback, loading spinners, and validation error announcements."),
        ("WCAG 1.4.10 Reflow (320px Viewport):", "Pending responsive browser verification to ensure no horizontal two-dimensional scrolling at 320px viewport width.")
    ]
    py = 725
    for q_tit, q_det in qa_pending:
        svg.append(f'<text x="1470" y="{py}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">[ ] {escape_xml(q_tit)}</text>')
        t_qd, _ = wrap_text(q_det, 1470, py+18, 92, 18, "'Manrope', sans-serif", 12, "#56645E")
        svg.append(t_qd)
        py += 58

    # -------------------------------------------------------------
    # 03. Core Web Vitals Performance Budgets
    # -------------------------------------------------------------
    svg.append('<rect x="80" y="1030" width="2640" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<rect x="80" y="1030" width="2640" height="60" fill="#183B35" rx="4 4 0 0"/>')
    svg.append('<text x="110" y="1070" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="20" font-weight="600">03. Core Web Vitals &amp; Performance Engineering Budgets</text>')

    budgets = [
        ("Largest Contentful Paint (LCP)", "< 1.8s (Good)", "Hero Image Optimization", "Preload hero photography in WebP/AVIF format with responsive srcset. Inline critical paper styling."),
        ("Cumulative Layout Shift (CLS)", "< 0.02 (Good)", "Layout Stability", "Strict aspect-ratio sizing on all photography containers (0px radius). Zero post-load height jumping."),
        ("Interaction to Next Paint (INP)", "< 120ms (Good)", "Input Responsiveness", "Lightweight JavaScript event listeners. Instant 150ms CSS color feedback on button presses."),
        ("Total Page Weight Budget", "< 1.4 MB Total", "Data Economy for Bangladesh", "Modern image compression, font subsetting for Noto Sans Bengali, zero bulky 3D WebGL libraries.")
    ]
    for b_idx, (b_name, b_target, b_focus, b_strat) in enumerate(budgets):
        bx = 110 + b_idx * 650
        by = 1120
        svg.append(f'<rect x="{bx}" y="{by}" width="620" height="300" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
        svg.append(f'<text x="{bx+20}" y="{by+40}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="18" font-weight="700">{escape_xml(b_name)}</text>')
        svg.append(f'<rect x="{bx+20}" y="{by+55}" width="160" height="30" fill="#183B35" rx="2"/>')
        svg.append(f'<text x="{bx+100}" y="{by+75}" fill="#F4F1E8" font-family="monospace" font-size="13" font-weight="700" text-anchor="middle">{escape_xml(b_target)}</text>')
        svg.append(f'<text x="{bx+20}" y="{by+120}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">Engineering Focus: {escape_xml(b_focus)}</text>')
        t_bs, _ = wrap_text(b_strat, bx+20, by+150, 42, 22, "'Manrope', sans-serif", 13, "#56645E")
        svg.append(t_bs)

    # -------------------------------------------------------------
    # 04. Single Actionable Client Business Questionnaire
    # -------------------------------------------------------------
    svg.append('<rect x="80" y="1480" width="2640" height="1060" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<rect x="80" y="1480" width="2640" height="60" fill="#183B35" rx="4 4 0 0"/>')
    svg.append('<text x="110" y="1520" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="20" font-weight="600">04. Actionable Client Business Questionnaire (Operational Fact Confirmation)</text>')

    questions = [
        ("1. Official Vector Logo & Wordmark", "Design currently uses typographic Bodoni Moda / Noto Sans Bengali. Please supply final production SVG/AI vector file if a dedicated geometric logo exists."),
        ("2. Designated Contact Phone & WhatsApp", "Design provisions placeholder +880 1700-000000 (observed FB: 01712-402422). Please confirm the authorized Bangladesh mobile line for public calls and WhatsApp."),
        ("3. Studio Location & Workshop Address", "Design provisions Mirpur-10, Dhaka 1216 based on Facebook audit. Please confirm exact street, building number, and whether client site visits are hosted at the workshop."),
        ("4. Commercial Delivery Model", "Please confirm if FlowGrid provides design-only consultancy (2D drawings, 3D renders, BOQ), turnkey fabrication & joinery execution, or both service tiers."),
        ("5. Spatial Assessment & Site Visit Policy", "Please clarify if initial on-site spatial assessment in Dhaka is complimentary, or subject to a consultation fee credited toward contract signing."),
        ("6. Verified Studio Team Profiles", "Please provide verified names, professional backgrounds, and authorized photographs for the Studio page team leadership section."),
        ("7. Authorized Founder Statement (Rumi)", "Please authorize exact copy describing Rumi's founder / community relationship to FlowGrid, strictly distinct from architectural practice."),
        ("8. Production Domain & DNS Activation", "Please authorize DNS activation for www.flowgrid-interiors.com or confirm alternative production web address.")
    ]
    qy = 1580
    for q_no, q_txt in questions:
        svg.append(f'<rect x="110" y="{qy}" width="2580" height="105" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
        svg.append(f'<text x="130" y="{qy+35}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="16" font-weight="700">{escape_xml(q_no)}</text>')
        t_qt, _ = wrap_text(q_txt, 130, qy+65, 150, 20, "'Manrope', sans-serif", 13, "#56645E")
        svg.append(t_qt)
        qy += 125

    svg.append('</svg>')

    out_path = 'figma_svgs_v3/08_handoff_qa.svg'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    
    valid, err = validate_svg_file(out_path)
    print(f'Board 08: {out_path} -> Valid XML? {valid} ({err})')

if __name__ == '__main__':
    generate_board_08()
