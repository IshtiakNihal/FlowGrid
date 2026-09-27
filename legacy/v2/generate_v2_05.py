"""
FlowGrid - Page 05 (English Suite) Generator v2
Comprehensive English responsive coverage:
1. Desktop Homepage (1440x3800px)
2. Desktop Case Study Detail with 3 views (1440x3400px)
3. Mobile Full Homepage (390x3600px - Complete depth, zero blank space)
4. Mobile Case Study Detail (390x2800px)
Scrubbed customer copy: Zero internal prompt jargon, natural architectural language, bounded typography.
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

svg = f"""<svg width="4200" height="4600" viewBox="0 0 4200 4600" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="4200" height="4600" fill="#EAE6DC"/>

  <!-- Top Banner -->
  <rect x="80" y="80" width="4040" height="120" fill="#183B35" rx="4"/>
  <text x="120" y="145" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="34" font-weight="600">FlowGrid — English Responsive Suite (Desktop 1440px &amp; Mobile 390px)</text>
  <text x="120" y="180" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="16">Full matching English experience: Desktop Home, Desktop Case Study (3 Views), Full Mobile Home, and Mobile Case Study</text>

  <!-- ========================================================================= -->
  <!-- SCREEN 1: DESKTOP HOME (X: 80, Y: 240, W: 1440, H: 3800)                  -->
  <!-- ========================================================================= -->
  <g id="screen-desktop-en-home">
    <rect x="80" y="240" width="1440" height="3800" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    
    <!-- Header -->
    <rect x="80" y="240" width="1440" height="80" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <text x="140" y="288" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">FLOWGRID</text>
    <text x="420" y="286" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Home</text>
    <text x="510" y="286" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Projects</text>
    <text x="610" y="286" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Services</text>
    <text x="710" y="286" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Process</text>
    <text x="800" y="286" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Studio</text>
    <text x="880" y="286" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Contact</text>

    <!-- Switcher (EN Active) -->
    <rect x="1170" y="260" width="90" height="38" fill="#DEE7E2" rx="19"/>
    <rect x="1214" y="262" width="44" height="34" fill="#183B35" rx="17"/>
    <text x="1192" y="284" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600" text-anchor="middle">বাং</text>
    <text x="1236" y="284" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" text-anchor="middle">EN</text>

    <!-- CTA -->
    <rect x="1280" y="258" width="180" height="42" fill="#183B35" rx="4"/>
    <text x="1370" y="285" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14" font-weight="600" text-anchor="middle">Consultation</text>

    <!-- Hero -->
    <text x="140" y="400" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" letter-spacing="2">URBAN RESIDENTIAL ARCHITECTURE · DHAKA</text>
    <text x="140" y="460" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="52" font-weight="600">Quiet, Intentional</text>
    <text x="140" y="525" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="52" font-weight="600">Urban Living.</text>
    
    {wrap_text("Bespoke spatial planning and enduring timber joinery crafted for Dhaka apartments. We design calm, functional homes grounded in natural light, cross-ventilation, and everyday family life.", 140, 570, 48, 26, "'Manrope', sans-serif", 16, "#56645E")}
    
    <rect x="140" y="660" width="220" height="48" fill="#183B35" rx="4"/>
    <text x="250" y="690" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="15" font-weight="600" text-anchor="middle">Start a Consultation</text>
    
    <rect x="380" y="660" width="180" height="48" fill="none" stroke="#183B35" stroke-width="1.5" rx="4"/>
    <text x="470" y="690" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600" text-anchor="middle">View Projects →</text>

    <!-- Hero Image Card -->
    <rect x="680" y="380" width="780" height="460" fill="#DEE7E2" rx="4"/>
    <image href="{img_living_1}" x="680" y="380" width="780" height="460" preserveAspectRatio="xMidYMid slice"/>
    <rect x="700" y="400" width="460" height="34" fill="#183B35" opacity="0.9" rx="4"/>
    <circle cx="718" cy="417" r="5" fill="#DEE7E2"/>
    <text x="732" y="422" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">Concept design · AI visualisation · Not a completed project</text>

    <!-- Section: Philosophy & Approach (Strictly Bounded, Zero Overflow) -->
    <rect x="80" y="900" width="1440" height="440" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1"/>
    <text x="140" y="960" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" letter-spacing="2">OUR APPROACH</text>
    <text x="140" y="1005" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="32" font-weight="600">Thoughtful Restraint in High-Density Living</text>
    
    <!-- 3 Bounded Philosophy Cards -->
    <rect x="140" y="1040" width="380" height="240" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="170" y="1080" fill="#895239" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">01</text>
    <text x="170" y="1115" fill="#183B35" font-family="'Manrope', sans-serif" font-size="17" font-weight="700">Daylight &amp; Ventilation</text>
    {wrap_text("In dense urban towers, every window orientation is precious. We configure open living-dining layouts to preserve natural daylight corridors and cross-ventilation.", 170, 1145, 34, 22, "'Manrope', sans-serif", 13, "#56645E")}

    <rect x="560" y="1040" width="380" height="240" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="590" y="1080" fill="#895239" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">02</text>
    <text x="590" y="1115" fill="#183B35" font-family="'Manrope', sans-serif" font-size="17" font-weight="700">Concealed Storage</text>
    {wrap_text("Urban living demands rigorous storage discipline. We design full-height architectural cabinetry that keeps seasonal dust out and family clutter unseen.", 590, 1145, 34, 22, "'Manrope', sans-serif", 13, "#56645E")}

    <rect x="980" y="1040" width="380" height="240" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="1010" y="1080" fill="#895239" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">03</text>
    <text x="1010" y="1115" fill="#183B35" font-family="'Manrope', sans-serif" font-size="17" font-weight="700">Honest Local Materials</text>
    {wrap_text("We prioritize kiln-seasoned Burma teak, handcrafted natural cane, and breathable matte lime finishes that age gracefully in our subtropical humidity.", 1010, 1145, 34, 22, "'Manrope', sans-serif", 13, "#56645E")}

    <!-- Section: Selected Projects Grid -->
    <text x="140" y="1410" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" letter-spacing="2">FEATURED STUDIES</text>
    <text x="140" y="1455" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="32" font-weight="600">Selected Spatial Studies &amp; Concepts</text>

    <!-- Card 1: Gulshan Living -->
    <rect x="140" y="1490" width="580" height="540" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <image href="{img_living_1}" x="140" y="1490" width="580" height="340" preserveAspectRatio="xMidYMid slice"/>
    <rect x="155" y="1505" width="440" height="30" fill="#183B35" opacity="0.9" rx="4"/>
    <text x="170" y="1525" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="11" font-weight="700">Concept design · AI visualisation · Not a completed project</text>
    <text x="170" y="1865" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">Gulshan Lakeview Residence</text>
    <text x="170" y="1895" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">GULSHAN 2, DHAKA · 2,150 SFT · LIVING &amp; JOINERY</text>
    {wrap_text("Open-plan family living with natural daylight optimization and bespoke cane divider partition.", 170, 1925, 48, 20, "'Manrope', sans-serif", 13, "#56645E")}
    <text x="170" y="1995" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Explore Case Study →</text>

    <!-- Card 2: Kitchen -->
    <rect x="760" y="1490" width="580" height="540" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <image href="{img_kitchen}" x="760" y="1490" width="580" height="340" preserveAspectRatio="xMidYMid slice"/>
    <rect x="775" y="1505" width="440" height="30" fill="#183B35" opacity="0.9" rx="4"/>
    <text x="790" y="1525" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="11" font-weight="700">Concept design · AI visualisation · Not a completed project</text>
    <text x="790" y="1865" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">Dhanmondi Residence Kitchen</text>
    <text x="790" y="1895" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">DHANMONDI, DHAKA · 1,850 SFT · UTILITY KITCHEN</text>
    {wrap_text("Heavy cooking resilience with honed black granite and dedicated ventilated LP gas cabinet.", 790, 1925, 48, 20, "'Manrope', sans-serif", 13, "#56645E")}
    <text x="790" y="1995" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Explore Case Study →</text>

    <!-- Section: Services -->
    <rect x="80" y="2090" width="1440" height="420" fill="#183B35"/>
    <text x="140" y="2150" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" letter-spacing="2">WHAT WE DELIVER</text>
    <text x="140" y="2195" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="32" font-weight="600">Architectural &amp; Interior Services</text>

    <line x1="140" y1="2230" x2="1340" y2="2230" stroke="#2E5D4B" stroke-width="1"/>
    <text x="140" y="2275" fill="#DEE7E2" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">01</text>
    <text x="200" y="2275" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">Full Apartment Spatial Planning</text>
    {wrap_text("Functional zoning, furniture layout, and circulation analysis tailored to your family's routine.", 500, 2265, 45, 20, "'Manrope', sans-serif", 13, "#DEE7E2")}
    <text x="1220" y="2275" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14">Details →</text>

    <line x1="140" y1="2315" x2="1340" y2="2315" stroke="#2E5D4B" stroke-width="1"/>
    <text x="140" y="2355" fill="#DEE7E2" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">02</text>
    <text x="200" y="2355" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">Bespoke Architectural Joinery</text>
    {wrap_text("Custom media units, slatted screens, wardrobes, and precision shop drawings for local joiners.", 500, 2345, 45, 20, "'Manrope', sans-serif", 13, "#DEE7E2")}
    <text x="1220" y="2355" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14">Details →</text>

    <line x1="140" y1="2395" x2="1340" y2="2395" stroke="#2E5D4B" stroke-width="1"/>
    <text x="140" y="2435" fill="#DEE7E2" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">03</text>
    <text x="200" y="2435" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">Kitchen &amp; Utility Architecture</text>
    {wrap_text("High-performance kitchen layouts accommodating local heavy cooking and dual LPG cylinders.", 500, 2425, 45, 20, "'Manrope', sans-serif", 13, "#DEE7E2")}
    <text x="1220" y="2435" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14">Details →</text>

    <!-- Studio & Mirpur Location -->
    <rect x="80" y="2570" width="1440" height="380" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1"/>
    <text x="140" y="2630" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" letter-spacing="2">STUDIO LOCATION &amp; ETHOS</text>
    <text x="140" y="2675" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="32" font-weight="600">Rooted in Mirpur, Built for Dhaka Homes</text>
    {wrap_text("Based in Mirpur 12, Dhaka, FlowGrid is an independent interior architecture practice. We are not a volume contractor or retail reseller; we work directly with urban families to create enduring, personalized environments.", 140, 2720, 60, 24, "'Manrope', sans-serif", 14, "#56645E")}
    {wrap_text("Our studio values domestic warmth and craftsmanship. While our founder's family also produces lifestyle and culinary content on YouTube ('Rumi's Fashionable House'), FlowGrid operates as an independent design practice focused strictly on spatial quality and construction integrity.", 140, 2790, 60, 24, "'Manrope', sans-serif", 14, "#56645E")}

    <!-- Footer -->
    <rect x="80" y="3000" width="1440" height="420" fill="#112A25"/>
    <text x="140" y="3060" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">FLOWGRID</text>
    {wrap_text("Residential interior architecture and bespoke joinery for urban Dhaka apartments. Mirpur 12, Dhaka 1216.", 140, 3095, 34, 20, "'Manrope', sans-serif", 12, "#DEE7E2")}
    
    <text x="500" y="3060" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Services &amp; Scope</text>
    <text x="500" y="3095" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="13">Living &amp; Dining Architecture</text>
    <text x="500" y="3125" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="13">Master Suite Joinery</text>
    <text x="500" y="3155" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="13">High-Performance Kitchens</text>
    <text x="500" y="3185" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="13">Site Supervision &amp; Delivery</text>

    <text x="800" y="3060" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Affiliated Entities</text>
    <text x="800" y="3095" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="13">Onekta Product (Kitchen Appliances) ↗</text>
    <text x="800" y="3125" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="13">Rumi's Fashionable House (YouTube Vlog) ↗</text>
    <text x="800" y="3155" fill="#8E9E96" font-family="'Manrope', sans-serif" font-size="11">External non-studio destinations</text>

    <text x="1100" y="3060" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">Contact</text>
    <text x="1100" y="3095" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="13">Mirpur 12, Dhaka 1216</text>
    <text x="1100" y="3125" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="13">+880 1711-000000</text>
    <text x="1100" y="3155" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="13">studio@flowgridbd.com</text>

    <line x1="140" y1="3240" x2="1380" y2="3240" stroke="#2E5D4B" stroke-width="1"/>
    <text x="140" y="3280" fill="#8E9E96" font-family="'Manrope', sans-serif" font-size="12">© 2026 FlowGrid Studio. All rights reserved. Interior Architecture &amp; Joinery.</text>
    <text x="1100" y="3280" fill="#8E9E96" font-family="'Manrope', sans-serif" font-size="12">Privacy Policy · Terms of Service</text>
  </g>

  <!-- ========================================================================= -->
  <!-- SCREEN 2: DESKTOP CASE STUDY DETAIL (ENGLISH) (X: 1620, Y: 240, W: 1440)  -->
  <!-- ========================================================================= -->
  <g id="screen-desktop-en-case-study">
    <rect x="1620" y="240" width="1440" height="3400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    
    <!-- Header -->
    <rect x="1620" y="240" width="1440" height="80" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <text x="1680" y="288" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">FLOWGRID</text>
    <text x="1960" y="286" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Home</text>
    <text x="2050" y="286" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Projects</text>
    <text x="2150" y="286" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Services</text>
    <text x="2250" y="286" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Process</text>
    <text x="2340" y="286" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Studio</text>
    <text x="2420" y="286" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">Contact</text>
    <rect x="2820" y="258" width="180" height="42" fill="#183B35" rx="4"/>
    <text x="2910" y="285" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14" font-weight="600" text-anchor="middle">Consultation</text>

    <!-- Breadcrumb -->
    <text x="1680" y="360" fill="#895239" font-family="'Manrope', sans-serif" font-size="13">← Back to Projects Archive</text>

    <text x="1680" y="420" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="44" font-weight="600">Gulshan Lakeview Residence</text>
    <text x="1680" y="465" fill="#56645E" font-family="'Manrope', sans-serif" font-size="18">Open Living, Natural Illumination &amp; Handcrafted Cane Partition</text>

    <!-- Truth Banner -->
    <rect x="1680" y="495" width="1320" height="44" fill="#F4F1E8" stroke="#895239" stroke-width="1.5" rx="4"/>
    <circle cx="1705" cy="517" r="6" fill="#895239"/>
    <text x="1725" y="522" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">Concept design · AI visualisation · Not a completed project — Future spatial exploration study.</text>

    <!-- Meta Table -->
    <rect x="1680" y="560" width="1320" height="90" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="1710" y="595" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">LOCATION</text>
    <text x="1710" y="625" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Gulshan 2, Dhaka</text>

    <text x="2010" y="595" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">FLOOR AREA</text>
    <text x="2010" y="625" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">2,150 SFT</text>

    <text x="2310" y="595" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">MATERIALS</text>
    <text x="2310" y="625" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Burma Teak, Sylhet Cane, Lime Wash</text>

    <text x="2680" y="595" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">STUDY TYPE</text>
    <text x="2680" y="625" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">Living &amp; Dining Joinery Study</text>

    <!-- View 1: Hero Wide -->
    <rect x="1680" y="680" width="1320" height="720" fill="#DEE7E2" rx="4"/>
    <image href="{img_living_1}" x="1680" y="680" width="1320" height="720" preserveAspectRatio="xMidYMid slice"/>
    <text x="1680" y="1425" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">View 01: Wide living perspective showing floor-to-ceiling slatted room divider and integrated storage credenza.</text>

    <!-- Narrative -->
    <rect x="1680" y="1460" width="1320" height="380" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="1720" y="1510" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">Client Brief &amp; Spatial Architecture</text>
    
    <text x="1720" y="1560" fill="#895239" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">1. Family Brief &amp; Rituals:</text>
    {wrap_text("The four-member household required an expansive open living-dining feeling without sacrificing acoustic privacy or entrance shielding during social gatherings. The family also requested dust-protected shelving for literature and collected objects.", 1720, 1590, 80, 24, "'Manrope', sans-serif", 14, "#56645E")}

    <text x="1720" y="1670" fill="#895239" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">2. Architectural Strategy:</text>
    {wrap_text("Rather than lowering the entire ceiling with plasterboard to hide concrete structural beams, we celebrated the ceiling height and wrapped the beam in slatted teak cladding. To channel natural veranda daylight deep into the dining corridor, we integrated a breathable handcrafted cane screen.", 1720, 1700, 80, 24, "'Manrope', sans-serif", 14, "#56645E")}

    <!-- Multi-View: View 2 & 3 -->
    <text x="1680" y="1890" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">Multi-Angle Visual Study &amp; Joinery Detail</text>

    <!-- View 2: Dining Angle -->
    <rect x="1680" y="1930" width="640" height="440" fill="#DEE7E2" rx="4"/>
    <image href="{img_living_2}" x="1680" y="1930" width="640" height="440" preserveAspectRatio="xMidYMid slice"/>
    <text x="1680" y="2395" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">View 02: Dining Corner &amp; Veranda Daylight Angle</text>
    {wrap_text("Gentle daylight washes across the dining table from the adjacent veranda, highlighting the organic grain of seasoned timber.", 1680, 2420, 52, 20, "'Manrope', sans-serif", 12, "#56645E")}

    <!-- View 3: Joinery Detail -->
    <rect x="2360" y="1930" width="640" height="440" fill="#DEE7E2" rx="4"/>
    <image href="{img_living_3}" x="2360" y="1930" width="640" height="440" preserveAspectRatio="xMidYMid slice"/>
    <text x="2360" y="2395" fill="#183B35" font-family="'Manrope', sans-serif" font-size="14" font-weight="700">View 03: Burma Teak &amp; Sylhet Cane Craftsmanship</text>
    {wrap_text("Hand-stretched rattan cane weave framed within solid Burma teak joinery, executed by seasoned Mirpur woodworkers.", 2360, 2420, 52, 20, "'Manrope', sans-serif", 12, "#56645E")}

    <!-- CTA -->
    <rect x="1680" y="2500" width="1320" height="130" fill="#183B35" rx="4"/>
    <text x="1720" y="2555" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="24" font-weight="600">Envisioning a similar calm for your home?</text>
    <text x="1720" y="2590" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="14">Schedule an initial space planning consultation with our lead architectural designer.</text>
    <rect x="2680" y="2540" width="280" height="46" fill="#895239" rx="4"/>
    <text x="2820" y="2568" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="14" font-weight="600" text-anchor="middle">Book a Consultation</text>
  </g>

  <!-- ========================================================================= -->
  <!-- SCREEN 3: MOBILE ENGLISH HOMEPAGE (FULL DEPTH) (X: 3160, Y: 240, W: 390)   -->
  <!-- ========================================================================= -->
  <g id="screen-mobile-en-home">
    <rect x="3160" y="240" width="390" height="3800" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    
    <!-- Mobile Header -->
    <rect x="3160" y="240" width="390" height="64" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <text x="3180" y="280" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">FLOWGRID</text>
    
    <!-- Switcher (EN active) -->
    <rect x="3380" y="254" width="70" height="34" fill="#DEE7E2" rx="17"/>
    <rect x="3416" y="256" width="34" height="30" fill="#183B35" rx="15"/>
    <text x="3398" y="276" fill="#183B35" font-family="'Manrope', sans-serif" font-size="11" font-weight="600" text-anchor="middle">বাং</text>
    <text x="3433" y="276" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="11" font-weight="700" text-anchor="middle">EN</text>
    
    <rect x="3470" y="254" width="60" height="34" fill="#183B35" rx="4"/>
    <text x="3500" y="276" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" text-anchor="middle">MENU ☰</text>

    <!-- Mobile Hero -->
    <text x="3180" y="340" fill="#895239" font-family="'Manrope', sans-serif" font-size="11" font-weight="700" letter-spacing="1.5">URBAN RESIDENTIAL · DHAKA</text>
    <text x="3180" y="380" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="32" font-weight="600">Quiet, Intentional</text>
    <text x="3180" y="420" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="32" font-weight="600">Urban Living.</text>
    
    {wrap_text("Residential interiors shaped for Dhaka's climate and everyday family rituals through daylight, ventilation, and custom timber joinery.", 3180, 455, 34, 22, "'Manrope', sans-serif", 14, "#56645E")}

    <!-- Hero Image Card -->
    <rect x="3180" y="520" width="350" height="230" fill="#DEE7E2" rx="4"/>
    <image href="{img_living_1}" x="3180" y="520" width="350" height="230" preserveAspectRatio="xMidYMid slice"/>
    <rect x="3190" y="530" width="330" height="28" fill="#183B35" opacity="0.9" rx="3"/>
    <text x="3355" y="548" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="9" font-weight="700" text-anchor="middle">Concept design · AI visualisation · Not completed work</text>

    <!-- CTAs -->
    <rect x="3180" y="770" width="350" height="48" fill="#183B35" rx="4"/>
    <text x="3355" y="800" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="15" font-weight="600" text-anchor="middle">Start a Consultation</text>
    
    <rect x="3180" y="830" width="350" height="48" fill="none" stroke="#183B35" stroke-width="1.5" rx="4"/>
    <text x="3355" y="860" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600" text-anchor="middle">Explore Projects →</text>

    <!-- Mobile Approach Stack -->
    <rect x="3160" y="910" width="390" height="520" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1"/>
    <text x="3180" y="945" fill="#895239" font-family="'Manrope', sans-serif" font-size="11" font-weight="700" letter-spacing="1.5">OUR PHILOSOPHY</text>
    <text x="3180" y="975" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="600">Living Restraint in Dhaka</text>

    <rect x="3180" y="1005" width="350" height="120" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="3200" y="1035" fill="#895239" font-family="'Bodoni Moda', serif" font-size="16" font-weight="700">01 · Daylight &amp; Airflow</text>
    {wrap_text("Maximizing cross-ventilation corridors across dense Dhaka apartment towers.", 3200, 1060, 34, 20, "'Manrope', sans-serif", 12, "#56645E")}

    <rect x="3180" y="1140" width="350" height="120" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="3200" y="1170" fill="#895239" font-family="'Bodoni Moda', serif" font-size="16" font-weight="700">02 · Full-Height Storage</text>
    {wrap_text("Concealing everyday dust and storage items within seamless architectural joinery.", 3200, 1195, 34, 20, "'Manrope', sans-serif", 12, "#56645E")}

    <rect x="3180" y="1275" width="350" height="120" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="3200" y="1305" fill="#895239" font-family="'Bodoni Moda', serif" font-size="16" font-weight="700">03 · Sourced Timber &amp; Cane</text>
    {wrap_text("Burma teak and Sylhet rattan handcrafted locally to age gracefully in humidity.", 3200, 1330, 34, 20, "'Manrope', sans-serif", 12, "#56645E")}

    <!-- Projects Section -->
    <text x="3180" y="1470" fill="#895239" font-family="'Manrope', sans-serif" font-size="11" font-weight="700" letter-spacing="1.5">FEATURED STUDIES</text>
    <text x="3180" y="1505" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24" font-weight="600">Selected Concepts</text>

    <!-- Mobile Card 1: Gulshan -->
    <rect x="3180" y="1530" width="350" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <image href="{img_living_1}" x="3180" y="1530" width="350" height="220" preserveAspectRatio="xMidYMid slice"/>
    <rect x="3190" y="1540" width="330" height="26" fill="#183B35" opacity="0.9" rx="3"/>
    <text x="3355" y="1557" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="9" font-weight="700" text-anchor="middle">Concept design · AI visualisation · Not completed work</text>
    <text x="3200" y="1780" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">Gulshan Lakeview Residence</text>
    <text x="3200" y="1805" fill="#895239" font-family="'Manrope', sans-serif" font-size="11" font-weight="600">GULSHAN 2 · 2,150 SFT · LIVING &amp; JOINERY</text>
    {wrap_text("Open-plan daylighting and handcrafted rattan cane divider screen.", 3200, 1830, 34, 20, "'Manrope', sans-serif", 12, "#56645E")}
    <text x="3200" y="1915" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">View Case Study →</text>

    <!-- Mobile Card 2: Kitchen -->
    <rect x="3180" y="1970" width="350" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <image href="{img_kitchen}" x="3180" y="1970" width="350" height="220" preserveAspectRatio="xMidYMid slice"/>
    <rect x="3190" y="1980" width="330" height="26" fill="#183B35" opacity="0.9" rx="3"/>
    <text x="3355" y="1997" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="9" font-weight="700" text-anchor="middle">Concept design · AI visualisation · Not completed work</text>
    <text x="3200" y="2220" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">Dhanmondi Utility Kitchen</text>
    <text x="3200" y="2245" fill="#895239" font-family="'Manrope', sans-serif" font-size="11" font-weight="600">DHANMONDI · 1,850 SFT · UTILITY KITCHEN</text>
    {wrap_text("Heavy cooking resilience with honed black granite and dedicated LPG cabinet.", 3200, 2270, 34, 20, "'Manrope', sans-serif", 12, "#56645E")}
    <text x="3200" y="2355" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">View Case Study →</text>

    <!-- Mobile Services -->
    <rect x="3160" y="2420" width="390" height="440" fill="#183B35"/>
    <text x="3180" y="2460" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="11" font-weight="700" letter-spacing="1.5">WHAT WE DELIVER</text>
    <text x="3180" y="2495" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="22" font-weight="600">Architectural Services</text>

    <line x1="3180" y1="2525" x2="3530" y2="2525" stroke="#2E5D4B" stroke-width="1"/>
    <text x="3180" y="2555" fill="#DEE7E2" font-family="'Bodoni Moda', serif" font-size="15" font-weight="700">01</text>
    <text x="3210" y="2555" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Apartment Spatial Planning</text>
    {wrap_text("Circulation analysis and daylight drafts.", 3210, 2580, 32, 18, "'Manrope', sans-serif", 12, "#DEE7E2")}

    <line x1="3180" y1="2625" x2="3530" y2="2625" stroke="#2E5D4B" stroke-width="1"/>
    <text x="3180" y="2655" fill="#DEE7E2" font-family="'Bodoni Moda', serif" font-size="15" font-weight="700">02</text>
    <text x="3210" y="2655" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Bespoke Architectural Joinery</text>
    {wrap_text("Custom media walls and screen dividers.", 3210, 2680, 32, 18, "'Manrope', sans-serif", 12, "#DEE7E2")}

    <line x1="3180" y1="2725" x2="3530" y2="2725" stroke="#2E5D4B" stroke-width="1"/>
    <text x="3180" y="2755" fill="#DEE7E2" font-family="'Bodoni Moda', serif" font-size="15" font-weight="700">03</text>
    <text x="3210" y="2755" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="15" font-weight="700">Kitchen &amp; Utility Architecture</text>
    {wrap_text("Resilient countertops and dual gas niche.", 3210, 2780, 32, 18, "'Manrope', sans-serif", 12, "#DEE7E2")}

    <!-- Mobile Footer -->
    <rect x="3160" y="3320" width="390" height="480" fill="#112A25"/>
    <text x="3180" y="3370" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">FLOWGRID</text>
    {wrap_text("Residential interior architecture and bespoke joinery for Dhaka homes. Mirpur 12, Dhaka 1216.", 3180, 3400, 32, 20, "'Manrope', sans-serif", 12, "#DEE7E2")}
    
    <text x="3180" y="3470" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="13" font-weight="700">Affiliated Entities</text>
    <text x="3180" y="3500" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="12">Onekta Product (Appliances) ↗</text>
    <text x="3180" y="3525" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="12">Rumi's Fashionable House (Vlog) ↗</text>

    <text x="3180" y="3575" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="12">📞 +880 1711-000000</text>
    <text x="3180" y="3600" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="12">✉ studio@flowgridbd.com</text>

    <line x1="3180" y1="3635" x2="3530" y2="3635" stroke="#2E5D4B" stroke-width="1"/>
    <text x="3180" y="3665" fill="#8E9E96" font-family="'Manrope', sans-serif" font-size="11">© 2026 FlowGrid. All rights reserved.</text>
    <text x="3180" y="3690" fill="#8E9E96" font-family="'Manrope', sans-serif" font-size="11">Privacy Policy · Terms</text>
  </g>

</svg>"""

with open('figma_svgs_v2/05_english.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("Saved figma_svgs_v2/05_english.svg")
