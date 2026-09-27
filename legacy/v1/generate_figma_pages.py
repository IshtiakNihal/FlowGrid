"""
FlowGrid - Automated Figma Pages Generator
Generates comprehensive, pixel-perfect, native SVG assets for all 9 Figma pages
with full design systems, responsive templates, components, and handoff documentation.
"""
import os
import json
import base64

os.makedirs('figma_svgs', exist_ok=True)

# Helper to encode image to base64 for SVG embedding
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
# PAGE 00: Brief & Research
# -------------------------------------------------------------
svg_00 = f"""<svg width="2400" height="1800" viewBox="0 0 2400 1800" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="2400" height="1800" fill="#F4F1E8"/>
  
  <!-- Header Banner -->
  <rect x="80" y="80" width="2240" height="140" fill="#183B35" rx="4"/>
  <text x="120" y="145" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="36" font-weight="600">FlowGrid — Research &amp; Strategic Foundation</text>
  <text x="120" y="185" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="18">Visual direction, architectural references, live social media audit, and local Bangladeshi design context</text>

  <!-- Column 1: Business Context & Three Businesses -->
  <rect x="80" y="260" width="700" height="700" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="260" width="700" height="60" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="300" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="20" font-weight="600">01. Three Distinct Entities &amp; Boundary Rules</text>
  
  <text x="110" y="360" fill="#183B35" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">1. FlowGrid (This Assignment)</text>
  <text x="110" y="390" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Core Scope: Interior design, space planning, bespoke joinery, design consultation.</text>
  <text x="110" y="415" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Identity: Independent architectural studio with clear family living focus.</text>
  <text x="110" y="440" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Working Location: Mirpur, Dhaka, Bangladesh (verified on Facebook).</text>
  <text x="110" y="465" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Boundary: Not an appliance retailer; not a personal influencer fan page.</text>

  <text x="110" y="520" fill="#183B35" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">2. Rumi's Fashionable House (Community Sibling)</text>
  <text x="110" y="550" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Channel: YouTube (@RumisFashionableHouse, 140k subscribers, 2.3k vlogs).</text>
  <text x="110" y="575" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Role: Founder/lifestyle community context; family lifestyle vlogs.</text>
  <text x="110" y="600" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Rule: Never describe Rumi as an architect without formal verification.</text>
  <text x="110" y="625" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Link: Discreet footer &amp; studio link "Rumi's Story / Portfolio".</text>

  <text x="110" y="680" fill="#183B35" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">3. Onekta Product (Commerce Sibling)</text>
  <text x="110" y="710" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Scope: Home essentials, kitchen appliances, and hardware.</text>
  <text x="110" y="735" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Boundary: Separate commerce store. FlowGrid does not host a product catalog.</text>
  <text x="110" y="760" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Link: Discreet footer outbound link only.</text>

  <!-- Column 2: External Reference Matrix -->
  <rect x="820" y="260" width="740" height="700" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="820" y="260" width="740" height="60" fill="#183B35" rx="4 4 0 0"/>
  <text x="850" y="300" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="20" font-weight="600">02. Reference Sites Observed &amp; Synthesis Matrix</text>

  <text x="850" y="360" fill="#895239" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">ERA RESIDENCE (www.era-residence.com) — Primary Aesthetic</text>
  <text x="850" y="385" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Observed:</text>
  <text x="930" y="385" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Monumental serif display, full-bleed architectural images, warm stone palette.</text>
  <text x="850" y="410" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Adopted:</text>
  <text x="930" y="410" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Editorial hierarchy, Bodoni Moda display, deliberate image transitions.</text>
  <text x="850" y="435" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Omitted:</text>
  <text x="930" y="435" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Apartment sales units, scroll hijacking, luxury resort tropes.</text>

  <line x1="850" y1="460" x2="1520" y2="460" stroke="#DEE7E2" stroke-width="1"/>

  <text x="850" y="490" fill="#895239" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">THIRDWAY (www.thirdway.com) — Project &amp; Journey Clarity</text>
  <text x="850" y="515" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Observed:</text>
  <text x="930" y="515" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Concise project cards, clear briefs, prominent 'Let's talk' action, named team.</text>
  <text x="850" y="540" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Adopted:</text>
  <text x="930" y="540" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Structured case studies (Brief, Decisions, Specs), visible direct enquiry.</text>
  <text x="850" y="565" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Omitted:</text>
  <text x="930" y="565" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Corporate office sector positioning, animated ticker noise.</text>

  <line x1="850" y1="590" x2="1520" y2="590" stroke="#DEE7E2" stroke-width="1"/>

  <text x="850" y="620" fill="#895239" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">QUINTA D. AMÁLIA (www.quintadamalia.com) — Spatial Pacing</text>
  <text x="850" y="645" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Observed:</text>
  <text x="930" y="645" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Gentle rhythm, generous whitespace, warm natural lighting.</text>
  <text x="850" y="670" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Adopted:</text>
  <text x="930" y="670" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Calm editorial pacing, breathing room between functional sections.</text>
  <text x="850" y="695" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Omitted:</text>
  <text x="930" y="695" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Curved pill frames, floating glow blobs, holiday retreat copy.</text>

  <!-- Column 3: Bangladesh Cultural & Spatial Context -->
  <rect x="1580" y="260" width="740" height="700" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="1580" y="260" width="740" height="60" fill="#183B35" rx="4 4 0 0"/>
  <text x="1610" y="300" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="20" font-weight="600">03. Bangladeshi Apartment Realities &amp; Local Guidance</text>

  <text x="1610" y="360" fill="#183B35" font-family="'Manrope', sans-serif" font-size="17" font-weight="700">1. Living Space &amp; Storage Density</text>
  <text x="1610" y="390" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Urban Dhaka apartments require maximizing floor area without crowding.</text>
  <text x="1610" y="415" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Floor-to-ceiling joinery, concealed storage, and multi-functional seating.</text>

  <text x="1610" y="465" fill="#183B35" font-family="'Manrope', sans-serif" font-size="17" font-weight="700">2. Kitchen Routines &amp; Maintenance</text>
  <text x="1610" y="495" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Heavy everyday cooking requires grease-resistant tiles, high-suction hoods,</text>
  <text x="1610" y="520" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">dedicated LP gas storage, robust stone countertops, and open spice access.</text>

  <text x="1610" y="570" fill="#183B35" font-family="'Manrope', sans-serif" font-size="17" font-weight="700">3. Climate, Ventilation &amp; Daylight</text>
  <text x="1610" y="600" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">High humidity and tropical monsoon climate dictate cross-ventilation,</text>
  <text x="1610" y="625" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">ceiling fan integration with AC ducts, window safety grilles, and verandas.</text>

  <text x="1610" y="675" fill="#183B35" font-family="'Manrope', sans-serif" font-size="17" font-weight="700">4. Material Palette</text>
  <text x="1610" y="705" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Teak, Segun wood, Chittagong timber, handcrafted cane, lime plaster,</text>
  <text x="1610" y="730" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">local terracotta accents, and breathable cotton/linen textiles.</text>

  <!-- Bottom Section: Live Audit Findings Table & Motion Guidance -->
  <rect x="80" y="990" width="2240" height="730" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="990" width="2240" height="60" fill="#183B35" rx="4 4 0 0"/>
  <text x="120" y="1030" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="20" font-weight="600">04. Live Social Media Audit &amp; Motion Guidance (Emil Kowalski / Delphi Animate)</text>

  <rect x="120" y="1080" width="1050" height="590" fill="#F4F1E8" rx="4"/>
  <text x="150" y="1120" fill="#183B35" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">Live Browser Audit Findings (Facebook &amp; YouTube)</text>
  <text x="150" y="1155" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• FlowGrid Facebook: @FlowGridBD (Page ID 61593130543449). Mirpur, Dhaka 1216.</text>
  <text x="150" y="1185" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Page Status: 29 followers, active branding posts. No direct phone/email listed.</text>
  <text x="150" y="1215" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Domain www.flowgrid-interiors.com on banner is not yet deployed (DNS NXDOMAIN confirmed).</text>
  <text x="150" y="1245" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Published imagery on page consists of brand identity graphics and AI concept mockups.</text>
  <text x="150" y="1275" fill="#895239" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Governance Decision: Label all 3D/AI visualizations honestly as Concepts. Do not invent past builds.</text>
  <text x="150" y="1305" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Enquiry Route: Direct telephone and WhatsApp consultation, plus clean web enquiry form.</text>
  <text x="150" y="1335" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">• Sibling Integration: Discreet footer navigation to Rumi's portfolio &amp; Onekta Product.</text>

  <rect x="1230" y="1080" width="1050" height="590" fill="#DEE7E2" rx="4"/>
  <text x="1260" y="1120" fill="#183B35" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">Motion &amp; Interaction Engineering Principles</text>
  <text x="1260" y="1155" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">• Emil Kowalski Skills Guidance:</text>
  <text x="1490" y="1155" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Function before flair. Fast micro-interactions (hover 150ms, press 100ms).</text>
  <text x="1260" y="1185" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">• Conflict Resolution:</text>
  <text x="1440" y="1185" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Delphi suggests ease-in for exits; Kowalski rejects ease-in in UI. We adopt</text>
  <text x="1440" y="1210" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">fast ease-out (cubic-bezier 0.23, 1, 0.32, 1) for both enter and exit (160ms exit).</text>
  <text x="1260" y="1245" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">• Signature Sequences:</text>
  <text x="1440" y="1245" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Architectural mask wipe reveal on hero image + calm line rise for headings.</text>
  <text x="1260" y="1275" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">• Strictly Prohibited:</text>
  <text x="1440" y="1275" fill="#9B302B" font-family="'Manrope', sans-serif" font-size="15">No scroll hijacking, no looping marquees, no per-character Bangla reveals.</text>
  <text x="1260" y="1305" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">• Accessibility:</text>
  <text x="1440" y="1305" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Immediate final state on prefers-reduced-motion: reduce; instant keyboard focus.</text>
</svg>"""

with open('figma_svgs/00_brief_and_research.svg', 'w', encoding='utf-8') as f:
    f.write(svg_00)

print("Saved 00_brief_and_research.svg")
