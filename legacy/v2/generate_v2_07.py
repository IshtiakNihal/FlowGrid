"""
FlowGrid - Page 07 (Project & Concept Assets) Generator v2
Comprehensive Concept Asset Register, all 5 photorealistic concept views,
material specimen swatches, and documented architectural assumptions.
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

def wrap_text(text, x, y, max_chars, line_height, font_family, font_size, fill, font_weight=400):
    lines = textwrap.wrap(text, width=max_chars)
    tspans = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else line_height
        tspans.append(f'<tspan x="{x}" dy="{dy}">{line}</tspan>')
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{font_family}" font-size="{font_size}" font-weight="{font_weight}">' + "".join(tspans) + '</text>'

svg = f"""<svg width="2800" height="2900" viewBox="0 0 2800 2900" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="2800" height="2900" fill="#F4F1E8"/>

  <!-- Top Banner -->
  <rect x="80" y="80" width="2640" height="130" fill="#183B35" rx="4"/>
  <text x="120" y="145" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="34" font-weight="600">FlowGrid — Architectural Concept Assets &amp; Material Register (v2)</text>
  <text x="120" y="180" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="16">5 Photorealistic Dhaka Apartment Studies, Multi-Angle Coherence, Material Swatches, and Truth-in-Advertising Governance</text>

  <!-- ========================================================================= -->
  <!-- SECTION 1: ASSET REGISTER AUDIT TABLE                                     -->
  <!-- ========================================================================= -->
  <rect x="80" y="250" width="2640" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="250" width="2640" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="283" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">01. Verified Asset Register &amp; Disclosure Traceability Table</text>

  <!-- Table Header -->
  <rect x="110" y="320" width="2580" height="40" fill="#DEE7E2" rx="2"/>
  <text x="130" y="345" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">ASSET ID</text>
  <text x="250" y="345" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">STUDY TITLE &amp; ANGLE</text>
  <text x="650" y="345" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">SPATIAL CONTEXT</text>
  <text x="1050" y="345" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">DIMENSIONS</text>
  <text x="1250" y="345" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">CLASSIFICATION</text>
  <text x="1600" y="345" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">MANDATORY DISCLOSURE STRING</text>

  <!-- Row 1 -->
  <line x1="110" y1="365" x2="2690" y2="365" stroke="#B8C2BA" stroke-width="1"/>
  <text x="130" y="395" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">AST-01A</text>
  <text x="250" y="395" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Gulshan Living — Wide Hero</text>
  <text x="650" y="395" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">Open living &amp; full-height bookcase</text>
  <text x="1050" y="395" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13">1024 × 1024 (1:1)</text>
  <text x="1250" y="395" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">AI Visualisation (Concept)</text>
  <text x="1600" y="395" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>

  <!-- Row 2 -->
  <line x1="110" y1="415" x2="2690" y2="415" stroke="#B8C2BA" stroke-width="1"/>
  <text x="130" y="445" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">AST-01B</text>
  <text x="250" y="445" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Gulshan Living — Dining &amp; Daylight</text>
  <text x="650" y="445" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">Veranda light wash &amp; cane divider</text>
  <text x="1050" y="445" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13">1024 × 1024 (1:1)</text>
  <text x="1250" y="445" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">AI Visualisation (Concept)</text>
  <text x="1600" y="445" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>

  <!-- Row 3 -->
  <line x1="110" y1="465" x2="2690" y2="465" stroke="#B8C2BA" stroke-width="1"/>
  <text x="130" y="495" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">AST-01C</text>
  <text x="250" y="495" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Gulshan Living — Teak &amp; Cane Joinery</text>
  <text x="650" y="495" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">Craftsmanship close-up &amp; joinery grain</text>
  <text x="1050" y="495" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13">1024 × 1024 (1:1)</text>
  <text x="1250" y="495" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">AI Visualisation (Concept)</text>
  <text x="1600" y="495" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>

  <!-- Row 4 -->
  <line x1="110" y1="515" x2="2690" y2="515" stroke="#B8C2BA" stroke-width="1"/>
  <text x="130" y="545" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">AST-02</text>
  <text x="250" y="545" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Dhanmondi Kitchen — Heavy Cooking</text>
  <text x="650" y="545" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">Granite counter &amp; ventilated gas niche</text>
  <text x="1050" y="545" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13">1024 × 1024 (1:1)</text>
  <text x="1250" y="545" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">AI Visualisation (Concept)</text>
  <text x="1600" y="545" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>

  <!-- Row 5 -->
  <line x1="110" y1="565" x2="2690" y2="565" stroke="#B8C2BA" stroke-width="1"/>
  <text x="130" y="595" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">AST-03</text>
  <text x="250" y="595" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">Uttara Bedroom — Master Platform Suite</text>
  <text x="650" y="595" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">Platform bed &amp; slatted wardrobe</text>
  <text x="1050" y="595" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13">1024 × 1024 (1:1)</text>
  <text x="1250" y="595" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">AI Visualisation (Concept)</text>
  <text x="1600" y="595" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>

  <!-- ========================================================================= -->
  <!-- SECTION 2: MULTI-VIEW CONCEPT EXHIBITS & DOCUMENTED ASSUMPTIONS           -->
  <!-- ========================================================================= -->
  <!-- Exhibit 1: Gulshan Living (3 Views) -->
  <rect x="80" y="700" width="2640" height="960" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="700" width="2640" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="733" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">02. Spatial Study 01: Gulshan Lakeview Living — Multi-Angle Visual Coherence</text>

  <!-- View 1A Card -->
  <rect x="110" y="770" width="820" height="580" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <image href="{img_living_1}" x="110" y="770" width="820" height="420" preserveAspectRatio="xMidYMid slice"/>
  <rect x="125" y="785" width="460" height="30" fill="#183B35" opacity="0.9" rx="3"/>
  <text x="355" y="805" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="11" font-weight="700" text-anchor="middle">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>
  <text x="130" y="1225" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">View 1A: Primary Living Room Hero</text>
  {wrap_text("Wide living perspective showing floor-to-ceiling slatted room divider, concealed credenza, and lime-wash plaster wall finish.", 130, 1255, 68, 20, "'Manrope', sans-serif", 12, "#56645E")}
  <text x="130" y="1320" fill="#895239" font-family="'Manrope', sans-serif" font-size="11" font-weight="700">DOCUMENTED ASSUMPTION: 10ft ceiling height; assumes structural concrete beam cladding.</text>

  <!-- View 1B Card -->
  <rect x="970" y="770" width="820" height="580" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <image href="{img_living_2}" x="970" y="770" width="820" height="420" preserveAspectRatio="xMidYMid slice"/>
  <rect x="985" y="785" width="460" height="30" fill="#183B35" opacity="0.9" rx="3"/>
  <text x="1215" y="805" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="11" font-weight="700" text-anchor="middle">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>
  <text x="990" y="1225" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">View 1B: Dining Angle &amp; Veranda Daylight</text>
  {wrap_text("Demonstrates cross-ventilation corridor and natural daylight penetration from adjacent south-facing veranda.", 990, 1255, 68, 20, "'Manrope', sans-serif", 12, "#56645E")}
  <text x="990" y="1320" fill="#895239" font-family="'Manrope', sans-serif" font-size="11" font-weight="700">DOCUMENTED ASSUMPTION: Unobstructed daylight access; qualified design intent.</text>

  <!-- View 1C Card -->
  <rect x="1830" y="770" width="820" height="580" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <image href="{img_living_3}" x="1830" y="770" width="820" height="420" preserveAspectRatio="xMidYMid slice"/>
  <rect x="1845" y="785" width="460" height="30" fill="#183B35" opacity="0.9" rx="3"/>
  <text x="2075" y="805" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="11" font-weight="700" text-anchor="middle">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>
  <text x="1850" y="1225" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">View 1C: Burma Teak &amp; Rattan Cane Detail</text>
  {wrap_text("Close-up joinery detailing showing hand-stretched natural cane weave mounted in solid Burma teak mortise and tenon frame.", 1850, 1255, 68, 20, "'Manrope', sans-serif", 12, "#56645E")}
  <text x="1850" y="1320" fill="#895239" font-family="'Manrope', sans-serif" font-size="11" font-weight="700">CRAFT SPECIFICATION: Seasoned timber at 12% moisture content; local Mirpur joinery craft.</text>

  <!-- Synthesis Note -->
  <rect x="110" y="1380" width="2540" height="240" fill="#FFF8F4" stroke="#895239" stroke-width="1" rx="4"/>
  <text x="140" y="1415" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">ARCHITECTURAL FIDELITY &amp; GOVERNANCE STATEMENT:</text>
  {wrap_text("1. Truth in Advertising: All 3 angles depict an AI-generated architectural exploration study, not a constructed client commission. The disclaimer badge is rendered permanently across every client-facing presentation.", 140, 1445, 120, 22, "'Manrope', sans-serif", 13, "#56645E")}
  {wrap_text("2. Spatial Claims Scoured: Blanket unsupported claims (such as '80% open floor space' or 'guaranteed zero additional costs') have been removed entirely. All descriptions now express qualified design intent.", 140, 1485, 120, 22, "'Manrope', sans-serif", 13, "#56645E")}
  {wrap_text("3. Structural Feasibility: While geometry and material dimensions are realistic for Dhaka apartments, actual execution requires on-site structural engineer validation prior to construction.", 140, 1525, 120, 22, "'Manrope', sans-serif", 13, "#56645E")}

  <!-- ========================================================================= -->
  <!-- SECTION 3: KITCHEN & BEDROOM STUDIES (SIDE BY SIDE)                       -->
  <!-- ========================================================================= -->
  <rect x="80" y="1690" width="2640" height="660" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="1690" width="2640" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="1723" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">03. Studies 02 &amp; 03: Heavy Cooking Kitchen &amp; Master Platform Bedroom</text>

  <!-- Kitchen Study -->
  <rect x="110" y="1760" width="1240" height="550" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <image href="{img_kitchen}" x="110" y="1760" width="1240" height="360" preserveAspectRatio="xMidYMid slice"/>
  <rect x="125" y="1775" width="460" height="30" fill="#183B35" opacity="0.9" rx="3"/>
  <text x="355" y="1795" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="11" font-weight="700" text-anchor="middle">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>
  <text x="130" y="2155" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">Concept 02: Dhanmondi Heavy Cooking Utility Kitchen</text>
  {wrap_text("Resilient design tailored for heavy spice and oil cooking. Features honed black granite worktop, high-suction exhaust hood niche, and dedicated dual LPG cylinder compartment with floor-level ventilation louvers.", 130, 2185, 96, 22, "'Manrope', sans-serif", 13, "#56645E")}
  <text x="130" y="2275" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">SAFETY NOTICE: Dedicated LPG cabinet geometry is an architectural layout concept; requires certified gas line installation.</text>

  <!-- Bedroom Study -->
  <rect x="1410" y="1760" width="1240" height="550" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <image href="{img_bedroom}" x="1410" y="1760" width="1240" height="360" preserveAspectRatio="xMidYMid slice"/>
  <rect x="1425" y="1775" width="460" height="30" fill="#183B35" opacity="0.9" rx="3"/>
  <text x="1655" y="1795" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="11" font-weight="700" text-anchor="middle">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>
  <text x="1430" y="2155" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">Concept 03: Uttara Master Suite Platform Bed &amp; Slatted Wardrobe</text>
  {wrap_text("Calm sleeping environment integrating a low-platform oak bed, integrated warm LED cove illumination, dust-tight slatted wardrobe doors, and a compact study alcove.", 1430, 2185, 96, 22, "'Manrope', sans-serif", 13, "#56645E")}
  <text x="1430" y="2275" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">JOINERY SPECIFICATION: Soft-close Blum hardware with acoustic felt backing behind slatted panels.</text>

  <!-- ========================================================================= -->
  <!-- SECTION 4: PHYSICAL MATERIAL BOARD REGISTER                               -->
  <!-- ========================================================================= -->
  <rect x="80" y="2380" width="2640" height="460" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="2380" width="2640" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="2413" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">04. Physical Material Specimen Board &amp; Local Sourcing Directory</text>

  <!-- Material 1: Burma Teak -->
  <rect x="110" y="2460" width="490" height="340" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="130" y="2480" width="450" height="120" fill="#895239" rx="4"/>
  <text x="130" y="2630" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">Seasoned Burma Teak</text>
  <text x="130" y="2655" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">SOURCE: Chittagong Timber / Mirpur Drying</text>
  {wrap_text("Dense hardwood naturally resistant to termites and seasonal humidity warping. Sanded to 320 grit with matte polyurethane seal.", 130, 2680, 42, 20, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Material 2: Sylhet Cane -->
  <rect x="630" y="2460" width="490" height="340" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="650" y="2480" width="450" height="120" fill="#C5A059" rx="4"/>
  <text x="650" y="2630" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">Natural Handwoven Cane</text>
  <text x="650" y="2655" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">SOURCE: Sreemangal &amp; Sylhet Artisans</text>
  {wrap_text("Flexible, breathable rattan wicker woven in traditional hexagonal pattern. Allows continuous air circulation across cabinets.", 650, 2680, 42, 20, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Material 3: Lime Plaster -->
  <rect x="1150" y="2460" width="490" height="340" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="1170" y="2480" width="450" height="120" fill="#D6CFBE" rx="4"/>
  <text x="1170" y="2630" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">Breathable Lime Wash Plaster</text>
  <text x="1170" y="2655" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">SPECIFICATION: Slaked Lime + Fine Sand</text>
  {wrap_text("Vapor-permeable mineral finish that prevents tropical mold growth behind wall-mounted joinery. Subtle natural depth under sunlight.", 1170, 2680, 42, 20, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Material 4: Honed Granite -->
  <rect x="1670" y="2460" width="490" height="340" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="1690" y="2480" width="450" height="120" fill="#2E3331" rx="4"/>
  <text x="1690" y="2630" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">Honed Black Granite</text>
  <text x="1690" y="2655" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">SOURCE: Local Stone Yard / Imported Slab</text>
  {wrap_text("Stain and heat resilient surface capable of handling turmeric, mustard oil, and boiling cookware without etching.", 1690, 2680, 42, 20, "'Manrope', sans-serif", 12, "#56645E")}

  <!-- Material 5: Forest Pine Accent -->
  <rect x="2190" y="2460" width="490" height="340" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="2210" y="2480" width="450" height="120" fill="#183B35" rx="4"/>
  <text x="2210" y="2630" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">Deep Pine Satin Lacquer</text>
  <text x="2210" y="2655" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">FINISH CODE: #183B35 (20% Satin Sheen)</text>
  {wrap_text("Studio signature green applied to metal accents, structural joinery framing, and brand focal points. Grounding and tranquil.", 2210, 2680, 42, 20, "'Manrope', sans-serif", 12, "#56645E")}
</svg>"""

with open('figma_svgs_v2/07_project_and_concept_assets.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("Saved figma_svgs_v2/07_project_and_concept_assets.svg")
