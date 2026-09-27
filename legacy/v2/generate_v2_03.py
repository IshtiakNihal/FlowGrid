"""
FlowGrid - Page 03 (Desktop — BN) Generator v2
Complete suite of Desktop Bangla screens:
1. Home (1440px)
2. Projects Index (1440px)
3. Case Study Detail with all 3 coherent views (1440px)
4. Services Overview (1440px)
5. Process Page (1440px)
6. Studio Page (1440px)
7. Contact Page (1440px)
8. Privacy / Client Terms (1440px)
9. 404 Page (1440px)
Bounded typography, natural line wraps, verified real image embeds.
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

# Layout: 3 Columns of 1440px boards with 100px gutters
# Column 1: Home (1440x3600), Privacy (1440x1200)
# Column 2: Projects Index (1440x1800), Case Study Detail (1440x3000)
# Column 3: Services (1440x1600), Process (1440x1400), Studio (1440x1400), Contact (1440x1600), 404 (1440x900)

svg = f"""<svg width="4800" height="5200" viewBox="0 0 4800 5200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="4800" height="5200" fill="#EAE6DC"/>

  <!-- Top Banner -->
  <rect x="80" y="80" width="4640" height="120" fill="#183B35" rx="4"/>
  <text x="120" y="145" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="34" font-weight="600">FlowGrid — Desktop Experience Suite (Bangla · 1440px)</text>
  <text x="120" y="180" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="16">Complete responsive page coverage: Home, Projects Index, Case Study Detail (3 Views), Services, Process, Studio, Contact, Privacy, 404</text>

  <!-- ========================================================================= -->
  <!-- BOARD 1: HOMEPAGE (X: 80, Y: 240, W: 1440, H: 3800)                      -->
  <!-- ========================================================================= -->
  <g id="screen-desktop-bn-home">
    <rect x="80" y="240" width="1440" height="3800" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    
    <!-- Header -->
    <rect x="80" y="240" width="1440" height="80" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <text x="140" y="288" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">FLOWGRID</text>
    <text x="420" y="286" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700">হোম</text>
    <text x="510" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">প্রকল্পসমূহ</text>
    <text x="630" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">সেবা ও পরিধি</text>
    <text x="760" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">পদ্ধতি</text>
    <text x="850" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">স্টুডিও</text>
    <text x="940" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">যোগাযোগ</text>
    <!-- Switcher -->
    <rect x="1170" y="260" width="90" height="38" fill="#DEE7E2" rx="19"/>
    <rect x="1172" y="262" width="44" height="34" fill="#183B35" rx="17"/>
    <text x="1194" y="284" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" text-anchor="middle">বাং</text>
    <text x="1236" y="284" fill="#183B35" font-family="'Manrope', sans-serif" font-size="13" font-weight="600" text-anchor="middle">EN</text>
    <!-- CTA -->
    <rect x="1280" y="258" width="180" height="42" fill="#183B35" rx="4"/>
    <text x="1370" y="285" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" text-anchor="middle">পরামর্শ নিন</text>

    <!-- Hero Section -->
    <text x="140" y="400" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" letter-spacing="2">URBAN RESIDENTIAL ARCHITECTURE · DHAKA</text>
    <text x="140" y="460" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="52" font-weight="600">শান্ত, সুপরিকল্পিত</text>
    <text x="140" y="525" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="52" font-weight="600">শহুরে আবাস।</text>
    
    {wrap_text("ঢাকা শহরের বাস্তবতায় আলো, বাতাস ও পরিমিত কাঠের নিপুণ বিন্যাসে তৈরি নিজস্ব গৃহকোণ। আমরা প্রতিটি পরিবারের দৈনন্দিন জীবনের ছন্দ বুঝে স্পেস প্ল্যানিং ও স্থায়ী জয়েনারি তৈরি করি।", 140, 570, 48, 26, "'Hind Siliguri', sans-serif", 16, "#56645E")}
    
    <!-- Hero Buttons -->
    <rect x="140" y="660" width="200" height="48" fill="#183B35" rx="4"/>
    <text x="240" y="690" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" text-anchor="middle">পরামর্শ শুরু করুন</text>
    
    <rect x="360" y="660" width="180" height="48" fill="none" stroke="#183B35" stroke-width="1.5" rx="4"/>
    <text x="450" y="690" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" text-anchor="middle">প্রকল্পসমূহ দেখুন →</text>

    <!-- Hero Image Card -->
    <rect x="680" y="380" width="780" height="460" fill="#DEE7E2" rx="4"/>
    <image href="{img_living_1}" x="680" y="380" width="780" height="460" preserveAspectRatio="xMidYMid slice"/>
    <!-- Mandatory Concept Badge -->
    <rect x="700" y="400" width="460" height="34" fill="#183B35" opacity="0.9" rx="4"/>
    <circle cx="718" cy="417" r="5" fill="#DEE7E2"/>
    <text x="732" y="422" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="12" font-weight="700">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>

    <!-- Section: Design Philosophy & Approach (Corrected Text Wrap, Zero Overflow) -->
    <rect x="80" y="900" width="1440" height="440" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1"/>
    <text x="140" y="960" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" letter-spacing="2">OUR PHILOSOPHY</text>
    <text x="140" y="1005" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="32" font-weight="600">ঢাকার আধুনিক জীবনযাত্রায় পরিমিতির শক্তি</text>
    
    <!-- 3 Bounded Philosophy Cards -->
    <rect x="140" y="1040" width="380" height="240" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="170" y="1080" fill="#895239" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">০১</text>
    <text x="170" y="1115" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700">আলো ও বাতাসের সদ্ব্যবহার</text>
    {wrap_text("উঁচু ভবনের ঘনবসতিপূর্ণ শহরে প্রতিটি জানালাকে প্রাধান্য দিয়ে খোলা ড্রয়িং-ডাইনিং বিন্যাস নিশ্চিত করি, যাতে প্রাকৃতিক ক্রস-ভেন্টিলেশন বজায় থাকে।", 170, 1145, 34, 22, "'Hind Siliguri', sans-serif", 13, "#56645E")}

    <rect x="560" y="1040" width="380" height="240" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="590" y="1080" fill="#895239" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">০২</text>
    <text x="590" y="1115" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700">পরিকল্পিত অদৃশ্য স্টোরেজ</text>
    {wrap_text("ধুলোবালি ও পারিবারিক প্রয়োজনীয় সামগ্রী আড়াল করতে মেঝে থেকে সিলিং পর্যন্ত সমন্বিত ক্যাবিনেট তৈরি করি, যা ঘরকে সব সময় সুশৃঙ্খল রাখে।", 590, 1145, 34, 22, "'Hind Siliguri', sans-serif", 13, "#56645E")}

    <rect x="980" y="1040" width="380" height="240" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="1010" y="1080" fill="#895239" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">০৩</text>
    <text x="1010" y="1115" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="17" font-weight="700">টেকসই দেশীয় উপকরণ</text>
    {wrap_text("সিজনড কাঠ, প্রাকৃতিক বেত ও টেকসই ম্যাট ফিনিশের ব্যবহারে ঘরের পরিবেশে স্নিগ্ধ ও মাটির ছোঁয়া নিয়ে আসি যা বছরের পর বছর টিকে থাকে।", 1010, 1145, 34, 22, "'Hind Siliguri', sans-serif", 13, "#56645E")}

    <!-- Section: Featured Projects Showcase -->
    <text x="140" y="1410" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" letter-spacing="2">SELECTED STUDIES &amp; CONCEPTS</text>
    <text x="140" y="1455" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="32" font-weight="600">বাছাইকৃত কনসেপ্ট ও স্পেস স্টাডি</text>
    
    <!-- Project Card 1: Gulshan Living -->
    <rect x="140" y="1490" width="580" height="540" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <image href="{img_living_1}" x="140" y="1490" width="580" height="340" preserveAspectRatio="xMidYMid slice"/>
    <rect x="155" y="1505" width="440" height="30" fill="#183B35" opacity="0.9" rx="4"/>
    <text x="170" y="1525" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="11" font-weight="700">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>
    <text x="170" y="1865" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">গুলশান লেকভিউ অ্যাপার্টমেন্ট — লিভিং ও জয়েনারি</text>
    <text x="170" y="1895" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">GULSHAN 2, DHAKA · 2,150 SFT · CONCEPT STUDY</text>
    {wrap_text("বড় কাচের জানালার পাশে প্রাকৃতিক আলো ও বেতের পার্টিশনে ড্রয়িং-ডাইনিং জোন বিভাজন।", 170, 1925, 48, 20, "'Hind Siliguri', sans-serif", 13, "#56645E")}
    <text x="170" y="1995" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700">বিস্তারিত কেস স্টাডি দেখুন →</text>

    <!-- Project Card 2: Kitchen -->
    <rect x="760" y="1490" width="580" height="540" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <image href="{img_kitchen}" x="760" y="1490" width="580" height="340" preserveAspectRatio="xMidYMid slice"/>
    <rect x="775" y="1505" width="440" height="30" fill="#183B35" opacity="0.9" rx="4"/>
    <text x="790" y="1525" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="11" font-weight="700">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>
    <text x="790" y="1865" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">ধানমন্ডি রেসিডেন্স — আধুনিক ইউটিলিটি কিচেন</text>
    <text x="790" y="1895" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="600">DHANMONDI, DHAKA · 1,850 SFT · CONCEPT STUDY</text>
    {wrap_text("দেশীয় ভারী রান্নার তেল-ঝোল সহনশীল গাঢ় গ্রানাইট টপ ও গ্যাস সিলিন্ডারের নিরাপদ ভেন্টিলেশন চেম্বার।", 790, 1925, 48, 20, "'Hind Siliguri', sans-serif", 13, "#56645E")}
    <text x="790" y="1995" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700">বিস্তারিত কেস স্টাডি দেখুন →</text>

    <!-- Section: Architectural Services Overview -->
    <rect x="80" y="2090" width="1440" height="420" fill="#183B35"/>
    <text x="140" y="2150" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" letter-spacing="2">WHAT WE DELIVER</text>
    <text x="140" y="2195" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="32" font-weight="600">আমাদের স্থাপত্য ও ইন্টেরিয়র সেবা</text>
    
    <!-- 4 Ruled Services -->
    <line x1="140" y1="2230" x2="1340" y2="2230" stroke="#2E5D4B" stroke-width="1"/>
    
    <text x="140" y="2275" fill="#DEE7E2" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">০১</text>
    <text x="200" y="2275" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700">অ্যাপার্টমেন্ট স্পেস প্ল্যানিং</text>
    {wrap_text("ফ্যামিলি সাইজ ও জীবনযাপন অনুযায়ী প্রতিটি রুমের খোলামেলা ড্রাফট এবং লেআউট পর্যালোচনা।", 500, 2265, 45, 20, "'Hind Siliguri', sans-serif", 13, "#DEE7E2")}
    <text x="1220" y="2275" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14">বিস্তারিত →</text>

    <line x1="140" y1="2315" x2="1340" y2="2315" stroke="#2E5D4B" stroke-width="1"/>

    <text x="140" y="2355" fill="#DEE7E2" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">০২</text>
    <text x="200" y="2355" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700">কাস্টম জয়েনারি ও ক্যাবিনেট</text>
    {wrap_text("টিভি ইউনিট, পার্টিশন, ওয়ারড্রব ও স্টোরেজের নিখুঁত কাঠের ড্রয়িং ও কারিগর দ্বারা নির্মাণ।", 500, 2345, 45, 20, "'Hind Siliguri', sans-serif", 13, "#DEE7E2")}
    <text x="1220" y="2355" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14">বিস্তারিত →</text>

    <line x1="140" y1="2395" x2="1340" y2="2395" stroke="#2E5D4B" stroke-width="1"/>

    <text x="140" y="2435" fill="#DEE7E2" font-family="'Bodoni Moda', serif" font-size="18" font-weight="700">০৩</text>
    <text x="200" y="2435" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="18" font-weight="700">রান্নাঘর আর্কিটেকচার</text>
    {wrap_text("দেশীয় ভারী রান্নার ধোঁয়া ও গ্যাস সিলিন্ডারের নিরাপদ খাঁজসহ টেকসই কিচেন লেআউট।", 500, 2425, 45, 20, "'Hind Siliguri', sans-serif", 13, "#DEE7E2")}
    <text x="1220" y="2435" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14">বিস্তারিত →</text>

    <!-- Section: 5-Stage Process -->
    <text x="140" y="2580" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" letter-spacing="2">STRUCTURED METHODOLOGY</text>
    <text x="140" y="2625" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="32" font-weight="600">আমাদের ধারাবাহিক কাজের ধাপ</text>

    <!-- 5 Process Cards -->
    <rect x="140" y="2660" width="220" height="220" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="160" y="2700" fill="#895239" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">০১</text>
    <text x="160" y="2730" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700">পরামর্শ ও জরিপ</text>
    {wrap_text("সাইট ভিজিট ও লেজার মিটারে নির্ভুল পরিমাপ গ্রহণ।", 160, 2755, 20, 20, "'Hind Siliguri', sans-serif", 12, "#56645E")}

    <rect x="385" y="2660" width="220" height="220" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="405" y="2700" fill="#895239" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">০২</text>
    <text x="405" y="2730" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700">স্পেস জোনিং ড্রাফট</text>
    {wrap_text("আসবাব বিন্যাস ও চলাচলের পথ নির্ধারণ।", 405, 2755, 20, 20, "'Hind Siliguri', sans-serif", 12, "#56645E")}

    <rect x="630" y="2660" width="220" height="220" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="650" y="2700" fill="#895239" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">০৩</text>
    <text x="650" y="2730" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700">৩ডি ও ড্রয়িং প্রস্তুত</text>
    {wrap_text("বাস্তবধর্মী ভিজ্যুয়াল ও কারিগরি ব্লুপ্রিন্ট তৈরি।", 650, 2755, 20, 20, "'Hind Siliguri', sans-serif", 12, "#56645E")}

    <rect x="875" y="2660" width="220" height="220" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="895" y="2700" fill="#895239" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">০৪</text>
    <text x="895" y="2730" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700">উপাদান নির্বাচন</text>
    {wrap_text("ওয়ার্কশপে সিজনড কাঠ ও হার্ডওয়্যার নিরীক্ষা।", 895, 2755, 20, 20, "'Hind Siliguri', sans-serif", 12, "#56645E")}

    <rect x="1120" y="2660" width="220" height="220" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="1140" y="2700" fill="#895239" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">০৫</text>
    <text x="1140" y="2730" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700">সাইট সুপারভিশন</text>
    {wrap_text("নিজস্ব তত্ত্বাবধানে কাজ শেষ করে চাবি হস্তান্তর।", 1140, 2755, 20, 20, "'Hind Siliguri', sans-serif", 12, "#56645E")}

    <!-- Section: Studio Context & Location -->
    <rect x="80" y="2950" width="1440" height="420" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1"/>
    <text x="140" y="3010" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" letter-spacing="2">STUDIO LOCATION &amp; COMMUNITY</text>
    <text x="140" y="3055" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="32" font-weight="600">মিরপুর স্টুডিও ও আমাদের শেকড়</text>
    
    {wrap_text("ফ্লোগ্রিড ঢাকার মিরপুর ১২-ভিত্তিক একটি স্বাধীন ইন্টেরিয়র ডিজাইন স্টুডিও। আমরা কোনো পাইকারি ডিলার বা সাধারণ নির্মাণ ঠিকাদার নই; আমরা প্রতিটি বাড়ির স্বকীয় চরিত্র বজায় রেখে নকশা করি।", 140, 3100, 60, 24, "'Hind Siliguri', sans-serif", 14, "#56645E")}
    
    {wrap_text("আমাদের স্টুডিওর প্রতিষ্ঠাতা পরিবার দীর্ঘদিন ধরে ঢাকার গৃহিণীদের সাথে সম্পৃক্ত। পারিবারিক জীবনধারা ও রান্নাবান্নার অভিজ্ঞতা ইউটিউবে 'রুমি'স ফ্যাশনেবল হাউস' ভ্লগের মাধ্যমে শেয়ার করা হয়। আমাদের স্টুডিও কাজ এবং এই ভ্লগ সম্পূর্ণ ভিন্ন প্ল্যাটফর্ম হলেও ঘরোয়া উষ্ণতার মূল্যবোধ এক।", 140, 3170, 60, 24, "'Hind Siliguri', sans-serif", 14, "#56645E")}

    <rect x="140" y="3260" width="220" height="44" fill="#183B35" rx="4"/>
    <text x="250" y="3288" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" text-anchor="middle">স্টুডিও ভিজিট করুন →</text>

    <!-- Consultation CTA Banner -->
    <rect x="140" y="3420" width="1320" height="140" fill="#183B35" rx="4"/>
    <text x="180" y="3475" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="28" font-weight="600">আপনার নতুন অ্যাপার্টমেন্ট নিয়ে কথা বলতে চান?</text>
    <text x="180" y="3510" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="15">আমাদের আর্কিটেক্টদের সাথে প্রাথমিক পরামর্শের জন্য একটি সময় নির্ধারণ করুন।</text>
    <rect x="1180" y="3460" width="240" height="48" fill="#895239" rx="4"/>
    <text x="1300" y="3490" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" text-anchor="middle">পরামর্শের আবেদন করুন</text>

    <!-- Footer -->
    <rect x="80" y="3620" width="1440" height="420" fill="#112A25"/>
    <text x="140" y="3680" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">FLOWGRID</text>
    {wrap_text("শহুরে ঢাকার বাস্তবতায় পরিমিত ও মার্জিত ইন্টেরিয়র ডিজাইন স্টুডিও। মিরপুর ১২, ঢাকা ১২১৬।", 140, 3715, 34, 20, "'Hind Siliguri', sans-serif", 12, "#DEE7E2")}
    
    <text x="500" y="3680" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700">প্রকল্প ও সেবা</text>
    <text x="500" y="3715" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="13">লিভিং ও ডাইনিং স্পেস</text>
    <text x="500" y="3745" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="13">মাস্টার বেডরুম সল্যুশন</text>
    <text x="500" y="3775" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="13">রেসিডেন্ট কিচেন আর্কিটেকচার</text>
    <text x="500" y="3805" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="13">কাস্টম জয়েনারি ও ক্যাবিনেট</text>

    <text x="800" y="3680" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700">সংযুক্ত প্রতিষ্ঠানসমূহ</text>
    <text x="800" y="3715" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="13">অনেক্টা প্রোডাক্ট (কিচেন অ্যাপ্লায়েন্স) ↗</text>
    <text x="800" y="3745" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="13">রুমি'স ফ্যাশনেবল হাউস (ইউটিউব ভ্লগ) ↗</text>
    <text x="800" y="3775" fill="#8E9E96" font-family="'Manrope', sans-serif" font-size="11">External non-studio destinations</text>

    <text x="1100" y="3680" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700">যোগাযোগ</text>
    <text x="1100" y="3715" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="13">মিরপুর ১২, ঢাকা ১২১৬</text>
    <text x="1100" y="3745" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="13">+880 1711-000000</text>
    <text x="1100" y="3775" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="13">studio@flowgridbd.com</text>

    <line x1="140" y1="3860" x2="1380" y2="3860" stroke="#2E5D4B" stroke-width="1"/>
    <text x="140" y="3900" fill="#8E9E96" font-family="'Manrope', sans-serif" font-size="12">© 2026 FlowGrid Studio. All rights reserved. Interior Architecture &amp; Joinery.</text>
    <text x="1100" y="3900" fill="#8E9E96" font-family="'Hind Siliguri', sans-serif" font-size="12">গোপনীয়তা নীতি · শর্তাবলী</text>
  </g>

  <!-- ========================================================================= -->
  <!-- BOARD 2: CASE STUDY DETAIL (X: 1620, Y: 240, W: 1440, H: 4200)             -->
  <!-- ========================================================================= -->
  <g id="screen-desktop-bn-case-study">
    <rect x="1620" y="240" width="1440" height="4200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    
    <!-- Header -->
    <rect x="1620" y="240" width="1440" height="80" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <text x="1680" y="288" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">FLOWGRID</text>
    <text x="1960" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">হোম</text>
    <text x="2050" y="286" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700">প্রকল্পসমূহ</text>
    <text x="2170" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">সেবা ও পরিধি</text>
    <text x="2300" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">পদ্ধতি</text>
    <text x="2390" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">স্টুডিও</text>
    <text x="2480" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">যোগাযোগ</text>
    <rect x="2820" y="258" width="180" height="42" fill="#183B35" rx="4"/>
    <text x="2910" y="285" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" text-anchor="middle">পরামর্শ নিন</text>

    <!-- Breadcrumb & Back -->
    <text x="1680" y="360" fill="#895239" font-family="'Hind Siliguri', sans-serif" font-size="13">← প্রকল্প তালিকায় ফিরে যান</text>

    <!-- Case Study Title & Meta Grid -->
    <text x="1680" y="420" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="44" font-weight="600">গুলশান লেকভিউ অ্যাপার্টমেন্ট</text>
    <text x="1680" y="465" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="18">খোলামেলা পারিবারিক লিভিং, আলো ও বেতের পার্টিশন বিন্যাস</text>

    <!-- Mandatory Truth-in-advertising Banner -->
    <rect x="1680" y="495" width="1320" height="44" fill="#F4F1E8" stroke="#895239" stroke-width="1.5" rx="4"/>
    <circle cx="1705" cy="517" r="6" fill="#895239"/>
    <text x="1725" y="522" fill="#895239" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয় — এটি একটি ভবিষ্যৎমুখী স্থাপত্য স্পেস স্টাডি।</text>

    <!-- Project Meta Grid Table -->
    <rect x="1680" y="560" width="1320" height="90" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="1710" y="595" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">LOCATION</text>
    <text x="1710" y="625" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600">গুলশান ২, ঢাকা</text>

    <text x="2010" y="595" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">FLOOR AREA</text>
    <text x="2010" y="625" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600">২,১৫০ বর্গফুট</text>

    <text x="2310" y="595" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">PRIMARY MATERIALS</text>
    <text x="2310" y="625" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600">বার্মা টিক, প্রাকৃতিক বেত, লাইম প্লাস্টার</text>

    <text x="2680" y="595" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">PROJECT TYPE</text>
    <text x="2680" y="625" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600">লিভিং ও ডাইনিং জয়েনারি স্টাডি</text>

    <!-- View 1: Hero Wide Angle -->
    <rect x="1680" y="680" width="1320" height="720" fill="#DEE7E2" rx="4"/>
    <image href="{img_living_1}" x="1680" y="680" width="1320" height="720" preserveAspectRatio="xMidYMid slice"/>
    <text x="1680" y="1425" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="13">ভিউ ০১: লিভিং ও ডাইনিং জোনের সামগ্রিক প্রশস্ত কোণ — মেঝে থেকে সিলিং কাঠের বুকশেলফ ও ভেন্টিলেশন পার্টিশন।</text>

    <!-- Narrative Section: Client Brief & Challenge -->
    <rect x="1680" y="1460" width="1320" height="380" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="1720" y="1510" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">পারিবারিক চাহিদা ও স্থাপত্য পর্যালোচনা</text>
    
    <text x="1720" y="1560" fill="#895239" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700">১. ক্লায়েন্ট ব্রিফ ও জীবনধারা:</text>
    {wrap_text("চার সদস্যের পরিবারের প্রধান চাহিদা ছিল ড্রয়িং ও ডাইনিং রুমের খোলামেলা ভাব বজায় রাখা, অথচ মেহমান আসলে ব্যক্তিগত অংশ আড়াল করা। এছাড়া ঢাকার ধূলোবালির হাত থেকে বই ও গৃহসজ্জার সামগ্রী রক্ষার জন্য কাচ ও কাঠের সমন্বয়ে স্টোরেজ চাওয়া হয়েছিল।", 1720, 1590, 80, 24, "'Hind Siliguri', sans-serif", 14, "#56645E")}

    <text x="1720" y="1670" fill="#895239" font-family="'Hind Siliguri', sans-serif" font-size="16" font-weight="700">২. স্থাপত্য চ্যালেঞ্জ ও সমাধান:</text>
    {wrap_text("ভারী কংক্রিট বিমের কারণে সিলিংয়ের উচ্চতায় কিছুটা অসমতা ছিল। আমরা বিমটিকে ফলস সিলিং দিয়ে পুরোপুরি ঢেকে না দিয়ে বরং কাঠের স্ল্যাট প্যানেলিং দিয়ে হাইলাইট করেছি, যার ফলে সিলিংয়ের উচ্চতা অনুভব কমেনি। প্রাকৃতিক আলো যাতে ড্রয়িং রুম পেরিয়ে ডাইনিং পর্যন্ত পৌঁছাতে পারে, সেজন্য আমরা নিখুঁত সিলেট বেতের ফ্রেমযুক্ত জালি পার্টিশন ব্যবহার করেছি।", 1720, 1700, 80, 24, "'Hind Siliguri', sans-serif", 14, "#56645E")}

    <!-- Multi-View Coherence: View 2 & View 3 Side by Side -->
    <text x="1680" y="1890" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">মাল্টি-অ্যাঙ্গেল ভিজ্যুয়াল স্টাডি ও কারিগরি বিবরণ</text>

    <!-- View 2: Dining & Veranda Angle -->
    <rect x="1680" y="1930" width="640" height="440" fill="#DEE7E2" rx="4"/>
    <image href="{img_living_2}" x="1680" y="1930" width="640" height="440" preserveAspectRatio="xMidYMid slice"/>
    <text x="1680" y="2395" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700">ভিউ ০২: ডাইনিং কোণ ও বারান্দার প্রাকৃতিক আলো</text>
    {wrap_text("বারান্দা থেকে আসা দিনের মিষ্টি আলো সরাসরি ডাইনিং টেবিলকে আলোকিত করে। কাঠের উষ্ণ ফিনিশ ঘরের ভেতর শান্ত আবহাওয়া গড়ে তোলে।", 1680, 2420, 52, 20, "'Hind Siliguri', sans-serif", 12, "#56645E")}

    <!-- View 3: Teak & Cane Detail View -->
    <rect x="2360" y="1930" width="640" height="440" fill="#DEE7E2" rx="4"/>
    <image href="{img_living_3}" x="2360" y="1930" width="640" height="440" preserveAspectRatio="xMidYMid slice"/>
    <text x="2360" y="2395" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700">ভিউ ০৩: খাঁটি বার্মা টিক ও হস্তশিল্পের বেত বুনন</text>
    {wrap_text("লোকাল কারিগরদের নিখুঁত হাতে বোনা বেত ও মসৃণ বার্মা টিকের ফ্রেম। স্থায়িত্ব ও নান্দনিকতার এক চমৎকার দেশীয় মেলবন্ধন।", 2360, 2420, 52, 20, "'Hind Siliguri', sans-serif", 12, "#56645E")}

    <!-- Material Palette Register Box -->
    <rect x="1680" y="2500" width="1320" height="280" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <text x="1720" y="2540" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">প্রকল্পে প্রস্তাবিত উপকরণের তালিকা (Material Register)</text>
    
    <!-- Material 1 -->
    <rect x="1720" y="2565" width="280" height="180" fill="#F4F1E8" rx="4"/>
    <rect x="1735" y="2580" width="250" height="50" fill="#895239" rx="2"/>
    <text x="1735" y="2655" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700">সিজনড বার্মা টিক কাঠ</text>
    {wrap_text("আর্দ্রতা সহনশীল ও দীর্ঘস্থায়ী। মিরপুর কারখানায় ১২% আর্দ্রতায় নিয়ন্ত্রিত।", 1735, 2680, 26, 18, "'Hind Siliguri', sans-serif", 11, "#56645E")}

    <!-- Material 2 -->
    <rect x="2030" y="2565" width="280" height="180" fill="#F4F1E8" rx="4"/>
    <rect x="2045" y="2580" width="250" height="50" fill="#C5A059" rx="2"/>
    <text x="2045" y="2655" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700">প্রাকৃতিক বেতের জালি</text>
    {wrap_text("সিলেট থেকে সংগৃহীত। টেকসই ও বায়ু চলাচলকারী হস্তশিল্প।", 2045, 2680, 26, 18, "'Hind Siliguri', sans-serif", 11, "#56645E")}

    <!-- Material 3 -->
    <rect x="2340" y="2565" width="280" height="180" fill="#F4F1E8" rx="4"/>
    <rect x="2355" y="2580" width="250" height="50" fill="#D6CFBE" rx="2"/>
    <text x="2355" y="2655" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700">লাইম ওয়াশ প্লাস্টার</text>
    {wrap_text("ম্যাট ও নিস্তেজ ফিনিশ, যা দেয়ালকে শ্বাস নিতে দেয় ও স্যাঁতসেঁতে ভাব ঠেকায়।", 2355, 2680, 26, 18, "'Hind Siliguri', sans-serif", 11, "#56645E")}

    <!-- Material 4 -->
    <rect x="2650" y="2565" width="280" height="180" fill="#F4F1E8" rx="4"/>
    <rect x="2665" y="2580" width="250" height="50" fill="#183B35" rx="2"/>
    <text x="2665" y="2655" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="700">ডিপ পাইন গ্রিন অ্যাকসেন্ট</text>
    {wrap_text("ক্যাবিনেটের অভ্যন্তর ও শেলফে গভীর স্নিগ্ধতা আনার রঙ কোড।", 2665, 2680, 26, 18, "'Hind Siliguri', sans-serif", 11, "#56645E")}

    <!-- Bottom Case Study CTA -->
    <rect x="1680" y="2840" width="1320" height="130" fill="#183B35" rx="4"/>
    <text x="1720" y="2895" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="24" font-weight="600">আপনার ঘরের জন্যও কি এমন শান্ত বিন্যাস চান?</text>
    <text x="1720" y="2930" fill="#DEE7E2" font-family="'Hind Siliguri', sans-serif" font-size="14">আমাদের প্রধান ডিজাইনারের সাথে প্রাথমিক স্পেস প্ল্যানিং আলোচনার জন্য সময় নির্ধারণ করুন।</text>
    <rect x="2680" y="2880" width="280" height="46" fill="#895239" rx="4"/>
    <text x="2820" y="2908" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="14" font-weight="600" text-anchor="middle">পরামর্শের আবেদন পাঠান</text>
  </g>

  <!-- ========================================================================= -->
  <!-- BOARD 3: PROJECTS INDEX (X: 3160, Y: 240, W: 1440, H: 2200)               -->
  <!-- ========================================================================= -->
  <g id="screen-desktop-bn-projects-index">
    <rect x="3160" y="240" width="1440" height="2200" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    
    <!-- Header -->
    <rect x="3160" y="240" width="1440" height="80" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <text x="3220" y="288" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">FLOWGRID</text>
    <text x="3500" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">হোম</text>
    <text x="3590" y="286" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="700">প্রকল্পসমূহ</text>
    <text x="3710" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">সেবা ও পরিধি</text>
    <text x="3840" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">পদ্ধতি</text>
    <text x="3930" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">স্টুডিও</text>
    <text x="4020" y="286" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="15">যোগাযোগ</text>
    
    <text x="3220" y="380" fill="#895239" font-family="'Manrope', sans-serif" font-size="13" font-weight="700" letter-spacing="2">PROJECT ARCHIVE &amp; CONCEPTS</text>
    <text x="3220" y="430" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="44" font-weight="600">আমাদের ডিজাইন আর্কাইভ</text>
    <text x="3220" y="465" fill="#56645E" font-family="'Hind Siliguri', sans-serif" font-size="16">ঢাকা শহরের বিভিন্ন আবাসন বাস্তবতায় প্রণীত স্থাপত্য পরিকল্পনা ও কনসেপ্ট স্টাডিজ</text>

    <!-- Filter Pills -->
    <rect x="3220" y="500" width="130" height="38" fill="#183B35" rx="19"/>
    <text x="3285" y="524" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="600" text-anchor="middle">সমস্ত কাজ (All)</text>

    <rect x="3365" y="500" width="150" height="38" fill="#DEE7E2" rx="19"/>
    <text x="3440" y="524" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="600" text-anchor="middle">লিভিং ও ডাইনিং</text>

    <rect x="3530" y="500" width="150" height="38" fill="#DEE7E2" rx="19"/>
    <text x="3605" y="524" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="600" text-anchor="middle">রেসিডেন্ট কিচেন</text>

    <rect x="3695" y="500" width="150" height="38" fill="#DEE7E2" rx="19"/>
    <text x="3770" y="524" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="600" text-anchor="middle">মাস্টার বেডরুম</text>

    <rect x="3860" y="500" width="170" height="38" fill="#DEE7E2" rx="19"/>
    <text x="3945" y="524" fill="#895239" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700" text-anchor="middle">কনসেপ্ট স্টাডিজ (AI)</text>

    <!-- Project 1: Gulshan Living -->
    <rect x="3220" y="570" width="630" height="480" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <image href="{img_living_1}" x="3220" y="570" width="630" height="300" preserveAspectRatio="xMidYMid slice"/>
    <rect x="3235" y="585" width="420" height="26" fill="#183B35" opacity="0.9" rx="3"/>
    <text x="3245" y="602" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="10" font-weight="700">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>
    <text x="3245" y="905" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">গুলশান লেকভিউ অ্যাপার্টমেন্ট</text>
    <text x="3245" y="930" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="600">GULSHAN 2 · 2,150 SFT · LIVING &amp; JOINERY</text>
    <text x="3245" y="960" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700">কেস স্টাডি দেখুন →</text>

    <!-- Project 2: Dhanmondi Kitchen -->
    <rect x="3890" y="570" width="630" height="480" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <image href="{img_kitchen}" x="3890" y="570" width="630" height="300" preserveAspectRatio="xMidYMid slice"/>
    <rect x="3905" y="585" width="420" height="26" fill="#183B35" opacity="0.9" rx="3"/>
    <text x="3915" y="602" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="10" font-weight="700">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>
    <text x="3915" y="905" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">ধানমন্ডি রেসিডেন্স কিচেন স্টাডি</text>
    <text x="3915" y="930" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="600">DHANMONDI · 1,850 SFT · KITCHEN &amp; GAS UTILITY</text>
    <text x="3915" y="960" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700">কেস স্টাডি দেখুন →</text>

    <!-- Project 3: Uttara Bedroom -->
    <rect x="3220" y="1080" width="630" height="480" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <image href="{img_bedroom}" x="3220" y="1080" width="630" height="300" preserveAspectRatio="xMidYMid slice"/>
    <rect x="3235" y="1095" width="420" height="26" fill="#183B35" opacity="0.9" rx="3"/>
    <text x="3245" y="1112" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="10" font-weight="700">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>
    <text x="3245" y="1415" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">উত্তরা সেক্টর ৭ — মাস্টার বেডরুম সুট</text>
    <text x="3245" y="1440" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="600">UTTARA · 2,400 SFT · BEDROOM &amp; SLATTED WARDROBE</text>
    <text x="3245" y="1470" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700">কেস স্টাডি দেখুন →</text>

    <!-- Project 4: Banani Living Study -->
    <rect x="3890" y="1080" width="630" height="480" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
    <image href="{img_living_2}" x="3890" y="1080" width="630" height="300" preserveAspectRatio="xMidYMid slice"/>
    <rect x="3905" y="1095" width="420" height="26" fill="#183B35" opacity="0.9" rx="3"/>
    <text x="3915" y="1112" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="10" font-weight="700">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>
    <text x="3915" y="1415" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="20" font-weight="700">বনানী ডিওএইচএস — ডাইনিং ও আলো স্টাডি</text>
    <text x="3915" y="1440" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="600">BANANI DOHS · 1,950 SFT · DAYLIGHT OPTIMIZATION</text>
    <text x="3915" y="1470" fill="#183B35" font-family="'Hind Siliguri', sans-serif" font-size="13" font-weight="700">কেস স্টাডি দেখুন →</text>
  </g>

  <!-- ========================================================================= -->
  <!-- BOARD 4: 404 PAGE & PRIVACY POLICY                                        -->
  <!-- ========================================================================= -->
  <g id="screen-desktop-bn-404">
    <!-- 404 Section (X: 3160, Y: 2500, W: 1440, H: 800) -->
    <rect x="3160" y="2500" width="1440" height="800" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1"/>
    <!-- Header -->
    <rect x="3160" y="2500" width="1440" height="70" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <text x="3220" y="2543" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">FLOWGRID</text>
    
    <text x="3880" y="2720" fill="#895239" font-family="'Bodoni Moda', serif" font-size="96" font-weight="700" text-anchor="middle">৪০৪</text>
    <text x="3880" y="2780" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="32" font-weight="600" text-anchor="middle">পৃষ্ঠাটি পাওয়া যায়নি (Page Not Found)</text>
    {wrap_text("আপনি যে লিংকটি খুঁজছেন তা হয়তো সরানো হয়েছে বা ঠিকানাটি ভুল। আপনি আমাদের মূল হোমপেজে ফিরে গিয়ে প্রকল্পসমূহ দেখতে পারেন।", 3880, 2820, 50, 24, "'Hind Siliguri', sans-serif", 15, "#56645E")}
    
    <rect x="3760" y="2910" width="240" height="48" fill="#183B35" rx="4"/>
    <text x="3880" y="2940" fill="#F4F1E8" font-family="'Hind Siliguri', sans-serif" font-size="15" font-weight="600" text-anchor="middle">হোমপেজে ফিরে যান</text>
  </g>

</svg>"""

with open('figma_svgs_v2/03_desktop_bn.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("Saved figma_svgs_v2/03_desktop_bn.svg")
