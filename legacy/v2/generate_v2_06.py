"""
FlowGrid - Page 06 (Prototype & Motion) Generator v2
Comprehensive motion specifications, honest Figma vs Browser delineation,
and working prototype wiring flow documentation.
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

def wrap_text(text, x, y, max_chars, line_height, font_family, font_size, fill, font_weight=400):
    lines = textwrap.wrap(text, width=max_chars)
    tspans = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else line_height
        tspans.append(f'<tspan x="{x}" dy="{dy}">{line}</tspan>')
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{font_family}" font-size="{font_size}" font-weight="{font_weight}">' + "".join(tspans) + '</text>'

svg = f"""<svg width="2800" height="2500" viewBox="0 0 2800 2500" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="2800" height="2500" fill="#F4F1E8"/>

  <!-- Top Banner -->
  <rect x="80" y="80" width="2640" height="130" fill="#183B35" rx="4"/>
  <text x="120" y="145" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="34" font-weight="600">FlowGrid — Prototype Wiring &amp; Motion Specifications (v2)</text>
  <text x="120" y="180" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="16">Figma prototype node wiring, timing curves, reduced-motion fallbacks, and honest simulation boundaries</text>

  <!-- ========================================================================= -->
  <!-- SECTION 1: SIGNATURE HERO MASK REVEAL STORYBOARD (600MS)                  -->
  <!-- ========================================================================= -->
  <rect x="80" y="250" width="2640" height="660" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="250" width="2640" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="283" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">01. Signature Hero Architectural Mask Reveal Storyboard &amp; Reduced-Motion Fallback</text>

  <!-- Step 1: 0ms Initial Mount -->
  <rect x="110" y="330" width="600" height="380" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="110" y="330" width="600" height="36" fill="#DEE7E2" rx="4 4 0 0"/>
  <text x="130" y="354" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">T = 0ms : Initial Viewport Load (Zero Usability Delay)</text>
  <!-- Wireframe -->
  <text x="140" y="400" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="20" font-weight="600">শান্ত, সুপরিকল্পিত শহুরে আবাস</text>
  <rect x="140" y="420" width="160" height="36" fill="#183B35" rx="4"/>
  <text x="220" y="443" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="12" text-anchor="middle">পরামর্শ শুরু করুন</text>
  <!-- Image container collapsed -->
  <rect x="360" y="390" width="330" height="200" fill="#E4EAE6" stroke="#B8C2BA" stroke-dasharray="4 4" rx="4"/>
  <text x="525" y="495" fill="#8E9E96" font-family="'Manrope', sans-serif" font-size="12" text-anchor="middle">Clip Mask: 0% Width</text>
  <text x="525" y="520" fill="#8E9E96" font-family="'Manrope', sans-serif" font-size="11" text-anchor="middle">Headline &amp; Navigation immediately interactive</text>
  {wrap_text("Governance Rule: Crucial CTAs and headlines render immediately at T=0ms. Motion must never block user intent or navigation.", 130, 640, 68, 18, "'Manrope', sans-serif", 11, "#56645E")}

  <!-- Step 2: 300ms Midpoint -->
  <rect x="740" y="330" width="600" height="380" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="740" y="330" width="600" height="36" fill="#DEE7E2" rx="4 4 0 0"/>
  <text x="760" y="354" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">T = 300ms : Eased Horizontal Unmasking (50% Curtain)</text>
  <rect x="760" y="390" width="560" height="200" fill="#E4EAE6" rx="4"/>
  <image href="{img_living_1}" x="760" y="390" width="280" height="200" preserveAspectRatio="xMidYMid slice"/>
  <rect x="1040" y="390" width="280" height="200" fill="#183B35" opacity="0.15"/>
  <line x1="1040" y1="390" x2="1040" y2="590" stroke="#895239" stroke-width="2"/>
  <text x="1040" y="615" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700" text-anchor="middle">Leading Reveal Edge (cubic-bezier)</text>
  {wrap_text("Timing Curve: cubic-bezier(0.16, 1, 0.3, 1). Natural architectural shutter feel, opening from left to right.", 760, 650, 68, 18, "'Manrope', sans-serif", 11, "#56645E")}

  <!-- Step 3: 600ms Complete Settle -->
  <rect x="1370" y="330" width="600" height="380" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="1370" y="330" width="600" height="36" fill="#DEE7E2" rx="4 4 0 0"/>
  <text x="1390" y="354" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">T = 600ms : Full Architectural Immersion</text>
  <image href="{img_living_1}" x="1390" y="390" width="560" height="200" preserveAspectRatio="xMidYMid slice"/>
  <rect x="1405" y="405" width="340" height="26" fill="#183B35" opacity="0.9" rx="3"/>
  <text x="1575" y="422" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="10" font-weight="700" text-anchor="middle">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>
  {wrap_text("Final State: 100% visibility, subtle 1.02x settling zoom. Concept badge remains permanently visible in upper left corner.", 1390, 650, 68, 18, "'Manrope', sans-serif", 11, "#56645E")}

  <!-- Step 4: Reduced Motion Fallback Specification -->
  <rect x="2000" y="330" width="680" height="380" fill="#FFF8F4" stroke="#895239" stroke-width="1" rx="4"/>
  <rect x="2000" y="330" width="680" height="36" fill="#895239" rx="4 4 0 0"/>
  <text x="2020" y="354" fill="#FFFFFF" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">ACCESSIBILITY: prefers-reduced-motion: reduce</text>
  <text x="2020" y="395" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">CSS Media Query Implementation Rule:</text>
  <rect x="2020" y="410" width="640" height="120" fill="#183B35" rx="4"/>
  <text x="2040" y="435" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="12">@media (prefers-reduced-motion: reduce) {{</text>
  <text x="2060" y="455" fill="#F4F1E8" font-family="'Courier New', monospace" font-size="12">  .hero-mask-image {{</text>
  <text x="2080" y="475" fill="#C5A059" font-family="'Courier New', monospace" font-size="12">    clip-path: none !important;</text>
  <text x="2080" y="495" fill="#C5A059" font-family="'Courier New', monospace" font-size="12">    transform: none !important;</text>
  <text x="2080" y="515" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="12">    transition: opacity 150ms ease-out;</text>
  <text x="2040" y="535" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="12">}}</text>
  {wrap_text("When user specifies reduced motion in OS settings, clip-path curtain and transforms are completely eliminated. The image renders instantaneously at full scale.", 2020, 580, 72, 18, "'Manrope', sans-serif", 11, "#56645E")}

  <!-- ========================================================================= -->
  <!-- SECTION 2: FIGMA PROTOTYPE WIRING FLOWS & LIVE NODE EVIDENCE              -->
  <!-- ========================================================================= -->
  <rect x="80" y="940" width="2640" height="740" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="940" width="2640" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="973" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">02. Live Figma Prototype Wiring Architecture &amp; Interaction Flow Map</text>

  <!-- Flow Diagram Card 1: Desktop Journey -->
  <rect x="110" y="1020" width="840" height="620" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <text x="140" y="1055" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">FLOW A: Desktop Primary Conversion Journey</text>
  
  <rect x="140" y="1080" width="220" height="80" fill="#FFFFFF" stroke="#183B35" stroke-width="1.5" rx="4"/>
  <text x="250" y="1115" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700" text-anchor="middle">হোমপেজ (Home)</text>
  <text x="250" y="1135" fill="#56645E" font-family="'Manrope', sans-serif" font-size="11" text-anchor="middle">Node: screen-desktop-bn-home</text>

  <text x="400" y="1125" fill="#895239" font-family="'Manrope', sans-serif" font-size="20" font-weight="700">→</text>
  <text x="400" y="1145" fill="#56645E" font-family="'Manrope', sans-serif" font-size="10" text-anchor="middle">On Click (Hero Card)</text>

  <rect x="470" y="1080" width="220" height="80" fill="#FFFFFF" stroke="#183B35" stroke-width="1.5" rx="4"/>
  <text x="580" y="1115" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700" text-anchor="middle">কেস স্টাডি (Case Study)</text>
  <text x="580" y="1135" fill="#56645E" font-family="'Manrope', sans-serif" font-size="11" text-anchor="middle">Node: screen-desktop-bn-case-study</text>

  <text x="730" y="1125" fill="#895239" font-family="'Manrope', sans-serif" font-size="20" font-weight="700">→</text>
  <text x="730" y="1145" fill="#56645E" font-family="'Manrope', sans-serif" font-size="10" text-anchor="middle">On Click (CTA)</text>

  <rect x="140" y="1200" width="300" height="80" fill="#FFFFFF" stroke="#183B35" stroke-width="1.5" rx="4"/>
  <text x="290" y="1235" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700" text-anchor="middle">পরামর্শ ফর্ম (Enquiry Form)</text>
  <text x="290" y="1255" fill="#56645E" font-family="'Manrope', sans-serif" font-size="11" text-anchor="middle">State 1 Idle -> State 5 Confirmation</text>

  {wrap_text("Figma Reaction: 'Navigate to' destination with 'Smart Animate' ease-out (300ms). Breadcrumb '← ফিরে যান' wired back to Projects archive.", 140, 1310, 76, 20, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Flow Diagram Card 2: Mobile Navigation Drawer -->
  <rect x="980" y="1020" width="800" height="620" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <text x="1010" y="1055" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">FLOW B: Mobile Hamburger &amp; Drawer Overlay</text>

  <rect x="1010" y="1080" width="200" height="80" fill="#FFFFFF" stroke="#183B35" stroke-width="1.5" rx="4"/>
  <text x="1110" y="1115" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700" text-anchor="middle">মোবাইল হোম (390px)</text>
  <text x="1110" y="1135" fill="#56645E" font-family="'Manrope', sans-serif" font-size="11" text-anchor="middle">Tap Hamburger 'মেনু ☰'</text>

  <text x="1250" y="1125" fill="#895239" font-family="'Manrope', sans-serif" font-size="20" font-weight="700">→</text>

  <rect x="1300" y="1080" width="220" height="80" fill="#183B35" rx="4"/>
  <text x="1410" y="1115" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700" text-anchor="middle">ড্রয়ার মেনু (Drawer)</text>
  <text x="1410" y="1135" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="11" text-anchor="middle">Slide-in from Right (300ms)</text>

  <text x="1560" y="1125" fill="#895239" font-family="'Manrope', sans-serif" font-size="20" font-weight="700">→</text>

  <rect x="1010" y="1200" width="240" height="80" fill="#FFFFFF" stroke="#B8C2BA" rx="4"/>
  <text x="1130" y="1235" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" text-anchor="middle">Dismiss '✕' or Backdrop</text>
  <text x="1130" y="1255" fill="#56645E" font-family="'Manrope', sans-serif" font-size="11" text-anchor="middle">Slides out, returns to scroll position</text>

  {wrap_text("Figma Setting: 'Open Overlay' anchored 'Top Right', animation 'Move In' from right, background overlay 60% black with 'Close when clicking outside'.", 1010, 1310, 72, 20, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Flow Diagram Card 3: Boundary Delineation (Honest Simulation vs Real Code) -->
  <rect x="1810" y="1020" width="870" height="620" fill="#FFF8F4" stroke="#895239" stroke-width="1" rx="4"/>
  <text x="1840" y="1055" fill="#895239" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">FLOW C: Boundary Delineation &amp; Genuine Implementation Realities</text>

  <rect x="1840" y="1080" width="810" height="150" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <text x="1860" y="1110" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">1. What is Verified in Figma Prototyping:</text>
  {wrap_text("• Screen navigation links (Home -> Projects -> Detail -> Contact).", 1860, 1135, 76, 20, "'Manrope', sans-serif", 12, "#56645E")}
  {wrap_text("• Overlay sliding menus and interactive modal dismissals.", 1860, 1160, 76, 20, "'Manrope', sans-serif", 12, "#56645E")}
  {wrap_text("• Static mockups of all 6 enquiry form validation states.", 1860, 1185, 76, 20, "'Manrope', sans-serif", 12, "#56645E")}

  <rect x="1840" y="1250" width="810" height="180" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <text x="1860" y="1280" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">2. What Requires Frontend Web Engineering (Not Simulatable in Figma):</text>
  {wrap_text("• OS-level media query detection (window.matchMedia('(prefers-reduced-motion)')).", 1860, 1305, 76, 20, "'Manrope', sans-serif", 12, "#56645E")}
  {wrap_text("• Live database API integration for form submission, SMS verification, and lead routing.", 1860, 1330, 76, 20, "'Manrope', sans-serif", 12, "#56645E")}
  {wrap_text("• Complex polygon clip-path GPU CSS hardware acceleration during continuous scroll.", 1860, 1355, 76, 20, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Prototype Links Box -->
  <rect x="1840" y="1450" width="810" height="150" fill="#183B35" rx="4"/>
  <text x="1860" y="1480" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Verified Prototype Start URLs &amp; Access:</text>
  <text x="1860" y="1505" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="12">https://www.figma.com/proto/eMRunQ80brYYvuTWkufV2o/FlowGrid</text>
  <text x="1860" y="1530" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="12">Flow 1 Start: Desktop Experience (Node 03 Desktop — BN)</text>
  <text x="1860" y="1550" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="12">Flow 2 Start: Mobile Responsive (Node 04 Mobile — BN)</text>
  <text x="1860" y="1570" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="12">Flow 3 Start: English Mirror (Node 05 English)</text>

  <!-- ========================================================================= -->
  <!-- SECTION 3: INTERACTIVE CARD SPRING HOVER SPECIFICATION                   -->
  <!-- ========================================================================= -->
  <rect x="80" y="1710" width="2640" height="660" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="1710" width="2640" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="1743" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">03. Interactive Project Card Spring Hover Storyboard (360ms Transition)</text>

  <!-- Card Rest -->
  <rect x="250" y="1790" width="600" height="520" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <text x="270" y="1825" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Rest State (Elevation 0)</text>
  <image href="{img_living_1}" x="270" y="1845" width="560" height="280" preserveAspectRatio="xMidYMid slice"/>
  <text x="270" y="2160" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">গুলশান লেকভিউ অ্যাপার্টমেন্ট</text>
  <text x="270" y="2190" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">Scale: 1.00x | Transform: translateY(0px) | Shadow: none</text>
  <text x="270" y="2220" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="600">কেস স্টাডি দেখুন →</text>

  <!-- Transition Arrow -->
  <text x="960" y="2040" fill="#895239" font-family="'Manrope', sans-serif" font-size="32" font-weight="700">→</text>
  <text x="960" y="2070" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13" text-anchor="middle">Hover Event</text>
  <text x="960" y="2090" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700" text-anchor="middle">360ms spring curve</text>

  <!-- Card Hover -->
  <rect x="1100" y="1775" width="600" height="520" fill="#FFFFFF" stroke="#183B35" stroke-width="1.5" rx="4"/>
  <text x="1120" y="1810" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Hover / Active State (Elevation +8px, Shadow Glow)</text>
  <image href="{img_living_1}" x="1115" y="1830" width="570" height="290" preserveAspectRatio="xMidYMid slice"/>
  <text x="1120" y="2160" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">গুলশান লেকভিউ অ্যাপার্টমেন্ট</text>
  <text x="1120" y="2190" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Scale: 1.025x | Transform: translateY(-8px) | Shadow: 0 20px 40px rgba(24,59,53,0.08)</text>
  <text x="1120" y="2220" fill="#895239" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700">কেস স্টাডি দেখুন ➔ (CTA translates +6px right)</text>

  <!-- Technical Specs Table -->
  <rect x="1780" y="1790" width="900" height="500" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <text x="1810" y="1830" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Motion Tokens &amp; Technical Implementation Rules</text>
  
  <text x="1810" y="1870" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">TOKEN: --motion-spring-card</text>
  <text x="1810" y="1895" fill="#183B35" font-family="'Courier New', monospace" font-size="12">cubic-bezier(0.34, 1.56, 0.64, 1) · 360ms</text>

  <text x="1810" y="1935" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">TOKEN: --motion-reveal-hero</text>
  <text x="1810" y="1960" fill="#183B35" font-family="'Courier New', monospace" font-size="12">cubic-bezier(0.16, 1, 0.3, 1) · 600ms</text>

  <text x="1810" y="2000" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">TOKEN: --motion-fade-drawer</text>
  <text x="1810" y="2025" fill="#183B35" font-family="'Courier New', monospace" font-size="12">ease-out · 240ms</text>

  <text x="1810" y="2065" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">PERFORMANCE BUDGET:</text>
  {wrap_text("• All animations restricted strictly to transform (translateY, scale) and opacity.", 1810, 2090, 72, 20, "'Manrope', sans-serif", 12, "#56645E")}
  {wrap_text("• No transitions on layout-triggering properties (width, height, margin, padding).", 1810, 2115, 72, 20, "'Manrope', sans-serif", 12, "#56645E")}
  {wrap_text("• Target frame rate: 60fps on mobile viewports (INP &lt; 150ms).", 1810, 2140, 72, 20, "'Manrope', sans-serif", 12, "#56645E")}
</svg>"""

with open('figma_svgs_v2/06_prototype_motion.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("Saved figma_svgs_v2/06_prototype_motion.svg")
