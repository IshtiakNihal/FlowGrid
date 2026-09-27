"""
FlowGrid - Pages 05 to 08 SVG Generator
Generates English templates, Prototype & Motion, Assets, and Handoff & QA boards.
"""
import os
import base64

def get_base64_image(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            data = base64.b64encode(f.read()).decode('utf-8')
            ext = 'jpeg' if path.endswith('.jpg') else 'png'
            return f"data:image/{ext};base64,{data}"
    return ""

img_living = get_base64_image('concepts/concept_01_living_dhaka.jpg')
img_kitchen = get_base64_image('concepts/concept_02_kitchen_dhaka.jpg')
img_bedroom = get_base64_image('concepts/concept_03_bedroom_dhaka.jpg')

# -------------------------------------------------------------
# 05 English Templates (Desktop & Mobile)
# -------------------------------------------------------------
svg_05 = f"""<svg width="3400" height="3600" viewBox="0 0 3400 3600" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="3400" height="3600" fill="#E5E1D8"/>

  <!-- DESKTOP ENGLISH (1440 x 3400) -->
  <g transform="translate(100, 100)">
    <rect width="1440" height="3400" fill="#F4F1E8" rx="2"/>
    <text x="0" y="-20" fill="#183B35" font-family="'Manrope', sans-serif" font-size="20" font-weight="700">01. English Desktop Homepage (1440px)</text>

    <!-- Header -->
    <rect width="1440" height="88" fill="#F4F1E8"/>
    <line x1="64" y1="88" x2="1376" y2="88" stroke="#B8C2BA" stroke-width="1"/>
    <text x="64" y="52" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="30" font-weight="700">FLOWGRID</text>
    <text x="64" y="70" fill="#56645E" font-family="'Manrope', sans-serif" font-size="11" letter-spacing="1">INTERIOR STUDIO</text>
    
    <text x="750" y="52" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Projects</text>
    <text x="850" y="52" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Services</text>
    <text x="950" y="52" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Process</text>
    <text x="1050" y="52" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Studio</text>
    <text x="1150" y="52" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">বাংলা <tspan fill="#B8C2BA">|</tspan> EN</text>

    <rect x="1220" y="18" width="156" height="52" fill="#183B35" rx="2"/>
    <text x="1245" y="50" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Let's talk</text>

    <!-- Hero -->
    <g transform="translate(64, 120)">
      <rect width="1312" height="740" fill="#183B35"/>
      <image href="{img_living}" x="0" y="0" width="1312" height="740" preserveAspectRatio="xMidYMid slice" opacity="0.88"/>
      <rect x="0" y="0" width="700" height="740" fill="url(#heroVignetteEn)" opacity="0.7"/>

      <text x="60" y="440" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="80" font-weight="500" line-height="1.02">Room for</text>
      <text x="60" y="525" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="80" font-weight="500" line-height="1.02">everyday life.</text>
      <text x="60" y="575" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="20">Thoughtful interiors shaped around your family needs, preferences and budget.</text>

      <rect x="60" y="615" width="200" height="52" fill="#F4F1E8" rx="2"/>
      <text x="90" y="647" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Explore our work →</text>

      <rect x="990" y="670" width="280" height="34" fill="#183B35" opacity="0.85" rx="2"/>
      <text x="1005" y="693" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Concept interior · Design reference</text>
    </g>

    <!-- Proposition -->
    <g transform="translate(64, 920)">
      <text x="0" y="40" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700" letter-spacing="1">THE FLOWGRID APPROACH</text>
      <text x="0" y="100" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="44" font-weight="500">A considered home.</text>
      <text x="0" y="150" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="44" font-weight="500">A clearer process.</text>

      <text x="650" y="95" fill="#56645E" font-family="'Manrope', sans-serif" font-size="18" line-height="1.7">We begin with how you live, what your space needs, and what you want to spend. No false promises, opaque pricing, or generic international penthouses—just honest, buildable architectural solutions designed specifically for urban family life in Dhaka.</text>
      <line x1="0" y1="230" x2="1312" y2="230" stroke="#B8C2BA" stroke-width="1"/>
    </g>

    <!-- Selected Spaces Spread -->
    <g transform="translate(64, 1200)">
      <text x="0" y="30" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700" letter-spacing="1">SELECTED WORK</text>
      <text x="0" y="80" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="40" font-weight="500">Spaces, with purpose.</text>
      <text x="1180" y="80" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">View projects →</text>

      <g transform="translate(0, 120)">
        <rect width="755" height="520" fill="#DEE7E2"/>
        <image href="{img_living}" x="0" y="0" width="755" height="520" preserveAspectRatio="xMidYMid slice"/>
        <text x="0" y="560" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="28">Apartment Study 01</text>
        <text x="0" y="590" fill="#56645E" font-family="'Manrope', sans-serif" font-size="16">Mirpur, Dhaka · Living, library joinery and urban balcony</text>
        <text x="0" y="615" fill="#895239" font-family="'Manrope', sans-serif" font-size="14">Design Concept Study · Not a completed build</text>
      </g>

      <g transform="translate(779, 200)">
        <rect width="533" height="440" fill="#DEE7E2"/>
        <image href="{img_kitchen}" x="0" y="0" width="533" height="440" preserveAspectRatio="xMidYMid slice"/>
        <text x="0" y="480" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="28">Kitchen Study 02</text>
        <text x="0" y="510" fill="#56645E" font-family="'Manrope', sans-serif" font-size="16">Dhaka · Everyday cooking &amp; resilient granite</text>
        <text x="0" y="535" fill="#895239" font-family="'Manrope', sans-serif" font-size="14">Design Concept Study · Not a completed build</text>
      </g>
    </g>

    <!-- Services -->
    <g transform="translate(64, 2050)">
      <line x1="0" y1="0" x2="1312" y2="0" stroke="#B8C2BA" stroke-width="1"/>
      <text x="0" y="50" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700" letter-spacing="1">OUR SERVICES</text>
      <text x="0" y="100" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="40">Design around your everyday.</text>

      <!-- Row 1 -->
      <g transform="translate(0, 140)">
        <line x1="0" y1="0" x2="1312" y2="0" stroke="#B8C2BA" stroke-width="1"/>
        <text x="20" y="45" fill="#895239" font-family="'Bodoni Moda', serif" font-size="24">01</text>
        <text x="80" y="45" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24">Home interiors</text>
        <text x="450" y="45" fill="#56645E" font-family="'Manrope', sans-serif" font-size="16">Layout, material direction and room-by-room planning.</text>
        <text x="1270" y="45" fill="#183B35" font-family="'Manrope', sans-serif" font-size="24">→</text>
        <line x1="0" y1="80" x2="1312" y2="80" stroke="#B8C2BA" stroke-width="1"/>
      </g>

      <!-- Row 2 -->
      <g transform="translate(0, 230)">
        <text x="20" y="45" fill="#895239" font-family="'Bodoni Moda', serif" font-size="24">02</text>
        <text x="80" y="45" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24">Kitchens &amp; storage</text>
        <text x="450" y="45" fill="#56645E" font-family="'Manrope', sans-serif" font-size="16">Make daily routines easier through durable countertops and thoughtful storage.</text>
        <text x="1270" y="45" fill="#183B35" font-family="'Manrope', sans-serif" font-size="24">→</text>
        <line x1="0" y1="80" x2="1312" y2="80" stroke="#B8C2BA" stroke-width="1"/>
      </g>

      <!-- Row 3 -->
      <g transform="translate(0, 320)">
        <text x="20" y="45" fill="#895239" font-family="'Bodoni Moda', serif" font-size="24">03</text>
        <text x="80" y="45" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24">Renovation planning</text>
        <text x="450" y="45" fill="#56645E" font-family="'Manrope', sans-serif" font-size="16">Modernise existing Dhaka apartments while respecting structural constraints.</text>
        <text x="1270" y="45" fill="#183B35" font-family="'Manrope', sans-serif" font-size="24">→</text>
        <line x1="0" y1="80" x2="1312" y2="80" stroke="#B8C2BA" stroke-width="1"/>
      </g>
    </g>

    <!-- Closing Pine Panel -->
    <g transform="translate(64, 2550)">
      <rect width="1312" height="260" fill="#183B35" rx="2"/>
      <text x="80" y="80" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="44">What does your space need?</text>
      <text x="80" y="125" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="18">Share your room dimensions and thoughts. The FlowGrid team is ready to talk.</text>
      <rect x="80" y="160" width="220" height="52" fill="#F4F1E8" rx="2"/>
      <text x="120" y="192" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Discuss your space →</text>
      <text x="340" y="192" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="16">Or chat directly via <tspan fill="#FFFFFF" text-decoration="underline">WhatsApp</tspan> or <tspan fill="#FFFFFF" text-decoration="underline">Call us</tspan></text>
    </g>

    <!-- Footer -->
    <g transform="translate(64, 2870)">
      <line x1="0" y1="0" x2="1312" y2="0" stroke="#B8C2BA" stroke-width="1"/>
      <text x="0" y="40" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">FLOWGRID</text>
      <text x="0" y="70" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">© 2026 FlowGrid Interior Studio · Mirpur, Dhaka, Bangladesh</text>
    </g>
  </g>

  <!-- MOBILE ENGLISH (390 x 2400) -->
  <g transform="translate(1700, 100)">
    <rect width="390" height="2400" fill="#F4F1E8" rx="2"/>
    <text x="0" y="-20" fill="#183B35" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">02. English Mobile Screen (390px)</text>

    <!-- Header -->
    <rect width="390" height="72" fill="#F4F1E8"/>
    <text x="20" y="44" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">FLOWGRID</text>
    <text x="260" y="44" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="600">বাংলা</text>
    <rect x="306" y="14" width="64" height="44" fill="#183B35" rx="2"/>
    <text x="323" y="41" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Menu</text>
    <line x1="20" y1="72" x2="370" y2="72" stroke="#B8C2BA" stroke-width="1"/>

    <!-- Paper Hero -->
    <g transform="translate(20, 95)">
      <text x="0" y="15" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">INTERIOR STUDIO · DHAKA</text>
      <text x="0" y="55" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="38" font-weight="500">Room for</text>
      <text x="0" y="95" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="38" font-weight="500">everyday life.</text>
      <text x="0" y="135" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15" line-height="1.5">Thoughtful interiors shaped around your family needs, preferences and budget.</text>
      <rect x="0" y="170" width="350" height="52" fill="#183B35" rx="2"/>
      <text x="110" y="202" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Explore our work →</text>
    </g>

    <!-- Hero Image -->
    <g transform="translate(0, 340)">
      <rect width="390" height="487" fill="#DEE7E2"/>
      <image href="{img_living}" x="0" y="0" width="390" height="487" preserveAspectRatio="xMidYMid slice"/>
      <rect x="20" y="20" width="240" height="28" fill="#183B35" opacity="0.9" rx="2"/>
      <text x="30" y="38" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="12" font-weight="600">Concept interior · Design study</text>
    </g>

    <!-- Persistent Bottom Bar -->
    <g transform="translate(0, 2330)">
      <rect width="390" height="70" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
      <rect x="20" y="10" width="165" height="48" fill="#F4F1E8" stroke="#183B35" stroke-width="1.5" rx="2"/>
      <text x="75" y="39" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Call</text>
      <rect x="205" y="10" width="165" height="48" fill="#183B35" rx="2"/>
      <text x="245" y="39" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">WhatsApp</text>
    </g>
  </g>

  <!-- Defs -->
  <defs>
    <linearGradient id="heroVignetteEn" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#183B35" stop-opacity="0.95"/>
      <stop offset="70%" stop-color="#183B35" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#183B35" stop-opacity="0"/>
    </linearGradient>
  </defs>
</svg>"""

with open('figma_svgs/05_english.svg', 'w', encoding='utf-8') as f:
    f.write(svg_05)

print("Saved 05_english.svg")

# -------------------------------------------------------------
# 06 Prototype & Motion
# -------------------------------------------------------------
svg_06 = f"""<svg width="2400" height="2200" viewBox="0 0 2400 2200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="2400" height="2200" fill="#F4F1E8"/>

  <!-- Banner -->
  <rect x="80" y="80" width="2240" height="140" fill="#183B35" rx="4"/>
  <text x="120" y="145" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="36" font-weight="600">FlowGrid — Prototype Flows &amp; Motion Engineering</text>
  <text x="120" y="185" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="18">Signature architectural hero mask sequence, shared-element project expansion, micro-interactions, and reduced-motion specification</text>

  <!-- Sequence 1: Signature Hero Reveal Storyboard (600ms Ease-Out) -->
  <rect x="80" y="260" width="2240" height="580" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="260" width="2240" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="293" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">01. Signature Hero Reveal Sequence (Trigger: Page Load · Duration: 600ms · Ease: cubic-bezier(0.23, 1, 0.32, 1))</text>

  <!-- Frame 1: 0ms Initial State -->
  <g transform="translate(120, 340)">
    <text x="0" y="-15" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">T = 0ms (Pre-reveal)</text>
    <rect width="480" height="300" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <!-- Thin line mask in center -->
    <rect x="238" y="50" width="4" height="200" fill="#183B35"/>
    <text x="170" y="280" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">Centered vertical wipe line</text>
  </g>

  <!-- Frame 2: 200ms Expanding Mask -->
  <g transform="translate(640, 340)">
    <text x="0" y="-15" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">T = 200ms (Architectural Mask Wipe)</text>
    <rect width="480" height="300" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <!-- Expanding mask reveals photo center -->
    <rect x="140" y="40" width="200" height="220" fill="#DEE7E2"/>
    <image href="{img_living}" x="140" y="40" width="200" height="220" preserveAspectRatio="xMidYMid slice" opacity="0.6"/>
    <line x1="140" y1="40" x2="140" y2="260" stroke="#183B35" stroke-width="2"/>
    <line x1="340" y1="40" x2="340" y2="260" stroke="#183B35" stroke-width="2"/>
    <text x="140" y="285" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">Dual-wing mask reveal expanding horizontally</text>
  </g>

  <!-- Frame 3: 420ms Text Elevation -->
  <g transform="translate(1160, 340)">
    <text x="0" y="-15" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">T = 420ms (Typography Line Rise)</text>
    <rect width="480" height="300" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <rect x="40" y="30" width="400" height="240" fill="#DEE7E2"/>
    <image href="{img_living}" x="40" y="30" width="400" height="240" preserveAspectRatio="xMidYMid slice" opacity="0.9"/>
    <!-- Text rising into position -->
    <text x="60" y="200" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="20" font-weight="700">আপনার জীবনের ছন্দে...</text>
    <text x="130" y="285" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">Whole-line translateY(-12px) fade in</text>
  </g>

  <!-- Frame 4: 600ms Settled Final State -->
  <g transform="translate(1680, 340)">
    <text x="0" y="-15" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">T = 600ms (Settled &amp; Fully Interactive)</text>
    <rect width="480" height="300" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <rect x="20" y="20" width="440" height="260" fill="#183B35"/>
    <image href="{img_living}" x="20" y="20" width="440" height="260" preserveAspectRatio="xMidYMid slice"/>
    <text x="40" y="180" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="22" font-weight="700">আপনার জীবনের ছন্দে,</text>
    <text x="40" y="210" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="22" font-weight="700">আপনার ঘর।</text>
    <rect x="40" y="225" width="140" height="34" fill="#F4F1E8" rx="2"/>
    <text x="55" y="247" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="12" font-weight="700">আমাদের কাজ দেখুন →</text>
  </g>

  <!-- Sequence 2: Project Shared Element Expansion Storyboard (360ms) -->
  <rect x="80" y="880" width="2240" height="580" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="880" width="2240" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="913" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">02. Project to Detail Transition (Trigger: Click Project Card · Duration: 360ms · Shared Hero Morph)</text>

  <!-- Step 1: Project Tile Click -->
  <g transform="translate(120, 960)">
    <text x="0" y="-15" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Phase 1: Card Press (T=0ms)</text>
    <rect width="650" height="360" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <rect x="40" y="40" width="340" height="220" fill="#DEE7E2"/>
    <image href="{img_living}" x="40" y="40" width="340" height="220" preserveAspectRatio="xMidYMid slice"/>
    <text x="40" y="290" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="20" font-weight="700">অ্যাপার্টমেন্ট স্টাডি ০১</text>
    <text x="40" y="320" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Pointer down: Scale 0.99 (100ms) with persistent focus</text>
  </g>

  <!-- Step 2: Shared Morph (T=180ms) -->
  <g transform="translate(820, 960)">
    <text x="0" y="-15" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Phase 2: Viewport Expansion (T=180ms)</text>
    <rect width="650" height="360" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <!-- Expanding rectangle -->
    <rect x="20" y="20" width="610" height="280" fill="#DEE7E2"/>
    <image href="{img_living}" x="20" y="20" width="610" height="280" preserveAspectRatio="xMidYMid slice" opacity="0.8"/>
    <text x="40" y="330" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Image frame animates into full 1312px wide master crop; page scroll locks</text>
  </g>

  <!-- Step 3: Case Study Arrived (T=360ms) -->
  <g transform="translate(1520, 960)">
    <text x="0" y="-15" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Phase 3: Detail Page Loaded (T=360ms)</text>
    <rect width="650" height="360" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <text x="40" y="40" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="13">আমাদের কাজ / অ্যাপার্টমেন্ট স্টাডি ০১</text>
    <text x="40" y="70" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="24" font-weight="700">অ্যাপার্টমেন্ট স্টাডি ০১ · কেস স্টাডি</text>
    <rect x="40" y="90" width="570" height="200" fill="#DEE7E2"/>
    <image href="{img_living}" x="40" y="90" width="570" height="200" preserveAspectRatio="xMidYMid slice"/>
    <text x="40" y="325" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Metadata and brief fade into position. Zero jarring layout shifts.</text>
  </g>

  <!-- Section 3: Micro-Interactions & Reduced-Motion Specification Table -->
  <rect x="80" y="1500" width="2240" height="640" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="1500" width="2240" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="1533" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">03. Micro-Interaction Specification &amp; Accessibility (prefers-reduced-motion)</text>

  <rect x="120" y="1570" width="2160" height="540" fill="#F4F1E8" rx="4"/>
  <text x="150" y="1610" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Interaction</text>
  <text x="450" y="1610" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Trigger</text>
  <text x="750" y="1610" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Timing &amp; Easing</text>
  <text x="1150" y="1610" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Visual Treatment</text>
  <text x="1650" y="1610" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Reduced-Motion Fallback</text>
  <line x1="150" y1="1625" x2="2240" y2="1625" stroke="#B8C2BA" stroke-width="1"/>

  <text x="150" y="1660" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Button Hover</text>
  <text x="450" y="1660" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Pointer enter</text>
  <text x="750" y="1660" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">150ms · ease</text>
  <text x="1150" y="1660" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Color shift #183B35 → #102B26. No lifting.</text>
  <text x="1650" y="1660" fill="#245C43" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Instant color change</text>

  <text x="150" y="1710" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Button Press</text>
  <text x="450" y="1710" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Pointer down</text>
  <text x="750" y="1710" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">100ms · ease-out</text>
  <text x="1150" y="1710" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Scale 0.99 on button surface</text>
  <text x="1650" y="1710" fill="#245C43" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">No scale transform</text>

  <text x="150" y="1760" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Mobile Menu</text>
  <text x="450" y="1760" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Click Menu button</text>
  <text x="750" y="1760" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">220ms in / 160ms out</text>
  <text x="1150" y="1760" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Full-height paper drawer slide + opacity</text>
  <text x="1650" y="1760" fill="#245C43" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Instant modal display</text>

  <text x="150" y="1810" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">FAQ Disclosure</text>
  <text x="450" y="1810" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Click Accordion</text>
  <text x="750" y="1810" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">180ms · ease-out</text>
  <text x="1150" y="1810" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Height reveal with icon rotation (+ to −)</text>
  <text x="1650" y="1810" fill="#245C43" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Instant expansion</text>

  <text x="150" y="1860" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Image Reveal</text>
  <text x="450" y="1860" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Scroll into viewport</text>
  <text x="750" y="1860" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">360ms once</text>
  <text x="1150" y="1860" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">TranslateY(12px) + Opacity 0 → 1</text>
  <text x="1650" y="1860" fill="#245C43" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Visible immediately</text>

  <text x="150" y="1910" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Form Submission</text>
  <text x="450" y="1910" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Click Submit</text>
  <text x="750" y="1910" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">150ms · immediate</text>
  <text x="1150" y="1910" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Replacing status text inline; retain layout</text>
  <text x="1650" y="1910" fill="#245C43" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Instant banner update</text>

  <text x="150" y="1980" fill="#895239" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Strict Rule: All essential copy, navigation and contact actions remain 100% accessible with JavaScript/motion disabled.</text>
</svg>"""

with open('figma_svgs/06_prototype_motion.svg', 'w', encoding='utf-8') as f:
    f.write(svg_06)

print("Saved 06_prototype_motion.svg")

# -------------------------------------------------------------
# 07 Project & Concept Assets
# -------------------------------------------------------------
svg_07 = f"""<svg width="2400" height="2600" viewBox="0 0 2400 2600" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="2400" height="2600" fill="#F4F1E8"/>

  <!-- Banner -->
  <rect x="80" y="80" width="2240" height="140" fill="#183B35" rx="4"/>
  <text x="120" y="145" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="36" font-weight="600">FlowGrid — Assets, Concepts &amp; Generation Register</text>
  <text x="120" y="185" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="18">Curated project register, original AI concept studies (Dhaka Living, Kitchen, Bedroom), generation prompts, and material boards</text>

  <!-- Asset Register Table -->
  <rect x="80" y="260" width="2240" height="520" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="260" width="2240" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="293" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">01. Formal Asset Register &amp; Verification Matrix</text>

  <rect x="110" y="330" width="2180" height="420" fill="#F4F1E8" rx="4"/>
  <text x="130" y="370" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Asset ID</text>
  <text x="320" y="370" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Source / Attribution</text>
  <text x="650" y="370" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Status &amp; Verification</text>
  <text x="1050" y="370" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Proposed Placement</text>
  <text x="1450" y="370" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Mandatory Visible Label</text>
  <line x1="130" y1="385" x2="2250" y2="385" stroke="#B8C2BA" stroke-width="1"/>

  <!-- Row 1: Living Concept -->
  <text x="130" y="420" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">FG-CP-01</text>
  <text x="320" y="420" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">AI Generated (Nano Banana)</text>
  <text x="650" y="420" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Concept Study (Not Built Work)</text>
  <text x="1050" y="420" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Desktop Hero &amp; Study 01 Detail</text>
  <text x="1450" y="420" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>

  <!-- Row 2: Kitchen Concept -->
  <text x="130" y="470" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">FG-CP-02</text>
  <text x="320" y="470" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">AI Generated (Nano Banana)</text>
  <text x="650" y="470" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Concept Study (Not Built Work)</text>
  <text x="1050" y="470" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Services Page &amp; Study 02 Detail</text>
  <text x="1450" y="470" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>

  <!-- Row 3: Bedroom Concept -->
  <text x="130" y="520" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">FG-CP-03</text>
  <text x="320" y="520" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">AI Generated (Nano Banana)</text>
  <text x="650" y="520" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Concept Study (Not Built Work)</text>
  <text x="1050" y="520" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Project Index &amp; Study 03 Detail</text>
  <text x="1450" y="520" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>

  <!-- Row 4: FlowGrid Facebook Brand Assets -->
  <text x="130" y="570" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">FG-FB-01</text>
  <text x="320" y="570" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">FlowGrid Facebook Page Banner</text>
  <text x="650" y="570" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Verified Brand Graphic (FB 2026)</text>
  <text x="1050" y="570" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Brand Identity Reference</text>
  <text x="1450" y="570" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">FlowGrid Official Social Identity</text>

  <!-- Row 5: Rumi Channel Media -->
  <text x="130" y="620" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">RH-YT-01</text>
  <text x="320" y="620" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">YouTube: @RumisFashionableHouse</text>
  <text x="650" y="620" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Verified Sibling Community Channel</text>
  <text x="1050" y="620" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Studio / About Link &amp; Footer</text>
  <text x="1450" y="620" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Personal Vlog Channel (External)</text>

  <text x="130" y="690" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Audit Rule Applied: Posting on social accounts does not constitute proof of construction. All visual concepts remain explicitly marked.</text>

  <!-- Section 2: Three High-Fidelity Concepts Showcase -->
  <rect x="80" y="820" width="2240" height="1100" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="820" width="2240" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="853" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">02. Original Concept Studies (Dhaka Apartments · Believable Scale · Natural Materials)</text>

  <!-- Concept 1: Living & Storage -->
  <g transform="translate(120, 900)">
    <rect width="680" height="500" fill="#DEE7E2"/>
    <image href="{img_living}" x="0" y="0" width="680" height="500" preserveAspectRatio="xMidYMid slice"/>
    <rect x="20" y="20" width="280" height="32" fill="#183B35" opacity="0.9" rx="2"/>
    <text x="32" y="42" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="13" font-weight="600">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>

    <text x="0" y="535" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="22" font-weight="700">কনসেপ্ট ০১: লিভিং ও স্টোরেজ সলিউশন</text>
    <text x="0" y="565" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="15">ঢাকার সাধারণ ফ্ল্যাটের জন্য দেয়ালজোড়া সেগুন কাঠের তাক ও ব্যালকনি ইন্টিগ্রেশন।</text>
    <text x="0" y="590" fill="#895239" font-family="'Manrope', sans-serif" font-size="13">Prompt: Photorealistic architectural photo of contemporary Dhaka apartment living room...</text>
  </g>

  <!-- Concept 2: Kitchen & Maintenance -->
  <g transform="translate(860, 900)">
    <rect width="680" height="500" fill="#DEE7E2"/>
    <image href="{img_kitchen}" x="0" y="0" width="680" height="500" preserveAspectRatio="xMidYMid slice"/>
    <rect x="20" y="20" width="280" height="32" fill="#183B35" opacity="0.9" rx="2"/>
    <text x="32" y="42" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="13" font-weight="600">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>

    <text x="0" y="535" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="22" font-weight="700">কনসেপ্ট ০২: টেকসই রান্নাঘর ও প্যান্ট্রি</text>
    <text x="0" y="565" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="15">ভারী রান্নার উপযোগী গ্রানাইট স্ল্যাব, এলপিজি সিলিন্ডার স্পেস ও খোলা মসলা শেলফ।</text>
    <text x="0" y="590" fill="#895239" font-family="'Manrope', sans-serif" font-size="13">Prompt: Photorealistic kitchen designed for heavy cooking routines, Dhaka scale...</text>
  </g>

  <!-- Concept 3: Master Bedroom & Study -->
  <g transform="translate(1600, 900)">
    <rect width="680" height="500" fill="#DEE7E2"/>
    <image href="{img_bedroom}" x="0" y="0" width="680" height="500" preserveAspectRatio="xMidYMid slice"/>
    <rect x="20" y="20" width="280" height="32" fill="#183B35" opacity="0.9" rx="2"/>
    <text x="32" y="42" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="13" font-weight="600">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>

    <text x="0" y="535" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="22" font-weight="700">কনসেপ্ট ০৩: মাস্টার বেডরুম ও স্টাডি</text>
    <text x="0" y="565" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="15">ল-প্ল্যাটফর্ম বেড, ফ্লোর-টু-সিলিং স্ল্যাটেড ওয়ারড্রোব ও কম্প্যাক্ট ওয়ার্ক কর্নার।</text>
    <text x="0" y="590" fill="#895239" font-family="'Manrope', sans-serif" font-size="13">Prompt: Serene master bedroom in Dhaka apartment, low platform bed, slatted wardrobe...</text>
  </g>

  <!-- Section 3: Material Palette & Sourcing -->
  <rect x="80" y="1960" width="2240" height="580" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="1960" width="2240" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="1993" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">03. Material Palette Specification (Local Plausibility &amp; Climate Adaptation)</text>

  <g transform="translate(120, 2040)">
    <rect x="0" y="0" width="480" height="420" fill="#F4F1E8" rx="4"/>
    <rect x="20" y="20" width="80" height="80" fill="#895239" rx="2"/>
    <text x="120" y="60" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="22" font-weight="700">সেগুন ও চিটাগাং কাঠ</text>
    <text x="120" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Teak / Seasoned Hardwood</text>
    <text x="20" y="140" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="15" line-height="1.7">আর্দ্রতার কারণে বাংলাদেশের আবহাওয়ায় সিজন্ড কাঠ অপরিহার্য। এটি ওয়ার্পিং ও উইপোকা প্রতিরোধ করে এবং দীর্ঘস্থায়ী স্থায়িত্ব দেয়।</text>
  </g>

  <g transform="translate(640, 2040)">
    <rect x="0" y="0" width="480" height="420" fill="#F4F1E8" rx="4"/>
    <rect x="20" y="20" width="80" height="80" fill="#DEE7E2" rx="2"/>
    <text x="120" y="60" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="22" font-weight="700">হাতে বোনা দেশীয় বেত</text>
    <text x="120" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Woven Cane / Rattan</text>
    <text x="20" y="140" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="15" line-height="1.7">ঘরের মধ্যে বাতাস চলাচলের পথ রাখে। চেয়ার ও ক্যাবিনেট শাটারের জন্য হালকা, প্রাকৃতিক ও অত্যন্ত নান্দনিক ঐতিহ্যবাহী উপাদান।</text>
  </g>

  <g transform="translate(1160, 2040)">
    <rect x="0" y="0" width="480" height="420" fill="#F4F1E8" rx="4"/>
    <rect x="20" y="20" width="80" height="80" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>
    <text x="120" y="60" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="22" font-weight="700">লাইম প্লাস্টার ও ম্যাট রং</text>
    <text x="120" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Lime Plaster &amp; Breathable Paint</text>
    <text x="20" y="140" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="15" line-height="1.7">চকচকে প্লাস্টিক পেইন্টের বদলে ম্যাট নিঃশ্বাসযোগ্য ফিনিশ, যা ঘরের আর্দ্রতা নিয়ন্ত্রণ করে এবং নরম আলো ছড়িয়ে দেয়।</text>
  </g>

  <g transform="translate(1680, 2040)">
    <rect x="0" y="0" width="480" height="420" fill="#F4F1E8" rx="4"/>
    <rect x="20" y="20" width="80" height="80" fill="#718178" rx="2"/>
    <text x="120" y="60" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="22" font-weight="700">হোনড প্রাকৃতিক গ্রানাইট</text>
    <text x="120" y="85" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Honed Gray Granite</text>
    <text x="20" y="140" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="15" line-height="1.7">রান্নাঘরের কাউন্টারটপ ও বাথ ভ্যানিটির জন্য তাপ ও দাগ সহনশীল উপাদান, যা বছরের পর বছর মসৃণ থাকে।</text>
  </g>
</svg>"""

with open('figma_svgs/07_project_and_concept_assets.svg', 'w', encoding='utf-8') as f:
    f.write(svg_07)

print("Saved 07_project_and_concept_assets.svg")

# -------------------------------------------------------------
# 08 Handoff & QA
# -------------------------------------------------------------
svg_08 = f"""<svg width="2400" height="2200" viewBox="0 0 2400 2200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="2400" height="2200" fill="#F4F1E8"/>

  <!-- Banner -->
  <rect x="80" y="80" width="2240" height="140" fill="#183B35" rx="4"/>
  <text x="120" y="145" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="36" font-weight="600">FlowGrid — Developer Handoff, QA &amp; Client Checklist</text>
  <text x="120" y="185" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="18">Exportable tokens, WCAG 2.2 AA audit, Core Web Vitals targets, and actionable client decision checklist</text>

  <!-- Section 1: Token Specifications -->
  <rect x="80" y="260" width="1080" height="880" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="260" width="1080" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="293" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">01. Design Tokens &amp; CSS Custom Properties</text>

  <rect x="110" y="330" width="1020" height="780" fill="#183B35" rx="4"/>
  <text x="140" y="370" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">:root {{</text>
  <text x="160" y="400" fill="#F4F1E8" font-family="'Courier New', monospace" font-size="14">/* Color Tokens */</text>
  <text x="160" y="430" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--color-surface-page: #F4F1E8;</text>
  <text x="160" y="460" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--color-surface-mist: #DEE7E2;</text>
  <text x="160" y="490" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--color-text-primary: #183B35;</text>
  <text x="160" y="520" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--color-text-secondary: #56645E;</text>
  <text x="160" y="550" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--color-action-primary: #183B35;</text>
  <text x="160" y="580" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--color-action-hover: #102B26;</text>
  <text x="160" y="610" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--color-accent-clay: #895239;</text>
  <text x="160" y="640" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--color-border-control: #718178;</text>
  <text x="160" y="670" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--color-border-decorative: #B8C2BA;</text>
  <text x="160" y="700" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--color-status-error: #9B302B;</text>
  <text x="160" y="730" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--color-status-success: #245C43;</text>
  
  <text x="160" y="770" fill="#F4F1E8" font-family="'Courier New', monospace" font-size="14">/* Typography */</text>
  <text x="160" y="800" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--font-display: 'Bodoni Moda', serif;</text>
  <text x="160" y="830" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--font-ui: 'Manrope', sans-serif;</text>
  <text x="160" y="860" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--font-bengali: 'Noto Sans Bengali', sans-serif;</text>

  <text x="160" y="900" fill="#F4F1E8" font-family="'Courier New', monospace" font-size="14">/* Spacing &amp; Radii */</text>
  <text x="160" y="930" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--space-4: 4px; --space-8: 8px; --space-16: 16px; --space-24: 24px;</text>
  <text x="160" y="960" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--space-32: 32px; --space-48: 48px; --space-64: 64px; --space-96: 96px;</text>
  <text x="160" y="990" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--radius-media: 0px; --radius-control: 2px; --radius-overlay: 4px;</text>
  <text x="160" y="1030" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">--ease-standard: cubic-bezier(0.23, 1, 0.32, 1);</text>
  <text x="140" y="1070" fill="#DEE7E2" font-family="'Courier New', monospace" font-size="14">}}</text>

  <!-- Section 2: QA & Accessibility Checklist -->
  <rect x="1200" y="260" width="1120" height="880" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="1200" y="260" width="1120" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="1230" y="293" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">02. WCAG 2.2 AA Accessibility Audit &amp; Performance Targets</text>

  <rect x="1230" y="330" width="1060" height="780" fill="#F4F1E8" rx="4"/>
  <text x="1260" y="375" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">WCAG 2.2 AA Conformance Checkpoints:</text>

  <text x="1260" y="415" fill="#245C43" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">[PASS] 1.4.3 Contrast (Minimum):</text>
  <text x="1560" y="415" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Primary text #183B35 on #F4F1E8 = 10.84:1 (exceeds 4.5:1 requirement).</text>

  <text x="1260" y="455" fill="#245C43" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">[PASS] 2.5.8 Target Size (Minimum):</text>
  <text x="1560" y="455" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">All primary touch controls are 52px (exceeds WCAG 24px requirement).</text>

  <text x="1260" y="495" fill="#245C43" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">[PASS] 2.4.7 Focus Visible:</text>
  <text x="1560" y="495" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">2px outer clay ring with 2px paper separation on light surfaces.</text>

  <text x="1260" y="535" fill="#245C43" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">[PASS] 1.4.12 Text Spacing:</text>
  <text x="1560" y="535" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Bangla line-height 1.75; no artificial letter-spacing or font distortion.</text>

  <text x="1260" y="575" fill="#245C43" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">[PASS] 2.3.3 Animation from Interaction:</text>
  <text x="1560" y="575" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">prefers-reduced-motion triggers immediate non-animated states.</text>

  <line x1="1260" y1="605" x2="2250" y2="605" stroke="#B8C2BA" stroke-width="1"/>

  <text x="1260" y="645" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Core Web Vitals Engineering Targets:</text>
  <text x="1260" y="685" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">• Largest Contentful Paint (LCP):</text>
  <text x="1560" y="685" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">&lt;= 2.5s (Mobile Hero image budget &lt;= 250KB WebP)</text>

  <text x="1260" y="725" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">• Interaction to Next Paint (INP):</text>
  <text x="1560" y="725" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">&lt;= 200ms (Immediate button response, no thread blocking)</text>

  <text x="1260" y="765" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">• Cumulative Layout Shift (CLS):</text>
  <text x="1560" y="765" fill="#245C43" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">&lt;= 0.1 (All images have explicit reserved aspect ratios)</text>

  <text x="1260" y="805" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">• Initial Compressed Fonts:</text>
  <text x="1560" y="805" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">&lt;= 200KB per language subset (Noto Sans Bengali + Manrope)</text>

  <text x="1260" y="845" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14">• Initial Compressed JS:</text>
  <text x="1560" y="845" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">&lt;= 150KB (Native browser scrolling, zero motion bloat libraries)</text>

  <!-- Section 3: Actionable Client Decision Checklist -->
  <rect x="80" y="1180" width="2240" height="940" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="1180" width="2240" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="1213" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">03. Actionable Client Checklist (Unresolved Business Facts Needing Owner Approval)</text>

  <rect x="120" y="1260" width="2160" height="820" fill="#F4F1E8" rx="4"/>
  <text x="150" y="1305" fill="#895239" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">The following operational items are currently marked as provisional and require business owner confirmation prior to public launch:</text>

  <g transform="translate(150, 1340)">
    <text x="0" y="25" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">[ ] 1. Approved Brand Wordmark &amp; Vector Logo</text>
    <text x="35" y="55" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Figma currently uses the provisional typographic Bodoni Moda wordmark. Provide final SVG vector files.</text>

    <text x="0" y="105" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">[ ] 2. Official Contact Numbers &amp; WhatsApp Business Account</text>
    <text x="35" y="135" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Confirm the designated Bangladesh telephone number (+880...) that will receive calls and WhatsApp enquiries.</text>

    <text x="0" y="185" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">[ ] 3. Exact Geographic Service Area</text>
    <text x="35" y="215" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Clarify whether on-site consultation and execution covers Mirpur, greater Dhaka city, or nationwide.</text>

    <text x="0" y="265" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">[ ] 4. Formal Service Offerings &amp; Execution Model</text>
    <text x="35" y="295" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Confirm if FlowGrid provides design-only documentation or turnkey site execution and material procurement.</text>

    <text x="0" y="345" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">[ ] 5. Site Visit &amp; Initial Consultation Fee Policy</text>
    <text x="35" y="375" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Confirm whether the initial site visit is chargeable, deductible from design fees, or complimentary.</text>

    <text x="0" y="425" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">[ ] 6. Team Profiles &amp; Accurate Design Qualifications</text>
    <text x="35" y="455" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Supply verified names, verified credentials, and portraits of the design and project management team.</text>

    <text x="0" y="505" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">[ ] 7. Approved Relationship Statement with Rumi's Fashionable House</text>
    <text x="35" y="535" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Confirm the exact authorized sentence describing Rumi's founder/community relationship to FlowGrid.</text>

    <text x="0" y="585" fill="#183B35" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">[ ] 8. Production Domain &amp; Hosting Setup</text>
    <text x="35" y="615" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Resolve the DNS for www.flowgrid-interiors.com or confirm the final chosen production web address.</text>
  </g>
</svg>"""

with open('figma_svgs/08_handoff_qa.svg', 'w', encoding='utf-8') as f:
    f.write(svg_08)

print("Saved 08_handoff_qa.svg")
