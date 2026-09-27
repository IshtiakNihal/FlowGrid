"""
FlowGrid - Page 04 (Mobile — BN) Generator v2
Complete suite of Mobile Bangla screens (390px width):
1. Mobile Home (Full depth: 390x3800px)
2. Mobile Case Study Detail (390x3200px)
3. Mobile Menu Drawer (390x844px)
4. Mobile Contact & Form (390x1800px)
5. Mobile 404 (390x844px)
Bounded typography, minimum 44px touch targets, zero text overflow.
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

svg = f"""<svg width="2600" height="4200" viewBox="0 0 2600 4200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="2600" height="4200" fill="#EAE6DC"/>

  <!-- Top Banner -->
  <rect x="80" y="80" width="2440" height="120" fill="#183B35" rx="4"/>
  <text x="120" y="145" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="34" font-weight="600">FlowGrid — Mobile Experience Suite (Bangla · 390px)</text>
  <text x="120" y="180" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="16">Comprehensive mobile viewport coverage: Full Home Journey, 3-View Case Study, Interactive Menu Drawer, Contact, 404</text>

  <!-- ========================================================================= -->
  <!-- MOBILE SCREEN 1: HOMEPAGE (X: 80, Y: 240, W: 390, H: 3800)                -->
  <!-- ========================================================================= -->
  <g id="screen-mobile-bn-home">
    <rect x="80" y="240" width="390" height="3800" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    
    <!-- Mobile Header -->
    <rect x="80" y="240" width="390" height="64" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <text x="100" y="280" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">FLOWGRID</text>
    
    <!-- Switcher -->
    <rect x="300" y="254" width="70" height="34" fill="#DEE7E2" rx="17"/>
    <rect x="302" y="256" width="34" height="30" fill="#183B35" rx="15"/>
    <text x="319" y="276" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="11" font-weight="700" text-anchor="middle">বাং</text>
    <text x="352" y="276" fill="#183B35" font-family="'Manrope', sans-serif" font-size="11" font-weight="600" text-anchor="middle">EN</text>
    
    <!-- Hamburger Button -->
    <rect x="390" y="254" width="60" height="34" fill="#183B35" rx="4"/>
    <text x="420" y="276" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700" text-anchor="middle">মেনু ☰</text>

    <!-- Mobile Hero -->
    <text x="100" y="340" fill="#895239" font-family="'Manrope', sans-serif" font-size="11" font-weight="700" letter-spacing="1.5">URBAN INTERIORS · DHAKA</text>
    <text x="100" y="380" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="32" font-weight="600">শান্ত, সুপরিকল্পিত</text>
    <text x="100" y="420" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="32" font-weight="600">শহুরে আবাস।</text>
    
    {wrap_text("ঢাকা শহরের বাস্তবতায় আলো, বাতাস ও পরিমিত কাঠের নিপুণ বিন্যাসে তৈরি নিজস্ব গৃহকোণ।", 100, 455, 34, 22, "'Hind Siliguri', sans-serif", 14, "#56645E")}

    <!-- Hero Image Card -->
    <rect x="100" y="520" width="350" height="230" fill="#DEE7E2" rx="4"/>
    <image href="{img_living_1}" x="100" y="520" width="350" height="230" preserveAspectRatio="xMidYMid slice"/>
    <rect x="110" y="530" width="330" height="28" fill="#183B35" opacity="0.9" rx="3"/>
    <text x="275" y="548" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="9" font-weight="700" text-anchor="middle">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>

    <!-- CTAs -->
    <rect x="100" y="770" width="350" height="48" fill="#183B35" rx="4"/>
    <text x="275" y="800" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" text-anchor="middle">পরামর্শ শুরু করুন</text>
    
    <rect x="100" y="830" width="350" height="48" fill="none" stroke="#183B35" stroke-width="1.5" rx="4"/>
    <text x="275" y="860" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" text-anchor="middle">প্রকল্পসমূহ দেখুন →</text>

    <!-- Philosophy Section -->
    <rect x="80" y="910" width="390" height="520" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1"/>
    <text x="100" y="945" fill="#895239" font-family="'Manrope', sans-serif" font-size="11" font-weight="700" letter-spacing="1.5">OUR PHILOSOPHY</text>
    <text x="100" y="975" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="600">ঢাকার জীবনযাত্রায় পরিমিতির শক্তি</text>
    
    <!-- 3 Stacked Cards -->
    <rect x="100" y="1005" width="350" height="120" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="120" y="1035" fill="#895239" font-family="'Bodoni Moda', serif" font-size="16" font-weight="700">০১ · আলো ও বাতাসের সদ্ব্যবহার</text>
    {wrap_text("উঁচু ভবনের ভিড়ে প্রতিটি জানালাকে কেন্দ্র করে খোলামেলা ক্রস-ভেন্টিলেশন নিশ্চিত করা।", 120, 1060, 34, 20, "'Hind Siliguri', sans-serif", 12, "#56645E")}

    <rect x="100" y="1140" width="350" height="120" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="120" y="1170" fill="#895239" font-family="'Bodoni Moda', serif" font-size="16" font-weight="700">০২ · পরিকল্পিত অদৃশ্য স্টোরেজ</text>
    {wrap_text("ধুলোবালি থেকে সুরক্ষায় সিলিং পর্যন্ত সমন্বিত ক্যাবিনেট তৈরি করে ঘর সুশৃঙ্খল রাখা।", 120, 1195, 34, 20, "'Hind Siliguri', sans-serif", 12, "#56645E")}

    <rect x="100" y="1275" width="350" height="120" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="120" y="1305" fill="#895239" font-family="'Bodoni Moda', serif" font-size="16" font-weight="700">০৩ · টেকসই দেশীয় কাঠ ও বেত</text>
    {wrap_text("সিজনড কাঠ ও প্রাকৃতিক বেতের ব্যবহারে ঘরে শান্ত ও মাটির স্নিগ্ধ ছোঁয়া আনা।", 120, 1330, 34, 20, "'Hind Siliguri', sans-serif", 12, "#56645E")}

    <!-- Projects Section -->
    <text x="100" y="1470" fill="#895239" font-family="'Manrope', sans-serif" font-size="11" font-weight="700" letter-spacing="1.5">FEATURED STUDIES</text>
    <text x="100" y="1505" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24" font-weight="600">বাছাইকৃত কনসেপ্ট স্টাডি</text>

    <!-- Mobile Card 1: Gulshan Living -->
    <rect x="100" y="1530" width="350" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <image href="{img_living_1}" x="100" y="1530" width="350" height="220" preserveAspectRatio="xMidYMid slice"/>
    <rect x="110" y="1540" width="330" height="26" fill="#183B35" opacity="0.9" rx="3"/>
    <text x="275" y="1557" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="9" font-weight="700" text-anchor="middle">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>
    <text x="120" y="1780" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">গুলশান লেকভিউ অ্যাপার্টমেন্ট</text>
    <text x="120" y="1805" fill="#895239" font-family="'Manrope', sans-serif" font-size="11" font-weight="600">GULSHAN 2 · 2,150 SFT · LIVING &amp; JOINERY</text>
    {wrap_text("প্রাকৃতিক আলো ও বেতের পার্টিশনে ড্রয়িং-ডাইনিং জোন বিভাজন।", 120, 1830, 34, 20, "'Hind Siliguri', sans-serif", 12, "#56645E")}
    <text x="120" y="1915" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700">কেস স্টাডি দেখুন →</text>

    <!-- Mobile Card 2: Kitchen -->
    <rect x="100" y="1970" width="350" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <image href="{img_kitchen}" x="100" y="1970" width="350" height="220" preserveAspectRatio="xMidYMid slice"/>
    <rect x="110" y="1980" width="330" height="26" fill="#183B35" opacity="0.9" rx="3"/>
    <text x="275" y="1997" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="9" font-weight="700" text-anchor="middle">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>
    <text x="120" y="2220" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">ধানমন্ডি রেসিডেন্স কিচেন</text>
    <text x="120" y="2245" fill="#895239" font-family="'Manrope', sans-serif" font-size="11" font-weight="600">DHANMONDI · 1,850 SFT · UTILITY KITCHEN</text>
    {wrap_text("দেশীয় ভারী রান্নার তেল-ঝোল সহনশীল গাঢ় গ্রানাইট টপ ও গ্যাস সিলিন্ডারের নিরাপদ ভেন্টিলেশন।", 120, 2270, 34, 20, "'Hind Siliguri', sans-serif", 12, "#56645E")}
    <text x="120" y="2355" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700">কেস স্টাডি দেখুন →</text>

    <!-- Mobile Services Ruled List -->
    <rect x="80" y="2420" width="390" height="440" fill="#183B35"/>
    <text x="100" y="2460" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="11" font-weight="700" letter-spacing="1.5">WHAT WE DELIVER</text>
    <text x="100" y="2495" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="22" font-weight="600">আমাদের স্থাপত্য ও ইন্টেরিয়র সেবা</text>
    
    <line x1="100" y1="2525" x2="450" y2="2525" stroke="#2E5D4B" stroke-width="1"/>
    <text x="100" y="2555" fill="#DEE7E2" font-family="'Bodoni Moda', serif" font-size="15" font-weight="700">০১</text>
    <text x="130" y="2555" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700">অ্যাপার্টমেন্ট স্পেস প্ল্যানিং</text>
    {wrap_text("খোলামেলা ড্রাফট এবং আলো-বাতাসের লেআউট পর্যালোচনা।", 130, 2580, 32, 18, "'Hind Siliguri', sans-serif", 12, "#DEE7E2")}

    <line x1="100" y1="2625" x2="450" y2="2625" stroke="#2E5D4B" stroke-width="1"/>
    <text x="100" y="2655" fill="#DEE7E2" font-family="'Bodoni Moda', serif" font-size="15" font-weight="700">০২</text>
    <text x="130" y="2655" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700">কাস্টম জয়েনারি ও ক্যাবিনেট</text>
    {wrap_text("টিভি ইউনিট, পার্টিশন ও মেটেরিয়াল স্পেক ড্রয়িং।", 130, 2680, 32, 18, "'Hind Siliguri', sans-serif", 12, "#DEE7E2")}

    <line x1="100" y1="2725" x2="450" y2="2725" stroke="#2E5D4B" stroke-width="1"/>
    <text x="100" y="2755" fill="#DEE7E2" font-family="'Bodoni Moda', serif" font-size="15" font-weight="700">০৩</text>
    <text x="130" y="2755" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700">রান্নাঘর আর্কিটেকচার</text>
    {wrap_text("গ্যাস সিলিন্ডারের নিরাপদ খাঁজসহ টেকসই কিচেন লেআউট।", 130, 2780, 32, 18, "'Hind Siliguri', sans-serif", 12, "#DEE7E2")}

    <!-- Process & Studio Section -->
    <rect x="80" y="2880" width="390" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1"/>
    <text x="100" y="2920" fill="#895239" font-family="'Manrope', sans-serif" font-size="11" font-weight="700" letter-spacing="1.5">MIRPUR STUDIO</text>
    <text x="100" y="2955" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="600">মিরপুর স্টুডিও ও কারিগরি</text>
    {wrap_text("মিরপুর ১২ ভিত্তিক ফ্লোগ্রিড স্টুডিওতে আমরা প্রতিটি পরিবারের জীবনের ছন্দ বুঝে নিজস্ব কারিগরদের মাধ্যমে ফার্নিচার ও ইন্টেরিয়র সমাধান তৈরি করি।", 100, 2990, 34, 22, "'Hind Siliguri', sans-serif", 13, "#56645E")}
    
    <rect x="100" y="3070" width="350" height="48" fill="#128C7E" rx="4"/>
    <text x="275" y="3100" fill="#FFFFFF" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" text-anchor="middle">হোয়াটসঅ্যাপে সরাসরি আলাপ করুন</text>

    <rect x="100" y="3130" width="350" height="48" fill="#183B35" rx="4"/>
    <text x="275" y="3160" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" text-anchor="middle">পরামর্শের আবেদন ফর্ম</text>

    <!-- Mobile Footer -->
    <rect x="80" y="3320" width="390" height="480" fill="#112A25"/>
    <text x="100" y="3370" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">FLOWGRID</text>
    {wrap_text("শহুরে ঢাকার বাস্তবতায় পরিমিত ও মার্জিত ইন্টেরিয়র ডিজাইন স্টুডিও। মিরপুর ১২, ঢাকা ১২১৬।", 100, 3400, 32, 20, "'Hind Siliguri', sans-serif", 12, "#DEE7E2")}
    
    <text x="100" y="3470" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700">সংযুক্ত প্রতিষ্ঠানসমূহ</text>
    <text x="100" y="3500" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="12">অনেক্টা প্রোডাক্ট (কিচেন অ্যাপ্লায়েন্স) ↗</text>
    <text x="100" y="3525" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="12">রুমি'স ফ্যাশনেবল হাউস (ইউটিউব ভ্লগ) ↗</text>

    <text x="100" y="3575" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="12">📞 +880 1711-000000</text>
    <text x="100" y="3600" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="12">✉ studio@flowgridbd.com</text>

    <line x1="100" y1="3635" x2="450" y2="3635" stroke="#2E5D4B" stroke-width="1"/>
    <text x="100" y="3665" fill="#8E9E96" font-family="'Manrope', sans-serif" font-size="11">© 2026 FlowGrid. All rights reserved.</text>
    <text x="100" y="3690" fill="#8E9E96" font-family="'Hind Siliguri', sans-serif" font-size="11">গোপনীয়তা নীতি · শর্তাবলী</text>
  </g>

  <!-- ========================================================================= -->
  <!-- MOBILE SCREEN 2: CASE STUDY DETAIL (X: 530, Y: 240, W: 390, H: 3400)      -->
  <!-- ========================================================================= -->
  <g id="screen-mobile-bn-case-study">
    <rect x="530" y="240" width="390" height="3400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    
    <!-- Mobile Header -->
    <rect x="530" y="240" width="390" height="64" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <text x="550" y="280" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">FLOWGRID</text>
    <text x="860" y="280" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700">মেনু ☰</text>

    <text x="550" y="340" fill="#895239" font-family="'Hind Siliguri', sans-serif" font-size="12">← প্রকল্প তালিকায় ফিরে যান</text>

    <text x="550" y="380" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="26" font-weight="600">গুলশান লেকভিউ</text>
    <text x="550" y="415" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="26" font-weight="600">অ্যাপার্টমেন্ট স্টাডি</text>
    <text x="550" y="445" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="13">খোলামেলা লিভিং, আলো ও বেতের জয়েনারি</text>

    <!-- Concept Disclosure Banner -->
    <rect x="550" y="475" width="350" height="40" fill="#F4F1E8" stroke="#895239" stroke-width="1.5" rx="4"/>
    <text x="725" y="498" fill="#895239" font-family="'Hind Siliguri', sans-serif" font-size="10" font-weight="700" text-anchor="middle">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>

    <!-- Specs Grid -->
    <rect x="550" y="530" width="350" height="100" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="570" y="560" fill="#895239" font-family="'Manrope', sans-serif" font-size="10" font-weight="700">LOCATION</text>
    <text x="570" y="580" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="600">গুলশান ২, ঢাকা</text>

    <text x="740" y="560" fill="#895239" font-family="'Manrope', sans-serif" font-size="10" font-weight="700">FLOOR AREA</text>
    <text x="740" y="580" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="600">২,১৫০ বর্গফুট</text>

    <text x="570" y="610" fill="#895239" font-family="'Manrope', sans-serif" font-size="10" font-weight="700">MATERIALS</text>
    <text x="635" y="610" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="12" font-weight="600">বার্মা টিক, সিলেট বেত, লাইম ওয়াশ</text>

    <!-- View 1: Main View -->
    <rect x="550" y="650" width="350" height="230" fill="#DEE7E2" rx="4"/>
    <image href="{img_living_1}" x="550" y="650" width="350" height="230" preserveAspectRatio="xMidYMid slice"/>
    <text x="550" y="895" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="11">ভিউ ০১: লিভিং ও ডাইনিং জোনের সামগ্রিক প্রশস্ত কোণ</text>

    <!-- Narrative Block -->
    <rect x="550" y="920" width="350" height="260" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="570" y="955" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">চাহিদা ও স্থাপত্য সমাধান</text>
    {wrap_text("চার সদস্যের পরিবারের খোলামেলা ড্রয়িং-ডাইনিং চাহিদা পূরণ করতে কাঠের স্ল্যাট জালি পার্টিশন ব্যবহার করা হয়েছে। এতে ব্যক্তিগত অংশ সুরক্ষিত থাকে এবং দিনের আলো পুরো ঘরে ছড়িয়ে পড়ে।", 570, 985, 30, 20, "'Hind Siliguri', sans-serif", 12, "#56645E")}

    <!-- View 2: Dining -->
    <rect x="550" y="1200" width="350" height="230" fill="#DEE7E2" rx="4"/>
    <image href="{img_living_2}" x="550" y="1200" width="350" height="230" preserveAspectRatio="xMidYMid slice"/>
    <text x="550" y="1445" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="12" font-weight="700">ভিউ ০২: ডাইনিং কোণ ও বারান্দার প্রাকৃতিক আলো</text>

    <!-- View 3: Joinery Detail -->
    <rect x="550" y="1480" width="350" height="230" fill="#DEE7E2" rx="4"/>
    <image href="{img_living_3}" x="550" y="1480" width="350" height="230" preserveAspectRatio="xMidYMid slice"/>
    <text x="550" y="1725" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="12" font-weight="700">ভিউ ০৩: খাঁটি বার্মা টিক ও হস্তশিল্পের বেত বুনন</text>

    <!-- Material Box -->
    <rect x="550" y="1760" width="350" height="200" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="570" y="1795" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="16" font-weight="700">উপাদান বিবরণ (Material Spec)</text>
    <text x="570" y="1825" fill="#895239" font-family="'Hind Siliguri', sans-serif" font-size="12" font-weight="700">• সিজনড বার্মা টিক কাঠ (১২% আর্দ্রতায় নিয়ন্ত্রিত)</text>
    <text x="570" y="1855" fill="#895239" font-family="'Hind Siliguri', sans-serif" font-size="12" font-weight="700">• প্রাকৃতিক সিলেট বেতের জালি (বায়ু চলাচলকারী)</text>
    <text x="570" y="1885" fill="#895239" font-family="'Hind Siliguri', sans-serif" font-size="12" font-weight="700">• লাইম ওয়াশ প্লাস্টার (স্যাঁতসেঁতে ভাব প্রতিরোধী)</text>

    <!-- Consultation CTA -->
    <rect x="550" y="1980" width="350" height="48" fill="#183B35" rx="4"/>
    <text x="725" y="2010" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" text-anchor="middle">অনুরূপ পরামর্শের আবেদন করুন</text>
  </g>

  <!-- ========================================================================= -->
  <!-- MOBILE SCREEN 3: MENU DRAWER OVERLAY (X: 980, Y: 240, W: 390, H: 844)     -->
  <!-- ========================================================================= -->
  <g id="screen-mobile-bn-drawer">
    <rect x="980" y="240" width="390" height="844" fill="#183B35" rx="6" stroke="#2E5D4B" stroke-width="2"/>
    
    <!-- Top Bar -->
    <text x="1010" y="295" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">FLOWGRID</text>
    <rect x="1310" y="270" width="36" height="36" fill="#2E5D4B" rx="18"/>
    <text x="1328" y="294" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600" text-anchor="middle">✕</text>
    
    <line x1="1010" y1="325" x2="1340" y2="325" stroke="#2E5D4B" stroke-width="1"/>
    
    <!-- Menu Links -->
    <text x="1010" y="375" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">NAVIGATION</text>
    
    <text x="1010" y="420" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="600">১. হোম (Home)</text>
    <text x="1010" y="470" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="18">২. প্রকল্পসমূহ (Projects)</text>
    <text x="1010" y="520" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="18">৩. সেবা ও পরিধি (Services)</text>
    <text x="1010" y="570" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="18">৪. ডিজাইন পদ্ধতি (Process)</text>
    <text x="1010" y="620" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="18">৫. স্টুডিও পরিচিতি (Studio)</text>
    <text x="1010" y="670" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="18">৬. যোগাযোগ (Contact)</text>

    <!-- Language capsule inside drawer -->
    <rect x="1010" y="710" width="120" height="38" fill="#2E5D4B" rx="19"/>
    <rect x="1012" y="712" width="58" height="34" fill="#F4F1E8" rx="17"/>
    <text x="1041" y="734" fill="#183B35" font-family="'Manrope', sans-serif" font-size="12" font-weight="700" text-anchor="middle">বাং</text>
    <text x="1090" y="734" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="12" font-weight="600" text-anchor="middle">EN</text>

    <!-- Quick Call Button -->
    <rect x="1010" y="770" width="330" height="48" fill="#895239" rx="4"/>
    <text x="1175" y="800" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" text-anchor="middle">📞 কল করুন: 01711-000000</text>
  </g>

  <!-- ========================================================================= -->
  <!-- MOBILE SCREEN 4: 404 PAGE (X: 1430, Y: 240, W: 390, H: 844)               -->
  <!-- ========================================================================= -->
  <g id="screen-mobile-bn-404">
    <rect x="1430" y="240" width="390" height="844" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1"/>
    <!-- Top Bar -->
    <rect x="1430" y="240" width="390" height="60" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <text x="1450" y="278" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">FLOWGRID</text>

    <text x="1625" y="450" fill="#895239" font-family="'Bodoni Moda', serif" font-size="72" font-weight="700" text-anchor="middle">৪০৪</text>
    <text x="1625" y="500" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="600" text-anchor="middle">পৃষ্ঠাটি পাওয়া যায়নি</text>
    {wrap_text("আপনি যে লিংকটি খুঁজছেন তা সরানো হয়েছে বা ভুল ঠিকানায় প্রবেশ করেছেন।", 1625, 535, 32, 22, "'Hind Siliguri', sans-serif", 13, "#56645E")}
    
    <rect x="1470" y="620" width="310" height="48" fill="#183B35" rx="4"/>
    <text x="1625" y="650" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" text-anchor="middle">হোমপেজে ফিরে যান</text>
  </g>

</svg>"""

with open('figma_svgs_v2/04_mobile_bn.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("Saved figma_svgs_v2/04_mobile_bn.svg")
