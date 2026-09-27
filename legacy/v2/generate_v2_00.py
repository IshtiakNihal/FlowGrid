"""
FlowGrid - Page 00 (Brief & Research) and Page 01 (Foundations) Generator v2
Fixes text overflow using textwrap and provides non-clipped, bounded layouts.
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

# -------------------------------------------------------------
# 00 Brief & Research v2
# -------------------------------------------------------------
svg_00 = f"""<svg width="2400" height="1900" viewBox="0 0 2400 1900" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="2400" height="1900" fill="#F4F1E8"/>
  
  <!-- Banner -->
  <rect x="80" y="80" width="2240" height="140" fill="#183B35" rx="4"/>
  <text x="120" y="145" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="36" font-weight="600">FlowGrid — Research &amp; Strategic Foundation (Audited v2)</text>
  <text x="120" y="185" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="18">Visual direction, architectural references, live social media audit, and local Bangladeshi design context</text>

  <!-- Column 1: Business Context & Three Businesses -->
  <rect x="80" y="260" width="700" height="740" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="260" width="700" height="60" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="300" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="20" font-weight="600">01. Three Entities &amp; Boundary Governance</text>
  
  <text x="110" y="360" fill="#183B35" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">1. FlowGrid (Interior Design Studio)</text>
  {wrap_text("• Core Scope: Space planning, bespoke joinery, family living solutions, and design consultation.", 110, 390, 68, 22, "'Manrope', sans-serif", 14, "#56645E")}
  {wrap_text("• Identity: Independent architectural studio serving urban Bangladeshi homeowners.", 110, 440, 68, 22, "'Manrope', sans-serif", 14, "#56645E")}
  {wrap_text("• Location: Mirpur, Dhaka 1216 (verified on official Facebook page).", 110, 490, 68, 22, "'Manrope', sans-serif", 14, "#56645E")}
  {wrap_text("• Boundary Rule: Not an appliance retailer; not an influencer fan club; not a generic construction contractor.", 110, 540, 68, 22, "'Manrope', sans-serif", 14, "#895239", 600)}

  <text x="110" y="610" fill="#183B35" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">2. Rumi's Fashionable House (Community Sibling)</text>
  {wrap_text("• Platform: YouTube (@RumisFashionableHouse, 140k subscribers, 2,368 videos, 36.6M views).", 110, 640, 68, 22, "'Manrope', sans-serif", 14, "#56645E")}
  {wrap_text("• Role: Personal lifestyle vlogs, home cooking, and loyal community context.", 110, 690, 68, 22, "'Manrope', sans-serif", 14, "#56645E")}
  {wrap_text("• Governance Rule: Rumi is not an architect and must not be described as one. She provides founder/lifestyle context. Linked discreetly in footer/studio.", 110, 740, 68, 22, "'Manrope', sans-serif", 14, "#895239", 600)}

  <text x="110" y="820" fill="#183B35" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">3. Onekta Product (Commerce Sibling)</text>
  {wrap_text("• Scope: Commercial appliances, kitchenware, and household merchandise.", 110, 850, 68, 22, "'Manrope', sans-serif", 14, "#56645E")}
  {wrap_text("• Boundary Rule: Completely separate commerce destination. FlowGrid hosts zero retail products or checkout flows. Outbound footer link only.", 110, 900, 68, 22, "'Manrope', sans-serif", 14, "#895239", 600)}

  <!-- Column 2: External Reference Synthesis Matrix -->
  <rect x="820" y="260" width="740" height="740" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="820" y="260" width="740" height="60" fill="#183B35" rx="4 4 0 0"/>
  <text x="850" y="300" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="20" font-weight="600">02. Reference Sites Observed &amp; Synthesis Matrix</text>

  <text x="850" y="355" fill="#895239" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">ERA RESIDENCE (www.era-residence.com) — Primary Aesthetic</text>
  <text x="850" y="380" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Observed:</text>
  {wrap_text("Monumental serif display type, full-bleed architectural photography, warm stone palette, confident scale transitions.", 930, 380, 60, 20, "'Manrope', sans-serif", 13, "#56645E")}
  <text x="850" y="430" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Adopted:</text>
  {wrap_text("Bodoni Moda editorial display type, architectural framing, deliberate image transitions, generous breathing room.", 930, 430, 60, 20, "'Manrope', sans-serif", 13, "#56645E")}
  <text x="850" y="480" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Omitted:</text>
  {wrap_text("Apartment sales units, scroll hijacking, luxury resort tropes.", 930, 480, 60, 20, "'Manrope', sans-serif", 13, "#56645E")}

  <line x1="850" y1="515" x2="1520" y2="515" stroke="#DEE7E2" stroke-width="1"/>

  <text x="850" y="545" fill="#895239" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">THIRDWAY (www.thirdway.com) — Project &amp; Journey Clarity</text>
  <text x="850" y="570" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Observed:</text>
  {wrap_text("Structured project cards, clear briefs and design responses, prominent 'Let's talk' action, named team.", 930, 570, 60, 20, "'Manrope', sans-serif", 13, "#56645E")}
  <text x="850" y="620" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Adopted:</text>
  {wrap_text("Concise case study hierarchy (Brief → Space Decisions → Material Specs), visible direct enquiry paths.", 930, 620, 60, 20, "'Manrope', sans-serif", 13, "#56645E")}
  <text x="850" y="670" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Omitted:</text>
  {wrap_text("Corporate office positioning, animated ticker noise.", 930, 670, 60, 20, "'Manrope', sans-serif", 13, "#56645E")}

  <line x1="850" y1="705" x2="1520" y2="705" stroke="#DEE7E2" stroke-width="1"/>

  <text x="850" y="735" fill="#895239" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">QUINTA D. AMÁLIA (www.quintadamalia.com) — Spatial Pacing</text>
  <text x="850" y="760" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Observed:</text>
  {wrap_text("Gentle rhythm, generous whitespace, warm natural lighting.", 930, 760, 60, 20, "'Manrope', sans-serif", 13, "#56645E")}
  <text x="850" y="805" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Adopted:</text>
  {wrap_text("Calm editorial pacing, breathing room between functional sections.", 930, 805, 60, 20, "'Manrope', sans-serif", 13, "#56645E")}
  <text x="850" y="850" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Omitted:</text>
  {wrap_text("Curved pill frames, floating glow blobs, holiday retreat copy.", 930, 850, 60, 20, "'Manrope', sans-serif", 13, "#56645E")}

  <!-- Column 3: Bangladesh Cultural & Spatial Context -->
  <rect x="1580" y="260" width="740" height="740" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="1580" y="260" width="740" height="60" fill="#183B35" rx="4 4 0 0"/>
  <text x="1610" y="300" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="20" font-weight="600">03. Bangladeshi Apartment Realities</text>

  <text x="1610" y="360" fill="#183B35" font-family="'Manrope', sans-serif" font-size="17" font-weight="700">1. Living Space &amp; Storage Density</text>
  {wrap_text("Urban Dhaka apartments require maximizing floor area without crowding. Floor-to-ceiling joinery, concealed storage, and multi-functional seating keep circulation clear.", 1610, 390, 68, 22, "'Manrope', sans-serif", 14, "#56645E")}

  <text x="1610" y="470" fill="#183B35" font-family="'Manrope', sans-serif" font-size="17" font-weight="700">2. Kitchen Routines &amp; Maintenance</text>
  {wrap_text("Intensive everyday cooking requires grease-resistant tiles, high-suction hoods, dedicated ventilated LP gas storage, robust stone countertops, and open spice access.", 1610, 500, 68, 22, "'Manrope', sans-serif", 14, "#56645E")}

  <text x="1610" y="580" fill="#183B35" font-family="'Manrope', sans-serif" font-size="17" font-weight="700">3. Climate, Ventilation &amp; Daylight</text>
  {wrap_text("High humidity and tropical monsoon climate dictate cross-ventilation, ceiling fan integration with AC ducts, window safety grilles, and verandas.", 1610, 610, 68, 22, "'Manrope', sans-serif", 14, "#56645E")}

  <text x="1610" y="690" fill="#183B35" font-family="'Manrope', sans-serif" font-size="17" font-weight="700">4. Material Palette</text>
  {wrap_text("Teak, Segun wood, Chittagong timber, handcrafted cane, lime plaster, local terracotta accents, and breathable cotton/linen textiles.", 1610, 720, 68, 22, "'Manrope', sans-serif", 14, "#56645E")}

  <!-- Bottom Section: Live Audit Findings Table & Motion Guidance -->
  <rect x="80" y="1030" width="2240" height="780" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="1030" width="2240" height="60" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="1070" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="20" font-weight="600">04. Dated Social Media Audit &amp; Motion Guidance (Emil Kowalski / Delphi Animate)</text>

  <rect x="120" y="1120" width="1050" height="650" fill="#F4F1E8" rx="4"/>
  <text x="150" y="1160" fill="#183B35" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">Live Browser Audit Findings (Audited 26 Sept 2026)</text>
  {wrap_text("• FlowGrid Facebook: @FlowGridBD (ID: 61593130543449). Address: Mirpur, Dhaka 1216.", 150, 1195, 80, 24, "'Manrope', sans-serif", 14, "#56645E")}
  {wrap_text("• Account Activity: 29 followers, active branding posts. No direct phone or email published.", 150, 1250, 80, 24, "'Manrope', sans-serif", 14, "#56645E")}
  {wrap_text("• Production Domain: Banner states www.flowgrid-interiors.com (DNS confirmed NXDOMAIN; not yet deployed).", 150, 1305, 80, 24, "'Manrope', sans-serif", 14, "#56645E")}
  {wrap_text("• Visual Assets: Imagery on social accounts consists of branding graphics and AI concept mockups.", 150, 1360, 80, 24, "'Manrope', sans-serif", 14, "#56645E")}
  {wrap_text("• Governance Decision: Label all 3D/AI visualizations honestly as Concepts. Do not invent past builds.", 150, 1415, 80, 24, "'Manrope', sans-serif", 14, "#895239", 700)}
  {wrap_text("• Enquiry Channels: Verified direct telephone dialer and WhatsApp consultation, plus clean web enquiry form.", 150, 1470, 80, 24, "'Manrope', sans-serif", 14, "#56645E")}
  {wrap_text("• Cross-Site Navigation: Discreet footer gateways to Rumi's portfolio & Onekta Product.", 150, 1525, 80, 24, "'Manrope', sans-serif", 14, "#56645E")}

  <rect x="1230" y="1120" width="1050" height="650" fill="#DEE7E2" rx="4"/>
  <text x="1260" y="1160" fill="#183B35" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">Motion &amp; Interaction Engineering Principles</text>
  {wrap_text("• Emil Kowalski Skills Guidance: Purpose-first motion. Economical timings: hover 150ms, press 100ms, menu 220ms in / 160ms out.", 1260, 1195, 80, 24, "'Manrope', sans-serif", 14, "#56645E")}
  {wrap_text("• Easing Conflict Resolution: Delphi suggests ease-in for exits; Kowalski rejects ease-in in UI. We adopt fast ease-out (cubic-bezier 0.23, 1, 0.32, 1) for both entrances and exits.", 1260, 1250, 80, 24, "'Manrope', sans-serif", 14, "#56645E")}
  {wrap_text("• Signature Sequences: Architectural dual-wing mask wipe reveal on hero image + whole-line text rise. Zero per-character Bengali letter splitting.", 1260, 1315, 80, 24, "'Manrope', sans-serif", 14, "#56645E")}
  {wrap_text("• Prohibited Behaviors: No scroll hijacking, no looping marquees, no cursor followers, no forced decorative preloader curtains.", 1260, 1380, 80, 24, "'Manrope', sans-serif", 14, "#9B302B", 600)}
  {wrap_text("• Accessibility Compliance: prefers-reduced-motion triggers immediate non-animated state. All essential navigation, copy and CTAs remain usable instantly without waiting for motion.", 1260, 1445, 80, 24, "'Manrope', sans-serif", 14, "#245C43", 600)}
</svg>"""

with open('figma_svgs_v2/00_brief_and_research.svg', 'w', encoding='utf-8') as f:
    f.write(svg_00)

print("Saved figma_svgs_v2/00_brief_and_research.svg")
