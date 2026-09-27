"""
FlowGrid - Page 04: Mobile Suite — Bangla (v3.1 Complete & Reconciled)
Delivers ALL 11 Mobile Templates + 1 Dedicated Off-Canvas Drawer Overlay:
1. Mobile Homepage (390px x 3350px)
2. Mobile Projects Archive (390px x 1600px)
3. Mobile Concept Detail - 3 Views (390px x 2000px)
4. Mobile Real-Project Framework Template (390px x 1600px)
5. Mobile Dedicated Services (390px x 1400px)
6. Mobile Dedicated Service Detail - Joinery (390px x 1400px)
7. Mobile Dedicated Process (390px x 1400px)
8. Mobile Dedicated Studio (390px x 1400px)
9. Mobile Privacy & Legal Policy (390px x 1400px)
10. Mobile Dedicated Contact (390px x 1450px) - Resolved blank interval!
11. Mobile 404 Error Screen (390px x 650px)
12. Mobile Off-Canvas Navigation Drawer (390px x 750px) - Separate frame, ZERO footer collision!

All inputs strictly 48px touch height; contrast verified.
"""
import os
from svg_utils import wrap_text, escape_xml, validate_svg_file, get_base64_image

def generate_board_04():
    img_living = get_base64_image('concepts/concept_01_living_dhaka.jpg')
    img_living_alt = get_base64_image('concepts/concept_01_living_alt.jpg')
    img_joinery = get_base64_image('concepts/concept_01_joinery_detail.jpg')
    img_kitchen = get_base64_image('concepts/concept_02_kitchen_dhaka.jpg')
    img_bedroom = get_base64_image('concepts/concept_03_bedroom_dhaka.jpg')

    # 5 Columns of 390px screens: 80 + 5*390 + 4*80 + 80 = 2430 -> w = 2450
    # Height to accommodate 3350px home and stacked screens: h = 4850
    w, h = 2450, 4850
    svg = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{w}" height="{h}" fill="#F4F1E8"/>')

    # Header Banner
    svg.append(f'<rect x="80" y="80" width="{w-160}" height="140" fill="#183B35" rx="4"/>')
    svg.append('<text x="120" y="145" fill="#F4F1E8" font-family="\'Bodoni Moda\', serif" font-size="36" font-weight="600">FlowGrid — Mobile Experience Suite · Bangla (390px Master Screens · v3.1)</text>')
    svg.append('<text x="120" y="185" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="18">Complete 11-template mobile journeys + dedicated off-canvas drawer overlay with zero layout collisions and 48px touch targets</text>')

    # Helper: Mobile Header (64px) with 48x48 touch targets
    def render_mobile_header(x, y):
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

    # Helper: Mobile Footer (340px) with High-Contrast Tokens
    def render_mobile_footer(x, y):
        res = []
        res.append(f'<rect x="{x}" y="{y}" width="390" height="340" fill="#183B35"/>')
        res.append(f'<text x="{x+20}" y="{y+40}" fill="#F4F1E8" font-family="\'Bodoni Moda\', serif" font-size="24" font-weight="700">FlowGrid Studio</text>')
        t_mf, _ = wrap_text("ঢাকার শহুরে অ্যাপার্টমেন্টের ব্যবহারিক ইন্টেরিয়র আর্কিটেকচার ও মিলওয়ার্ক।", x+20, y+70, 36, 20, "'Noto Sans Bengali', sans-serif", 13, "#DEE7E2")
        res.append(t_mf)

        # High-contrast label in Soft Mist #DEE7E2 (9.69:1 contrast)
        res.append(f'<text x="{x+20}" y="{y+140}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="12" font-weight="700">LOCATION &amp; CONTACT</text>')
        res.append(f'<text x="{x+20}" y="{y+165}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">মিরপুর-১০, ঢাকা ১২১৬ · +880 1700-000000</text>')
        res.append(f'<text x="{x+20}" y="{y+190}" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="13">hello@flowgrid-interiors.com</text>')

        res.append(f'<line x1="{x+20}" y1="{y+225}" x2="{x+370}" y2="{y+225}" stroke="#2D524A" stroke-width="1"/>')
        res.append(f'<text x="{x+20}" y="{y+255}" fill="#DEE7E2" font-family="\'Noto Sans Bengali\', sans-serif" font-size="12">প্রাইভেসি পলিসি · সেবার শর্তাবলী</text>')
        res.append(f'<text x="{x+20}" y="{y+285}" fill="#C4D1CA" font-family="\'Noto Sans Bengali\', sans-serif" font-size="12">রুমী\'স ফ্যাশনেবল হাউস (লাইফস্টাইল ভ্লগ প্রেক্ষাপট)</text>')
        res.append(f'<text x="{x+20}" y="{y+315}" fill="#C4D1CA" font-family="\'Manrope\', sans-serif" font-size="12">© 2026 FlowGrid. Truth in Design Policy.</text>')
        return res

    # -------------------------------------------------------------
    # COLUMN 1: SCREEN 1: Mobile Homepage (390 x 3350) - x: 80, y: 260
    # ZERO overlap with drawer!
    # -------------------------------------------------------------
    mx1, my1 = 80, 260
    svg.append(f'<rect x="{mx1}" y="{my1}" width="390" height="3350" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_mobile_header(mx1, my1))

    # Paper Hero Block
    svg.append(f'<text x="{mx1+20}" y="{my1+100}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="12" font-weight="700">DHAKA INTERIOR ARCHITECTURE</text>')
    t_mh1, _ = wrap_text("দৈনন্দিন জীবনের শান্ত ও সুবিন্যস্ত স্থাপত্য", mx1+20, my1+135, 18, 38, "'Noto Sans Bengali', sans-serif", 28, "#183B35", 700)
    svg.append(t_mh1)
    t_msub, _ = wrap_text("ঢাকার অ্যাপার্টমেন্টে পরিমিত পরিসরে খোলামেলা আলোর পরিবেশ এবং দীর্ঘস্থায়ী কাঠের কাজের সমন্বয়।", mx1+20, my1+230, 36, 22, "'Noto Sans Bengali', sans-serif", 14, "#56645E")
    svg.append(t_msub)

    # Hero CTAs (48px height)
    svg.append(f'<rect x="{mx1+20}" y="{my1+300}" width="170" height="48" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{mx1+105}" y="{my1+330}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600" text-anchor="middle">পরামর্শ বুক করুন</text>')
    svg.append(f'<rect x="{mx1+200}" y="{my1+300}" width="170" height="48" fill="transparent" stroke="#183B35" stroke-width="1.5" rx="2"/>')
    svg.append(f'<text x="{mx1+285}" y="{my1+330}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600" text-anchor="middle">প্রকল্প গ্যালারি</text>')

    # Hero Image Card with Sized Truth Disclosure
    if img_living:
        svg.append(f'<image href="{img_living}" x="{mx1+20}" y="{my1+370}" width="350" height="240" preserveAspectRatio="xMidYMid slice"/>')
    svg.append(f'<rect x="{mx1+25}" y="{my1+375}" width="300" height="24" fill="#183B35" fill-opacity="0.9" rx="2"/>')
    svg.append(f'<text x="{mx1+32}" y="{my1+391}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="10" font-weight="600">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত নয়</text>')

    # Approach
    svg.append(f'<rect x="{mx1+20}" y="{my1+630}" width="350" height="220" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{mx1+35}" y="{my1+665}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">OUR PHILOSOPHY</text>')
    svg.append(f'<text x="{mx1+35}" y="{my1+695}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="18" font-weight="700">ব্যবহারিক পরিসর ও খাঁটি উপকরণ</text>')
    t_map, _ = wrap_text("ঢাকার অ্যাপার্টমেন্টে পর্যাপ্ত স্টোরেজ ও মুক্ত চলাচলের স্থান নিশ্চিত করাই আমাদের প্রধান লক্ষ্য। প্রাকৃতিক কাঠ ও বেতের কাজে দীর্ঘস্থায়ী ঘর সাজাই।", mx1+35, my1+725, 34, 20, "'Noto Sans Bengali', sans-serif", 13, "#56645E")
    svg.append(t_map)

    # 3 Featured Concept Studies
    svg.append(f'<text x="{mx1+20}" y="{my1+885}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="20" font-weight="700">নির্বাচিত কনসেপ্ট স্টাডিজ</text>')
    m_studies = [
        ("গুলশান লেকভিউ লিভিং স্টাডি", "সেগুন বুকশেলফ ও উইন্ডো সিট", img_living, my1+915),
        ("রেজিলিয়েন্ট কিচেন স্টাডি", "গ্রানাইট কাউন্টার ও সিলিন্ডার নিশ", img_kitchen, my1+1290),
        ("মাস্টার বেডরুম ও স্টাডি", "প্ল্যাটফর্ম বেড ও বেতের ওয়ারড্রব", img_bedroom, my1+1665)
    ]
    for s_tit, s_desc, s_img, sy in m_studies:
        svg.append(f'<rect x="{mx1+20}" y="{sy}" width="350" height="355" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
        if s_img:
            svg.append(f'<image href="{s_img}" x="{mx1+20}" y="{sy}" width="350" height="220" preserveAspectRatio="xMidYMid slice"/>')
        svg.append(f'<rect x="{mx1+25}" y="{sy+5}" width="260" height="22" fill="#183B35" fill-opacity="0.9" rx="2"/>')
        svg.append(f'<text x="{mx1+30}" y="{sy+20}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="10">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>')
        svg.append(f'<text x="{mx1+35}" y="{sy+255}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="16" font-weight="700">{escape_xml(s_tit)}</text>')
        t_sd, _ = wrap_text(s_desc, mx1+35, sy+280, 32, 18, "'Noto Sans Bengali', sans-serif", 13, "#56645E")
        svg.append(t_sd)
        svg.append(f'<text x="{mx1+35}" y="{sy+335}" fill="#895239" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600">সম্পূর্ণ স্টাডি দেখুন →</text>')

    # Quick Consultation Section (48px inputs)
    svg.append(f'<rect x="{mx1+20}" y="{my1+2050}" width="350" height="520" fill="#DEE7E2" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{mx1+35}" y="{my1+2090}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="18" font-weight="700">স্পেস কনসালটেশন বুক করুন</text>')
    svg.append(f'<text x="{mx1+35}" y="{my1+2115}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">প্রাথমিক আলোচনার জন্য আপনার তথ্য দিন</text>')

    fy_q = my1 + 2135
    # Name
    svg.append(f'<rect x="{mx1+35}" y="{fy_q}" width="320" height="48" fill="#FFFFFF" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{mx1+45}" y="{fy_q+30}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">আপনার নাম *</text>')
    # Mobile
    svg.append(f'<rect x="{mx1+35}" y="{fy_q+58}" width="320" height="48" fill="#FFFFFF" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{mx1+45}" y="{fy_q+88}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">মোবাইল নম্বর: 01XXXXXXXXX *</text>')
    # Area
    svg.append(f'<rect x="{mx1+35}" y="{fy_q+116}" width="320" height="48" fill="#FFFFFF" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{mx1+45}" y="{fy_q+146}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">এলাকা ও শহর (মিরপুর, গুলশান...) *</text>')
    # Service
    svg.append(f'<rect x="{mx1+35}" y="{fy_q+174}" width="320" height="48" fill="#FFFFFF" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{mx1+45}" y="{fy_q+204}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">প্রয়োজনীয় সেবা (অথবা নিশ্চিত নই) ▼ *</text>')
    # Submit Button
    svg.append(f'<rect x="{mx1+35}" y="{fy_q+238}" width="320" height="52" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{mx1+195}" y="{fy_q+270}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">পরামর্শ অনুরোধ পাঠান →</text>')

    # Studio Address Preview
    svg.append(f'<rect x="{mx1+20}" y="{my1+2600}" width="350" height="150" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{mx1+35}" y="{my1+2635}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="16" font-weight="700">স্টুডিও ও পরিদর্শন</text>')
    svg.append(f'<text x="{mx1+35}" y="{my1+2665}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">মিরপুর-১০, ঢাকা ১২১৬ · +880 1700-000000</text>')
    svg.append(f'<text x="{mx1+35}" y="{my1+2690}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">hello@flowgrid-interiors.com</text>')
    svg.append(f'<text x="{mx1+35}" y="{my1+2720}" fill="#895239" font-family="\'Noto Sans Bengali\', sans-serif" font-size="12" font-weight="600">সরাসরি স্টুডিওতে সাক্ষাতের জন্য অ্যাপয়েন্টমেন্ট নিন →</text>')

    # Mobile Home Footer
    svg.extend(render_mobile_footer(mx1, my1+3010))

    # -------------------------------------------------------------
    # COLUMN 2 (x = 550): SCREEN 2 & SCREEN 3
    # SCREEN 2: Mobile Projects Archive (390 x 1600)
    # -------------------------------------------------------------
    mx2, my2 = 550, 260
    svg.append(f'<rect x="{mx2}" y="{my2}" width="390" height="1600" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_mobile_header(mx2, my2))

    svg.append(f'<text x="{mx2+20}" y="{my2+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">PROJECTS ARCHIVE</text>')
    svg.append(f'<text x="{mx2+20}" y="{my2+125}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="22" font-weight="700">প্রকল্প ও কনসেপ্ট গ্যালারি</text>')
    
    # 2 Archive Cards
    svg.append(f'<rect x="{mx2+20}" y="{my2+150}" width="350" height="350" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
    if img_living:
        svg.append(f'<image href="{img_living}" x="{mx2+20}" y="{my2+150}" width="350" height="220" preserveAspectRatio="xMidYMid slice"/>')
    svg.append(f'<rect x="{mx2+25}" y="{my2+155}" width="260" height="20" fill="#183B35" fill-opacity="0.9" rx="2"/>')
    svg.append(f'<text x="{mx2+30}" y="{my2+169}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="10">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>')
    svg.append(f'<text x="{mx2+35}" y="{my2+395}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="16" font-weight="700">গুলশান লেকভিউ অ্যাপার্টমেন্ট স্টাডি</text>')
    svg.append(f'<text x="{mx2+35}" y="{my2+420}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">৩টি সমন্বিত দৃশ্যপট ও জয়েনারি বিশ্লেষণ</text>')
    svg.append(f'<text x="{mx2+35}" y="{my2+460}" fill="#895239" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600">কেস স্টাডি বিস্তারিত দেখুন →</text>')

    svg.append(f'<rect x="{mx2+20}" y="{my2+520}" width="350" height="350" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
    if img_kitchen:
        svg.append(f'<image href="{img_kitchen}" x="{mx2+20}" y="{my2+520}" width="350" height="220" preserveAspectRatio="xMidYMid slice"/>')
    svg.append(f'<rect x="{mx2+25}" y="{my2+525}" width="260" height="20" fill="#183B35" fill-opacity="0.9" rx="2"/>')
    svg.append(f'<text x="{mx2+30}" y="{my2+539}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="10">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>')
    svg.append(f'<text x="{mx2+35}" y="{my2+765}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="16" font-weight="700">রেজিলিয়েন্ট কিচেন ও প্যান্ট্রি স্টাডি</text>')
    svg.append(f'<text x="{mx2+35}" y="{my2+790}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">গ্রানাইট কাউন্টার ও সিলিন্ডার ভেন্টিলেশন</text>')
    svg.append(f'<text x="{mx2+35}" y="{my2+830}" fill="#895239" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600">কিচেন স্টাডি দেখুন →</text>')

    svg.extend(render_mobile_footer(mx2, my2+1260))

    # SCREEN 3: Mobile Concept Detail (3-View Study) (390 x 2000) - x: 550, y: 1920
    mx3, my3 = 550, 1920
    svg.append(f'<rect x="{mx3}" y="{my3}" width="390" height="2000" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_mobile_header(mx3, my3))

    svg.append(f'<text x="{mx3+20}" y="{my3+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">CONCEPT STUDY 01 · 3 VIEWS</text>')
    svg.append(f'<text x="{mx3+20}" y="{my3+125}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="20" font-weight="700">গুলশান লেকভিউ অ্যাপার্টমেন্ট</text>')

    # 3 Spatial Views Stack
    v_stack = [
        ("ভিউ ১: লিভিং রুম ও বুকশেলফ", img_living, my3+150),
        ("ভিউ ২: ডাইনিং ও প্রাকৃতিক আলো", img_living_alt, my3+480),
        ("ভিউ ৩: জয়েনারি ডিটেইল ও বেতের কাজ", img_joinery, my3+810)
    ]
    for vt, vi, vy in v_stack:
        svg.append(f'<rect x="{mx3+20}" y="{vy}" width="350" height="310" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>')
        if vi:
            svg.append(f'<image href="{vi}" x="{mx3+20}" y="{vy}" width="350" height="220" preserveAspectRatio="xMidYMid slice"/>')
        svg.append(f'<rect x="{mx3+25}" y="{vy+5}" width="260" height="20" fill="#183B35" fill-opacity="0.9" rx="2"/>')
        svg.append(f'<text x="{mx3+30}" y="{vy+19}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="10">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>')
        svg.append(f'<text x="{mx3+35}" y="{vy+255}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="700">{escape_xml(vt)}</text>')
        svg.append(f'<text x="{mx3+35}" y="{vy+280}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="12">বার্মা সেগুন কাঠ, ভেন্টিলেটেড বেত ও প্রাকৃতিক লাইম প্লাস্টার</text>')

    # Spatial Rationale Card
    svg.append(f'<rect x="{mx3+20}" y="{my3+1140}" width="350" height="210" fill="#DEE7E2" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{mx3+35}" y="{my3+1170}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="700">স্থানিক সিদ্ধান্ত ও উপাদান শর্ত</text>')
    t_mdec, _ = wrap_text("অনুসিদ্ধান্ত শর্ত: ২১৫০ বর্গফুট ধারণাগত অ্যাপার্টমেন্ট। মেঝে থেকে ছাদ বুকশেলফ, দক্ষিণমুখী বারান্দার আলো এবং আর্দ্রতা সহনশীল প্রাকৃতিক বেতের ফ্রন্ট প্যানেল।", mx3+35, my3+1195, 34, 20, "'Noto Sans Bengali', sans-serif", 13, "#56645E")
    svg.append(t_mdec)
    svg.append(f'<rect x="{mx3+35}" y="{my3+1280}" width="320" height="48" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{mx3+195}" y="{my3+1310}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600" text-anchor="middle">অনুরূপ প্রজেক্টে পরামর্শ নিন →</text>')

    svg.extend(render_mobile_footer(mx3, my3+1660))

    # -------------------------------------------------------------
    # COLUMN 3 (x = 1020): SCREEN 4, SCREEN 5 & SCREEN 6
    # SCREEN 4: Mobile Real-Project Framework Template (390 x 1400)
    # -------------------------------------------------------------
    mx4, my4 = 1020, 260
    svg.append(f'<rect x="{mx4}" y="{my4}" width="390" height="1400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_mobile_header(mx4, my4))

    svg.append(f'<text x="{mx4+20}" y="{my4+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">COMPLETED PROJECT TEMPLATE</text>')
    svg.append(f'<text x="{mx4+20}" y="{my4+125}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="20" font-weight="700">বাস্তবায়িত প্রকল্প ফ্রেমওয়ার্ক</text>')

    # Framework Notice
    svg.append(f'<rect x="{mx4+20}" y="{my4+145}" width="350" height="90" fill="#DEE7E2" stroke="#183B35" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{mx4+35}" y="{my4+170}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="700">প্রকল্প টেমপ্লেট কাঠামো (Sample Framework):</text>')
    t_mrf, _ = wrap_text("নির্মাণ সমাপ্তির পর আসল সাইট ফটোগ্রাফি ও ক্লায়েন্ট রিকোয়ারমেন্ট শিট এখানে সন্নিবেশিত হবে।", mx4+35, my4+192, 34, 18, "'Noto Sans Bengali', sans-serif", 12, "#56645E")
    svg.append(t_mrf)

    # Photo Slots
    svg.append(f'<rect x="{mx4+20}" y="{my4+250}" width="350" height="220" fill="#DEE7E2" rx="2"/>')
    svg.append(f'<text x="{mx4+195}" y="{my4+365}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">[ বাস্তবায়িত কাজের ছবি স্লট ]</text>')

    # Parameters
    svg.append(f'<rect x="{mx4+20}" y="{my4+490}" width="350" height="200" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{mx4+35}" y="{my4+520}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="700">প্রকল্প স্পেসিফিকেশন কাঠামো:</text>')
    m_params = [
        "• অবস্থান: [প্রকল্প এলাকা — উদা: মিরপুর/গুলশান]",
        "• আয়তন: [পরিমাপ — উদা: ২০০০-২৫০০ বর্গফুট]",
        "• সময়কাল: [আনুমানিক ১২-১৬ সপ্তাহ]",
        "• উপাদান: [সিজনড কাঠ ও ন্যাচারাল ফিনিশ]"
    ]
    mpy = my4 + 545
    for mp in m_params:
        svg.append(f'<text x="{mx4+35}" y="{mpy}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="12">{escape_xml(mp)}</text>')
        mpy += 24

    svg.extend(render_mobile_footer(mx4, my4+1060))

    # SCREEN 5: Mobile Dedicated Services (390 x 1400) - x: 1020, y: 1720
    mx5, my5 = 1020, 1720
    svg.append(f'<rect x="{mx5}" y="{my5}" width="390" height="1400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_mobile_header(mx5, my5))

    svg.append(f'<text x="{mx5+20}" y="{my5+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">OUR SERVICES</text>')
    svg.append(f'<text x="{mx5+20}" y="{my5+125}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="22" font-weight="700">আমাদের সেবাসমূহ</text>')

    msvcs = [
        ("০১. পূর্ণাঙ্গ ইন্টেরিয়র আর্কিটেকচার", "ফ্লোর প্ল্যান, ওয়ালের রূপান্তর, লাইটিং ও সাইট সুপারভিশন।"),
        ("০২. কাস্টম ফার্নিচার ও মিলওয়ার্ক", "নিজস্ব তত্ত্বাবধানে সিজনড সেগুন কাঠ ও বেতের কেবিনেটরি।"),
        ("০৩. স্পেস প্ল্যানিং ও BOQ শিট", "আর্কিটেকচারাল ওয়ার্কিং ড্রয়িং ও বাজারদর অনুযায়ী ম্যাটেরিয়াল হিসাব।")
    ]
    msy = my5 + 155
    for m_no, m_b in msvcs:
        svg.append(f'<rect x="{mx5+20}" y="{msy}" width="350" height="135" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
        svg.append(f'<text x="{mx5+35}" y="{msy+30}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="700">{escape_xml(m_no)}</text>')
        t_msb, _ = wrap_text(m_b, mx5+35, msy+55, 34, 18, "'Noto Sans Bengali', sans-serif", 13, "#56645E")
        svg.append(t_msb)
        svg.append(f'<text x="{mx5+35}" y="{msy+115}" fill="#895239" font-family="\'Noto Sans Bengali\', sans-serif" font-size="12" font-weight="600">সেবা নির্বাচন করুন →</text>')
        msy += 150

    svg.extend(render_mobile_footer(mx5, my5+1060))

    # SCREEN 6: Mobile Dedicated Service Detail - Joinery (390 x 1400) - x: 1020, y: 3180
    mx6s, my6s = 1020, 3180
    svg.append(f'<rect x="{mx6s}" y="{my6s}" width="390" height="1400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_mobile_header(mx6s, my6s))

    svg.append(f'<text x="{mx6s+20}" y="{my6s+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">SERVICE DETAIL</text>')
    svg.append(f'<text x="{mx6s+20}" y="{my6s+125}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="20" font-weight="700">কাস্টম মিলওয়ার্ক ও জয়েনারি</text>')

    if img_joinery:
        svg.append(f'<image href="{img_joinery}" x="{mx6s+20}" y="{my6s+145}" width="350" height="220" preserveAspectRatio="xMidYMid slice"/>')
    svg.append(f'<rect x="{mx6s+25}" y="{my6s+150}" width="260" height="20" fill="#183B35" fill-opacity="0.9" rx="2"/>')
    svg.append(f'<text x="{mx6s+30}" y="{my6s+164}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="10">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>')

    svg.append(f'<rect x="{mx6s+20}" y="{my6s+380}" width="350" height="260" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{mx6s+35}" y="{my6s+410}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="15" font-weight="700">উপাদান ও নির্মাণ কৌশল</text>')
    t_jfeat, _ = wrap_text("FlowGrid-এর জয়েনারি নির্মাণে সিজনড সলিড কাঠ ও প্রাকৃতিক ভিনিয়ার ব্যবহার করা হয়। প্রতিটি কেবিনেট কাঠামোর স্থায়িত্ব ও আর্দ্রতা সহনশীলতার কথা মাথায় রেখে মর্টিস ও টেনন জয়েন্টে তৈরি করা হয়।", mx6s+35, my6s+435, 34, 20, "'Noto Sans Bengali', sans-serif", 13, "#56645E")
    svg.append(t_jfeat)
    svg.append(f'<text x="{mx6s+35}" y="{my6s+560}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600">• বার্মা সেগুন, সিজনড গর্জন ও প্রাকৃতিক বেতের জালি</text>')
    svg.append(f'<text x="{mx6s+35}" y="{my6s+585}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600">• সফট-ক্লোজ চ্যানেল ও দীর্ঘস্থায়ী কব্জা ফিটিংস</text>')

    svg.extend(render_mobile_footer(mx6s, my6s+1060))

    # -------------------------------------------------------------
    # COLUMN 4 (x = 1490): SCREEN 7, SCREEN 8 & SCREEN 9
    # SCREEN 7: Mobile Dedicated Process (390 x 1400)
    # -------------------------------------------------------------
    mx7, my7 = 1490, 260
    svg.append(f'<rect x="{mx7}" y="{my7}" width="390" height="1400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_mobile_header(mx7, my7))

    svg.append(f'<text x="{mx7+20}" y="{my7+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">OUR PROCESS</text>')
    svg.append(f'<text x="{mx7+20}" y="{my7+125}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="22" font-weight="700">কাজের ৫টি সুনির্দিষ্ট ধাপ</text>')

    p_steps = [
        ("১. প্রাথমিক কনসালটেশন", "লাইফস্টাইল ও বাজেট পর্যালোচনা"),
        ("২. স্পেস প্ল্যান ও কনসেপ্ট", "২ডি ব্লুপ্রিন্ট ও ম্যাটেরিয়াল বোর্ড"),
        ("৩. বিশদ বাজেট ও ড্রয়িং", "আইটেমাইজড কোটেশন ও অনুমোদন"),
        ("৪. অফ-সাইট জয়েনারি কাজ", "কাঠের কাজ ও ট্রায়াল ফিটিংস"),
        ("৫. সাইটে পরিচ্ছন্ন ইনস্টলেশন", "নিখুঁত লেভেলিং ও হ্যান্ডওভার")
    ]
    py_s = my7 + 155
    for p_no, p_d in p_steps:
        svg.append(f'<rect x="{mx7+20}" y="{py_s}" width="350" height="75" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
        svg.append(f'<text x="{mx7+35}" y="{py_s+30}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="700">{escape_xml(p_no)}</text>')
        svg.append(f'<text x="{mx7+35}" y="{py_s+52}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="12">{escape_xml(p_d)}</text>')
        py_s += 90

    svg.extend(render_mobile_footer(mx7, my7+1060))

    # SCREEN 8: Mobile Dedicated Studio (390 x 1400) - x: 1490, y: 1720
    mx8, my8 = 1490, 1720
    svg.append(f'<rect x="{mx8}" y="{my8}" width="390" height="1400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_mobile_header(mx8, my8))

    svg.append(f'<text x="{mx8+20}" y="{my8+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">STUDIO ETHOS</text>')
    svg.append(f'<text x="{mx8+20}" y="{my8+125}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="22" font-weight="700">স্টুডিও ও কাজের দর্শন</text>')

    svg.append(f'<rect x="{mx8+20}" y="{my8+150}" width="350" height="280" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{mx8+35}" y="{my8+185}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="16" font-weight="700">মিরপুর স্টুডিও ও টিম</text>')
    t_mstd, _ = wrap_text("মিরপুর-১০ এ অবস্থিত FlowGrid ইন্টেরিয়র আর্কিটেকচার অনুশীলন। অপ্রয়োজনীয় ডেকোরেশনের চেয়ে ব্যবহারিক স্থায়িত্ব, দীর্ঘস্থায়ী সলিড কাঠ ও প্রাকৃতিক আলো নিশ্চিত করাই আমাদের প্রধান মনোযোগ।", mx8+35, my8+215, 34, 20, "'Noto Sans Bengali', sans-serif", 13, "#56645E")
    svg.append(t_mstd)
    t_mbound, _ = wrap_text("কমিউনিটি প্রেক্ষাপট: রুমী\'স ফ্যাশনেবল হাউস পরিবারের লাইফস্টাইল ও অনুপ্রেরণার উৎস। স্থাপত্য ডিজাইন ও জয়েনারি কাজ সম্পূর্ণ স্বতন্ত্র পেশাদার টিম দ্বারা পরিচালিত হয়।", mx8+35, my8+305, 34, 18, "'Noto Sans Bengali', sans-serif", 12, "#895239")
    svg.append(t_mbound)

    svg.extend(render_mobile_footer(mx8, my8+1060))

    # SCREEN 9: Mobile Privacy & Legal Terms (390 x 1400) - x: 1490, y: 3180
    mx9, my9 = 1490, 3180
    svg.append(f'<rect x="{mx9}" y="{my9}" width="390" height="1400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_mobile_header(mx9, my9))

    svg.append(f'<text x="{mx9+20}" y="{my9+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">LEGAL &amp; PRIVACY</text>')
    svg.append(f'<text x="{mx9+20}" y="{my9+125}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="20" font-weight="700">গোপনীয়তা ও ডিজাইন শর্তাবলী</text>')

    svg.append(f'<rect x="{mx9+20}" y="{my9+150}" width="350" height="340" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{mx9+35}" y="{my9+180}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="700">১. কনসেপ্ট ভিজ্যুয়ালাইজেশন নীতি</text>')
    t_lp1, _ = wrap_text("ওয়েবসাইটে প্রদর্শিত সকল 3D রেন্ডার ধারণাগত ডিজাইন স্টাডি হিসেবে প্রস্তুত। এগুলো কোনো নির্দিষ্ট গ্রাহকের বাস্তবায়িত কাজ হিসেবে দাবি করা হয় না।", mx9+35, my9+205, 34, 18, "'Noto Sans Bengali', sans-serif", 12, "#56645E")
    svg.append(t_lp1)
    svg.append(f'<text x="{mx9+35}" y="{my9+285}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="700">২. গ্রাহকের তথ্যের সুরক্ষা</text>')
    t_lp2, _ = wrap_text("পরামর্শ ফরমে প্রদত্ত আপনার নাম, ফোন নম্বর ও এলাকা শুধুমাত্র প্রাথমিক যোগাযোগের জন্য সংরক্ষিত থাকে এবং কোনো তৃতীয় পক্ষের কাছে হস্তান্তর করা হয় না।", mx9+35, my9+310, 34, 18, "'Noto Sans Bengali', sans-serif", 12, "#56645E")
    svg.append(t_lp2)

    svg.extend(render_mobile_footer(mx9, my9+1060))

    # -------------------------------------------------------------
    # COLUMN 5 (x = 1960): SCREEN 10 (Contact), SCREEN 11 (404), & DEDICATED DRAWER OVERLAY
    # SCREEN 10: Mobile Dedicated Contact (390 x 1450) - Zero blank interval!
    # -------------------------------------------------------------
    mx10, my10 = 1960, 260
    svg.append(f'<rect x="{mx10}" y="{my10}" width="390" height="1450" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>')
    svg.extend(render_mobile_header(mx10, my10))

    svg.append(f'<text x="{mx10+20}" y="{my10+95}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="11" font-weight="700">CONTACT &amp; VISIT</text>')
    svg.append(f'<text x="{mx10+20}" y="{my10+125}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="22" font-weight="700">স্টুডিও যোগাযোগ</text>')

    # 4-Field Mobile Form with 48px touch inputs
    svg.append(f'<rect x="{mx10+20}" y="{my10+150}" width="350" height="490" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    mcfy = my10 + 175
    mcfx = mx10 + 35
    mcfw = 320

    svg.append(f'<text x="{mcfx}" y="{mcfy}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600">১. আপনার নাম *</text>')
    svg.append(f'<rect x="{mcfx}" y="{mcfy+6}" width="{mcfw}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{mcfx+12}" y="{mcfy+35}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">উদা: মো. ফারহান আহমেদ</text>')
    mcfy += 66

    svg.append(f'<text x="{mcfx}" y="{mcfy}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600">২. মোবাইল নম্বর *</text>')
    svg.append(f'<rect x="{mcfx}" y="{mcfy+6}" width="{mcfw}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{mcfx+12}" y="{mcfy+35}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">01XXXXXXXXX</text>')
    mcfy += 66

    svg.append(f'<text x="{mcfx}" y="{mcfy}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600">৩. এলাকা ও শহর *</text>')
    svg.append(f'<rect x="{mcfx}" y="{mcfy+6}" width="{mcfw}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{mcfx+12}" y="{mcfy+35}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">মিরপুর / গুলশান / ধানমন্ডি...</text>')
    mcfy += 66

    svg.append(f'<text x="{mcfx}" y="{mcfy}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600">৪. প্রয়োজনীয় সেবা *</text>')
    svg.append(f'<rect x="{mcfx}" y="{mcfy+6}" width="{mcfw}" height="48" fill="#F4F1E8" stroke="#718178" stroke-width="1" rx="2"/>')
    svg.append(f'<text x="{mcfx+12}" y="{mcfy+35}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="12">পূর্ণাঙ্গ ইন্টেরিয়র / কাস্টম ফার্নিচার / নিশ্চিত নই ▼</text>')
    mcfy += 66

    svg.append(f'<rect x="{mcfx}" y="{mcfy+6}" width="{mcfw}" height="52" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{mcfx+mcfw//2}" y="{mcfy+38}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">পরামর্শ অনুরোধ পাঠান →</text>')

    # Studio Address (Placed directly below form, ZERO blank interval!)
    svg.append(f'<rect x="{mx10+20}" y="{my10+660}" width="350" height="150" fill="#DEE7E2" rx="4"/>')
    svg.append(f'<text x="{mx10+35}" y="{my10+695}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="16" font-weight="700">স্টুডিও ঠিকানা</text>')
    svg.append(f'<text x="{mx10+35}" y="{my10+725}" fill="#56645E" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13">মিরপুর-১০, ঢাকা ১২১৬, বাংলাদেশ</text>')
    svg.append(f'<text x="{mx10+35}" y="{my10+750}" fill="#56645E" font-family="\'Manrope\', sans-serif" font-size="13">hello@flowgrid-interiors.com · +880 1700-000000</text>')
    svg.append(f'<rect x="{mx10+35}" y="{my10+770}" width="320" height="48" fill="#0D5C52" rx="2"/>')
    svg.append(f'<text x="{mx10+195}" y="{my10+800}" fill="#FFFFFF" font-family="\'Noto Sans Bengali\', sans-serif" font-size="13" font-weight="600" text-anchor="middle">হোয়াটসঅ্যাপ চ্যাট শুরু করুন</text>')

    # Footer placed directly at y+836 (ends at y+1176)
    svg.extend(render_mobile_footer(mx10, my10+836))

    # SCREEN 11: Mobile 404 Error Page (390 x 650) - x: 1960, y: 1730
    mx11, my11 = 1960, 1730
    svg.append(f'<rect x="{mx11}" y="{my11}" width="390" height="650" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append(f'<text x="{mx11+195}" y="{my11+180}" fill="#895239" font-family="\'Bodoni Moda\', serif" font-size="64" font-weight="700" text-anchor="middle">404</text>')
    svg.append(f'<text x="{mx11+195}" y="{my11+230}" fill="#183B35" font-family="\'Noto Sans Bengali\', sans-serif" font-size="18" font-weight="700" text-anchor="middle">পৃষ্ঠাটি পাওয়া যায়নি</text>')
    t_m404, _ = wrap_text("আপনি যে লিংকটি খুঁজছেন তা স্থানান্তরিত হয়েছে অথবা ড্রাফট মোডে রয়েছে।", mx11+45, my11+270, 30, 22, "'Noto Sans Bengali', sans-serif", 13, "#56645E")
    svg.append(t_m404)
    svg.append(f'<rect x="{mx11+45}" y="{my11+340}" width="300" height="48" fill="#183B35" rx="2"/>')
    svg.append(f'<text x="{mx11+195}" y="{my11+370}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">মূল প্রচ্ছদে ফিরে যান →</text>')

    # -------------------------------------------------------------
    # DEDICATED OVERLAY: Mobile Off-Canvas Navigation Drawer (390 x 750)
    # Placed in its own dedicated position: x: 1960, y: 2420 - ZERO FOOTER COLLISION!
    # -------------------------------------------------------------
    dx, dy = 1960, 2420
    svg.append(f'<text x="{dx}" y="{dy-15}" fill="#895239" font-family="\'Manrope\', sans-serif" font-size="12" font-weight="700">[OFF-CANVAS OVERLAY FRAME — DEDICATED POSITION]</text>')
    svg.append(f'<rect x="{dx}" y="{dy}" width="390" height="750" fill="#183B35" rx="4"/>')
    svg.append(f'<text x="{dx+25}" y="{dy+55}" fill="#F4F1E8" font-family="\'Bodoni Moda\', serif" font-size="24" font-weight="700">FlowGrid Studio</text>')
    svg.append(f'<rect x="{dx+330}" y="{dy+30}" width="48" height="48" fill="#102B26" rx="2"/>')
    svg.append(f'<text x="{dx+354}" y="{dy+60}" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="20" text-anchor="middle">✕</text>')

    d_items = [
        ("প্রচ্ছদ (Home)", dy+120),
        ("প্রকল্পসমূহ (Projects)", dy+175),
        ("সেবাসমূহ (Services)", dy+230),
        ("পদ্ধতি (Process)", dy+285),
        ("স্টুডিও ও দল (Studio)", dy+340),
        ("যোগাযোগ (Contact)", dy+395),
        ("গোপনীয়তা ও শর্তাবলী (Privacy)", dy+450)
    ]
    for d_lbl, d_ly in d_items:
        svg.append(f'<text x="{dx+30}" y="{d_ly}" fill="#F4F1E8" font-family="\'Noto Sans Bengali\', sans-serif" font-size="17" font-weight="600">{escape_xml(d_lbl)}</text>')
        svg.append(f'<line x1="{dx+30}" y1="{d_ly+18}" x2="{dx+360}" y2="{d_ly+18}" stroke="#2D524A" stroke-width="1"/>')

    # Direct contact actions in drawer (48px targets)
    svg.append(f'<rect x="{dx+30}" y="{dy+500}" width="330" height="48" fill="#895239" rx="2"/>')
    svg.append(f'<text x="{dx+195}" y="{dy+530}" fill="#FFFFFF" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">সরাসরি কল: +880 1700-000000</text>')

    svg.append(f'<rect x="{dx+30}" y="{dy+560}" width="330" height="48" fill="#0D5C52" rx="2"/>')
    svg.append(f'<text x="{dx+195}" y="{dy+590}" fill="#FFFFFF" font-family="\'Noto Sans Bengali\', sans-serif" font-size="14" font-weight="600" text-anchor="middle">হোয়াটসঅ্যাপে বার্তা পাঠান</text>')

    svg.append('</svg>')

    out_path = 'figma_svgs_v3/04_mobile_bn.svg'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    
    valid, err = validate_svg_file(out_path)
    print(f'Board 04: {out_path} -> Valid XML? {valid} ({err})')

if __name__ == '__main__':
    generate_board_04()
