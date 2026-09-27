"""
FlowGrid - Page 05: English Suite Generator (v3.2 Complete & Reconciled)
Delivers comprehensive English templates matching the Bangla architectural suite:
- English Desktop Suite (1440px):
  1. Homepage (1440 x 2500)
  2. Projects Archive (1440 x 2200)
  3. Concept Study Detail - 3 Views (1440 x 2200)
  4. Real-Project Framework Template (1440 x 2200)
  5. Dedicated Services (1440 x 2200)
  6. Service Detail - Bespoke Joinery (1440 x 2200)
  7. Dedicated Process (1440 x 1950)
  8. Dedicated Studio & Ethos (1440 x 1950)
  9. Dedicated Contact (1440 x 1950)
  10. Legal & Privacy Terms (1440 x 1500)
  11. 404 Error Screen (1440 x 900)
- English Mobile Suite (390px):
  12. Mobile Homepage (390 x 3350)
  13. Mobile Projects Archive (390 x 1600)
  14. Mobile Concept Detail - 3 Views (390 x 2000)
  15. Mobile Real-Project Framework Template (390 x 1400)
  16. Mobile Dedicated Services (390 x 1400)
  17. Mobile Dedicated Joinery Detail (390 x 1400)
  18. Mobile Dedicated Process (390 x 1400)
  19. Mobile Dedicated Studio & Ethos (390 x 1400)
  20. Mobile Legal & Privacy Terms (390 x 1400)
  21. Mobile Dedicated Contact (390 x 1450)
  22. Mobile 404 Error Screen (390 x 650)
  23. Mobile Off-Canvas Drawer Overlay (390 x 750)

Total Layouts on Board 05: 11 Desktop + 11 Mobile + 1 Drawer Overlay.
Across the Entire FlowGrid Suite: Exactly 44 Page Layouts + 2 Drawer Overlays!
"""
import os
from svg_utils import wrap_text, escape_xml, validate_svg_file, get_base64_image

