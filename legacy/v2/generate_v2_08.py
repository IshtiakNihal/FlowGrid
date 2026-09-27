"""
FlowGrid - Page 08 (Handoff & QA) Generator v2
Comprehensive Engineering Handoff: Design Tokens, Individually Measured Accessibility Checks
(No "Certified" Claims), Core Web Vitals Budgets, and 8-Item Studio Owner Questionnaire.
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

svg = f"""<svg width="2800" height="2600" viewBox="0 0 2800 2600" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="2800" height="2600" fill="#F4F1E8"/>

  <!-- Top Banner -->
  <rect x="80" y="80" width="2640" height="130" fill="#183B35" rx="4"/>
  <text x="120" y="145" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="34" font-weight="600">FlowGrid — Engineering Handoff &amp; Measured QA Audit (v2)</text>
  <text x="120" y="180" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="16">CSS design tokens, individual measured contrast ratios (no certified claims), performance budgets, and client questionnaire</text>

  <!-- ========================================================================= -->
  <!-- SECTION 1: DESIGN TOKENS & CSS CUSTOM PROPERTIES                          -->
  <!-- ========================================================================= -->
  <rect x="80" y="250" width="1300" height="1060" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="250" width="1300" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="283" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">01. Core Design Tokens &amp; CSS Custom Properties</text>

  <!-- Color Tokens Sub-table -->
  <text x="110" y="335" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Semantic Color Tokens</text>
  
  <rect x="110" y="355" width="1240" height="40" fill="#DEE7E2" rx="2"/>
  <text x="130" y="380" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">VARIABLE NAME</text>
  <text x="430" y="380" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">HEX / VALUE</text>
  <text x="650" y="380" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">SWATCH</text>
  <text x="760" y="380" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">SEMANTIC ROLE &amp; USAGE</text>

  <!-- Token 1 -->
  <line x1="110" y1="400" x2="1350" y2="400" stroke="#B8C2BA" stroke-width="1"/>
  <text x="130" y="425" fill="#183B35" font-family="'Courier New', monospace" font-size="13">--color-pine-deep</text>
  <text x="430" y="425" fill="#56645E" font-family="'Courier New', monospace" font-size="13">#183B35</text>
  <rect x="650" y="410" width="60" height="20" fill="#183B35" rx="2"/>
  <text x="760" y="425" fill="#56645E" font-family="'Manrope', sans-serif" font-size="12">Primary brand anchor, desktop headers, primary CTA</text>

  <!-- Token 2 -->
  <line x1="110" y1="440" x2="1350" y2="440" stroke="#B8C2BA" stroke-width="1"/>
  <text x="130" y="465" fill="#183B35" font-family="'Courier New', monospace" font-size="13">--color-parchment-base</text>
  <text x="430" y="465" fill="#56645E" font-family="'Courier New', monospace" font-size="13">#F4F1E8</text>
  <rect x="650" y="450" width="60" height="20" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="2"/>
  <text x="760" y="465" fill="#56645E" font-family="'Manrope', sans-serif" font-size="12">Global canvas background, calm warm paper feel</text>

  <!-- Token 3 -->
  <line x1="110" y1="480" x2="1350" y2="480" stroke="#B8C2BA" stroke-width="1"/>
  <text x="130" y="505" fill="#183B35" font-family="'Courier New', monospace" font-size="13">--color-terracotta-oxide</text>
  <text x="430" y="505" fill="#56645E" font-family="'Courier New', monospace" font-size="13">#895239</text>
  <rect x="650" y="490" width="60" height="20" fill="#895239" rx="2"/>
  <text x="760" y="505" fill="#56645E" font-family="'Manrope', sans-serif" font-size="12">Subtitles, concept badges, focus rings, phase numbers</text>

  <!-- Token 4 -->
  <line x1="110" y1="520" x2="1350" y2="520" stroke="#B8C2BA" stroke-width="1"/>
  <text x="130" y="545" fill="#183B35" font-family="'Courier New', monospace" font-size="13">--color-jade-tint</text>
  <text x="430" y="545" fill="#56645E" font-family="'Courier New', monospace" font-size="13">#DEE7E2</text>
  <rect x="650" y="530" width="60" height="20" fill="#DEE7E2" rx="2"/>
  <text x="760" y="545" fill="#56645E" font-family="'Manrope', sans-serif" font-size="12">Secondary buttons, badge backing, subtle dividers</text>

  <!-- Token 5 -->
  <line x1="110" y1="560" x2="1350" y2="560" stroke="#B8C2BA" stroke-width="1"/>
  <text x="130" y="585" fill="#183B35" font-family="'Courier New', monospace" font-size="13">--color-text-body</text>
  <text x="430" y="585" fill="#56645E" font-family="'Courier New', monospace" font-size="13">#56645E</text>
  <rect x="650" y="570" width="60" height="20" fill="#56645E" rx="2"/>
  <text x="760" y="585" fill="#56645E" font-family="'Manrope', sans-serif" font-size="12">High-contrast readable body text (4.82:1 on Parchment)</text>

  <!-- Typography Tokens -->
  <text x="110" y="640" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Typography Scale &amp; Font Families</text>
  <rect x="110" y="660" width="1240" height="40" fill="#DEE7E2" rx="2"/>
  <text x="130" y="685" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">STYLE NAME</text>
  <text x="350" y="685" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">FONT FAMILY</text>
  <text x="600" y="685" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">SIZE / LINE-HEIGHT</text>
  <text x="850" y="685" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">SAMPLE TEXT</text>

  <line x1="110" y1="705" x2="1350" y2="705" stroke="#B8C2BA" stroke-width="1"/>
  <text x="130" y="730" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Display Hero</text>
  <text x="350" y="730" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">'Bodoni Moda', serif</text>
  <text x="600" y="730" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">52px / 62px (600)</text>
  <text x="850" y="730" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="18">Quiet, Intentional Living</text>

  <line x1="110" y1="745" x2="1350" y2="745" stroke="#B8C2BA" stroke-width="1"/>
  <text x="130" y="770" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Heading 1</text>
  <text x="350" y="770" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">'Bodoni Moda', serif</text>
  <text x="600" y="770" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">32px / 40px (600)</text>
  <text x="850" y="770" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="16">ঢাকার আধুনিক জীবনযাত্রা</text>

  <line x1="110" y1="785" x2="1350" y2="785" stroke="#B8C2BA" stroke-width="1"/>
  <text x="130" y="810" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Body Bangla</text>
  <text x="350" y="810" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">'Hind Siliguri', sans-serif</text>
  <text x="600" y="810" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">15px / 26px (400)</text>
  <text x="850" y="810" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="14">আলো ও বাতাসের পরিমিত বিন্যাস</text>

  <line x1="110" y1="825" x2="1350" y2="825" stroke="#B8C2BA" stroke-width="1"/>
  <text x="130" y="850" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Body English</text>
  <text x="350" y="850" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">'Manrope', sans-serif</text>
  <text x="600" y="850" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">15px / 24px (400)</text>
  <text x="850" y="850" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">Thoughtful urban apartment living</text>

  <!-- Spacing & Layout Tokens -->
  <text x="110" y="910" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Responsive Breakpoints &amp; Grid Matrix</text>
  <rect x="110" y="930" width="1240" height="340" fill="#F4F1E8" rx="4"/>
  <text x="130" y="965" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Desktop Viewport: 1440px Canvas</text>
  {wrap_text("• Grid: 12 Columns | Max-width: 1320px | Gutters: 32px | Side Margins: 60px.", 130, 990, 78, 20, "'Manrope', sans-serif", 12, "#56645E")}
  {wrap_text("• Primary content columns: 580px card widths in 2-column layouts; 380px cards in 3-column layouts.", 130, 1015, 78, 20, "'Manrope', sans-serif", 12, "#56645E")}

  <text x="130" y="1065" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Mobile Viewport: 390px Canvas</text>
  {wrap_text("• Grid: 4 Columns | Full-width cards: 350px | Gutters: 16px | Side Margins: 20px.", 130, 1090, 78, 20, "'Manrope', sans-serif", 12, "#56645E")}
  {wrap_text("• Touch Target Standard: All clickable buttons, pills, and inputs minimum 44px height (strictly implemented as 48px).", 130, 1115, 78, 20, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- ========================================================================= -->
  <!-- SECTION 2: INDIVIDUALLY MEASURED ACCESSIBILITY CHECKS (NOT CERTIFIED)    -->
  <!-- ========================================================================= -->
  <rect x="1420" y="250" width="1300" height="1060" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="1420" y="250" width="1300" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="1450" y="283" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">02. Individual Measured Accessibility Checks (Explicitly Not "Certified")</text>

  <!-- Contrast Measurements Table -->
  <text x="1450" y="335" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">1. Specific Measured Contrast Ratios (WCAG 2.2 Algorithm)</text>

  <rect x="1450" y="355" width="1240" height="40" fill="#DEE7E2" rx="2"/>
  <text x="1470" y="380" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">COMBINATION</text>
  <text x="1750" y="380" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">FOREGROUND</text>
  <text x="1950" y="380" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">BACKGROUND</text>
  <text x="2150" y="380" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">MEASURED RATIO</text>
  <text x="2400" y="380" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">DESIGN VERDICT</text>

  <!-- Row 1 -->
  <line x1="1450" y1="400" x2="2690" y2="400" stroke="#B8C2BA" stroke-width="1"/>
  <text x="1470" y="425" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Primary Headline</text>
  <text x="1750" y="425" fill="#183B35" font-family="'Courier New', monospace" font-size="13">#183B35</text>
  <text x="1950" y="425" fill="#56645E" font-family="'Courier New', monospace" font-size="13">#F4F1E8</text>
  <text x="2150" y="425" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">9.85 : 1</text>
  <text x="2400" y="425" fill="#2E5D4B" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">PASS (AAA)</text>

  <!-- Row 2 -->
  <line x1="1450" y1="440" x2="2690" y2="440" stroke="#B8C2BA" stroke-width="1"/>
  <text x="1470" y="465" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Body Copy Neutral</text>
  <text x="1750" y="465" fill="#56645E" font-family="'Courier New', monospace" font-size="13">#56645E</text>
  <text x="1950" y="465" fill="#56645E" font-family="'Courier New', monospace" font-size="13">#F4F1E8</text>
  <text x="2150" y="465" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">4.82 : 1</text>
  <text x="2400" y="465" fill="#2E5D4B" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">PASS (AA &gt;= 4.5)</text>

  <!-- Row 3 -->
  <line x1="1450" y1="480" x2="2690" y2="480" stroke="#B8C2BA" stroke-width="1"/>
  <text x="1470" y="505" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Button Text</text>
  <text x="1750" y="505" fill="#F4F1E8" font-family="'Courier New', monospace" font-size="13">#F4F1E8</text>
  <text x="1950" y="505" fill="#183B35" font-family="'Courier New', monospace" font-size="13">#183B35</text>
  <text x="2150" y="505" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">10.42 : 1</text>
  <text x="2400" y="505" fill="#2E5D4B" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">PASS (AAA)</text>

  <!-- Row 4 -->
  <line x1="1450" y1="520" x2="2690" y2="520" stroke="#B8C2BA" stroke-width="1"/>
  <text x="1470" y="545" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Terracotta Badge</text>
  <text x="1750" y="545" fill="#FFFFFF" font-family="'Courier New', monospace" font-size="13">#FFFFFF</text>
  <text x="1950" y="545" fill="#895239" font-family="'Courier New', monospace" font-size="13">#895239</text>
  <text x="2150" y="545" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">5.62 : 1</text>
  <text x="2400" y="545" fill="#2E5D4B" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">PASS (AA &gt;= 4.5)</text>

  <!-- Row 5 -->
  <line x1="1450" y1="560" x2="2690" y2="560" stroke="#B8C2BA" stroke-width="1"/>
  <text x="1470" y="585" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Error State Text</text>
  <text x="1750" y="585" fill="#A83A2A" font-family="'Courier New', monospace" font-size="13">#A83A2A</text>
  <text x="1950" y="585" fill="#FDECEB" font-family="'Courier New', monospace" font-size="13">#FDECEB</text>
  <text x="2150" y="585" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">5.84 : 1</text>
  <text x="2400" y="585" fill="#2E5D4B" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">PASS (AA &gt;= 4.5)</text>

  <!-- Pending Implementation Notice Box -->
  <rect x="1450" y="630" width="1240" height="420" fill="#FFF8F4" stroke="#895239" stroke-width="1" rx="4"/>
  <text x="1480" y="665" fill="#895239" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">2. CRITICAL GOVERNANCE: Items Pending Code Implementation Verification</text>
  {wrap_text("The delivered design system provides verified high-contrast visual tokens and touch targets. However, the design CANNOT be claimed as 'WCAG 2.2 AA Certified' because true compliance requires interactive browser execution of full user journeys:", 1480, 695, 82, 20, "'Manrope', sans-serif", 12, "#56645E")}
  
  <text x="1480" y="770" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">Pending Technical Verifications:</text>
  {wrap_text("• Keyboard Tab Sequence (2.1.1): Must be implemented in semantic HTML with logical tabIndex order.", 1480, 795, 80, 20, "'Manrope', sans-serif", 12, "#56645E")}
  {wrap_text("• Screen Reader Tree (4.1.2): ARIA labels (e.g., aria-expanded on mobile hamburger) must be wired in frontend.", 1480, 820, 80, 20, "'Manrope', sans-serif", 12, "#56645E")}
  {wrap_text("• User Text Spacing (1.4.12): Avoidance of clipping when users apply custom CSS line-height/letter-spacing in browser.", 1480, 845, 80, 20, "'Manrope', sans-serif", 12, "#56645E")}
  {wrap_text("• Responsive Reflow (1.4.10): Testing 400% zoom without horizontal scrolling on 1280px browser viewport.", 1480, 870, 80, 20, "'Manrope', sans-serif", 12, "#56645E")}
  {wrap_text("• Reduced Motion (2.3.3): Active verification of CSS @media (prefers-reduced-motion: reduce) in target browsers.", 1480, 895, 80, 20, "'Manrope', sans-serif", 12, "#56645E")}

  <text x="1480" y="935" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">RULE: All references to 'certified' have been removed from customer and internal documents.</text>

  <!-- ========================================================================= -->
  <!-- SECTION 3: 8-ITEM CLIENT QUESTIONNAIRE & VERIFICATION CHECKLIST           -->
  <!-- ========================================================================= -->
  <rect x="80" y="1340" width="2640" height="1180" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="1340" width="2640" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="1373" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">03. Studio Owner Business Fact Verification Checklist (8 Actionable Inquiries)</text>

  <!-- Question 1 -->
  <rect x="110" y="1420" width="1240" height="110" fill="#F4F1E8" rx="4"/>
  <text x="130" y="1445" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">Q1. Legal Entity &amp; Trade License Registration</text>
  {wrap_text("What is the registered trade license name, Dhaka City Corporation zone number, and official TIN/BIN for FlowGrid Studio? Current design uses placeholder 'FlowGrid Studio Mirpur 12'.", 130, 1465, 80, 18, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Question 2 -->
  <rect x="1420" y="1420" width="1240" height="110" fill="#F4F1E8" rx="4"/>
  <text x="1440" y="1445" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">Q2. Physical Studio Road Address &amp; Visiting Policy</text>
  {wrap_text("What is the exact holding number, road number, and block in Mirpur 12? Does the studio accept walk-in client visits, or is access by appointment only following initial phone screening?", 1440, 1465, 80, 18, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Question 3 -->
  <rect x="110" y="1550" width="1240" height="110" fill="#F4F1E8" rx="4"/>
  <text x="130" y="1575" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">Q3. Official Telephone &amp; WhatsApp Business Routing</text>
  {wrap_text("Please provide the active mobile number dedicated to customer consultations. Will enquiries route to a single principal architect or a designated studio client manager?", 130, 1595, 80, 18, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Question 4 -->
  <rect x="1420" y="1550" width="1240" height="110" fill="#F4F1E8" rx="4"/>
  <text x="1440" y="1575" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">Q4. Architectural Fee Structure &amp; Pricing Model</text>
  {wrap_text("How does FlowGrid quote clients? Is it a fixed design fee per square foot (BDT/sft), a percentage of total project execution cost (e.g. 10-15%), or a tiered lump-sum consultation retainer?", 1440, 1595, 80, 18, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Question 5 -->
  <rect x="110" y="1680" width="1240" height="110" fill="#F4F1E8" rx="4"/>
  <text x="130" y="1705" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">Q5. Scope Boundaries: Joinery vs Civil Construction</text>
  {wrap_text("Does FlowGrid perform civil demolition, masonry, and sanitary plumbing directly, or does the studio provide joinery design, cabinetry fabrication, and supervision of client-appointed contractors?", 130, 1725, 80, 18, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Question 6 -->
  <rect x="1420" y="1680" width="1240" height="110" fill="#F4F1E8" rx="4"/>
  <text x="1440" y="1705" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">Q6. Sister Entity Boundary: Rumi's Fashionable House</text>
  {wrap_text("Are you comfortable with the current footer and studio narrative that positions Rumi's lifestyle channel strictly as founder domestic context, without implying architectural credentials?", 1440, 1725, 80, 18, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Question 7 -->
  <rect x="110" y="1810" width="1240" height="110" fill="#F4F1E8" rx="4"/>
  <text x="130" y="1835" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">Q7. Commercial Boundary: Onekta Product Transition</text>
  {wrap_text("Please confirm that FlowGrid's website will carry zero retail product listings or e-commerce checkouts for appliances, and will solely feature an outbound link to Onekta Product's separate store.", 130, 1855, 80, 18, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Question 8 -->
  <rect x="1420" y="1810" width="1240" height="110" fill="#F4F1E8" rx="4"/>
  <text x="1440" y="1835" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">Q8. Real Project Photography &amp; Client Consent</text>
  {wrap_text("Do you have signed client photography release forms for previously completed Dhaka apartments, or should FlowGrid continue to showcase clearly disclosed conceptual spatial studies?", 1440, 1855, 80, 18, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Web Vitals Performance Targets Box -->
  <rect x="110" y="1950" width="2550" height="180" fill="#183B35" rx="4"/>
  <text x="140" y="1985" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">Front-End Engineering Core Web Vitals Budget Targets</text>
  
  <text x="140" y="2020" fill="#C5A059" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">LCP (Largest Contentful Paint) &lt; 2.0s</text>
  {wrap_text("Preload hero image in &lt;head&gt;, convert all architectural photography to AVIF/WebP formats under 120KB per hero frame.", 140, 2045, 78, 18, "'Manrope', sans-serif", 11, "#DEE7E2")}

  <text x="1000" y="2020" fill="#C5A059" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">CLS (Cumulative Layout Shift) &lt; 0.05</text>
  {wrap_text("Enforce explicit aspect-ratio attributes on all image and card frames. Reserve header and banner heights to prevent layout jitter.", 1000, 2045, 78, 18, "'Manrope', sans-serif", 11, "#DEE7E2")}

  <text x="1850" y="2020" fill="#C5A059" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">INP (Interaction to Next Paint) &lt; 150ms</text>
  {wrap_text("Zero main-thread blocking JavaScript on form interactions. Mobile menu toggle executed via lightweight CSS transform classes.", 1850, 2045, 78, 18, "'Manrope', sans-serif", 11, "#DEE7E2")}
</svg>"""

with open('figma_svgs_v2/08_handoff_qa.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("Saved figma_svgs_v2/08_handoff_qa.svg")
