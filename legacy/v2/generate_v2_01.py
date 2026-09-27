"""
FlowGrid - Page 01 (Foundations) Generator v2
"""
import os
import textwrap

os.makedirs('figma_svgs_v2', exist_ok=True)

def wrap_text(text, x, y, max_chars, line_height, font_family, font_size, fill, font_weight=400):
    lines = textwrap.wrap(text, width=max_chars)
    tspans = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else line_height
        tspans.append(f'<tspan x="{x}" dy="{dy}">{line}</tspan>')
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{font_family}" font-size="{font_size}" font-weight="{font_weight}">' + "".join(tspans) + '</text>'

svg_01 = f"""<svg width="2400" height="2050" viewBox="0 0 2400 2050" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="2400" height="2050" fill="#F4F1E8"/>
  
  <!-- Banner -->
  <rect x="80" y="80" width="2240" height="140" fill="#183B35" rx="4"/>
  <text x="120" y="145" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="36" font-weight="600">FlowGrid — Design System Foundations (Audited v2)</text>
  <text x="120" y="185" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="18">Color tokens, measured contrast ratios (WCAG 2.2 AA), bilingual typography scale, spacing units, and responsive layout grids</text>

  <!-- Section 1: Color Tokens & Contrast Ratios -->
  <rect x="80" y="260" width="1080" height="880" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="260" width="1080" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="293" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">01. Semantic Color Tokens &amp; Measured WCAG Contrast Ratios</text>

  <!-- Color Swatches Grid -->
  <g transform="translate(110, 340)">
    <!-- Swatch 1: Page Paper -->
    <rect x="0" y="0" width="220" height="110" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="2"/>
    <text x="15" y="35" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">surface.page</text>
    <text x="15" y="60" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">#F4F1E8</text>
    <text x="15" y="85" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12">Warm Paper Canvas</text>

    <!-- Swatch 2: Deep Pine -->
    <rect x="250" y="0" width="220" height="110" fill="#183B35" rx="2"/>
    <text x="265" y="35" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">text.primary / action</text>
    <text x="265" y="60" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="14">#183B35</text>
    <text x="265" y="85" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="12">Deep Pine Ink (10.84:1)</text>

    <!-- Swatch 3: Surface Mist -->
    <rect x="500" y="0" width="220" height="110" fill="#DEE7E2" stroke="#B8C2BA" stroke-width="1" rx="2"/>
    <text x="515" y="35" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">surface.mist</text>
    <text x="515" y="60" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">#DEE7E2</text>
    <text x="515" y="85" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12">Process Panel Surface</text>

    <!-- Swatch 4: Clay Accent -->
    <rect x="750" y="0" width="220" height="110" fill="#895239" rx="2"/>
    <text x="765" y="35" fill="#FFFFFF" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">accent.clay / focus</text>
    <text x="765" y="60" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14">#895239</text>
    <text x="765" y="85" fill="#FFFFFF" font-family="'Manrope', sans-serif" font-size="12">Terracotta (5.58:1)</text>

    <!-- Swatch 5: Text Secondary -->
    <rect x="0" y="130" width="220" height="110" fill="#56645E" rx="2"/>
    <text x="15" y="165" fill="#FFFFFF" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">text.secondary</text>
    <text x="15" y="190" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14">#56645E</text>
    <text x="15" y="215" fill="#FFFFFF" font-family="'Manrope', sans-serif" font-size="12">Supporting Text (5.50:1)</text>

    <!-- Swatch 6: Control Border -->
    <rect x="250" y="130" width="220" height="110" fill="#FFFFFF" stroke="#718178" stroke-width="2" rx="2"/>
    <text x="265" y="165" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">border.control</text>
    <text x="265" y="190" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">#718178</text>
    <text x="265" y="215" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12">Inputs &amp; Focus (3.64:1)</text>

    <!-- Swatch 7: Status Error -->
    <rect x="500" y="130" width="220" height="110" fill="#9B302B" rx="2"/>
    <text x="515" y="165" fill="#FFFFFF" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">status.error</text>
    <text x="515" y="190" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14">#9B302B</text>
    <text x="515" y="215" fill="#FFFFFF" font-family="'Manrope', sans-serif" font-size="12">Validation (6.52:1)</text>

    <!-- Swatch 8: Status Success -->
    <rect x="750" y="130" width="220" height="110" fill="#245C43" rx="2"/>
    <text x="765" y="165" fill="#FFFFFF" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">status.success</text>
    <text x="765" y="190" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14">#245C43</text>
    <text x="765" y="215" fill="#FFFFFF" font-family="'Manrope', sans-serif" font-size="12">Receipt (6.92:1)</text>
  </g>

  <!-- Contrast Ratios Table -->
  <rect x="110" y="630" width="1020" height="470" fill="#F4F1E8" rx="4"/>
  <text x="130" y="660" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Measured WCAG Contrast Checks (Design Phase Audit)</text>
  
  <text x="130" y="700" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Color Pair</text>
  <text x="450" y="700" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Hex Combination</text>
  <text x="730" y="700" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Contrast Ratio</text>
  <text x="920" y="700" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Evaluation</text>
  <line x1="130" y1="715" x2="1100" y2="715" stroke="#B8C2BA" stroke-width="1"/>

  <text x="130" y="745" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">Primary text / Paper</text>
  <text x="450" y="745" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">#183B35 on #F4F1E8</text>
  <text x="730" y="745" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">10.84 : 1</text>
  <text x="920" y="745" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Exceeds AAA (7.0:1)</text>

  <text x="130" y="785" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">White text / Action Pine</text>
  <text x="450" y="785" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">#FFFFFF on #183B35</text>
  <text x="730" y="785" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">12.24 : 1</text>
  <text x="920" y="785" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Exceeds AAA (7.0:1)</text>

  <text x="130" y="825" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">Secondary text / Paper</text>
  <text x="450" y="825" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">#56645E on #F4F1E8</text>
  <text x="730" y="825" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">5.50 : 1</text>
  <text x="920" y="825" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Meets AA (4.5:1)</text>

  <text x="130" y="865" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">Clay accent / Paper</text>
  <text x="450" y="865" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">#895239 on #F4F1E8</text>
  <text x="730" y="865" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">5.58 : 1</text>
  <text x="920" y="865" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Meets AA (4.5:1)</text>

  <text x="130" y="905" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">Error text / Paper</text>
  <text x="450" y="905" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">#9B302B on #F4F1E8</text>
  <text x="730" y="905" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">6.52 : 1</text>
  <text x="920" y="905" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Meets AA (4.5:1)</text>

  <text x="130" y="945" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">Success text / Paper</text>
  <text x="450" y="945" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">#245C43 on #F4F1E8</text>
  <text x="730" y="945" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">6.92 : 1</text>
  <text x="920" y="945" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Meets AA (4.5:1)</text>

  <text x="130" y="985" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">Control boundary / Paper</text>
  <text x="450" y="985" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">#718178 on #F4F1E8</text>
  <text x="730" y="985" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">3.64 : 1</text>
  <text x="920" y="985" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Meets UI (3.0:1)</text>

  <text x="130" y="1025" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">Primary text / Mist</text>
  <text x="450" y="1025" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">#183B35 on #DEE7E2</text>
  <text x="730" y="1025" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">9.69 : 1</text>
  <text x="920" y="1025" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Exceeds AAA (7.0:1)</text>
  <text x="130" y="1065" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">*Note: Contrast passes indicate palette compliance; full site AA certification requires implementation testing.</text>

  <!-- Section 2: Typography System -->
  <rect x="1200" y="260" width="1120" height="880" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="1200" y="260" width="1120" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="1230" y="293" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">02. Bilingual Typography Scale &amp; Bounded Text Rules</text>

  <g transform="translate(1230, 330)">
    <rect x="0" y="0" width="510" height="240" fill="#F4F1E8" rx="2"/>
    <text x="20" y="35" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">LATIN EDITORIAL DISPLAY — Bodoni Moda</text>
    <text x="20" y="80" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="36" font-weight="500">Room for everyday life.</text>
    <text x="20" y="125" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">• Desktop Hero: 88-112px / 1.02 line-height / Weight 500</text>
    <text x="20" y="150" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">• Mobile Hero: 44-52px / 1.08 line-height / Weight 500</text>
    <text x="20" y="175" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">• Section Titles: 48-64px / 1.10 line-height</text>
    {wrap_text("Usage: Architectural editorial headlines only. Never used for body copy.", 20, 205, 55, 18, "'Manrope', sans-serif", 12, "#183B35", 600)}

    <rect x="530" y="0" width="550" height="240" fill="#F4F1E8" rx="2"/>
    <text x="20" y="35" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">BANGLA PRIMARY DISPLAY &amp; UI — Noto Sans Bengali</text>
    <text x="20" y="80" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="28" font-weight="600">আপনার জীবনের ছন্দে, আপনার ঘর।</text>
    <text x="20" y="125" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">• Desktop Hero: 56-64px / 1.35 line-height / Weight 600</text>
    <text x="20" y="150" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">• Mobile Hero: 36-42px / 1.35 line-height / Weight 600</text>
    <text x="20" y="175" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">• Body reading: 18px / 1.75 line-height (prevents conjunct clipping)</text>
    {wrap_text("Rule: Never letter-space or italicize Bangla. Maintain natural ligature shaping.", 20, 205, 55, 18, "'Manrope', sans-serif", 12, "#183B35", 600)}
  </g>

  <!-- Typography Comparison & Scale Spec -->
  <g transform="translate(1230, 590)">
    <rect x="0" y="0" width="1080" height="510" fill="#F4F1E8" rx="2"/>
    <text x="20" y="35" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Latin Interface &amp; Body Text Specifications (Manrope)</text>
    {wrap_text("Body Copy Rule: Line length strictly limited to 45–70 characters (max-width 640px) to ensure optimal reading ergonomics across viewports. All text blocks use bounded wrapping containers.", 20, 65, 95, 20, "'Manrope', sans-serif", 13, "#56645E")}
    
    <g transform="translate(20, 120)">
      <rect x="0" y="0" width="1040" height="360" fill="#FFFFFF" stroke="#DEE7E2" stroke-width="1" rx="2"/>
      <text x="20" y="30" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">SCALE</text>
      <text x="200" y="30" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">FONT &amp; WEIGHT</text>
      <text x="450" y="30" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">DESKTOP</text>
      <text x="650" y="30" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">MOBILE</text>
      <text x="850" y="30" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">LINE-HEIGHT</text>
      <line x1="20" y1="45" x2="1020" y2="45" stroke="#B8C2BA" stroke-width="1"/>

      <text x="20" y="80" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Hero Display (EN)</text>
      <text x="200" y="80" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Bodoni Moda 500</text>
      <text x="450" y="80" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">88–112px</text>
      <text x="650" y="80" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">44–52px</text>
      <text x="850" y="80" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">1.02 / 1.08</text>

      <text x="20" y="120" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Hero Display (BN)</text>
      <text x="200" y="120" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Noto Sans Bengali 600</text>
      <text x="450" y="120" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">56–64px</text>
      <text x="650" y="120" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">36–42px</text>
      <text x="850" y="120" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">1.35</text>

      <text x="20" y="160" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Section Headings</text>
      <text x="200" y="160" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Bodoni Moda / Noto 600</text>
      <text x="450" y="160" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">48–64px / 36–42px</text>
      <text x="650" y="160" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">32–40px / 28–32px</text>
      <text x="850" y="160" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">1.10 / 1.40</text>

      <text x="20" y="200" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Project / Service Title</text>
      <text x="200" y="200" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Bodoni Moda / Noto 600</text>
      <text x="450" y="200" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">28–36px</text>
      <text x="650" y="200" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">24–28px</text>
      <text x="850" y="200" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">1.25 / 1.45</text>

      <text x="20" y="240" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Body Reading</text>
      <text x="200" y="240" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Manrope / Noto 400</text>
      <text x="450" y="240" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">18px</text>
      <text x="650" y="240" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">18px</text>
      <text x="850" y="240" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">1.60 / 1.75</text>

      <text x="20" y="280" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Controls &amp; Buttons</text>
      <text x="200" y="280" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Manrope 600 / Noto 600</text>
      <text x="450" y="280" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">16px</text>
      <text x="650" y="280" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">16–18px</text>
      <text x="850" y="280" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">1.50</text>

      <text x="20" y="320" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Secondary Metadata</text>
      <text x="200" y="320" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Manrope 400 / Noto 400</text>
      <text x="450" y="320" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">14px</text>
      <text x="650" y="320" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">16px</text>
      <text x="850" y="320" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">1.50 / 1.65</text>
    </g>
  </g>

  <!-- Section 3: Spacing Scale & Layout Grids -->
  <rect x="80" y="1170" width="2240" height="820" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="1170" width="2240" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="1203" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">03. Spacing Tokens, Radius Rules &amp; Responsive Layout Grids</text>

  <!-- Spacing Scale -->
  <g transform="translate(110, 1250)">
    <text x="0" y="0" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">8px Base Spacing Scale (with 4px Subdivisions):</text>
    
    <g transform="translate(0, 20)">
      <rect x="0" y="0" width="4" height="60" fill="#895239"/>
      <text x="0" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">4px</text>

      <rect x="40" y="0" width="8" height="60" fill="#895239"/>
      <text x="40" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">8px</text>

      <rect x="90" y="0" width="12" height="60" fill="#895239"/>
      <text x="90" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">12px</text>

      <rect x="150" y="0" width="16" height="60" fill="#895239"/>
      <text x="150" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">16px</text>

      <rect x="220" y="0" width="24" height="60" fill="#895239"/>
      <text x="220" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">24px</text>

      <rect x="300" y="0" width="32" height="60" fill="#895239"/>
      <text x="300" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">32px</text>

      <rect x="390" y="0" width="48" height="60" fill="#895239"/>
      <text x="390" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">48px</text>

      <rect x="500" y="0" width="64" height="60" fill="#895239"/>
      <text x="500" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">64px</text>

      <rect x="630" y="0" width="80" height="60" fill="#895239"/>
      <text x="630" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">80px</text>

      <rect x="780" y="0" width="96" height="60" fill="#895239"/>
      <text x="780" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">96px</text>

      <rect x="950" y="0" width="128" height="60" fill="#895239"/>
      <text x="950" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">128px</text>
    </g>
  </g>

  <!-- Responsive Grids -->
  <g transform="translate(110, 1390)">
    <text x="0" y="0" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Responsive Grids &amp; Viewport Adaptations:</text>

    <!-- Desktop Card -->
    <g transform="translate(0, 25)">
      <rect width="680" height="500" fill="#F4F1E8" rx="2"/>
      <text x="20" y="35" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Desktop Viewport (1440px and above)</text>
      <text x="20" y="65" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">• 12 Columns, Max Content Width: 1312px, Outer Gutters: 64px, Gap: 24px</text>
      <text x="20" y="90" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">• Asymmetrical 7/5 and 5/7 column project spreads</text>
      <text x="20" y="115" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">• Solid 88px header, zero translucent blur or floating pill navigation</text>
      <rect x="20" y="140" width="640" height="80" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1"/>
      <!-- 12 cols -->
      <g transform="translate(30, 150)">
        <rect x="0" y="0" width="40" height="60" fill="#DEE7E2"/>
        <rect x="52" y="0" width="40" height="60" fill="#DEE7E2"/>
        <rect x="104" y="0" width="40" height="60" fill="#DEE7E2"/>
        <rect x="156" y="0" width="40" height="60" fill="#DEE7E2"/>
        <rect x="208" y="0" width="40" height="60" fill="#DEE7E2"/>
        <rect x="260" y="0" width="40" height="60" fill="#DEE7E2"/>
        <rect x="312" y="0" width="40" height="60" fill="#DEE7E2"/>
        <rect x="364" y="0" width="40" height="60" fill="#DEE7E2"/>
        <rect x="416" y="0" width="40" height="60" fill="#DEE7E2"/>
        <rect x="468" y="0" width="40" height="60" fill="#DEE7E2"/>
        <rect x="520" y="0" width="40" height="60" fill="#DEE7E2"/>
        <rect x="572" y="0" width="40" height="60" fill="#DEE7E2"/>
      </g>
      {wrap_text("Radius Tokens: Media = 0px (pure architectural straight corners); Controls & Buttons = 2px; Overlays = 4px max. Default pill buttons are prohibited.", 20, 250, 75, 20, "'Manrope', sans-serif", 13, "#895239", 600)}
    </g>

    <!-- Tablet Card -->
    <g transform="translate(740, 25)">
      <rect width="680" height="500" fill="#F4F1E8" rx="2"/>
      <text x="20" y="35" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Tablet Viewport (768px – 1023px)</text>
      <text x="20" y="65" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">• 8 Columns, Outer Gutters: 32px, Column Gap: 24px</text>
      <text x="20" y="90" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">• Two-column cards collapse to balanced 4/4 or stacked 8-col blocks</text>
      <text x="20" y="115" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">• Header: 80px tall, compact menu drawer if links collide</text>
      <rect x="20" y="140" width="640" height="80" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1"/>
      <!-- 8 cols -->
      <g transform="translate(35, 150)">
        <rect x="0" y="0" width="60" height="60" fill="#DEE7E2"/>
        <rect x="77" y="0" width="60" height="60" fill="#DEE7E2"/>
        <rect x="154" y="0" width="60" height="60" fill="#DEE7E2"/>
        <rect x="231" y="0" width="60" height="60" fill="#DEE7E2"/>
        <rect x="308" y="0" width="60" height="60" fill="#DEE7E2"/>
        <rect x="385" y="0" width="60" height="60" fill="#DEE7E2"/>
        <rect x="462" y="0" width="60" height="60" fill="#DEE7E2"/>
        <rect x="539" y="0" width="60" height="60" fill="#DEE7E2"/>
      </g>
      {wrap_text("Responsive Adaptation: Maintain logical reading order. Never stack captions above their image during tablet collapse.", 20, 250, 75, 20, "'Manrope', sans-serif", 13, "#56645E")}
    </g>

    <!-- Mobile Card -->
    <g transform="translate(1480, 25)">
      <rect width="680" height="500" fill="#F4F1E8" rx="2"/>
      <text x="20" y="35" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Mobile Viewport (320px – 767px, Primary 390px)</text>
      <text x="20" y="65" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">• 4 Columns, Outer Gutters: 20px (16px at 320px), Gap: 16px</text>
      <text x="20" y="90" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">• Content-First Paper Hero: Title + CTA on paper BEFORE hero image</text>
      <text x="20" y="115" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">• Header: 72px tall with 48px touch-target Menu button</text>
      <rect x="20" y="140" width="640" height="80" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1"/>
      <!-- 4 cols -->
      <g transform="translate(35, 150)">
        <rect x="0" y="0" width="130" height="60" fill="#DEE7E2"/>
        <rect x="150" y="0" width="130" height="60" fill="#DEE7E2"/>
        <rect x="300" y="0" width="130" height="60" fill="#DEE7E2"/>
        <rect x="450" y="0" width="130" height="60" fill="#DEE7E2"/>
      </g>
      {wrap_text("Touch Accessibility: Minimum primary touch target is 48px (buttons 52px, inputs 52px). Persistent bottom contact bar automatically hidden on forms and drawer menus.", 20, 250, 75, 20, "'Manrope', sans-serif", 13, "#245C43", 600)}
    </g>
  </g>
</svg>"""

with open('figma_svgs_v2/01_foundations.svg', 'w', encoding='utf-8') as f:
    f.write(svg_01)

print("Saved figma_svgs_v2/01_foundations.svg")