def generate_board_05():
    img_living = get_base64_image('concepts/concept_01_living_dhaka.jpg')
    img_living_alt = get_base64_image('concepts/concept_01_living_alt.jpg')
    img_joinery = get_base64_image('concepts/concept_01_joinery_detail.jpg')
    img_kitchen = get_base64_image('concepts/concept_02_kitchen_dhaka.jpg')
    img_bedroom = get_base64_image('concepts/concept_03_bedroom_dhaka.jpg')

    # Canvas: accommodates 4 Desktop columns (1440px) + 5 Mobile columns (390px)
    w, h = 7000, 7400
    svg = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{w}" height="{h}" fill="#F4F1E8"/>')

    # Header Banner
    svg.append(f'<rect x="80" y="80" width="{w-160}" height="140" fill="#183B35" rx="4"/>')
    svg.append('<text x="120" y="145" fill="#F4F1E8" font-family="\'Bodoni Moda\', serif" font-size="36" font-weight="600">FlowGrid — English Experience Suite · Desktop (1440px) &amp; Mobile (390px) · v3.2</text>')
    svg.append('<text x="120" y="185" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="18">Complete 11 Desktop &amp; 11 Mobile English architectural templates + dedicated drawer overlay with 48px touch targets and verified image embeds</text>')

    # Helper: English Desktop Header (88px) with 48px button target
    def render_en_header(x, y, active=""):
        res = []
        res.append(f'<rect x="{x}" y="{y}" width="1440" height="88" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
        res.append(f'<text x="{x+80}" y="{y+55}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="28" font-weight="700">FlowGrid</text>')
        res.append(f'<text x="{x+210}" y="{y+55}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="12" font-weight="700">STUDIO</text>')

        menu_items = [
            ("Home", x+420, "home"),
            ("Projects", x+510, "projects"),
            ("Services", x+620, "services"),
            ("Process", x+730, "process"),
            ("Studio", x+830, "studio"),
            ("Contact", x+930, "contact")
        ]
        for label, mx, pid in menu_items:
            color = "#183B35" if pid != active else "#895239"
            weight = "600" if pid != active else "700"
            res.append(f'<text x="{mx}" y="{y+54}" fill="{color}" font-family="\'Manrope\', sans-serif" font-size="15" font-weight="{weight}">{escape_xml(label)}</text>')
            if pid == active:
                res.append(f'<line x1="{mx}" y1="{y+62}" x2="{mx+len(label)*10}" y2="{y+62}" stroke="#895239" stroke-width="2"/>')

        res.append(f'<rect x="{x+1180}" y="{y+24}" width="50" height="40" fill="#DEE7E2" rx="2"/>')
        res.append(f'<text x="{x+1205}" y="{y+49}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="700" text-anchor="middle">বাং</text>')
        # 48px height CTA button
        res.append(f'<rect x="{x+1245}" y="{y+20}" width="145" height="48" fill="#183B35" rx="2"/>')
        res.append(f'<text x="{x+1317}" y="{y+50}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Book Consultation</text>')
        return res

    # Helper: English Desktop Footer (280px)
    def render_en_footer(x, y):
        res = []
        res.append(f'<rect x="{x}" y="{y}" width="1440" height="280" fill="#183B35"/>')
        res.append(f'<text x="{x+80}" y="{y+70}" fill="#F4F1E8" font-family="\'Bodoni Moda\', serif" font-size="32" font-weight="700">FlowGrid Studio</text>')
        t_ef, _ = wrap_text("Quiet, resilient interior architecture and bespoke joinery tailored for urban Dhaka apartments.", x+80, y+105, 45, 22, "'Manrope', sans-serif", 14, "#DEE7E2")
        res.append(t_ef)

        res.append(f'<text x="{x+540}" y="{y+70}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">NAVIGATION</text>')
        for idx, l in enumerate(["Home", "Projects Archive", "Services", "Process", "Studio & Team"]):
            res.append(f'<text x="{x+540}" y="{y+100+idx*24}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="13">{escape_xml(l)}</text>')

        res.append(f'<text x="{x+820}" y="{y+70}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">STUDIO CONTACT</text>')
        res.append(f'<text x="{x+820}" y="{y+100}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="13">Mirpur-10, Dhaka 1216, Bangladesh</text>')
        res.append(f'<text x="{x+820}" y="{y+124}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="13">Hotline: +880 1700-000000</text>')
        res.append(f'<text x="{x+820}" y="{y+148}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="13">Email: hello@flowgrid-interiors.com</text>')
        res.append(f'<text x="{x+820}" y="{y+172}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="12">Privacy Policy &amp; Terms of Service</text>')

        res.append(f'<text x="{x+1120}" y="{y+70}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">COMMUNITY SIBLINGS</text>')
        res.append(f'<text x="{x+1120}" y="{y+100}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="13">Rumi\'s Fashionable House (Vlogs)</text>')
        res.append(f'<text x="{x+1120}" y="{y+124}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="13">Onekta Product (Home Appliances)</text>')
        res.append(f'<text x="{x+1120}" y="{y+160}" fill="#C4D1CA" font-family="\'Manrope\', sans-serif" font-size="11">Distinct Architectural Practice &amp; Governance</text>')

        res.append(f'<line x1="{x+80}" y1="{y+220}" x2="{x+1360}" y2="{y+220}" stroke="#2D524A" stroke-width="1"/>')
        res.append(f'<text x="{x+80}" y="{y+250}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="12">© 2026 FlowGrid Interior Studio. All rights reserved. Dhaka, Bangladesh.</text>')
        res.append(f'<text x="{x+1360}" y="{y+250}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="12" text-anchor="end">Adheres to truth-in-advertising visualization standards</text>')
        return res

    # Helper: English Mobile Header (64px) with 48x48 touch targets
    def render_en_mobile_header(x, y):
        res = []
        res.append(f'<rect x="{x}" y="{y}" width="390" height="64" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
        res.append(f'<text x="{x+20}" y="{y+40}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="20" font-weight="700">FlowGrid</text>')
        # Hotline action (48x48)
        res.append(f'<rect x="{x+270}" y="{y+8}" width="48" height="48" fill="#DEE7E2" rx="2"/>')
        res.append(f'<text x="{x+294}" y="{y+38}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="16" text-anchor="middle">📞</text>')
        # Hamburger button (48x48)
        res.append(f'<rect x="{x+326}" y="{y+8}" width="48" height="48" fill="#DEE7E2" rx="2"/>')
        res.append(f'<line x1="{x+338}" y1="{y+26}" x2="{x+362}" y2="{y+26}" stroke="#183B35" stroke-width="2"/>')
        res.append(f'<line x1="{x+338}" y1="{y+32}" x2="{x+362}" y2="{y+32}" stroke="#183B35" stroke-width="2"/>')
        res.append(f'<line x1="{x+338}" y1="{y+38}" x2="{x+362}" y2="{y+38}" stroke="#183B35" stroke-width="2"/>')
        return res

    # Helper: English Mobile Footer (340px)
    def render_en_mobile_footer(x, y):
        res = []
        res.append(f'<rect x="{x}" y="{y}" width="390" height="340" fill="#183B35"/>')
        res.append(f'<text x="{x+20}" y="{y+40}" fill="#F4F1E8" font-family="\'Bodoni Moda\', serif" font-size="24" font-weight="700">FlowGrid Studio</text>')
        t_mf, _ = wrap_text("Quiet, resilient interior architecture and millwork for urban Dhaka apartments.", x+20, y+70, 36, 20, "'Manrope', sans-serif", 13, "#DEE7E2")
        res.append(t_mf)
        res.append(f'<text x="{x+20}" y="{y+140}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="12" font-weight="700">LOCATION &amp; CONTACT</text>')
        res.append(f'<text x="{x+20}" y="{y+165}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="13">Mirpur-10, Dhaka 1216 · +880 1700-000000</text>')
        res.append(f'<text x="{x+20}" y="{y+190}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="13">hello@flowgrid-interiors.com</text>')
        res.append(f'<line x1="{x+20}" y1="{y+225}" x2="{x+370}" y2="{y+225}" stroke="#2D524A" stroke-width="1"/>')
        res.append(f'<text x="{x+20}" y="{y+255}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="12">Privacy Policy · Terms of Service</text>')
        res.append(f'<text x="{x+20}" y="{y+285}" fill="#C4D1CA" font-family="\'Manrope\', sans-serif" font-size="12">Rumi\'s Fashionable House (Community Sibling)</text>')
        res.append(f'<text x="{x+20}" y="{y+315}" fill="#C4D1CA" font-family="\'Manrope\', sans-serif" font-size="12">© 2026 FlowGrid. Truth in Design Policy.</text>')
        return res

    # -------------------------------------------------------------
    # SCREEN 1: English Desktop Homepage (1440px) - x: 80, y: 260
    # -------------------------------------------------------------
    ex1, ey1 = 80, 260
    svg.append(f'<rect x="{ex1}" y="{ey1}" width="1440" height="2500" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_header(ex1, ey1, "home"))

    svg.append(f'<text x="{ex1+80}" y="{ey1+160}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">DHAKA INTERIOR ARCHITECTURE &amp; MILLWORK</text>')
    t_eh1, _ = wrap_text("Quiet, Resilient Architecture for Everyday Life", ex1+80, ey1+215, 26, 64, "'Bodoni Moda', serif", 52, "#183B35", 700)
    svg.append(t_eh1)
    t_ehsub, _ = wrap_text("Balancing spatial calm, generous daylight, seasoned Burma teak timber, and heavy daily cooking routines for urban Dhaka homes.", ex1+80, ey1+360, 54, 26, "'Manrope', sans-serif", 17, "#56645E")
    svg.append(t_ehsub)

    svg.append(f'<rect x="{ex1+80}" y="{ey1+435}" width="200" height="52" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{ex1+180}" y="{ey1+468}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="15" font-weight="600" text-anchor="middle">Book Consultation →</text>')
    svg.append(f'<rect x="{ex1+300}" y="{ey1+435}" width="180" height="52" fill="transparent" stroke="#183B35" stroke-width="1.5" rx="2"/>')
    svg.append(f'<text x="{ex1+390}" y="{ey1+468}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="15" font-weight="600" text-anchor="middle">View Archive</text>')

    if img_living:
        svg.append(f'<image href="{img_living}" x="{ex1+80}" y="{ey1+515}" width="1280" height="600" preserveAspectRatio="xMidYMid slice"/>')
    svg.append(f'<rect x="{ex1+100}" y="{ey1+535}" width="420" height="34" fill="#183B35" fill-opacity="0.9" rx="2"/>')
    svg.append(f'<text x="{ex1+120}" y="{ey1+557}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600">Concept Design · AI Visualisation · Not a Completed Project</text>')

    svg.append(f'<rect x="{ex1+80}" y="{ey1+1145}" width="1280" height="240" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{ex1+120}" y="{ey1+1190}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">OUR PHILOSOPHY</text>')
    svg.append(f'<text x="{ex1+120}" y="{ey1+1225}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="28" font-weight="700">Purposeful Space, Honest Materials &amp; Enduring Joinery</text>')
    t_ee, _ = wrap_text("Urban Dhaka apartments demand maximum circulation and ventilated, moisture-resilient storage. We replace fragile decorative laminates with solid Burma teak, seasoned Garjan structural frames, and breathable handwoven Sylhet cane panels.", ex1+120, ey1+1265, 80, 24, "'Manrope', sans-serif", 15, "#56645E")
    svg.append(t_ee)

    svg.append(f'<text x="{ex1+80}" y="{ey1+1430}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="32" font-weight="700">Selected Architectural Studies</text>')
    studies_en = [
        ("Gulshan Lakeview Study", "Media wall & integrated joinery", img_living, ex1+80),
        ("Resilient Kitchen Study", "Honed granite and LPG cylinder ventilation", img_kitchen, ex1+520),
        ("Master Bedroom Study", "Platform bed and slatted wardrobe", img_bedroom, ex1+960)
    ]
    for stit, ssub, simg, scx in studies_en:
        svg.append(f'<rect x="{scx}" y="{ey1+1475}" width="400" height="380" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
        if simg:
            svg.append(f'<image href="{simg}" x="{scx}" y="{ey1+1475}" width="400" height="230" preserveAspectRatio="xMidYMid slice"/>')
        svg.append(f'<rect x="{scx+10}" y="{ey1+1485}" width="260" height="24" fill="#183B35" fill-opacity="0.9" rx="2"/>')
        svg.append(f'<text x="{scx+20}" y="{ey1+1501}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="11">Concept Design · AI Visualisation</text>')
        svg.append(f'<text x="{scx+15}" y="{ey1+1735}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="18" font-weight="700">{escape_xml(stit)}</text>')
        t_ess, _ = wrap_text(ssub, scx+15, ey1+1760, 34, 20, "'Manrope', sans-serif", 13, "#56645E")
        svg.append(t_ess)
        svg.append(f'<text x="{scx+15}" y="{ey1+1825}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600">View Full Study →</text>')

    svg.extend(render_en_footer(ex1, ey1+1920))

    # -------------------------------------------------------------
    # SCREEN 2: English Projects Archive (1440px) - x: 1600, y: 260
    # -------------------------------------------------------------
    ex2, ey2 = 1600, 260
    svg.append(f'<rect x="{ex2}" y="{ey2}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_header(ex2, ey2, "projects"))

    svg.append(f'<text x="{ex2+80}" y="{ey2+150}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">PROJECTS &amp; CONCEPT ARCHIVE</text>')
    svg.append(f'<text x="{ex2+80}" y="{ey2+195}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="36" font-weight="700">Architectural Concepts &amp; Study Gallery</text>')
    t_en_arch, _ = wrap_text("Tailored residential solutions for urban Dhaka apartments. All 3D interior renders are presented as exploratory architectural design studies.", ex2+80, ey2+235, 75, 22, "'Manrope', sans-serif", 16, "#56645E")
    svg.append(t_en_arch)

    tabs_en = [("All Studies", True), ("Living & Dining", False), ("Kitchen & Pantry", False), ("Bedroom & Alcove", False), ("Joinery Details", False)]
    etx = ex2 + 80
    for tn, is_a in tabs_en:
        bg_t = "#183B35" if is_a else "#DEE7E2"
        col_t = "#F4F1E8" if is_a else "#183B35"
        svg.append(f'<rect x="{etx}" y="{ey2+280}" width="160" height="48" fill="{bg_t}" rx="2"/>')
        svg.append(f'<text x="{etx+80}" y="{ey2+310}" fill="{col_t}" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600" text-anchor="middle">{escape_xml(tn)}</text>')
        etx += 175

    cards_en = [
        ("Gulshan Lakeview Residence", "Living room media wall & natural daylighting", img_living, ex2+80, ey2+350, "3-View Coherent Study"),
        ("Resilient Kitchen & Pantry", "Granite worktops & ventilated LPG niche", img_kitchen, ex2+740, ey2+350, "Kitchen Specification"),
        ("Master Bedroom & Study Alcove", "Platform bed & slatted cane wardrobe", img_bedroom, ex2+80, ey2+1020, "Bedroom Study"),
        ("Burma Teak & Brass Lap Joint", "Mortise-and-tenon millwork craftsmanship", img_joinery, ex2+740, ey2+1020, "Material Specification")
    ]
    for ctit, csub, cimg, cx, cy, ctag in cards_en:
        svg.append(f'<rect x="{cx}" y="{cy}" width="620" height="630" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
        if cimg:
            svg.append(f'<image href="{cimg}" x="{cx}" y="{cy}" width="620" height="420" preserveAspectRatio="xMidYMid slice"/>')
        svg.append(f'<rect x="{cx+15}" y="{cy+15}" width="340" height="28" fill="#183B35" fill-opacity="0.9" rx="2"/>')
        svg.append(f'<text x="{cx+25}" y="{cy+34}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="12">Concept Design · AI Visualisation · Not Completed</text>')
        svg.append(f'<text x="{cx+24}" y="{cy+465}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">{escape_xml(ctag)}</text>')
        svg.append(f'<text x="{cx+24}" y="{cy+495}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="22" font-weight="700">{escape_xml(ctit)}</text>')
        t_csub, _ = wrap_text(csub, cx+24, cy+525, 45, 20, "'Manrope', sans-serif", 14, "#56645E")
        svg.append(t_csub)
        svg.append(f'<text x="{cx+24}" y="{cy+595}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">View Detailed Study →</text>')

    svg.extend(render_en_footer(ex2, ey2+1920))

    # -------------------------------------------------------------
    # SCREEN 3: English Desktop Concept Detail (3-View) - x: 3120, y: 260
    # -------------------------------------------------------------
    ex3, ey3 = 3120, 260
    svg.append(f'<rect x="{ex3}" y="{ey3}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_header(ex3, ey3, "projects"))

    svg.append(f'<text x="{ex3+80}" y="{ey3+140}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">CASE STUDY · CONCEPT 01 (3 COHERENT SPATIAL VIEWS)</text>')
    svg.append(f'<text x="{ex3+80}" y="{ey3+185}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="34" font-weight="700">Gulshan Lakeview Residence — 3 Spatial Angles</text>')

    views_en = [
        ("View 1: Living Area & Media Wall", img_living, ex3+80, 620),
        ("View 2: Dining & Veranda Daylight", img_living_alt, ex3+720, 620),
    ]
    for v_title, v_img, vx, vw in views_en:
        svg.append(f'<rect x="{vx}" y="{ey3+215}" width="{vw}" height="380" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
        if v_img:
            svg.append(f'<image href="{v_img}" x="{vx}" y="{ey3+215}" width="{vw}" height="340" preserveAspectRatio="xMidYMid slice"/>')
        svg.append(f'<text x="{vx+15}" y="{ey3+580}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600">{escape_xml(v_title)}</text>')

    svg.append(f'<rect x="{ex3+80}" y="{ey3+615}" width="1280" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
    if img_joinery:
        svg.append(f'<image href="{img_joinery}" x="{ex3+80}" y="{ey3+615}" width="540" height="420" preserveAspectRatio="xMidYMid slice"/>')
    svg.append(f'<text x="{ex3+650}" y="{ey3+660}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">VIEW 3: MATERIAL &amp; JOINERY DETAIL</text>')
    svg.append(f'<text x="{ex3+650}" y="{ey3+695}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="24" font-weight="700">Burma Teak Lap Joint &amp; Brass Inlay Detail</text>')
    t_v3e, _ = wrap_text("To withstand monsoon humidity, precision timber millwork utilizes interlocking mortise-and-tenon joints with polished brass accent inlays. Timber is hand-finished with matte organic oils rather than synthetic high-gloss lacquers.", ex3+650, ey3+735, 45, 22, "'Manrope', sans-serif", 15, "#56645E")
    svg.append(t_v3e)

    svg.append(f'<rect x="{ex3+80}" y="{ey3+1060}" width="1280" height="340" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<rect x="{ex3+80}" y="{ey3+1060}" width="1280" height="50" fill="#183B35" rx="4 4 0 0"/>')
    svg.append(f'<text x="{ex3+110}" y="{ey3+1092}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="18" font-weight="600">Three Core Spatial Strategies (Design Intent)</text>')

    decs_en = [
        ("1. Floor-to-Ceiling Media Wall", "Utilizing 9.5-foot ceilings for continuous vertical joinery, concealing wires and electronic equipment behind slatted teak cabinetry."),
        ("2. Cross-Ventilation & Daylight", "Eliminating rigid partition walls between living and dining areas, allowing unhindered southwest daylight to wash through the interior."),
        ("3. Precision Joinery Engineering", "Interlocking lap joints and seasoned timber frames prevent warping during humid Dhaka rainy seasons.")
    ]
    edx = ex3 + 110
    for dt, dd in decs_en:
        svg.append(f'<text x="{edx}" y="{ey3+1145}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="16" font-weight="700">{escape_xml(dt)}</text>')
        tdd, _ = wrap_text(dd, edx, ey3+1175, 34, 22, "'Manrope', sans-serif", 14, "#56645E")
        svg.append(tdd)
        edx += 420

    svg.append(f'<rect x="{ex3+80}" y="{ey3+1430}" width="1280" height="440" fill="#DEE7E2" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{ex3+110}" y="{ey3+1470}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="22" font-weight="700">Material Schedule &amp; Study Parameters</text>')
    t_he, _ = wrap_text("Study Constraint: Formulated for a hypothetical 2,150 SFT apartment layout in Gulshan, Dhaka. Exploratory visualization, not a commissioned client build.", ex3+110, ey3+1505, 80, 20, "'Manrope', sans-serif", 13, "#895239")
    svg.append(t_he)

    specs_en = [
        ("Primary Joinery Timber", "Seasoned Burma Teak (Tectona grandis) · Matte organic oil finish"),
        ("Structural Joinery Accent", "Hand-fitted lap joint with polished brass inlay"),
        ("Countertops & Vanities", "20mm natural honed granite slab · Heat and spice resistant"),
        ("Wall Treatment", "Natural breathable lime plaster (Chuna polish) · Matte mineral texture"),
        ("Hardware & Mechanisms", "German soft-close concealed hinges and full-extension under-mount slides")
    ]
    emy_sp = ey3 + 1545
    for sn, sv in specs_en:
        svg.append(f'<text x="{ex3+110}" y="{emy_sp}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">{escape_xml(sn)}:</text>')
        svg.append(f'<text x="{ex3+380}" y="{emy_sp}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="14">{escape_xml(sv)}</text>')
        emy_sp += 34

    svg.append(f'<rect x="{ex3+110}" y="{ey3+1760}" width="260" height="52" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{ex3+240}" y="{ey3+1792}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="15" font-weight="600" text-anchor="middle">Enquire on this Study →</text>')
    svg.extend(render_en_footer(ex3, ey3+1920))

    # -------------------------------------------------------------
    # SCREEN 4: English Desktop Real-Project Framework Template - x: 80, y: 2860
    # -------------------------------------------------------------
    ex4, ey4 = 80, 2860
    svg.append(f'<rect x="{ex4}" y="{ey4}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_header(ex4, ey4, "projects"))

    svg.append(f'<text x="{ex4+80}" y="{ey4+140}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">COMPLETED RESIDENTIAL TEMPLATE · ARCHITECTURAL SPECIFICATION</text>')
    svg.append(f'<text x="{ex4+80}" y="{ey4+185}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="34" font-weight="700">Built Project Photography &amp; Case Study Framework</text>')

    svg.append(f'<rect x="{ex4+80}" y="{ey4+215}" width="1280" height="105" fill="#DEE7E2" stroke="#183B35" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{ex4+110}" y="{ey4+245}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="15" font-weight="700">Sample Project Framework (Placeholder Notice):</text>')
    t_efn, _ = wrap_text("This framework is structured to document verified completed residential projects, client requirements, floor plans, and on-site photography upon completion of physical builds.", ex4+110, ey4+270, 85, 20, "'Manrope', sans-serif", 13, "#56645E")
    svg.append(t_efn)

    svg.append(f'<rect x="{ex4+80}" y="{ey4+335}" width="800" height="450" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
    svg.append(f'<rect x="{ex4+90}" y="{ey4+345}" width="780" height="430" fill="#DEE7E2"/>')
    svg.append(f'<text x="{ex4+480}" y="{ey4+550}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="18" font-weight="600" text-anchor="middle">[ Built Residential Living &amp; Dining Photography Slot ]</text>')

    d_en = [
        ("Cabinetry Joinery & Edge Detailing", ey4+335),
        ("Dining Table & Solid Timber Joint", ey4+490),
        ("Indoor Planting & Architectural Lighting", ey4+645)
    ]
    for dn, dy in d_en:
        svg.append(f'<rect x="{ex4+910}" y="{dy}" width="450" height="135" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
        svg.append(f'<rect x="{ex4+920}" y="{dy+10}" width="180" height="115" fill="#DEE7E2"/>')
        svg.append(f'<text x="{ex4+1010}" y="{dy+70}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="12" text-anchor="middle">[ Photo ]</text>')
        svg.append(f'<text x="{ex4+1120}" y="{dy+50}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">{escape_xml(dn)}</text>')
        svg.append(f'<text x="{ex4+1120}" y="{dy+80}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="12">Verified site shot &amp; client sign-off</text>')

    svg.append(f'<rect x="{ex4+80}" y="{ey4+810}" width="1280" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<rect x="{ex4+80}" y="{ey4+810}" width="1280" height="50" fill="#183B35" rx="4 4 0 0"/>')
    svg.append(f'<text x="{ex4+110}" y="{ey4+842}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="18" font-weight="600">Project Parameters &amp; Architectural Analysis (Sample Framework)</text>')

    params_en = [
        ("Project Discipline", "[Residential Interior Architecture & Bespoke Joinery]"),
        ("Location", "[Project Area / Suburb — e.g. Mirpur DOHS / Gulshan / Dhanmondi]"),
        ("Floor Area", "[Square Footage — e.g. 2,000–2,500 SFT (4 Bedrooms & Study)]"),
        ("Execution Schedule", "[Project Timeline — Approx. 12–16 weeks (Subject to site readiness)]"),
        ("Primary Material Schedule", "[Seasoned Solid Timber, Natural Veneer, Hand-polished Brass]")
    ]
    epy = ey4 + 890
    for pl, pv in params_en:
        svg.append(f'<text x="{ex4+110}" y="{epy}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="15" font-weight="700">{escape_xml(pl)}:</text>')
        svg.append(f'<text x="{ex4+340}" y="{epy}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="15">{escape_xml(pv)}</text>')
        epy += 40

    t_edesc, _ = wrap_text("Spatial Rationale Framework: Optimizing natural ventilation and tailored storage based on multi-generational family routines. Site survey data and execution drawings will be integrated upon build commissioning.", ex4+110, epy+20, 80, 22, "'Manrope', sans-serif", 14, "#183B35")
    svg.append(t_edesc)
    svg.extend(render_en_footer(ex4, ey4+1920))

    # -------------------------------------------------------------
    # SCREEN 5: English Desktop Dedicated Services - x: 1600, y: 2860
    # -------------------------------------------------------------
    ex5, ey5 = 1600, 2860
    svg.append(f'<rect x="{ex5}" y="{ey5}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_header(ex5, ey5, "services"))

    svg.append(f'<text x="{ex5+80}" y="{ey5+150}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">ARCHITECTURAL SERVICES &amp; EXPERTISE</text>')
    svg.append(f'<text x="{ex5+80}" y="{ey5+195}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="36" font-weight="700">Our Services &amp; Architectural Collaboration</text>')

    esvcs = [
        ("01", "Full Interior Architecture",
         "End-to-end residential transformation: 2D space planning, masonry modification, electrical schematics, clean glare-free lighting design, and continuous site supervision.",
         ["• Comprehensive 2D blueprints & furniture schedules", "• Electrical, plumbing, and HVAC coordinates", "• Photorealistic 3D visualization & material palettes", "• Quality control and turnkey handover"]),
        ("02", "Bespoke Joinery & Millwork",
         "Tailored floor-to-ceiling bookcases, wardrobe partitions, vanity counters, and heavy-duty kitchen cabinetry using seasoned solid wood and cane under dedicated craft supervision.",
         ["• Seasoned Burma teak, Garjan, and Oak timbers", "• Moisture-resistant handwoven cane panel inserts", "• German soft-close concealed hardware fittings", "• Supervised trial assembly and clean installation"]),
        ("03", "Spatial Planning & Bill of Quantities (BOQ)",
         "Architectural consultancy for clients managing execution independently: measured site drawings, execution sheets, and itemized material schedules.",
         ["• Detailed architectural CAD drawings", "• Trade execution sheets for carpenters & electricians", "• Transparent BOQ market costing estimates", "• Scheduled design review sessions"])
    ]
    esy = ey5 + 320
    for sno, stit, sbody, spoints in esvcs:
        svg.append(f'<rect x="{ex5+80}" y="{esy}" width="1280" height="380" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
        svg.append(f'<text x="{ex5+120}" y="{esy+55}" fill="#895239" font-family="\'Bodoni Moda\', serif" font-size="32" font-weight="700">{sno}</text>')
        svg.append(f'<text x="{ex5+180}" y="{esy+52}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="24" font-weight="700">{escape_xml(stit)}</text>')
        t_sb, _ = wrap_text(sbody, ex5+120, esy+95, 80, 22, "'Manrope', sans-serif", 15, "#56645E")
        svg.append(t_sb)

        px = ex5 + 120
        py = esy + 175
        for p in spoints:
            svg.append(f'<text x="{px}" y="{py}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600">{escape_xml(p)}</text>')
            py += 26

        svg.append(f'<rect x="{ex5+120}" y="{esy+300}" width="200" height="48" fill="#183B35" rx="2"/>')
        svg.append(f'<text x="{ex5+220}" y="{esy+330}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">Select Service →</text>')
        esy += 420

    svg.extend(render_en_footer(ex5, ey5+1920))

    # -------------------------------------------------------------
    # SCREEN 6: English Desktop Service Detail (Bespoke Joinery) - x: 3120, y: 2860
    # -------------------------------------------------------------
    ex6, ey6 = 3120, 2860
    svg.append(f'<rect x="{ex6}" y="{ey6}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_header(ex6, ey6, "services"))

    svg.append(f'<text x="{ex6+80}" y="{ey6+140}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">SERVICE DETAIL · BESPOKE JOINERY &amp; MILLWORK</text>')
    svg.append(f'<text x="{ex6+80}" y="{ey6+185}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="34" font-weight="700">Custom Furniture &amp; Millwork Execution</text>')

    svg.append(f'<rect x="{ex6+80}" y="{ey6+230}" width="680" height="480" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
    if img_joinery:
        svg.append(f'<image href="{img_joinery}" x="{ex6+80}" y="{ey6+230}" width="680" height="480" preserveAspectRatio="xMidYMid slice"/>')

    svg.append(f'<rect x="{ex6+800}" y="{ey6+230}" width="560" height="480" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{ex6+830}" y="{ey6+275}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="24" font-weight="700">Joinery Craft &amp; Timber Engineering</text>')
    t_j_en, _ = wrap_text("FlowGrid millwork utilizes seasoned solid timber and architectural-grade natural veneers. Every cabinet joint is engineered with mortise-and-tenon construction to ensure structural stability through seasonal humidity fluctuations.", ex6+830, ey6+315, 38, 22, "'Manrope', sans-serif", 15, "#56645E")
    svg.append(t_j_en)

    svg.append(f'<text x="{ex6+830}" y="{ey6+445}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="16" font-weight="700">Timber &amp; Material Options:</text>')
    t_opts = [
        "• Seasoned Burma Teak (Tectona grandis) - Premium visible surfaces",
        "• Seasoned Garjan Timber - Structural internal frames",
        "• Breathable Sylhet Cane Inserts - Monsoon humidity control",
        "• German soft-close concealed slides and architectural hinges"
    ]
    ety = ey6 + 475
    for to in t_opts:
        svg.append(f'<text x="{ex6+830}" y="{ety}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="14">{escape_xml(to)}</text>')
        ety += 28

    svg.extend(render_en_footer(ex6, ey6+1920))

    # -------------------------------------------------------------
    # SCREEN 7: English Dedicated Process (1440px) - x: 80, y: 5160
    # -------------------------------------------------------------
    ex7, ey7 = 80, 5160
    svg.append(f'<rect x="{ex7}" y="{ey7}" width="1440" height="1950" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_header(ex7, ey7, "process"))

    svg.append(f'<text x="{ex7+80}" y="{ey7+140}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">OUR METHODOLOGY</text>')
    svg.append(f'<text x="{ex7+80}" y="{ey7+185}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="34" font-weight="700">The 5-Stage Architectural Journey</text>')

    p_cards_en = [
        ("Stage 1: Spatial Audit", "Week 1", "Site laser measurement, lifestyle consultation, and structural viability assessment."),
        ("Stage 2: 2D & 3D Concepts", "Weeks 2–3", "Detailed floor plan schematics, daylight routing, and photorealistic 3D visual concepts."),
        ("Stage 3: Detail BOQ Budget", "Week 4", "Itemized material pricing, hardware selection, and contractual approval."),
        ("Stage 4: Joinery Fabrication", "Weeks 5–11", "Seasoned timber milling, mortise assembly, and pre-installation trial fit under specialist supervision."),
        ("Stage 5: Turnkey Handover", "Week 12", "On-site precise leveling, clean installation, and final handover walk-through.")
    ]
    epy_card = ey7 + 240
    for ps_t, ps_w, ps_d in p_cards_en:
        svg.append(f'<rect x="{ex7+80}" y="{epy_card}" width="1280" height="120" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
        svg.append(f'<text x="{ex7+120}" y="{epy_card+45}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="20" font-weight="700">{escape_xml(ps_t)}</text>')
        svg.append(f'<rect x="{ex7+120}" y="{epy_card+60}" width="90" height="24" fill="#DEE7E2" rx="2"/>')
        svg.append(f'<text x="{ex7+165}" y="{epy_card+77}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="12" font-weight="700" text-anchor="middle">{escape_xml(ps_w)}</text>')
        t_psd, _ = wrap_text(ps_d, ex7+240, epy_card+55, 75, 20, "'Manrope', sans-serif", 14, "#56645E")
        svg.append(t_psd)
        epy_card += 140

    svg.extend(render_en_footer(ex7, ey7+1670))

    # -------------------------------------------------------------
    # SCREEN 8: English Dedicated Studio (1440px) - x: 1600, y: 5160
    # -------------------------------------------------------------
    ex8, ey8 = 1600, 5160
    svg.append(f'<rect x="{ex8}" y="{ey8}" width="1440" height="1950" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_header(ex8, ey8, "studio"))

    svg.append(f'<text x="{ex8+80}" y="{ey8+140}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">STUDIO ETHOS</text>')
    svg.append(f'<text x="{ex8+80}" y="{ey8+185}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="34" font-weight="700">Mirpur Practice, Craft &amp; Governance</text>')

    svg.append(f'<rect x="{ex8+80}" y="{ey8+240}" width="1280" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{ex8+120}" y="{ey8+290}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="24" font-weight="700">Architecture Rooted in Dhaka Homes</text>')
    t_std_en, _ = wrap_text("Operating in Mirpur-10, FlowGrid provides thoughtful interior architecture and joinery execution tailored to Dhaka's urban density. We believe homes should feel calm, well-ventilated, and built with honest materials that age gracefully over decades.", ex8+120, ey8+330, 80, 24, "'Manrope', sans-serif", 15, "#56645E")
    svg.append(t_std_en)

    t_gov_en, _ = wrap_text("Clear Governance Boundary: Rumi's Fashionable House represents lifestyle vlogging and family community inspiration. FlowGrid operates as an independent architectural studio with dedicated technical practitioners.", ex8+120, ey8+440, 80, 22, "'Manrope', sans-serif", 14, "#895239")
    svg.append(t_gov_en)

    svg.extend(render_en_footer(ex8, ey8+1670))

    # -------------------------------------------------------------
    # SCREEN 9: English Dedicated Contact (1440px) - x: 3120, y: 5160
    # -------------------------------------------------------------
    ex9, ey9 = 3120, 5160
    svg.append(f'<rect x="{ex9}" y="{ey9}" width="1440" height="1950" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_header(ex9, ey9, "contact"))

    svg.append(f'<text x="{ex9+80}" y="{ey9+140}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">START A CONVERSATION</text>')
    svg.append(f'<text x="{ex9+80}" y="{ey9+185}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="34" font-weight="700">Studio Contact &amp; Consultation</text>')

    svg.append(f'<rect x="{ex9+80}" y="{ey9+240}" width="780" height="520" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    efy = ey9 + 270
    efx = ex9 + 120
    efw = 700

    svg.append(f'<text x="{efx}" y="{efy}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600">1. Full Name *</text>')
    svg.append(f'<rect x="{efx}" y="{efy+8}" width="{efw}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{efx+15}" y="{efy+38}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="14">e.g. Farhan Ahmed</text>')
    efy += 74

    svg.append(f'<text x="{efx}" y="{efy}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600">2. Mobile Number *</text>')
    svg.append(f'<rect x="{efx}" y="{efy+8}" width="{efw}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{efx+15}" y="{efy+38}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="14">01XXXXXXXXX or +880 1XXXXXXXXX</text>')
    efy += 74

    svg.append(f'<text x="{efx}" y="{efy}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600">3. Area &amp; City *</text>')
    svg.append(f'<rect x="{efx}" y="{efy+8}" width="{efw}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{efx+15}" y="{efy+38}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="14">e.g. Mirpur DOHS, Gulshan, Dhanmondi</text>')
    efy += 74

    svg.append(f'<text x="{efx}" y="{efy}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600">4. Service Required *</text>')
    svg.append(f'<rect x="{efx}" y="{efy+8}" width="{efw}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{efx+15}" y="{efy+38}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="14">Full Interior / Custom Joinery / Not Sure Yet ▼</text>')
    efy += 74

    svg.append(f'<rect x="{efx}" y="{efy+10}" width="220" height="52" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{efx+110}" y="{efy+42}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">Request Consultation →</text>')

    # Studio Address Card on Right
    svg.append(f'<rect x="{ex9+890}" y="{ey9+240}" width="470" height="320" fill="#DEE7E2" rx="4"/>')
    svg.append(f'<text x="{ex9+920}" y="{ey9+285}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="22" font-weight="700">Studio Address</text>')
    svg.append(f'<text x="{ex9+920}" y="{ey9+325}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="14">Mirpur-10, Dhaka 1216, Bangladesh</text>')
    svg.append(f'<text x="{ex9+920}" y="{ey9+355}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="14">Hotline: +880 1700-000000</text>')
    svg.append(f'<text x="{ex9+920}" y="{ey9+385}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="14">Email: hello@flowgrid-interiors.com</text>')
    svg.append(f'<rect x="{ex9+920}" y="{ey9+420}" width="260" height="48" fill="#0D5C52" rx="2"/>')
    svg.append(f'<text x="{ex9+1050}" y="{ey9+450}" fill="#FFFFFF" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">WhatsApp Direct Chat</text>')

    svg.extend(render_en_footer(ex9, ey9+1670))

    # -------------------------------------------------------------
    # SCREEN 10: English Desktop Legal & Privacy (1440px) - x: 4640, y: 260
    # -------------------------------------------------------------
    ex10, ey10 = 4640, 260
    svg.append(f'<rect x="{ex10}" y="{ey10}" width="1440" height="1500" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_header(ex10, ey10, "privacy"))

    svg.append(f'<text x="{ex10+80}" y="{ey10+140}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">TERMS &amp; PRIVACY</text>')
    svg.append(f'<text x="{ex10+80}" y="{ey10+185}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="34" font-weight="700">Design Ownership &amp; Privacy Policy</text>')

    svg.append(f'<rect x="{ex10+80}" y="{ey10+240}" width="1280" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{ex10+120}" y="{ey10+285}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="20" font-weight="700">1. Truth in Architectural Visualization</text>')
    t_lp_en1, _ = wrap_text("All 3D interior renders presented across FlowGrid platforms are conceptual design studies and AI-assisted visualizations. They represent spatial strategies and material intent, not completed client commissions.", ex10+120, ey10+315, 80, 22, "'Manrope', sans-serif", 14, "#56645E")
    svg.append(t_lp_en1)

    svg.append(f'<text x="{ex10+120}" y="{ey10+425}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="20" font-weight="700">2. Client Data &amp; Consultation Rights</text>')
    t_lp_en2, _ = wrap_text("Contact information entered in enquiry forms is retained strictly for spatial consultation scheduling. Intellectual property rights for customized blueprints remain protected under standard design contracts.", ex10+120, ey10+455, 80, 22, "'Manrope', sans-serif", 14, "#56645E")
    svg.append(t_lp_en2)

    svg.extend(render_en_footer(ex10, ey10+1220))

    # -------------------------------------------------------------
    # SCREEN 11: English Desktop 404 (1440px) - x: 4640, y: 1860
    # -------------------------------------------------------------
    ex11, ey11 = 4640, 1860
    svg.append(f'<rect x="{ex11}" y="{ey11}" width="1440" height="900" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_header(ex11, ey11, "404"))

    svg.append(f'<text x="{ex11+720}" y="{ey11+260}" fill="#895239" font-family="\'Bodoni Moda\', serif" font-size="96" font-weight="700" text-anchor="middle">404</text>')
    svg.append(f'<text x="{ex11+720}" y="{ey11+320}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="28" font-weight="700" text-anchor="middle">Page Not Located</text>')
    t_404_en, _ = wrap_text("The requested page may have relocated or is undergoing architectural drafting. Return to the studio homepage or browse our project archive.", ex11+420, ey11+360, 60, 22, "'Manrope', sans-serif", 15, "#56645E")
    svg.append(t_404_en)
    svg.append(f'<rect x="{ex11+600}" y="{ey11+440}" width="240" height="52" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{ex11+720}" y="{ey11+472}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">Return to Homepage →</text>')
    svg.extend(render_en_footer(ex11, ey11+620))

    # =============================================================
    # COMPLETE ENGLISH MOBILE EXPERIENCE SUITE (390px Master Screens)
    # Starts at y = 2860 in 5 columns (x = 4640, 5110, 5580, 6050, 6520)
    # =============================================================

    # -------------------------------------------------------------
    # COLUMN M1 (x = 4640): Mobile Home & Mobile 404
    # -------------------------------------------------------------
    emx1, emy1 = 4640, 2860
    # SCREEN 12: Mobile Homepage (390 x 3350)
    svg.append(f'<rect x="{emx1}" y="{emy1}" width="390" height="3350" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_mobile_header(emx1, emy1))

    svg.append(f'<text x="{emx1+20}" y="{emy1+100}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">DHAKA INTERIOR ARCHITECTURE</text>')
    t_emh1, _ = wrap_text("Quiet, Resilient Architecture for Everyday Life", emx1+20, emy1+135, 20, 36, "'Bodoni Moda', serif", 26, "#183B35", 700)
    svg.append(t_emh1)
    t_emsub, _ = wrap_text("Balancing spatial calm, daylight, seasoned teak joinery, and heavy cooking routines for urban Dhaka.", emx1+20, emy1+225, 36, 20, "'Manrope', sans-serif", 13, "#56645E")
    svg.append(t_emsub)

    svg.append(f'<rect x="{emx1+20}" y="{emy1+290}" width="170" height="48" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{emx1+105}" y="{emy1+320}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Book Consultation</text>')
    svg.append(f'<rect x="{emx1+200}" y="{emy1+290}" width="170" height="48" fill="transparent" stroke="#183B35" stroke-width="1.5" rx="2"/>')
    svg.append(f'<text x="{emx1+285}" y="{emy1+320}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600" text-anchor="middle">View Archive</text>')

    if img_living:
        svg.append(f'<image href="{img_living}" x="{emx1+20}" y="{emy1+360}" width="350" height="230" preserveAspectRatio="xMidYMid slice"/>')
    svg.append(f'<rect x="{emx1+25}" y="{emy1+365}" width="280" height="22" fill="#183B35" fill-opacity="0.9" rx="2"/>')
    svg.append(f'<text x="{emx1+30}" y="{emy1+380}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="10">Concept Design · AI Visualisation</text>')

    svg.append(f'<rect x="{emx1+20}" y="{emy1+610}" width="350" height="200" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{emx1+35}" y="{emy1+645}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">OUR ETHOS</text>')
    svg.append(f'<text x="{emx1+35}" y="{emy1+675}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="16" font-weight="700">Honest Materials &amp; Purposeful Craft</text>')
    t_eeth, _ = wrap_text("Tailored floor-to-ceiling joinery, natural stone surfaces, and ventilated cane millwork.", emx1+35, emy1+705, 34, 18, "'Manrope', sans-serif", 13, "#56645E")
    svg.append(t_eeth)

    svg.append(f'<text x="{emx1+20}" y="{emy1+845}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="20" font-weight="700">Selected Concept Studies</text>')
    mstudies_en = [
        ("Gulshan Lakeview Study", "Media wall & daybed", img_living, emy1+875),
        ("Resilient Kitchen Study", "Granite & LPG niche", img_kitchen, emy1+1240),
        ("Master Bedroom Study", "Platform bed & study alcove", img_bedroom, emy1+1605)
    ]
    for st, sd, si, sy in mstudies_en:
        svg.append(f'<rect x="{emx1+20}" y="{sy}" width="350" height="345" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
        if si:
            svg.append(f'<image href="{si}" x="{emx1+20}" y="{sy}" width="350" height="215" preserveAspectRatio="xMidYMid slice"/>')
        svg.append(f'<rect x="{emx1+25}" y="{sy+5}" width="260" height="20" fill="#183B35" fill-opacity="0.9" rx="2"/>')
        svg.append(f'<text x="{emx1+30}" y="{sy+19}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="10">Concept Design · AI Visualisation</text>')
        svg.append(f'<text x="{emx1+35}" y="{sy+250}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="16" font-weight="700">{escape_xml(st)}</text>')
        t_msd, _ = wrap_text(sd, emx1+35, sy+275, 32, 18, "'Manrope', sans-serif", 13, "#56645E")
        svg.append(t_msd)
        svg.append(f'<text x="{emx1+35}" y="{sy+325}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600">View Full Study →</text>')

    svg.append(f'<rect x="{emx1+20}" y="{emy1+1980}" width="350" height="520" fill="#DEE7E2" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{emx1+35}" y="{emy1+2020}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="18" font-weight="700">Book a Spatial Consultation</text>')
    svg.append(f'<text x="{emx1+35}" y="{emy1+2045}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="12">Enter project details for initial discussion</text>')

    fy_enq = emy1 + 2065
    svg.append(f'<rect x="{emx1+35}" y="{fy_enq}" width="320" height="48" fill="#FFFFFF" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{emx1+45}" y="{fy_enq+30}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">Your Name *</text>')
    svg.append(f'<rect x="{emx1+35}" y="{fy_enq+58}" width="320" height="48" fill="#FFFFFF" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{emx1+45}" y="{fy_enq+88}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">Mobile Number: 01XXXXXXXXX *</text>')
    svg.append(f'<rect x="{emx1+35}" y="{fy_enq+116}" width="320" height="48" fill="#FFFFFF" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{emx1+45}" y="{fy_enq+146}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">Area / City (e.g. Mirpur, Gulshan) *</text>')
    svg.append(f'<rect x="{emx1+35}" y="{fy_enq+174}" width="320" height="48" fill="#FFFFFF" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{emx1+45}" y="{fy_enq+204}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">Service Required (or Not Sure) ▼ *</text>')
    svg.append(f'<rect x="{emx1+35}" y="{fy_enq+238}" width="320" height="52" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{emx1+195}" y="{fy_enq+270}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">Request Consultation →</text>')

    svg.extend(render_en_mobile_footer(emx1, emy1+3010))

    # SCREEN 22: English Mobile 404 (390 x 650) - placed directly below Home at y=6280
    emx11, emy11 = emx1, 6280
    svg.append(f'<rect x="{emx11}" y="{emy11}" width="390" height="650" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{emx11+195}" y="{emy11+180}" fill="#895239" font-family="\'Bodoni Moda\', serif" font-size="64" font-weight="700" text-anchor="middle">404</text>')
    svg.append(f'<text x="{emx11+195}" y="{emy11+230}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="18" font-weight="700" text-anchor="middle">Page Not Found</text>')
    t_me404, _ = wrap_text("The requested page may have relocated or is undergoing architectural drafting.", emx11+45, emy11+270, 30, 22, "'Manrope', sans-serif", 13, "#56645E")
    svg.append(t_me404)
    svg.append(f'<rect x="{emx11+45}" y="{emy11+340}" width="300" height="48" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{emx11+195}" y="{emy11+370}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">Return to Home →</text>')

    # -------------------------------------------------------------
    # COLUMN M2 (x = 5110): Mobile Archive & Mobile Concept Detail
    # -------------------------------------------------------------
    emx2, emy2 = 5110, 2860
    # SCREEN 13: English Mobile Projects Archive (390 x 1600)
    svg.append(f'<rect x="{emx2}" y="{emy2}" width="390" height="1600" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_mobile_header(emx2, emy2))

    svg.append(f'<text x="{emx2+20}" y="{emy2+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">PROJECTS ARCHIVE</text>')
    svg.append(f'<text x="{emx2+20}" y="{emy2+125}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="22" font-weight="700">Concept Gallery</text>')

    svg.append(f'<rect x="{emx2+20}" y="{emy2+150}" width="350" height="350" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
    if img_living:
        svg.append(f'<image href="{img_living}" x="{emx2+20}" y="{emy2+150}" width="350" height="220" preserveAspectRatio="xMidYMid slice"/>')
    svg.append(f'<rect x="{emx2+25}" y="{emy2+155}" width="260" height="20" fill="#183B35" fill-opacity="0.9" rx="2"/>')
    svg.append(f'<text x="{emx2+30}" y="{emy2+169}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="10">Concept Design · AI Visualisation</text>')
    svg.append(f'<text x="{emx2+35}" y="{emy2+395}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="16" font-weight="700">Gulshan Lakeview Study</text>')
    svg.append(f'<text x="{emx2+35}" y="{emy2+420}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">3 Coherent views &amp; millwork study</text>')
    svg.append(f'<text x="{emx2+35}" y="{emy2+460}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600">View Full Study →</text>')

    svg.append(f'<rect x="{emx2+20}" y="{emy2+520}" width="350" height="350" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
    if img_kitchen:
        svg.append(f'<image href="{img_kitchen}" x="{emx2+20}" y="{emy2+520}" width="350" height="220" preserveAspectRatio="xMidYMid slice"/>')
    svg.append(f'<rect x="{emx2+25}" y="{emy2+525}" width="260" height="20" fill="#183B35" fill-opacity="0.9" rx="2"/>')
    svg.append(f'<text x="{emx2+30}" y="{emy2+539}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="10">Concept Design · AI Visualisation</text>')
    svg.append(f'<text x="{emx2+35}" y="{emy2+765}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="16" font-weight="700">Resilient Kitchen &amp; Pantry</text>')
    svg.append(f'<text x="{emx2+35}" y="{emy2+790}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">Granite countertops &amp; ventilation</text>')
    svg.append(f'<text x="{emx2+35}" y="{emy2+830}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600">View Kitchen Study →</text>')

    svg.extend(render_en_mobile_footer(emx2, emy2+1260))

    # SCREEN 14: English Mobile Concept Detail - 3 Views (390 x 2000) - x: 5110, y: 4540
    emx3, emy3 = 5110, 4540
    svg.append(f'<rect x="{emx3}" y="{emy3}" width="390" height="2000" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_mobile_header(emx3, emy3))

    svg.append(f'<text x="{emx3+20}" y="{emy3+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">CONCEPT STUDY 01 · 3 VIEWS</text>')
    svg.append(f'<text x="{emx3+20}" y="{emy3+125}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="20" font-weight="700">Gulshan Lakeview Apartment</text>')

    v_stack_en = [
        ("View 1: Living Area & Media Wall", img_living, emy3+150),
        ("View 2: Dining & Veranda Daylight", img_living_alt, emy3+480),
        ("View 3: Lap Joint & Brass Inlay", img_joinery, emy3+810)
    ]
    for vt, vi, vy in v_stack_en:
        svg.append(f'<rect x="{emx3+20}" y="{vy}" width="350" height="310" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
        if vi:
            svg.append(f'<image href="{vi}" x="{emx3+20}" y="{vy}" width="350" height="220" preserveAspectRatio="xMidYMid slice"/>')
        svg.append(f'<rect x="{emx3+25}" y="{vy+5}" width="260" height="20" fill="#183B35" fill-opacity="0.9" rx="2"/>')
        svg.append(f'<text x="{emx3+30}" y="{vy+19}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="10">Concept Design · AI Visualisation</text>')
        svg.append(f'<text x="{emx3+35}" y="{vy+255}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="15" font-weight="700">{escape_xml(vt)}</text>')
        svg.append(f'<text x="{emx3+35}" y="{vy+280}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="12">Burma teak timber, brass detail, natural lime plaster</text>')

    svg.append(f'<rect x="{emx3+20}" y="{emy3+1140}" width="350" height="210" fill="#DEE7E2" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{emx3+35}" y="{emy3+1170}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="15" font-weight="700">Spatial Intent &amp; Material Strategy</text>')
    t_emdec, _ = wrap_text("Study premise: 2,150 SFT conceptual apartment. Floor-to-ceiling joinery, southwest veranda light, and moisture-resilient interlocking lap joints.", emx3+35, emy3+1195, 34, 20, "'Manrope', sans-serif", 13, "#56645E")
    svg.append(t_emdec)
    svg.append(f'<rect x="{emx3+35}" y="{emy3+1280}" width="320" height="48" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{emx3+195}" y="{emy3+1310}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Enquire on this Study →</text>')
    svg.extend(render_en_mobile_footer(emx3, emy3+1660))

    # -------------------------------------------------------------
    # COLUMN M3 (x = 5580): Mobile Built Project, Services, Joinery
    # -------------------------------------------------------------
    emx4, emy4 = 5580, 2860
    # SCREEN 15: Mobile Real-Project Framework Template (390 x 1400)
    svg.append(f'<rect x="{emx4}" y="{emy4}" width="390" height="1400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_mobile_header(emx4, emy4))

    svg.append(f'<text x="{emx4+20}" y="{emy4+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">COMPLETED PROJECT TEMPLATE</text>')
    svg.append(f'<text x="{emx4+20}" y="{emy4+125}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="20" font-weight="700">Built Project Framework</text>')

    svg.append(f'<rect x="{emx4+20}" y="{emy4+145}" width="350" height="90" fill="#DEE7E2" stroke="#183B35" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{emx4+35}" y="{emy4+170}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">Sample Project Framework Notice:</text>')
    t_mref, _ = wrap_text("Upon physical build completion, authentic site photography and client requirements will populate this framework.", emx4+35, emy4+192, 34, 18, "'Manrope', sans-serif", 12, "#56645E")
    svg.append(t_mref)

    svg.append(f'<rect x="{emx4+20}" y="{emy4+250}" width="350" height="220" fill="#DEE7E2" rx="2"/>')
    svg.append(f'<text x="{emx4+195}" y="{emy4+365}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">[ Built Photography Slot ]</text>')

    svg.append(f'<rect x="{emx4+20}" y="{emy4+490}" width="350" height="200" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{emx4+35}" y="{emy4+520}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">Project Parameters Framework:</text>')
    m_params_en = [
        "• Location: [Project Suburb — e.g. Mirpur/Gulshan]",
        "• Area: [Measurement — e.g. 2,000–2,500 SFT]",
        "• Timeline: [Approx. 12–16 weeks]",
        "• Materials: [Seasoned Timber & Natural Stone]"
    ]
    mpy_e = emy4 + 545
    for mp in m_params_en:
        svg.append(f'<text x="{emx4+35}" y="{mpy_e}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="12">{escape_xml(mp)}</text>')
        mpy_e += 24
    svg.extend(render_en_mobile_footer(emx4, emy4+1060))

    # SCREEN 16: Mobile Dedicated Services (390 x 1400) - x: 5580, y: 4330
    emx5, emy5 = 5580, 4330
    svg.append(f'<rect x="{emx5}" y="{emy5}" width="390" height="1400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_mobile_header(emx5, emy5))

    svg.append(f'<text x="{emx5+20}" y="{emy5+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">OUR SERVICES</text>')
    svg.append(f'<text x="{emx5+20}" y="{emy5+125}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="22" font-weight="700">Architectural Services</text>')

    msvcs_en = [
        ("01. Full Interior Architecture", "Floor plans, partition shifts, lighting, and site supervision."),
        ("02. Bespoke Joinery & Millwork", "Seasoned Burma teak & cane cabinetry under specialist supervision."),
        ("03. Space Planning & BOQ Sheet", "Architectural CAD drawings and transparent market material estimates.")
    ]
    msy_e = emy5 + 155
    for m_no, m_b in msvcs_en:
        svg.append(f'<rect x="{emx5+20}" y="{msy_e}" width="350" height="135" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
        svg.append(f'<text x="{emx5+35}" y="{msy_e+30}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="15" font-weight="700">{escape_xml(m_no)}</text>')
        t_msb, _ = wrap_text(m_b, emx5+35, msy_e+55, 34, 18, "'Manrope', sans-serif", 13, "#56645E")
        svg.append(t_msb)
        svg.append(f'<text x="{emx5+35}" y="{msy_e+115}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="12" font-weight="600">Select Service →</text>')
        msy_e += 150
    svg.extend(render_en_mobile_footer(emx5, emy5+1060))

    # SCREEN 17: Mobile Dedicated Joinery Detail (390 x 1400) - x: 5580, y: 5800
    emx6, emy6 = 5580, 5800
    svg.append(f'<rect x="{emx6}" y="{emy6}" width="390" height="1400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_mobile_header(emx6, emy6))

    svg.append(f'<text x="{emx6+20}" y="{emy6+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">SERVICE DETAIL</text>')
    svg.append(f'<text x="{emx6+20}" y="{emy6+125}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="20" font-weight="700">Bespoke Millwork &amp; Joinery</text>')

    if img_joinery:
        svg.append(f'<image href="{img_joinery}" x="{emx6+20}" y="{emy6+145}" width="350" height="220" preserveAspectRatio="xMidYMid slice"/>')
    svg.append(f'<rect x="{emx6+25}" y="{emy6+150}" width="260" height="20" fill="#183B35" fill-opacity="0.9" rx="2"/>')
    svg.append(f'<text x="{emx6+30}" y="{emy6+164}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="10">Concept Design · AI Visualisation</text>')

    svg.append(f'<rect x="{emx6+20}" y="{emy6+380}" width="350" height="260" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{emx6+35}" y="{emy6+410}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="15" font-weight="700">Craft &amp; Timber Engineering</text>')
    t_jfeat_e, _ = wrap_text("FlowGrid joinery utilizes seasoned solid timber and natural veneers. Each cabinet frame is constructed with mortise-and-tenon joints engineered for monsoon humidity stability.", emx6+35, emy6+435, 34, 20, "'Manrope', sans-serif", 13, "#56645E")
    svg.append(t_jfeat_e)
    svg.append(f'<text x="{emx6+35}" y="{emy6+560}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600">• Burma teak, seasoned Garjan &amp; brass inlays</text>')
    svg.append(f'<text x="{emx6+35}" y="{emy6+585}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600">• Soft-close concealed German hinges and slides</text>')
    svg.extend(render_en_mobile_footer(emx6, emy6+1060))

    # -------------------------------------------------------------
    # COLUMN M4 (x = 6050): Mobile Process, Studio, Legal
    # -------------------------------------------------------------
    emx7, emy7 = 6050, 2860
    # SCREEN 18: Mobile Dedicated Process (390 x 1400)
    svg.append(f'<rect x="{emx7}" y="{emy7}" width="390" height="1400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_mobile_header(emx7, emy7))

    svg.append(f'<text x="{emx7+20}" y="{emy7+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">OUR PROCESS</text>')
    svg.append(f'<text x="{emx7+20}" y="{emy7+125}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="22" font-weight="700">5 Clear Project Stages</text>')

    p_steps_en = [
        ("1. Initial Consultation", "Lifestyle audit and budget review"),
        ("2. Space Plan & Concepts", "2D blueprints and material palette"),
        ("3. Detailed BOQ & Drawings", "Itemized quotation and sign-off"),
        ("4. Joinery Fabrication", "Supervised timber milling & trial fit"),
        ("5. Clean On-Site Installation", "Precise leveling and handover")
    ]
    py_s_e = emy7 + 155
    for p_no, p_d in p_steps_en:
        svg.append(f'<rect x="{emx7+20}" y="{py_s_e}" width="350" height="75" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
        svg.append(f'<text x="{emx7+35}" y="{py_s_e+30}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="14" font-weight="700">{escape_xml(p_no)}</text>')
        svg.append(f'<text x="{emx7+35}" y="{py_s_e+52}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="12">{escape_xml(p_d)}</text>')
        py_s_e += 90
    svg.extend(render_en_mobile_footer(emx7, emy7+1060))

    # SCREEN 19: Mobile Dedicated Studio (390 x 1400) - x: 6050, y: 4330
    emx8, emy8 = 6050, 4330
    svg.append(f'<rect x="{emx8}" y="{emy8}" width="390" height="1400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_mobile_header(emx8, emy8))

    svg.append(f'<text x="{emx8+20}" y="{emy8+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">STUDIO ETHOS</text>')
    svg.append(f'<text x="{emx8+20}" y="{emy8+125}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="22" font-weight="700">Studio &amp; Philosophy</text>')

    svg.append(f'<rect x="{emx8+20}" y="{emy8+150}" width="350" height="280" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{emx8+35}" y="{emy8+185}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="16" font-weight="700">Mirpur Studio &amp; Team</text>')
    t_mstd_e, _ = wrap_text("Located in Mirpur-10, FlowGrid practices interior architecture focusing on endurance, natural daylight, and seasoned timber rather than ephemeral ornamentation.", emx8+35, emy8+215, 34, 20, "'Manrope', sans-serif", 13, "#56645E")
    svg.append(t_mstd_e)
    t_mbound_e, _ = wrap_text("Governance note: Rumi's Fashionable House represents family lifestyle inspiration. Architectural design and joinery execution are managed by an independent professional team.", emx8+35, emy8+305, 34, 18, "'Manrope', sans-serif", 12, "#895239")
    svg.append(t_mbound_e)
    svg.extend(render_en_mobile_footer(emx8, emy8+1060))

    # SCREEN 20: Mobile Legal & Privacy Terms (390 x 1400) - x: 6050, y: 5800
    emx9, emy9 = 6050, 5800
    svg.append(f'<rect x="{emx9}" y="{emy9}" width="390" height="1400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_mobile_header(emx9, emy9))

    svg.append(f'<text x="{emx9+20}" y="{emy9+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">LEGAL &amp; PRIVACY</text>')
    svg.append(f'<text x="{emx9+20}" y="{emy9+125}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="20" font-weight="700">Privacy &amp; Design Terms</text>')

    svg.append(f'<rect x="{emx9+20}" y="{emy9+150}" width="350" height="340" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{emx9+35}" y="{emy9+180}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="14" font-weight="700">1. Architectural Visualizations</text>')
    t_lep1, _ = wrap_text("All 3D interior renders are conceptual design studies and AI visual intent models. They do not claim completed commissions for specific clients.", emx9+35, emy9+205, 34, 18, "'Manrope', sans-serif", 12, "#56645E")
    svg.append(t_lep1)
    svg.append(f'<text x="{emx9+35}" y="{emy9+285}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="14" font-weight="700">2. Client Data Protection</text>')
    t_lep2, _ = wrap_text("Personal information submitted in consultation forms is used strictly for design scheduling and never shared with external third parties.", emx9+35, emy9+310, 34, 18, "'Manrope', sans-serif", 12, "#56645E")
    svg.append(t_lep2)
    svg.extend(render_en_mobile_footer(emx9, emy9+1060))

    # -------------------------------------------------------------
    # COLUMN M5 (x = 6520): Mobile Contact & Off-Canvas Drawer Overlay
    # -------------------------------------------------------------
    emx10, emy10 = 6520, 2860
    # SCREEN 21: Mobile Dedicated Contact (390 x 1450)
    svg.append(f'<rect x="{emx10}" y="{emy10}" width="390" height="1450" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_en_mobile_header(emx10, emy10))

    svg.append(f'<text x="{emx10+20}" y="{emy10+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">CONTACT &amp; VISIT</text>')
    svg.append(f'<text x="{emx10+20}" y="{emy10+125}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="22" font-weight="700">Studio Contact</text>')

    svg.append(f'<rect x="{emx10+20}" y="{emy10+150}" width="350" height="490" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    mcfy_e = emy10 + 175
    mcfx_e = emx10 + 35
    mcfw_e = 320

    svg.append(f'<text x="{mcfx_e}" y="{mcfy_e}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600">1. Your Name *</text>')
    svg.append(f'<rect x="{mcfx_e}" y="{mcfy_e+6}" width="{mcfw_e}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{mcfx_e+12}" y="{mcfy_e+35}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">e.g. Farhan Ahmed</text>')
    mcfy_e += 66

    svg.append(f'<text x="{mcfx_e}" y="{mcfy_e}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600">2. Mobile Number *</text>')
    svg.append(f'<rect x="{mcfx_e}" y="{mcfy_e+6}" width="{mcfw_e}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{mcfx_e+12}" y="{mcfy_e+35}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">01XXXXXXXXX</text>')
    mcfy_e += 66

    svg.append(f'<text x="{mcfx_e}" y="{mcfy_e}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600">3. Area &amp; City *</text>')
    svg.append(f'<rect x="{mcfx_e}" y="{mcfy_e+6}" width="{mcfw_e}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{mcfx_e+12}" y="{mcfy_e+35}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">Mirpur / Gulshan / Dhanmondi...</text>')
    mcfy_e += 66

    svg.append(f'<text x="{mcfx_e}" y="{mcfy_e}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600">4. Service Required *</text>')
    svg.append(f'<rect x="{mcfx_e}" y="{mcfy_e+6}" width="{mcfw_e}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{mcfx_e+12}" y="{mcfy_e+35}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="12">Full Interior / Custom Joinery / Not Sure ▼</text>')
    mcfy_e += 66

    svg.append(f'<rect x="{mcfx_e}" y="{mcfy_e+6}" width="{mcfw_e}" height="52" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{mcfx_e+mcfw_e//2}" y="{mcfy_e+38}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">Request Consultation →</text>')

    # Studio Address (Placed directly below form)
    svg.append(f'<rect x="{emx10+20}" y="{emy10+660}" width="350" height="150" fill="#DEE7E2" rx="4"/>')
    svg.append(f'<text x="{emx10+35}" y="{emy10+695}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="16" font-weight="700">Studio Address</text>')
    svg.append(f'<text x="{emx10+35}" y="{emy10+725}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">Mirpur-10, Dhaka 1216, Bangladesh</text>')
    svg.append(f'<text x="{emx10+35}" y="{emy10+750}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">hello@flowgrid-interiors.com · +880 1700-000000</text>')
    # 48px height WhatsApp button
    svg.append(f'<rect x="{emx10+35}" y="{emy10+770}" width="320" height="48" fill="#0D5C52" rx="2"/>')
    svg.append(f'<text x="{emx10+195}" y="{emy10+800}" fill="#FFFFFF" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="600" text-anchor="middle">Start WhatsApp Chat</text>')

    svg.extend(render_en_mobile_footer(emx10, emy10+836))

    # DEDICATED OVERLAY: English Mobile Off-Canvas Navigation Drawer (390 x 750)
    # Placed in its own dedicated position: x: 6520, y: 4380 - ZERO FOOTER COLLISION!
    edx, edy = 6520, 4380
    svg.append(f'<text x="{edx}" y="{edy-15}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="12" font-weight="700">[OFF-CANVAS OVERLAY FRAME — ENGLISH]</text>')
    svg.append(f'<rect x="{edx}" y="{edy}" width="390" height="750" fill="#183B35" rx="4"/>')
    svg.append(f'<text x="{edx+25}" y="{edy+55}" fill="#F4F1E8" font-family="\'Bodoni Moda\', serif" font-size="24" font-weight="700">FlowGrid Studio</text>')
    svg.append(f'<rect x="{edx+330}" y="{edy+30}" width="48" height="48" fill="#102B26" rx="2"/>')
    svg.append(f'<text x="{edx+354}" y="{edy+60}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="20" text-anchor="middle">✕</text>')

    en_drawer_items = [
        ("Home", edy+120),
        ("Projects Archive", edy+175),
        ("Services", edy+230),
        ("Process", edy+285),
        ("Studio & Team", edy+340),
        ("Contact & Visit", edy+395),
        ("Privacy & Terms", edy+450)
    ]
    for d_lbl, d_ly in en_drawer_items:
        svg.append(f'<text x="{edx+30}" y="{d_ly}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="17" font-weight="600">{escape_xml(d_lbl)}</text>')
        svg.append(f'<line x1="{edx+30}" y1="{d_ly+18}" x2="{edx+360}" y2="{d_ly+18}" stroke="#2D524A" stroke-width="1"/>')

    svg.append(f'<rect x="{edx+30}" y="{edy+500}" width="330" height="48" fill="#895239" rx="2"/>')
    svg.append(f'<text x="{edx+195}" y="{edy+530}" fill="#FFFFFF" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">Direct Call: +880 1700-000000</text>')
    svg.append(f'<rect x="{edx+30}" y="{edy+560}" width="330" height="48" fill="#0D5C52" rx="2"/>')
    svg.append(f'<text x="{edx+195}" y="{edy+590}" fill="#FFFFFF" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">Chat on WhatsApp</text>')

    svg.append('</svg>')

    out_path = 'figma_svgs_v3/05_english.svg'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    
    valid, err = validate_svg_file(out_path)
    print(f'Board 05: {out_path} -> Valid XML? {valid} ({err})')

if __name__ == '__main__':
    generate_board_05()
