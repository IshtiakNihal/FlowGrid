"""
FlowGrid - Page 03: Desktop Suite — Bangla (v3)
Complete 1440px Desktop Page Scope:
1. Homepage (/)
2. Projects Archive (/projects)
3. Concept Study Detail (/projects/concept-dhaka-living) - 3 Coherent Views
4. Real-Project Detail Template (/projects/gulshan-residence-01)
5. Dedicated Services Page (/services)
6. Dedicated Service Detail Template (/services/bespoke-joinery)
7. Dedicated Process Page (/process)
8. Dedicated Studio Page (/studio)
9. Dedicated Contact Page (/contact)
10. Privacy & Service Information (/privacy)
11. 404 Error Page (/404)
"""
import os
from svg_utils import wrap_text, escape_xml, validate_svg_file, get_base64_image

def generate_board_03():
    # Load base64 concept images
    img_living = get_base64_image('concepts/concept_01_living_dhaka.jpg')
    img_living_alt = get_base64_image('concepts/concept_01_living_alt.jpg')
    img_joinery = get_base64_image('concepts/concept_01_joinery_detail.jpg')
    img_kitchen = get_base64_image('concepts/concept_02_kitchen_dhaka.jpg')
    img_bedroom = get_base64_image('concepts/concept_03_bedroom_dhaka.jpg')

    # Canvas: 4 Columns of 1440px screens with 160px gutters
    # Total width: 80 + 4 * 1440 + 3 * 160 + 80 = 6480
    # Rows: 3 rows of screens, height ~7200
    w, h = 6480, 7200
    svg = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{w}" height="{h}" fill="#F4F1E8"/>')

    # Header Banner
    svg.append('<rect x="80" y="80" width="6320" height="140" fill="#183B35" rx="4"/>')
    svg.append('<text x="120" y="145" fill="#F4F1E8" font-family="\'Bodoni Moda\', serif" font-size="36" font-weight="600">FlowGrid — Desktop Experience Suite · Bangla (1440px Master Screens · v3)</text>')
    svg.append('<text x="120" y="185" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="18">Complete architectural templates: Homepage, Projects Archive, 3-View Concept Study, Built-Project Template, Services, Process, Studio, Contact, Privacy, and 404</text>')

    # Helper: Desktop Global Header (88px)
    def render_desktop_header(x, y, active_page=""):
        res = []
        res.append(f'<rect x="{x}" y="{y}" width="1440" height="88" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
        res.append(f'<text x="{x+80}" y="{y+55}" fill="#183B35" font-family="\'Bodoni Moda\', serif" font-size="28" font-weight="700">FlowGrid</text>')
        res.append(f'<text x="{x+210}" y="{y+55}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="12" font-weight="700">STUDIO</text>')

        menu_items = [
            ("প্রচ্ছদ", x+380, "home"),
            ("প্রকল্পসমূহ", x+480, "projects"),
            ("সেবাসমূহ", x+610, "services"),
            ("পদ্ধতি", x+730, "process"),
            ("স্টুডিও", x+830, "studio"),
            ("যোগাযোগ", x+930, "contact")
        ]
        for label, mx, pid in menu_items:
            color = "#183B35" if pid != active_page else "#895239"
            weight = "600" if pid != active_page else "700"
            res.append(f'<text x="{mx}" y="{y+54}" fill="{color}" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="{weight}">{escape_xml(label)}</text>')
            if pid == active_page:
                res.append(f'<line x1="{mx}" y1="{y+62}" x2="{mx+len(label)*12}" y2="{y+62}" stroke="#895239" stroke-width="2"/>')

        # Language Switch & CTA (Min 48px touch target)
        res.append(f'<rect x="{x+1180}" y="{y+20}" width="50" height="48" fill="#DEE7E2" rx="2"/>')
        res.append(f'<text x="{x+1205}" y="{y+50}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700" text-anchor="middle">EN</text>')
        res.append(f'<rect x="{x+1245}" y="{y+20}" width="125" height="48" fill="#183B35" rx="2"/>')
        res.append(f'<text x="{x+1307}" y="{y+50}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600" text-anchor="middle">পরামর্শ নিন</text>')
        return res

    # Helper: Desktop Global Footer
    def render_desktop_footer(x, y):
        res = []
        res.append(f'<rect x="{x}" y="{y}" width="1440" height="280" fill="#183B35"/>')
        res.append(f'<text x="{x+80}" y="{y+70}" fill="#F4F1E8" font-family="\'Bodoni Moda\', serif" font-size="32" font-weight="700">FlowGrid Studio</text>')
        t_foot, _ = wrap_text("ঢাকার শহুরে অ্যাপার্টমেন্টের জন্য ব্যবহারিক, শান্ত ও টেকসই ইন্টেরিয়র আর্কিটেকচার এবং কাস্টম কেবিনেটরি।", x+80, y+105, 45, 22, "'Noto Sans Bengali', sans-serif", 14, "#DEE7E2")
        res.append(t_foot)

        # Col 2: Navigation
        res.append(f'<text x="{x+540}" y="{y+70}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">পৃষ্ঠাসমূহ</text>')
        links = ["প্রচ্ছদ (Home)", "প্রকল্পসমূহ (Projects)", "সেবাসমূহ (Services)", "পদ্ধতি (Process)", "স্টুডিও ও দল (Studio)"]
        ly = y + 100
        for l in links:
            res.append(f'<text x="{x+540}" y="{ly}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">{escape_xml(l)}</text>')
            ly += 24

        # Col 3: Direct Contact
        res.append(f'<text x="{x+820}" y="{y+70}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">স্টুডিও যোগাযোগ</text>')
        res.append(f'<text x="{x+820}" y="{y+100}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">মিরপুর-১০, ঢাকা ১২১৬, বাংলাদেশ</text>')
        res.append(f'<text x="{x+820}" y="{y+124}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="13">হটলাইন: +880 1700-000000</text>')
        res.append(f'<text x="{x+820}" y="{y+148}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="13">ইমেইল: hello@flowgrid-interiors.com</text>')
        res.append(f'<text x="{x+820}" y="{y+172}" fill="#DEE7E2" font-family="\'Noto Sans Bengali\', sans-serif" font-size="12">প্রাইভেসি পলিসি ও শর্তাবলী</text>')

        # Col 4: Sibling Context (Clear Boundaries)
        res.append(f'<text x="{x+1120}" y="{y+70}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">কমিউনিটি ও পার্টনার</text>')
        res.append(f'<text x="{x+1120}" y="{y+100}" fill="#DEE7E2" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">রুমী\'স ফ্যাশনেবল হাউস (লাইফস্টাইল ভ্লগ)</text>')
        res.append(f'<text x="{x+1120}" y="{y+124}" fill="#DEE7E2" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">অনেকটা প্রোডাক্ট (গৃহস্থালি সামগ্রী)</text>')
        res.append(f'<text x="{x+1120}" y="{y+160}" fill="#C4D1CA" font-family="\'Noto Sans Bengali\', sans-serif" font-size="11">স্বতন্ত্র স্থাপত্য অনুশীলন ও ব্র্যান্ড সীমানা</text>')

        # Copyright bar
        res.append(f'<line x1="{x+80}" y1="{y+220}" x2="{x+1360}" y2="{y+220}" stroke="#2D524A" stroke-width="1"/>')
        res.append(f'<text x="{x+80}" y="{y+250}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="12">© 2026 FlowGrid Interior Studio. All rights reserved. Dhaka, Bangladesh.</text>')
        res.append(f'<text x="{x+1360}" y="{y+250}" fill="#DEE7E2" font-family="\'Noto Sans Bengali\', sans-serif" font-size="12" text-anchor="end">সত্যনিষ্ঠ কনসেপ্ট ভিজ্যুয়ালাইজেশন নীতি অনুসরণীয়</text>')
        return res

    # -------------------------------------------------------------
    # SCREEN 1: Homepage (/) - x: 80, y: 260, h: 2200
    # -------------------------------------------------------------
    sx1, sy1 = 80, 260
    svg.append(f'<rect x="{sx1}" y="{sy1}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_desktop_header(sx1, sy1, "home"))

    # Hero Section
    svg.append(f'<text x="{sx1+80}" y="{sy1+160}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">DHAKA INTERIOR ARCHITECTURE &amp; MILLWORK</text>')
    t_h1, _ = wrap_text("দৈনন্দিন জীবনের শান্ত ও সুবিন্যস্ত স্থাপত্য", sx1+80, sy1+215, 26, 56, "'Noto Sans Bengali', sans-serif", 46, "#183B35", 700)
    svg.append(t_h1)
    t_hsub, _ = wrap_text("ঢাকার বাস্তবতায় পরিমিত পরিসরে খোলামেলা আলোর পরিবেশ, দীর্ঘস্থায়ী বার্মা সেগুন কাঠ এবং সুপরিকল্পিত স্টোরেজের মেলবন্ধন।", sx1+80, sy1+320, 50, 26, "'Noto Sans Bengali', sans-serif", 17, "#56645E")
    svg.append(t_hsub)

    # Hero Actions
    svg.append(f'<rect x="{sx1+80}" y="{sy1+385}" width="190" height="52" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{sx1+175}" y="{sy1+418}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="600" text-anchor="middle">পরামর্শ বুক করুন →</text>')
    svg.append(f'<rect x="{sx1+290}" y="{sy1+385}" width="170" height="52" fill="transparent" stroke="#183B35" stroke-width="1.5" rx="2"/>')
    svg.append(f'<text x="{sx1+375}" y="{sy1+418}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="600" text-anchor="middle">প্রকল্প গ্যালারি</text>')

    # Hero Image Card with Strict Truth Tag
    if img_living:
        svg.append(f'<image href="{img_living}" x="{sx1+80}" y="{sy1+470}" width="1280" height="620" preserveAspectRatio="xMidYMid slice"/>')
    else:
        svg.append(f'<rect x="{sx1+80}" y="{sy1+470}" width="1280" height="620" fill="#183B35"/>')
    
    # Truth Disclosure Tag on Hero (Properly sized 460px width for 55 Bangla characters)
    svg.append(f'<rect x="{sx1+100}" y="{sy1+490}" width="460" height="34" fill="#183B35" fill-opacity="0.9" rx="2"/>')
    svg.append(f'<text x="{sx1+120}" y="{sy1+512}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>')

    # Section: Philosophy & Approach
    svg.append(f'<rect x="{sx1+80}" y="{sy1+1130}" width="1280" height="260" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{sx1+120}" y="{sy1+1175}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">OUR PHILOSOPHY</text>')
    svg.append(f'<text x="{sx1+120}" y="{sy1+1210}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="24" font-weight="700">ব্যবহারিক পরিসর ও খাঁটি উপকরণের মেলবন্ধন</text>')
    t_ap1, _ = wrap_text("ঢাকার অ্যাপার্টমেন্টে পর্যাপ্ত স্টোরেজ ও মুক্ত চলাচলের স্থান নিশ্চিত করাই আমাদের প্রধান লক্ষ্য। অতিরিক্ত কৃত্রিম জাঁকজমক পরিহার করে প্রাকৃতিক কাঠ, রড-আয়রন ও স্থানীয় বেতের কাজের মাধ্যমে দীর্ঘস্থায়ী গৃহকোণ গড়ে তুলি।", sx1+120, sy1+1250, 75, 24, "'Noto Sans Bengali', sans-serif", 15, "#56645E")
    svg.append(t_ap1)

    # Section: Featured Projects Grid Preview
    svg.append(f'<text x="{sx1+80}" y="{sy1+1440}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="28" font-weight="700">নির্বাচিত কনসেপ্ট স্টাডিজ</text>')
    svg.append(f'<text x="{sx1+80}" y="{sy1+1470}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15">ঢাকার বিভিন্ন আবাসিক এলাকার উপযোগী স্থাপত্য পরিকল্পনা</text>')

    # 3 Cards (Captioned strictly by visible features of 1376x768 concept renders)
    cards = [
        ("গুলশান লেকভিউ লিভিং ও ব্যালকনি স্টাডি", "সেগুন কাঠের স্ল্যাট মিডিয়া ওয়াল ও উন্মুক্ত আলো", img_living, sx1+80),
        ("রেজিলিয়েন্ট অ্যাপার্টমেন্ট কিচেন স্টাডি", "ভারী রান্নার উপযোগী গ্রানাইট কাউন্টারটপ ও ডাক্টেড হুড", img_kitchen, sx1+520),
        ("মাস্টার বেডরুম ও ফ্লুটেড হেডবোর্ড স্টাডি", "ভাসমান সেগুন প্ল্যাটফর্ম বেড ও পরিমিত কোভ লাইটিং", img_bedroom, sx1+960)
    ]
    for c_title, c_sub, c_img, cx in cards:
        svg.append(f'<rect x="{cx}" y="{sy1+1500}" width="400" height="380" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
        if c_img:
            svg.append(f'<image href="{c_img}" x="{cx}" y="{sy1+1500}" width="400" height="230" preserveAspectRatio="xMidYMid slice"/>')
        else:
            svg.append(f'<rect x="{cx}" y="{sy1+1500}" width="400" height="230" fill="#DEE7E2"/>')
        
        # Disclosure on card
        svg.append(f'<rect x="{cx+10}" y="{sy1+1510}" width="260" height="24" fill="#183B35" fill-opacity="0.9" rx="2"/>')
        svg.append(f'<text x="{cx+20}" y="{sy1+1526}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="11">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>')

        svg.append(f'<text x="{cx+15}" y="{sy1+1760}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="16" font-weight="700">{escape_xml(c_title)}</text>')
        t_csub, _ = wrap_text(c_sub, cx+15, sy1+1785, 32, 18, "'Noto Sans Bengali', sans-serif", 13, "#56645E")
        svg.append(t_csub)
        svg.append(f'<text x="{cx+15}" y="{sy1+1850}" fill="#895239" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600">সম্পূর্ণ স্টাডি দেখুন →</text>')

    svg.extend(render_desktop_footer(sx1, sy1+1920))

    # -------------------------------------------------------------
    # SCREEN 2: Projects Archive (/projects) - x: 1680, y: 260, h: 2200
    # -------------------------------------------------------------
    sx2, sy2 = 1680, 260
    svg.append(f'<rect x="{sx2}" y="{sy2}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_desktop_header(sx2, sy2, "projects"))

    svg.append(f'<text x="{sx2+80}" y="{sy2+150}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">PROJECTS &amp; CONCEPT ARCHIVE</text>')
    svg.append(f'<text x="{sx2+80}" y="{sy2+195}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="36" font-weight="700">স্থাপত্য পরিকল্পনা ও কনসেপ্ট গ্যালারি</text>')
    t_arch_desc, _ = wrap_text("ঢাকার বাস্তবতায় মধ্যবিত্ত ও উচ্চ-মধ্যবিত্ত পরিবারের অ্যাপার্টমেন্ট স্পেসের সমন্বিত ডিজাইন সমাধান। সকল 3D রেন্ডার স্বাধীন কনসেপ্ট স্টাডি হিসেবে উপস্থাপিত।", sx2+80, sy2+235, 75, 22, "'Noto Sans Bengali', sans-serif", 16, "#56645E")
    svg.append(t_arch_desc)

    # Filter Tabs (48px ergonomic touch target height)
    tabs = [("সকল প্রকল্প (All)", True), ("লিভিং ও ড্রয়িং", False), ("রান্নাঘর ও প্যান্ট্রি", False), ("বেডরুম ও স্টাডি", False), ("কাস্টম মিলওয়ার্ক", False)]
    tx = sx2 + 80
    for t_name, is_act in tabs:
        t_bg = "#183B35" if is_act else "#DEE7E2"
        t_col = "#F4F1E8" if is_act else "#183B35"
        svg.append(f'<rect x="{tx}" y="{sy2+280}" width="160" height="48" fill="{t_bg}" rx="2"/>')
        svg.append(f'<text x="{tx+80}" y="{sy2+310}" fill="{t_col}" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600" text-anchor="middle">{escape_xml(t_name)}</text>')
        tx += 175

    # 4 Detailed Archive Cards (2x2 Grid)
    arch_cards = [
        ("গুলশান লেকভিউ অ্যাপার্টমেন্ট স্টাডি", "আবাসিক লিভিং ও ফার্নিচার বিন্যাস", img_living, sx2+80, sy2+350, "৩টি ভিউ সমন্বিত স্টাডি"),
        ("রেজিলিয়েন্ট কিচেন ও প্যান্ট্রি স্টাডি", "গ্রানাইট কাউন্টার ও সিলিন্ডার ভেন্টিলেশন", img_kitchen, sx2+740, sy2+350, "রান্নাঘর স্পেসিফিকেশন"),
        ("মাস্টার বেডরুম ও হোম অফিস অ্যালকোভ", "সেগুন কাঠ ও বেতের প্যানেল ওয়ারড্রব", img_bedroom, sx2+80, sy2+1020, "বেডরুম ও স্টাডি বিন্যাস"),
        ("বার্মা সেগুন কাঠ ও বেতের সূক্ষ্ম জয়েনারি", "টেকসই কাঠের কাজ ও হ্যান্ডক্রাফটেড ফিনিশ", img_joinery, sx2+740, sy2+1020, "ম্যাটেরিয়াল ডিটেইল স্টাডি")
    ]
    for a_title, a_sub, a_img, ax, ay, a_tag in arch_cards:
        svg.append(f'<rect x="{ax}" y="{ay}" width="620" height="630" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
        if a_img:
            svg.append(f'<image href="{a_img}" x="{ax}" y="{ay}" width="620" height="420" preserveAspectRatio="xMidYMid slice"/>')
        else:
            svg.append(f'<rect x="{ax}" y="{ay}" width="620" height="420" fill="#DEE7E2"/>')
        
        # Disclosure
        svg.append(f'<rect x="{ax+15}" y="{ay+15}" width="320" height="28" fill="#183B35" fill-opacity="0.9" rx="2"/>')
        svg.append(f'<text x="{ax+25}" y="{ay+34}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="12">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত নয়</text>')

        svg.append(f'<text x="{ax+24}" y="{ay+465}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">{escape_xml(a_tag)}</text>')
        svg.append(f'<text x="{ax+24}" y="{ay+495}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="20" font-weight="700">{escape_xml(a_title)}</text>')
        t_asub, _ = wrap_text(a_sub, ax+24, ay+525, 45, 20, "'Noto Sans Bengali', sans-serif", 14, "#56645E")
        svg.append(t_asub)
        svg.append(f'<text x="{ax+24}" y="{ay+595}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="700">বিস্তারিত কেস স্টাডি দেখুন →</text>')

    svg.extend(render_desktop_footer(sx2, sy2+1920))

    # -------------------------------------------------------------
    # SCREEN 3: Concept Study Detail (/projects/concept-dhaka-living) - x: 3280, y: 260, h: 2200
    # 3 Coherent Spatial Views: Living Hero, Dining & Veranda, Joinery Detail
    # -------------------------------------------------------------
    sx3, sy3 = 3280, 260
    svg.append(f'<rect x="{sx3}" y="{sy3}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_desktop_header(sx3, sy3, "projects"))

    svg.append(f'<text x="{sx3+80}" y="{sy3+140}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">CASE STUDY · CONCEPT 01 (3 COHERENT SPATIAL VIEWS)</text>')
    svg.append(f'<text x="{sx3+80}" y="{sy3+185}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="34" font-weight="700">গুলশান লেকভিউ অ্যাপার্টমেন্ট স্টাডি — ৩টি দৃশ্যপট</text>')

    # 3 Views Row (Accurately captioned from new 1376x768 imagery)
    views = [
        ("ভিউ ১: লিভিং স্পেস ও সেগুন স্ল্যাট মিডিয়া ওয়াল", img_living, sx3+80, 620),
        ("ভিউ ২: সংযুক্ত ডাইনিং ও ব্যালকনির বিকেল আলো", img_living_alt, sx3+720, 620),
    ]
    for v_title, v_img, vx, vw in views:
        svg.append(f'<rect x="{vx}" y="{sy3+215}" width="{vw}" height="380" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
        if v_img:
            svg.append(f'<image href="{v_img}" x="{vx}" y="{sy3+215}" width="{vw}" height="340" preserveAspectRatio="xMidYMid slice"/>')
        svg.append(f'<text x="{vx+15}" y="{sy3+580}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="600">{escape_xml(v_title)}</text>')

    # View 3: Macro Joinery Detail
    svg.append(f'<rect x="{sx3+80}" y="{sy3+615}" width="1280" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
    if img_joinery:
        svg.append(f'<image href="{img_joinery}" x="{sx3+80}" y="{sy3+615}" width="540" height="420" preserveAspectRatio="xMidYMid slice"/>')
    svg.append(f'<text x="{sx3+650}" y="{sy3+660}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">VIEW 3: MATERIAL &amp; JOINERY DETAIL</text>')
    svg.append(f'<text x="{sx3+650}" y="{sy3+695}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="22" font-weight="700">সলিড সেগুন কাঠ ও ব্রাশড সাটিন ব্রাস ইনলে জয়েনারি</text>')
    t_v3_desc, _ = wrap_text("হস্তনির্মিত ল্যাপ জয়েন্ট ও ব্রাশড সাটিন ব্রাস ইনলে চ্যানেল। উদ্ভিজ্জ তেলের ম্যাট পলিশ কাঠের স্বাভাবিক আঁশ ও দীর্ঘস্থায়িত্ব বজায় রাখে। সফট-ক্লোজ জার্মান হিঞ্জ দীর্ঘ বহু বছর মসৃণ ব্যবহারের নিশ্চয়তা দেয়।", sx3+650, sy3+735, 45, 22, "'Noto Sans Bengali', sans-serif", 15, "#56645E")
    svg.append(t_v3_desc)

    # 3 Spatial Decisions
    svg.append(f'<rect x="{sx3+80}" y="{sy3+1060}" width="1280" height="340" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<rect x="{sx3+80}" y="{sy3+1060}" width="1280" height="50" fill="#183B35" rx="4 4 0 0"/>')
    svg.append(f'<text x="{sx3+110}" y="{sy3+1092}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="18" font-weight="600">৩টি প্রধান স্থাপত্য ও স্থানিক সিদ্ধান্ত (Spatial Decisions)</text>')

    decisions = [
        ("১. সমন্বিত মিডিয়া ওয়াল ও স্ল্যাট প্যানেল", "ভার্টিক্যাল সেগুন কাঠের স্ল্যাট প্যানেল ও ফ্লোটিং মিডিয়া কনসোল। ওয়্যারিং ও গ্যাজেট আড়াল করে নিরবচ্ছিন্ন স্থাপত্যিক দেয়াল প্রতিষ্ঠা।"),
        ("২. বারান্দার আলো ও ক্রস-ভেন্টিলেশন", "লিভিং ও ডাইনিংয়ের মাঝখানে উন্মুক্ত করিডোর যাতে দক্ষিণ-পশ্চিমের বারান্দা থেকে আসা আলো সম্পূর্ণ স্পেসে পৌঁছায়।"),
        ("৩. খাঁটি সেগুন ও মেটাল ইনলে অ্যাকসেন্ট", "প্রাকৃতিক সিজনড কাঠ ও সূক্ষ্ম ব্রাস চ্যানেলের মেলবন্ধন যা আধুনিক অ্যাপার্টমেন্টে পরিশীলিত রূপ দেয়।")
    ]
    dx = sx3 + 110
    for d_title, d_desc in decisions:
        svg.append(f'<text x="{dx}" y="{sy3+1145}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="16" font-weight="700">{escape_xml(d_title)}</text>')
        td_desc, _ = wrap_text(d_desc, dx, sy3+1175, 34, 22, "'Noto Sans Bengali', sans-serif", 14, "#56645E")
        svg.append(td_desc)
        dx += 420

    # Material Specs Table & Assumed Brief Notice
    svg.append(f'<rect x="{sx3+80}" y="{sy3+1430}" width="1280" height="440" fill="#DEE7E2" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{sx3+110}" y="{sy3+1470}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="20" font-weight="700">উপকরণ বিবরণী ও স্টাডি স্পেসিফিকেশন (Material Specs)</text>')
    t_hypo, _ = wrap_text("অনুসিদ্ধান্ত ও কনসেপ্ট শর্ত: এই স্টাডিটি ঢাকার একটি আনুমানিক ১৮০০-২১৫০ বর্গফুটের ফ্ল্যাটের ওপর প্রণীত। বাস্তবায়িত নির্মাণ নয়।", sx3+110, sy3+1505, 80, 20, "'Noto Sans Bengali', sans-serif", 13, "#895239")
    svg.append(t_hypo)

    m_specs = [
        ("প্রধান কাঠামোগত কাঠ", "ম্যাসিভ বার্মা সেগুন কাঠ (Burma Teak) · সিজনড ও তেল ফিনিশ"),
        ("কেবিনেট ডোর প্যানেল", "সিলেটের হাতে বোনা প্রাকৃতিক বেত (Handwoven Sylhet Cane) · ভেন্টিলেটেড"),
        ("কাউন্টারটপ ও সারফেস", "২০ মিমি প্রাকৃতিক গ্রানাইট স্ল্যাব · ম্যাট হোনড ফিনিশ · দাগ প্রতিরোধক"),
        ("দেয়ালের টেক্সচার", "ন্যাচারাল লাইম প্লাস্টার (Chuna Polish) · নন-টক্সিক ও শ্বাসপ্রশ্বাসের উপযোগী"),
        ("হার্ডওয়্যার ও কব্জা", "সফট-ক্লোজ হিঞ্জেস ও কনসিলড ফুল-এক্সটেনশন চ্যানেল")
    ]
    my = sy3 + 1545
    for s_name, s_val in m_specs:
        svg.append(f'<text x="{sx3+110}" y="{my}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="700">{escape_xml(s_name)}:</text>')
        svg.append(f'<text x="{sx3+350}" y="{my}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14">{escape_xml(s_val)}</text>')
        my += 34

    svg.append(f'<rect x="{sx3+110}" y="{sy3+1760}" width="240" height="52" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{sx3+230}" y="{sy3+1792}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="600" text-anchor="middle">এই ডিজাইনে পরামর্শ নিন →</text>')

    svg.extend(render_desktop_footer(sx3, sy3+1920))

    # -------------------------------------------------------------
    # SCREEN 4: Built-Project Detail Template (/projects/gulshan-residence-01) - x: 4880, y: 260, h: 2200
    # Dedicated architectural template with photography slots, spatial brief, material specifications, and honest placeholder notice
    # -------------------------------------------------------------
    sx4, sy4 = 4880, 260
    svg.append(f'<rect x="{sx4}" y="{sy4}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_desktop_header(sx4, sy4, "projects"))

    svg.append(f'<text x="{sx4+80}" y="{sy4+140}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">COMPLETED RESIDENTIAL TEMPLATE · ARCHITECTURAL SPECIFICATION</text>')
    svg.append(f'<text x="{sx4+80}" y="{sy4+185}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="34" font-weight="700">বাস্তবায়িত প্রকল্প ফ্রেমওয়ার্ক ও ফটোগ্রাফি টেমপ্লেট</text>')

    # Honest Real-Project Template Notice Banner (Properly bounded, zero overflow!)
    svg.append(f'<rect x="{sx4+80}" y="{sy4+215}" width="1280" height="105" fill="#DEE7E2" stroke="#183B35" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{sx4+110}" y="{sy4+245}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="700">বাস্তবায়িত প্রকল্প ফ্রেমওয়ার্ক কাঠামো (Real-Project Commission Template):</text>')
    t_temp_desc, _ = wrap_text("এই ফ্রেমওয়ার্কটি সম্পূর্ণ বাস্তবায়িত আবাসিক কাজের ফটোগ্রাফি, ক্লায়েন্টের আসল রিকোয়ারমেন্ট, ফ্লোর প্ল্যান ও সাইট পরিদর্শনের তথ্য প্রদর্শনের জন্য প্রস্তুত রাখা হয়েছে। নির্মাণ সমাপ্তির পর মূল ছবি এখানে প্রতিস্থাপিত হবে।", sx4+110, sy4+270, 78, 20, "'Noto Sans Bengali', sans-serif", 13, "#56645E")
    svg.append(t_temp_desc)

    # Photography Placeholder Grid (Hero + 3 Details)
    svg.append(f'<rect x="{sx4+80}" y="{sy4+335}" width="800" height="450" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
    svg.append(f'<rect x="{sx4+90}" y="{sy4+345}" width="780" height="430" fill="#DEE7E2"/>')
    svg.append(f'<text x="{sx4+480}" y="{sy4+550}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="18" font-weight="600" text-anchor="middle">[ বাস্তবায়িত আবাসিক লিভিং ও ড্রয়িং ফটোগ্রাফি স্লট ]</text>')
    svg.append(f'<text x="{sx4+480}" y="{sy4+580}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" text-anchor="middle">High-Resolution Architectural Photography (1920 × 1080px)</text>')

    # 3 Detail Slots on Right
    d_slots = [
        ("কেবিনেটরি ডিটেইল ও কাটিং ফিনিশ", sy4+335),
        ("ডাইনিং টেবিল ও কাঠের জয়েন্ট", sy4+490),
        ("ইনডোর প্ল্যান্টস ও লাইটিং ডিটেইল", sy4+645)
    ]
    for d_name, dy in d_slots:
        svg.append(f'<rect x="{sx4+910}" y="{dy}" width="450" height="135" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
        svg.append(f'<rect x="{sx4+920}" y="{dy+10}" width="180" height="115" fill="#DEE7E2"/>')
        svg.append(f'<text x="{sx4+1010}" y="{dy+70}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="12" text-anchor="middle">[ Photo ]</text>')
        svg.append(f'<text x="{sx4+1120}" y="{dy+50}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="700">{escape_xml(d_name)}</text>')
        svg.append(f'<text x="{sx4+1120}" y="{dy+80}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="12">প্রকৃত সাইট শট ও ক্লায়েন্ট এপ্রুভাল</text>')

    # Project Summary & Specifications (Fictional Framework Placeholders)
    svg.append(f'<rect x="{sx4+80}" y="{sy4+810}" width="1280" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<rect x="{sx4+80}" y="{sy4+810}" width="1280" height="50" fill="#183B35" rx="4 4 0 0"/>')
    svg.append(f'<text x="{sx4+110}" y="{sy4+842}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="18" font-weight="600">প্রকল্প পরিচিতি ও স্থাপত্য বিশ্লেষণ (Project Parameters — Sample Framework)</text>')

    params = [
        ("প্রকল্পের ধরন", "[আবাসিক ইন্টেরিয়র ও কাস্টম কাঠের কাজ — ফ্রেমওয়ার্ক কাঠামো]"),
        ("অবস্থান", "[প্রকল্প এলাকা / অবস্থান — যেমন: মিরপুর ডিওএইচএস / গুলশান / ধানমন্ডি]"),
        ("পরিমাপ ও আয়তন", "[পরিমাপ ও আয়তন — উদা: ২০০০-২৫০০ বর্গফুট (৪ বেডরুম ও স্টাডি)]"),
        ("বাস্তবায়ন সময়সীমা", "[প্রকল্প সময়সীমা — আনুমানিক ১২-১৬ সপ্তাহ (সাইট প্রস্তুতি সাপেক্ষে)]"),
        ("ব্যবহৃত উপাদান", "[ব্যবহৃত উপাদান — সিজনড সলিড কাঠ, ন্যাচারাল ভিনিয়ার ও ব্রাস হার্ডওয়্যার]")
    ]
    py = sy4 + 890
    for p_label, p_val in params:
        svg.append(f'<text x="{sx4+110}" y="{py}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="700">{escape_xml(p_label)}:</text>')
        svg.append(f'<text x="{sx4+280}" y="{py}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15">{escape_xml(p_val)}</text>')
        py += 40

    t_pdesc, _ = wrap_text("স্থানিক চ্যালেঞ্জ ও ক্লায়েন্ট রিকোয়ারমেন্ট কাঠামো: পরিবারের লাইফস্টাইল, বুকশেলফ স্টোরেজ ও শিশুদের খোলামেলা চলাচলের স্পেস অপ্টিমাইজেশন বিশ্লেষণ। আর্কিটেকচারাল সাইট সার্ভে ও ড্রয়িং চূড়ান্তকরণের পর মূল স্পেসিফিকেশন সন্নিবেশিত হবে।", sx4+110, py+20, 80, 22, "'Noto Sans Bengali', sans-serif", 14, "#183B35")
    svg.append(t_pdesc)

    # Next Project CTA
    svg.append(f'<rect x="{sx4+80}" y="{sy4+1260}" width="1280" height="160" fill="#DEE7E2" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{sx4+120}" y="{sy4+1315}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="22" font-weight="700">আপনার অ্যাপার্টমেন্টের জন্য কাস্টম পরিকল্পনা চান?</text>')
    svg.append(f'<text x="{sx4+120}" y="{sy4+1355}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15">আমাদের স্টুডিওর সাথে প্রাথমিক স্পেস কনসালটেশনের জন্য যোগাযোগ করুন।</text>')
    svg.append(f'<rect x="{sx4+1120}" y="{sy4+1310}" width="200" height="52" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{sx4+1220}" y="{sy4+1342}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="600" text-anchor="middle">যোগাযোগ করুন →</text>')

    svg.extend(render_desktop_footer(sx4, sy4+1920))

    # -------------------------------------------------------------
    # ROW 2 OF SCREENS (y: 2560)
    # SCREEN 5: Dedicated Services Page (/services) - x: 80, y: 2560
    # SCREEN 6: Dedicated Service Detail Template (/services/bespoke-joinery) - x: 1680, y: 2560
    # SCREEN 7: Dedicated Process Page (/process) - x: 3280, y: 2560
    # SCREEN 8: Dedicated Studio Page (/studio) - x: 4880, y: 2560
    # -------------------------------------------------------------

    # SCREEN 5: Dedicated Services (/services)
    sx5, sy5 = 80, 2560
    svg.append(f'<rect x="{sx5}" y="{sy5}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_desktop_header(sx5, sy5, "services"))

    svg.append(f'<text x="{sx5+80}" y="{sy5+150}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="14" font-weight="700">ARCHITECTURAL SERVICES &amp; EXPERTISE</text>')
    svg.append(f'<text x="{sx5+80}" y="{sy5+195}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="36" font-weight="700">আমাদের সেবাসমূহ ও স্থাপত্য সহযোগিতা</text>')
    t_s5_sub, _ = wrap_text("পরিমিত পরিকল্পনা থেকে অভিজ্ঞ কারিগরি তত্ত্বাবধান—প্রতিটি ধাপে স্বচ্ছতা ও উপাদানের সততা আমাদের কাজের মূলভিত্তি।", sx5+80, sy5+235, 75, 22, "'Noto Sans Bengali', sans-serif", 16, "#56645E")
    svg.append(t_s5_sub)

    # 3 Full Ruled Services
    svcs = [
        ("০১", "পূর্ণাঙ্গ ইন্টেরিয়র আর্কিটেকচার (Full Interior Architecture)",
         "সম্পূর্ণ অ্যাপার্টমেন্টের স্থানিক বিন্যাস, দেয়াল রূপান্তর, ইলেকট্রিক্যাল লেআউট, ফলস সিলিং পরিহার করে পরিচ্ছন্ন লাইটিং ও প্রতিটি রুমের স্থাপত্য সমাধান।",
         ["• টু-ডি ফ্লোর প্ল্যান ও ফার্নিচার লেআউট ড্রয়িং", "• লাইটিং, সুইচবোর্ড ও সেনিটারি পজিশনিং গাইড", "• থ্রি-ডি ভিজ্যুয়ালাইজেশন ও ম্যাটেরিয়াল স্পেক্স", "• সাইট সুপারভিশন ও মান নিয়ন্ত্রণ"]),
        ("০২", "কাস্টম ফার্নিচার ও মিলওয়ার্ক (Bespoke Joinery & Cabinetry)",
         "ফ্লোর-টু-সিলিং বুকশেলফ, টিভি ইউনিট, ওয়াক-ইন ক্লোজেট ও রান্নাঘরের টেকসই কেবিনেটরি। দক্ষ কারিগরদের তত্ত্বাবধানে সিজনড কাঠ দিয়ে নিখুঁত ফিনিশিং।",
         ["• বার্মা সেগুন, গর্জন ও ওক কাঠের কাজ", "• আর্দ্রতা প্রতিরোধী বেতের প্যানেল", "• সফট-ক্লোজ জার্মান হার্ডওয়্যার ফিটিংস", "• সাইটে নিখুঁত ইনস্টলেশন ও লেভেলিং"]),
        ("০৩", "স্থান বিন্যাস ও ড্রয়িং কনসালটেশন (Spatial Planning & Drawings)",
         "যাঁরা নিজেরাই কাজ বাস্তবায়ন করতে চান, তাঁদের জন্য বিশদ টু-ডি ওয়ার্কিং ড্রয়িং, ইলেকট্রিক্যাল লেআউট ও ম্যাটেরিয়াল কোটেশন (BOQ) প্রস্তুতকরণ।",
         ["• বিশদ পরিমাপ ও আর্কিটেকচারাল ব্লুপ্রিন্ট", "• কাঠমিস্ত্রি ও ইলেকট্রিশিয়ানের এক্সিকিউশন শিট", "• আনুমানিক বাজারদর ও কাঠের পরিমাপ শিট", "• পরামর্শ সেশন ও ডিজাইন রিভিউ"])
    ]
    sv_y = sy5 + 320
    for s_no, s_tit, s_body, s_points in svcs:
        svg.append(f'<rect x="{sx5+80}" y="{sv_y}" width="1280" height="380" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
        svg.append(f'<text x="{sx5+120}" y="{sv_y+55}" fill="#895239" font-family="\'Bodoni Moda\', serif" font-size="32" font-weight="700">{s_no}</text>')
        svg.append(f'<text x="{sx5+180}" y="{sv_y+52}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="22" font-weight="700">{escape_xml(s_tit)}</text>')
        
        t_sb, _ = wrap_text(s_body, sx5+120, sv_y+95, 75, 22, "'Noto Sans Bengali', sans-serif", 15, "#56645E")
        svg.append(t_sb)

        # Points
        px = sx5 + 120
        py = sv_y + 175
        for p in s_points:
            svg.append(f'<text x="{px}" y="{py}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="600">{escape_xml(p)}</text>')
            py += 26

        svg.append(f'<rect x="{sx5+120}" y="{sv_y+300}" width="180" height="46" fill="#183B35" rx="2"/>')
        svg.append(f'<text x="{sx5+210}" y="{sv_y+329}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">সেবাটি নির্বাচন করুন →</text>')
        sv_y += 420

    svg.extend(render_desktop_footer(sx5, sy5+1920))

    # SCREEN 6: Service Detail Template (/services/bespoke-joinery)
    sx6, sy6 = 1680, 2560
    svg.append(f'<rect x="{sx6}" y="{sy6}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_desktop_header(sx6, sy6, "services"))

    svg.append(f'<text x="{sx6+80}" y="{sy6+140}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">SERVICE DETAIL · BESPOKE JOINERY &amp; MILLWORK</text>')
    svg.append(f'<text x="{sx6+80}" y="{sy6+185}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="34" font-weight="700">কাস্টম ফার্নিচার ও মিলওয়ার্ক এক্সিকিউশন</text>')

    # 2-Col Detail Layout
    svg.append(f'<rect x="{sx6+80}" y="{sy6+230}" width="680" height="480" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
    if img_joinery:
        svg.append(f'<image href="{img_joinery}" x="{sx6+80}" y="{sy6+230}" width="680" height="480" preserveAspectRatio="xMidYMid slice"/>')
    
    svg.append(f'<rect x="{sx6+800}" y="{sy6+230}" width="560" height="480" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{sx6+830}" y="{sy6+275}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="22" font-weight="700">আমাদের কাঠের কাজের বৈশিষ্ট্য</text>')
    t_s6_feat, _ = wrap_text("FlowGrid-এর জয়েনারি নির্মাণে সিজনড সলিড কাঠ ও উচ্চমানের প্রাকৃতিক ভিনিয়ার ব্যবহার করা হয়। প্রতিটি কেবিনেট কাঠামোর স্থায়িত্ব ও আর্দ্রতা সহনশীলতার কথা মাথায় রেখে নিখুঁত মর্টিস ও টেনন জয়েন্টে তৈরি করা হয়।", sx6+830, sy6+315, 38, 22, "'Noto Sans Bengali', sans-serif", 15, "#56645E")
    svg.append(t_s6_feat)

    # Timber options list (Safely positioned at sy6+445 with zero overlap)
    svg.append(f'<text x="{sx6+830}" y="{sy6+445}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="16" font-weight="700">উপলব্ধ কাঠ ও উপকরণ:</text>')
    timbers = [
        "• প্রাকৃতিক বার্মা সেগুন (Burma Teak) - প্রিমিয়াম সারফেস",
        "• সিজনড গর্জন কাঠ (Garjan) - শক্তিশালী অভ্যন্তরীণ ফ্রেম",
        "• প্রাকৃতিক হাতে বোনা বেত (Natural Cane) - আর্দ্রতা প্রতিরোধী",
        "• সফট-ক্লোজ ড্রয়ার চ্যানেল ও কনসিল্ড কব্জা"
    ]
    ty = sy6 + 475
    for tm in timbers:
        svg.append(f'<text x="{sx6+830}" y="{ty}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14">{escape_xml(tm)}</text>')
        ty += 28

    # Joinery Workflow Steps (Horizontal)
    svg.append(f'<rect x="{sx6+80}" y="{sy6+750}" width="1280" height="340" fill="#DEE7E2" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{sx6+120}" y="{sy6+795}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="22" font-weight="700">ফার্নিচার নির্মাণের ৫টি ধাপ</text>')

    j_steps = [
        ("১. মাপগ্রহণ ও সাইট অডিট", "লেজার পরিমাপের সাহায্যে দেয়ালের নিখুঁত মাপ গ্রহণ ও অসমান ফ্লোর লেভেলিং যাচাই।"),
        ("২. ৩ডি শপ ড্রয়িং অনুমোদন", "প্রতিটি তাক ও ড্রয়ারের মাপ ক্লায়েন্ট কর্তৃক চূড়ান্ত করার পর কারিগরদের কাছে ড্রয়িং হস্তান্তর।"),
        ("৩. কাঠ নির্বাচন ও সিজনিং", "আর্দ্রতা পরীক্ষা করে কাঠের সিজনিং নিশ্চিতকরণ ও ফালি কাটাই।"),
        ("৪. অফ-সাইট ফিটিংস পরীক্ষা", "সাইটে নেওয়ার আগে দক্ষ তত্ত্বাবধানে সম্পূর্ণ কেবিনেট একবার ট্রায়াল অ্যাসেম্বল করে পরীক্ষা।"),
        ("৫. সাইটে পরিচ্ছন্ন ইনস্টলেশন", "ধূলাবালি কমিয়ে সাইটে মাত্র ২-৩ দিনে সুশৃঙ্খলভাবে স্থায়ী ফিক্সিং সম্পন্ন।")
    ]
    jx = sx6 + 120
    for j_tit, j_desc in j_steps:
        svg.append(f'<text x="{jx}" y="{sy6+845}" fill="#895239" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="700">{escape_xml(j_tit)}</text>')
        td, _ = wrap_text(j_desc, jx, sy6+875, 20, 20, "'Noto Sans Bengali', sans-serif", 13, "#183B35")
        svg.append(td)
        jx += 250

    # Pricing & BOQ Transparency
    svg.append(f'<rect x="{sx6+80}" y="{sy6+1130}" width="1280" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{sx6+120}" y="{sy6+1180}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="22" font-weight="700">স্বচ্ছ কোটেশন ও পেমেন্ট পলিসি</text>')
    t_boq, _ = wrap_text("আমাদের কাছে কোনো লুকানো খরচ বা এককালীন অস্পষ্ট প্যাকেজ নেই। প্রতিটি ফার্নিচারের জন্য কাঠের বর্গফুট, হার্ডওয়্যার আইটেম ও লেবার কস্টের বিশদ হিসাব (BOQ) প্রদান করা হয়। ক্লায়েন্ট অনুমোদন করার পরই কেবল নির্মাণ কাজ শুরু হয়।", sx6+120, sy6+1220, 80, 22, "'Noto Sans Bengali', sans-serif", 15, "#56645E")
    svg.append(t_boq)

    svg.append(f'<rect x="{sx6+120}" y="{sy6+1350}" width="220" height="52" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{sx6+230}" y="{sy6+1382}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="600" text-anchor="middle">কাস্টম ফার্নিচার আলোচনা →</text>')

    svg.extend(render_desktop_footer(sx6, sy6+1920))

    # SCREEN 7: Dedicated Process Page (/process)
    sx7, sy7 = 3280, 2560
    svg.append(f'<rect x="{sx7}" y="{sy7}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_desktop_header(sx7, sy7, "process"))

    svg.append(f'<text x="{sx7+80}" y="{sy7+150}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">STEP-BY-STEP ARCHITECTURAL JOURNEY</text>')
    svg.append(f'<text x="{sx7+80}" y="{sy7+195}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="36" font-weight="700">আমাদের কাজের পূর্ণাঙ্গ কর্মপদ্ধতি</text>')
    t_s7_sub, _ = wrap_text("একটি সফল ইন্টেরিয়র প্রকল্পের প্রতিটি পর্যায়ে সুস্পষ্ট দায়িত্ব, সময়সীমা ও ডেলিভারেবল নিশ্চিত করা হয়।", sx7+80, sy7+235, 75, 22, "'Noto Sans Bengali', sans-serif", 16, "#56645E")
    svg.append(t_s7_sub)

    # 5 Major Process Stages (Vertical Stack)
    stages = [
        ("পর্যায় ০১", "প্রাথমিক স্পেস কনসালটেশন ও চাহিদা নিরূপণ", "সপ্তাহ ০১",
         "অ্যাপার্টমেন্ট সাইট পরিদর্শন, পরিবারের প্রতিটি সদস্যের দৈনন্দিন রুটিন ও স্টোরেজ বিশ্লেষণ। বর্তমান ফ্লোর প্ল্যানের খসড়া তৈরি।",
         "ডেলিভারেবল: স্পেস রিকোয়ারমেন্টস ডকুমেন্ট ও প্রাথমিক বাজেট রেঞ্জ।"),
        ("পর্যায় ০২", "কনসেপ্ট ডিজাইন ও স্থানিক বিন্যাস (2D & 3D)", "সপ্তাহ ০২-০৩",
         "টু-ডি ফার্নিচার লেআউট প্ল্যান, প্রধান এরিয়াগুলোর থ্রি-ডি ভিজ্যুয়ালাইজেশন এবং ম্যাটেরিয়াল মুডবোর্ড উপস্থাপন।",
         "ডেলিভারেবল: চূড়ান্ত টু-ডি ড্রয়িং, কালার প্যালেট ও অনুমোদিত কনসেপ্ট রেন্ডার।"),
        ("পর্যায় ০৩", "ডিটেইল ইঞ্জিনিয়ারিং ও স্বচ্ছ বাজেট (BOQ)", "সপ্তাহ ০৪",
         "ইলেকট্রিক্যাল, প্লাম্বিং ও ফলস সিলিং সংক্রান্ত ওয়ার্কিং ড্রয়িং প্রণয়ন। প্রতিটি উপাদানের বিশদ কোটেশন (Bill of Quantities)।",
         "ডেলিভারেবল: সম্পূর্ণ কাজের চুক্তিপত্র ও আইটেমাইজড বাজেট শিট।"),
        ("পর্যায় ০৪", "অফ-সাইট প্রি-ফেব্রিকেশন ও কারিগরি নির্মাণ", "সপ্তাহ ০৫-১১",
         "সাইটে ধূলাবালি কমাতে অফ-সাইট তত্ত্বাবধানে কাঠ কাটা, সিজনিং, কেবিনেট সংযোজন ও ফিনিশিং পরিচালনা।",
         "ডেলিভারেবল: কারিগরি অগ্রগতি প্রতিবেদন ও ক্লায়েন্ট সাইট ভিজিট।"),
        ("পর্যায় ০৫", "সাইটে নিখুঁত ইনস্টলেশন ও মান নিয়ন্ত্রণ হ্যান্ডওভার", "সপ্তাহ ১২",
         "তৈরিকৃত কেবিনেটরি অ্যাপার্টমেন্টে নিয়ে এসে নিখুঁত লেভেলিং ও স্ক্রু ফিক্সিং। ড্রয়ারের সফট-ক্লোজ পরীক্ষা ও ক্লায়েন্ট হ্যান্ডওভার।",
         "ডেলিভারেবল: গুণগত মান অডিট, মেইনটেন্যান্স গাইড ও প্রকল্প হ্যান্ডওভার।")
    ]
    py = sy7 + 300
    for st_no, st_tit, st_time, st_desc, st_deliv in stages:
        svg.append(f'<rect x="{sx7+80}" y="{py}" width="1280" height="230" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
        svg.append(f'<rect x="{sx7+80}" y="{py}" width="140" height="230" fill="#183B35" rx="4 0 0 4"/>')
        svg.append(f'<text x="{sx7+150}" y="{py+105}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="20" font-weight="700" text-anchor="middle">{st_no}</text>')
        svg.append(f'<text x="{sx7+150}" y="{py+140}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="13" text-anchor="middle">{st_time}</text>')

        svg.append(f'<text x="{sx7+260}" y="{py+45}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="20" font-weight="700">{escape_xml(st_tit)}</text>')
        t_pdesc, _ = wrap_text(st_desc, sx7+260, py+80, 75, 22, "'Noto Sans Bengali', sans-serif", 15, "#56645E")
        svg.append(t_pdesc)

        svg.append(f'<rect x="{sx7+260}" y="{py+160}" width="980" height="42" fill="#DEE7E2" rx="2"/>')
        svg.append(f'<text x="{sx7+280}" y="{py+186}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600">✓ {escape_xml(st_deliv)}</text>')
        py += 260

    svg.extend(render_desktop_footer(sx7, sy7+1920))

    # SCREEN 8: Dedicated Studio Page (/studio)
    sx8, sy8 = 4880, 2560
    svg.append(f'<rect x="{sx8}" y="{sy8}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_desktop_header(sx8, sy8, "studio"))

    svg.append(f'<text x="{sx8+80}" y="{sy8+150}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">STUDIO ETHOS &amp; WORKSHOP TEAM</text>')
    svg.append(f'<text x="{sx8+80}" y="{sy8+195}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="36" font-weight="700">ফ্লোগ্রিড স্টুডিও ও আমাদের কারিগর দল</text>')
    t_s8_sub, _ = wrap_text("মিরপুরের কাঠের কর্মশালা এবং অভিজ্ঞ কাঠমিস্ত্রিদের সমন্বয়ে আমরা গড়ে তুলেছি ব্যবহারিক ও খাঁটি স্থাপত্য অনুশীলন।", sx8+80, sy8+235, 75, 22, "'Noto Sans Bengali', sans-serif", 16, "#56645E")
    svg.append(t_s8_sub)

    # Studio Story & Values (2 Cols)
    svg.append(f'<rect x="{sx8+80}" y="{sy8+290}" width="620" height="460" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{sx8+110}" y="{sy8+340}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="22" font-weight="700">আমাদের দর্শন ও কাজের সততা</text>')
    t_st_phil, _ = wrap_text("FlowGrid কোনো মধ্যস্বত্বভোগী এজেন্সি নয়। আমরা বিশ্বাস করি প্রতিটি পরিবারের বাড়ি একটি ব্যক্তিগত প্রশান্তির স্থান। আমরা অহেতুক দামি লাইটিং বা অপ্রয়োজনীয় প্যানেলিংয়ের মাধ্যমে বাজেট বাড়িয়ে তুলি না। আলো, বাতাস এবং প্রাকৃতিক কাঠের স্বাভাবিক বিন্যাসেই ফুটে ওঠে গৃহকোণের সৌন্দর্য।", sx8+110, sy8+380, 42, 24, "'Noto Sans Bengali', sans-serif", 15, "#56645E")
    svg.append(t_st_phil)

    svg.append(f'<rect x="{sx8+740}" y="{sy8+290}" width="620" height="460" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{sx8+770}" y="{sy8+340}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="22" font-weight="700">স্থানীয় কারিগরি দক্ষতা ও সুপারভিশন</text>')
    t_st_wrk, _ = wrap_text("মিরপুরের দক্ষ প্রবীণ কাঠমিস্ত্রিদের নিবিড় তত্ত্বাবধানে কাঠের প্রতিটি জয়েন্ট নিখুঁতভাবে তৈরি করা হয়। হস্তশিল্পের ঐতিহ্য এবং আধুনিক মেকানিক্যাল নির্ভুলতার মেলবন্ধনে প্রতিটি ড্রয়ার ও আলমারি দীর্ঘ বহু বছর ব্যবহারের উপযোগী থাকে।", sx8+770, sy8+380, 42, 24, "'Noto Sans Bengali', sans-serif", 15, "#56645E")
    svg.append(t_st_wrk)

    # Verified Team Roles Grid (No unverified claims)
    svg.append(f'<text x="{sx8+80}" y="{sy8+810}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="26" font-weight="700">স্টুডিও টিম ও কারিগরি নেতৃত্ব</text>')

    team = [
        ("প্রধান স্থপতি ও ডিজাইনার", "স্থাপত্য পরিকল্পনা ও ড্রয়িং প্রধান", "আবাসিক স্পেস প্ল্যানিং ও টু-ডি/থ্রি-ডি কোঅর্ডিনেশন।"),
        ("জয়েনারি ও ক্রাফট লিড", "অভিজ্ঞ কাঠমিস্ত্রি ও কারিগরি সুপারভাইজার", "কাঠ নির্বাচন, সিজনিং ও মর্টিস জয়েনারি ফিনিশিং।"),
        ("সাইট প্রজেক্ট ইঞ্জিনিয়ার", "অন-সাইট ইনস্টলেশন ও সুপারভাইজার", "লেভেলিং, ইলেকট্রিক্যাল সমন্বয় ও হ্যান্ডওভার কোয়ালিটি।")
    ]
    tx = sx8 + 80
    for t_role, t_title, t_resp in team:
        svg.append(f'<rect x="{tx}" y="{sy8+850}" width="400" height="340" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
        svg.append(f'<rect x="{tx+20}" y="{sy8+870}" width="360" height="150" fill="#DEE7E2" rx="2"/>')
        svg.append(f'<text x="{tx+200}" y="{sy8+955}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="14" text-anchor="middle">[ Verified Team Portrait ]</text>')
        svg.append(f'<text x="{tx+20}" y="{sy8+1055}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="18" font-weight="700">{escape_xml(t_role)}</text>')
        svg.append(f'<text x="{tx+20}" y="{sy8+1085}" fill="#895239" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600">{escape_xml(t_title)}</text>')
        t_tr, _ = wrap_text(t_resp, tx+20, sy8+1115, 30, 20, "'Noto Sans Bengali', sans-serif", 13, "#56645E")
        svg.append(t_tr)
        tx += 440

    # Ethical Boundary Statement Banner
    svg.append(f'<rect x="{sx8+80}" y="{sy8+1240}" width="1280" height="180" fill="#DEE7E2" stroke="#183B35" stroke-width="1.5" rx="4"/>')
    svg.append(f'<text x="{sx8+110}" y="{sy8+1285}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="20" font-weight="700">স্বতন্ত্র ব্যবসায়িক পরিচয় ও নীতিগত অবস্থান</text>')
    t_eth, _ = wrap_text("ফ্লোগ্রিড একটি স্বাধীন ইন্টেরিয়র ডিজাইন স্টুডিও। রুমী\'স ফ্যাশনেবল হাউস আমাদের পারিবারিক প্রতিষ্ঠাতা প্রেক্ষাপট হলেও ফ্লোগ্রিড সম্পূর্ণ পৃথক পেশাদার স্থাপত্য দল দ্বারা পরিচালিত হয়। এখানে কোনো খুচরা গৃহস্থালি পণ্য বিক্রি করা হয় না।", sx8+110, sy8+1320, 80, 22, "'Noto Sans Bengali', sans-serif", 14, "#183B35")
    svg.append(t_eth)

    svg.extend(render_desktop_footer(sx8, sy8+1920))

    # -------------------------------------------------------------
    # ROW 3 OF SCREENS (y: 4860)
    # SCREEN 9: Dedicated Contact Page (/contact) - x: 80, y: 4860
    # SCREEN 10: Privacy & Service Information (/privacy) - x: 1680, y: 4860
    # SCREEN 11: 404 Not Found Page (/404) - x: 3280, y: 4860
    # -------------------------------------------------------------

    # SCREEN 9: Dedicated Contact Page (/contact)
    sx9, sy9 = 80, 4860
    svg.append(f'<rect x="{sx9}" y="{sy9}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_desktop_header(sx9, sy9, "contact"))

    svg.append(f'<text x="{sx9+80}" y="{sy9+150}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">DIRECT CONSULTATION &amp; STUDIO VISIT</text>')
    svg.append(f'<text x="{sx9+80}" y="{sy9+195}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="36" font-weight="700">স্টুডিওর সাথে যোগাযোগ করুন</text>')
    t_c9_sub, _ = wrap_text("আপনার অ্যাপার্টমেন্ট বা কাস্টম ফার্নিচার সংক্রান্ত যেকোনো আলোচনার জন্য আমাদের সরাসরি কল করতে পারেন অথবা ফর্মটি পূরণ করে পাঠান।", sx9+80, sy9+235, 75, 22, "'Noto Sans Bengali', sans-serif", 16, "#56645E")
    svg.append(t_c9_sub)

    # 2-Col Layout: Left Form, Right Contact Info & FAQ
    # Left: 4-Field Form Container
    svg.append(f'<rect x="{sx9+80}" y="{sy9+290}" width="680" height="740" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{sx9+110}" y="{sy9+335}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="20" font-weight="700">পরামর্শের আবেদন ফর্ম</text>')

    cfy = sy9 + 375
    cfx = sx9 + 110
    cfw = 620

    # Field 1
    svg.append(f'<text x="{cfx}" y="{cfy}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="600">১. আপনার নাম (Full Name) *</text>')
    svg.append(f'<rect x="{cfx}" y="{cfy+10}" width="{cfw}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{cfx+15}" y="{cfy+40}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14">উদা: মো. ফারহান আহমেদ</text>')
    cfy += 78

    # Field 2
    svg.append(f'<text x="{cfx}" y="{cfy}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="600">২. মোবাইল নম্বর (Mobile Number) *</text>')
    svg.append(f'<rect x="{cfx}" y="{cfy+10}" width="{cfw}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{cfx+15}" y="{cfy+40}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="14">+880 17XX-XXXXXX</text>')
    cfy += 78

    # Field 3
    svg.append(f'<text x="{cfx}" y="{cfy}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="600">৩. এলাকা ও শহর (Area / City) *</text>')
    svg.append(f'<rect x="{cfx}" y="{cfy+10}" width="{cfw}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{cfx+15}" y="{cfy+40}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14">উদা: মিরপুর / গুলশান / ধানমন্ডি / চট্টগ্রাম</text>')
    cfy += 78

    # Field 4
    svg.append(f'<text x="{cfx}" y="{cfy}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="600">৪. প্রয়োজনীয় সেবা (Service Interest) *</text>')
    svg.append(f'<rect x="{cfx}" y="{cfy+10}" width="{cfw}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{cfx+15}" y="{cfy+40}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14">সেবা নির্বাচন করুন (কাস্টম ফার্নিচার / ড্রয়িং / নিশ্চিত নই) ▼</text>')
    cfy += 78

    # Optional Field
    svg.append(f'<text x="{cfx}" y="{cfy}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">প্রকল্পের বিবরণ ও আনুমানিক আয়তন (ঐচ্ছিক)</text>')
    svg.append(f'<rect x="{cfx}" y="{cfy+10}" width="{cfw}" height="80" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{cfx+15}" y="{cfy+38}" fill="#B8C2BA" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">ফ্লোর এরিয়া, রুমের সংখ্যা বা নির্দিষ্ট চাহিদা উল্লেখ করতে পারেন...</text>')
    cfy += 115

    # Button
    svg.append(f'<rect x="{cfx}" y="{cfy}" width="{cfw}" height="52" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{cfx+cfw//2}" y="{cfy+32}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="600" text-anchor="middle">পরামর্শ অনুরোধ পাঠান →</text>')

    # Right: Direct Info & Map Reference
    svg.append(f'<rect x="{sx9+800}" y="{sy9+290}" width="560" height="740" fill="#DEE7E2" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{sx9+830}" y="{sy9+340}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="22" font-weight="700">সরাসরি যোগাযোগের ঠিকানা</text>')

    contacts = [
        ("স্টুডিও অবস্থান", "মিরপুর-১০, ঢাকা ১২১৬, বাংলাদেশ"),
        ("হটলাইন টেলিফোন", "+880 1700-000000 (প্রভিশনাল প্লেসহোল্ডার)"),
        ("ইমেইল যোগাযোগ", "hello@flowgrid-interiors.com"),
        ("সরাসরি বার্তা", "WhatsApp: +880 1700-000000 (অফিশিয়াল চ্যাট)"),
        ("স্টুডিও ও সাইট ভিজিট", "অ্যাপয়েন্টমেন্টের ভিত্তিতে প্রাথমিক পরামর্শ ও সাইট পরিদর্শনের ব্যবস্থা")
    ]
    cy = sy9 + 390
    for c_tit, c_val in contacts:
        svg.append(f'<text x="{sx9+830}" y="{cy}" fill="#895239" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="700">{escape_xml(c_tit)}</text>')
        svg.append(f'<text x="{sx9+830}" y="{cy+24}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15">{escape_xml(c_val)}</text>')
        cy += 64

    # Map Reference Frame
    svg.append(f'<rect x="{sx9+830}" y="{cy+15}" width="500" height="190" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{sx9+1080}" y="{cy+105}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" text-anchor="middle">[ মিরপুর মেট্রো স্টেশন সংলগ্ন ম্যাপ রেফারেন্স ]</text>')
    svg.append(f'<text x="{sx9+1080}" y="{cy+130}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="12" text-anchor="middle">Mirpur-10, Dhaka 1216</text>')

    svg.extend(render_desktop_footer(sx9, sy9+1920))

    # SCREEN 10: Privacy & Service Information (/privacy)
    sx10, sy10 = 1680, 4860
    svg.append(f'<rect x="{sx10}" y="{sy10}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_desktop_header(sx10, sy10, ""))

    svg.append(f'<text x="{sx10+80}" y="{sy10+150}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="13" font-weight="700">LEGAL &amp; SERVICE INFORMATION</text>')
    svg.append(f'<text x="{sx10+80}" y="{sy10+195}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="36" font-weight="700">গোপনীয়তা নীতি ও সেবার শর্তাবলী</text>')

    # 4 Policy Blocks
    policies = [
        ("০১. গ্রাহক তথ্যের গোপনীয়তা ও সুরক্ষা",
         "ফর্মের মাধ্যমে সংগৃহীত আপনার নাম, মোবাইল নম্বর ও ঠিকানা শুধুমাত্র ইন্টেরিয়র ডিজাইন সংক্রান্ত যোগাযোগের উদ্দেশ্যে সংরক্ষিত হয়। আমরা কোনো তৃতীয় পক্ষের সাথে বাণিজ্যিক উদ্দেশ্যে গ্রাহকের তথ্য শেয়ার করি না।"),
        ("০২. কনসেপ্ট ভিজ্যুয়ালাইজেশন ও সত্যনিষ্ঠ ডিসক্লোজার",
         "ওয়েবসাইটে প্রদর্শিত সকল থ্রি-ডি রেন্ডার স্বাধীন স্থাপত্য অনুসিদ্ধান্ত (Concept Design) হিসেবে তৈরি। বাস্তব সাইটে নির্মাণের ক্ষেত্রে কাঠামোগত ফিজিবিলিটি ও সাইটের মাপ অনুযায়ী ডিজাইন সমন্বয় করা হয়।"),
        ("০৩. বৌদ্ধিক সম্পত্তি ও স্থাপত্য অধিকার (IP Rights)",
         "ফ্লোগ্রিড স্টুডিওর প্রণীত সকল টু-ডি ড্রয়িং, ফার্নিচার মডেল ও ৩ডি ডিজাইনের বৌদ্ধিক স্বত্বাধিকার সংরক্ষিত। ক্লায়েন্টের লিখিত অনুমতি ছাড়া কোনো ড্রয়িং অন্য প্ল্যাটফর্মে ব্যবহার করা নিষিদ্ধ।"),
        ("০৪. সাইট ভিজিট ও প্রাথমিক পরিমাপ সংক্রান্ত নীতি",
         "প্রাথমিক স্থানিক মূল্যায়ন ও সাইট ভিজিটের শর্তাবলী ক্লায়েন্টের সাথে পারস্পরিক আলোচনার মাধ্যমে নির্ধারিত হয়। কোটেশন অনুমোদনের পর সম্পূর্ণ কাজের শিডিউল কার্যকর হয়।")
    ]
    py = sy10 + 260
    for p_no, p_desc in policies:
        svg.append(f'<rect x="{sx10+80}" y="{py}" width="1280" height="200" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
        svg.append(f'<text x="{sx10+120}" y="{py+50}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="20" font-weight="700">{escape_xml(p_no)}</text>')
        t_pd, _ = wrap_text(p_desc, sx10+120, py+90, 75, 24, "'Noto Sans Bengali', sans-serif", 15, "#56645E")
        svg.append(t_pd)
        py += 230

    svg.extend(render_desktop_footer(sx10, sy10+1920))

    # SCREEN 11: 404 Error Page (/404)
    sx11, sy11 = 3280, 4860
    svg.append(f'<rect x="{sx11}" y="{sy11}" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_desktop_header(sx11, sy11, ""))

    svg.append(f'<rect x="{sx11+280}" y="{sy11+400}" width="880" height="700" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{sx11+720}" y="{sy11+540}" fill="#895239" font-family="\'Bodoni Moda\', serif" font-size="96" font-weight="700" text-anchor="middle">404</text>')
    svg.append(f'<text x="{sx11+720}" y="{sy11+620}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="28" font-weight="700" text-anchor="middle">অনুরোধকৃত স্থাপত্য পৃষ্ঠাটি পাওয়া যায়নি</text>')
    t_404, _ = wrap_text("আপনি যে লিংকটি খুঁজছেন তা স্থানান্তরিত হয়েছে অথবা ড্রাফট মোডে রয়েছে। ফ্লোগ্রিড স্টুডিওর মূল প্রচ্ছদে ফিরে গিয়ে আমাদের প্রকল্প ও সেবাসমূহ দেখতে পারেন।", sx11+720-300, sy11+670, 45, 24, "'Noto Sans Bengali', sans-serif", 16, "#56645E", text_anchor="start")
    svg.append(t_404)

    svg.append(f'<rect x="{sx11+720-130}" y="{sy11+780}" width="260" height="52" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{sx11+720}" y="{sy11+812}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="600" text-anchor="middle">মূল প্রচ্ছদে ফিরে যান →</text>')

    svg.extend(render_desktop_footer(sx11, sy11+1920))

    svg.append('</svg>')

    out_path = 'figma_svgs_v3/03_desktop_bn.svg'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    
    valid, err = validate_svg_file(out_path)
    print(f'Board 03: {out_path} -> Valid XML? {valid} ({err})')

if __name__ == '__main__':
    generate_board_03()
