"""
FlowGrid - Page 04: Mobile — BN (Bangla 390px Templates) SVG Generator
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

svg_04 = f"""<svg width="2400" height="2800" viewBox="0 0 2400 2800" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="2400" height="2800" fill="#E5E1D8"/>

  <!-- ========================================================= -->
  <!-- SCREEN 1: MOBILE HOME (390 x 2400) -->
  <!-- ========================================================= -->
  <g transform="translate(100, 100)">
    <rect width="390" height="2400" fill="#F4F1E8" rx="2"/>
    <text x="0" y="-20" fill="#183B35" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">01. মোবাইল হোমপেজ (Mobile Home — BN · 390px)</text>

    <!-- Mobile Header (72px) -->
    <rect width="390" height="72" fill="#F4F1E8"/>
    <line x1="20" y1="72" x2="370" y2="72" stroke="#B8C2BA" stroke-width="1"/>
    <text x="20" y="44" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">FLOWGRID</text>
    <text x="270" y="44" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">EN</text>
    <rect x="306" y="14" width="64" height="44" fill="#183B35" rx="2"/>
    <text x="323" y="41" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="600">মেনু</text>

    <!-- Content-First Paper Hero Block (Text BEFORE image on mobile) -->
    <g transform="translate(20, 95)">
      <text x="0" y="15" fill="#895239" font-family="'Noto Sans Bengali', sans-serif" font-size="13" font-weight="700">ইন্টেরিয়র ডিজাইন স্টুডিও</text>
      <text x="0" y="55" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="34" font-weight="700" line-height="1.3">আপনার জীবনের ছন্দে,</text>
      <text x="0" y="100" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="34" font-weight="700" line-height="1.3">আপনার ঘর।</text>
      <text x="0" y="145" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="16" line-height="1.6">আপনার প্রয়োজন, পছন্দ ও বাজেট বুঝে প্রতিটি কোণের সুচিন্তিত পরিকল্পনা।</text>

      <rect x="0" y="180" width="350" height="52" fill="#183B35" rx="2"/>
      <text x="105" y="212" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="700">আমাদের কাজ দেখুন →</text>
    </g>

    <!-- Edge-to-Edge Hero Image (4:5 Aspect Ratio: 390 x 487) -->
    <g transform="translate(0, 360)">
      <rect width="390" height="487" fill="#DEE7E2"/>
      <image href="{img_living}" x="0" y="0" width="390" height="487" preserveAspectRatio="xMidYMid slice"/>
      
      <!-- Honest Concept Pill -->
      <rect x="20" y="20" width="260" height="30" fill="#183B35" opacity="0.9" rx="2"/>
      <text x="30" y="40" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="12" font-weight="600">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>
    </g>

    <!-- Mobile Proposition (Single Column) -->
    <g transform="translate(20, 880)">
      <text x="0" y="20" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700" letter-spacing="1">THE FLOWGRID APPROACH</text>
      <text x="0" y="60" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="26" font-weight="700">ভাবনা থেকে পরিকল্পনা</text>
      <text x="0" y="105" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="16" line-height="1.7">আমরা শুরু করি আপনার পরিবার কীভাবে ঘরে থাকে, কী পরিমাণ স্টোরেজ আপনার প্রয়োজন, এবং আপনি কতটুকু ব্যয় করতে চান তা দিয়ে।</text>
      <text x="0" y="180" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="700">আমাদের কাজের পদ্ধতি দেখুন →</text>
      <line x1="0" y1="210" x2="350" y2="210" stroke="#B8C2BA" stroke-width="1"/>
    </g>

    <!-- Mobile Selected Projects Feed -->
    <g transform="translate(20, 1130)">
      <text x="0" y="20" fill="#895239" font-family="'Manrope', sans-serif" font-size="12" font-weight="700" letter-spacing="1">SELECTED WORK</text>
      <text x="0" y="55" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="26" font-weight="700">আমাদের কাজ</text>

      <!-- Project 1 Card -->
      <g transform="translate(0, 80)">
        <rect width="350" height="260" fill="#DEE7E2"/>
        <image href="{img_living}" x="0" y="0" width="350" height="260" preserveAspectRatio="xMidYMid slice"/>
        <rect x="15" y="15" width="220" height="26" fill="#183B35" opacity="0.9" rx="2"/>
        <text x="25" y="32" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="11" font-weight="600">কনসেপ্ট ডিজাইন</text>

        <text x="0" y="290" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="20" font-weight="700">অ্যাপার্টমেন্ট স্টাডি ০১</text>
        <text x="0" y="315" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">মিরপুর, ঢাকা · লিভিং ও মাল্টিফাংশনাল স্টোরেজ</text>
        <text x="0" y="340" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="700">বিস্তারিত দেখুন →</text>
      </g>

      <!-- Project 2 Card -->
      <g transform="translate(0, 460)">
        <rect width="350" height="260" fill="#DEE7E2"/>
        <image href="{img_kitchen}" x="0" y="0" width="350" height="260" preserveAspectRatio="xMidYMid slice"/>
        <rect x="15" y="15" width="220" height="26" fill="#183B35" opacity="0.9" rx="2"/>
        <text x="25" y="32" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="11" font-weight="600">কনসেপ্ট ডিজাইন</text>

        <text x="0" y="290" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="20" font-weight="700">কিচেন স্টাডি ০২</text>
        <text x="0" y="315" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">ঢাকা · নিত্যদিনের রান্না ও দীর্ঘস্থায়ী গ্রানাইট</text>
        <text x="0" y="340" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="700">বিস্তারিত দেখুন →</text>
      </g>
    </g>

    <!-- Mobile Closing Enquiry Banner -->
    <g transform="translate(20, 2020)">
      <rect width="350" height="220" fill="#183B35" rx="2"/>
      <text x="20" y="45" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="24" font-weight="700">ঘরের কথা বলুন</text>
      <text x="20" y="80" fill="#DEE7E2" font-family="'Noto Sans Bengali', sans-serif" font-size="14">আপনার ফ্ল্যাটের পরিসর জানান। FlowGrid টিম আলোচনা শুরু করতে প্রস্তুত।</text>
      
      <rect x="20" y="125" width="310" height="48" fill="#F4F1E8" rx="2"/>
      <text x="105" y="155" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="700">অনুরোধ পাঠান →</text>
    </g>

    <!-- Persistent Bottom Mobile Contact Bar -->
    <g transform="translate(0, 2330)">
      <rect width="390" height="70" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
      <rect x="20" y="10" width="165" height="48" fill="#F4F1E8" stroke="#183B35" stroke-width="1.5" rx="2"/>
      <text x="65" y="39" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="700">কল করুন</text>

      <rect x="205" y="10" width="165" height="48" fill="#183B35" rx="2"/>
      <text x="245" y="39" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="700">কথা বলুন</text>
    </g>
  </g>

  <!-- ========================================================= -->
  <!-- SCREEN 2: MOBILE ENQUIRY FORM (390 x 1800) -->
  <!-- ========================================================= -->
  <g transform="translate(600, 100)">
    <rect width="390" height="1800" fill="#F4F1E8" rx="2"/>
    <text x="0" y="-20" fill="#183B35" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">02. মোবাইল অনুরোধ ফরম (Mobile Enquiry — BN · 390px)</text>

    <!-- Header -->
    <rect width="390" height="72" fill="#F4F1E8"/>
    <line x1="20" y1="72" x2="370" y2="72" stroke="#B8C2BA" stroke-width="1"/>
    <text x="20" y="44" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">FLOWGRID</text>
    <rect x="306" y="14" width="64" height="44" fill="#183B35" rx="2"/>
    <text x="323" y="41" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="600">মেনু</text>

    <!-- Form Heading -->
    <g transform="translate(20, 100)">
      <text x="0" y="30" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="30" font-weight="700">আপনার ঘর নিয়ে</text>
      <text x="0" y="70" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="30" font-weight="700">কথা বলি।</text>
      <text x="0" y="110" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="15" line-height="1.6">কিছু তথ্য দিন। FlowGrid টিম আপনার সঙ্গে যোগাযোগ করে বিস্তারিত জানবে।</text>

      <!-- Field 1: Name -->
      <g transform="translate(0, 140)">
        <text x="0" y="0" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="600">আপনার নাম <tspan fill="#9B302B">*</tspan></text>
        <rect y="10" width="350" height="52" fill="#FFFFFF" stroke="#718178" stroke-width="1.5" rx="2"/>
        <text x="16" y="42" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">নাম লিখুন</text>
      </g>

      <!-- Field 2: Mobile -->
      <g transform="translate(0, 230)">
        <text x="0" y="0" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="600">মোবাইল নম্বর <tspan fill="#9B302B">*</tspan></text>
        <rect y="10" width="350" height="52" fill="#FFFFFF" stroke="#718178" stroke-width="1.5" rx="2"/>
        <text x="16" y="42" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">01XXXXXXXXX</text>
      </g>

      <!-- Field 3: City / Area -->
      <g transform="translate(0, 320)">
        <text x="0" y="0" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="600">এলাকা বা শহর <tspan fill="#9B302B">*</tspan></text>
        <rect y="10" width="350" height="52" fill="#FFFFFF" stroke="#718178" stroke-width="1.5" rx="2"/>
        <text x="16" y="42" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">যেমন: মিরপুর, ঢাকা</text>
      </g>

      <!-- Field 4: Service -->
      <g transform="translate(0, 410)">
        <text x="0" y="0" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="600">কী ধরনের কাজ প্রয়োজন? <tspan fill="#9B302B">*</tspan></text>
        <rect y="10" width="350" height="52" fill="#FFFFFF" stroke="#718178" stroke-width="1.5" rx="2"/>
        <text x="16" y="42" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">বেছে নিন</text>
        <text x="315" y="42" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">▼</text>
      </g>

      <!-- Collapsed Optional Fields -->
      <g transform="translate(0, 500)">
        <rect width="350" height="48" fill="#DEE7E2" rx="2"/>
        <text x="15" y="30" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="600">+ আরও তথ্য (ঐচ্ছিক: আয়তন, বাজেট)</text>
      </g>

      <!-- Submit Button -->
      <g transform="translate(0, 580)">
        <rect width="350" height="52" fill="#183B35" rx="2"/>
        <text x="125" y="32" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="700">অনুরোধ পাঠান</text>
        <text x="0" y="80" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="12">যোগাযোগের জন্য এই তথ্য ব্যবহার করা হবে। <tspan text-decoration="underline">গোপনীয়তা নীতি</tspan></text>
      </g>

      <!-- Direct Alternatives -->
      <g transform="translate(0, 700)">
        <text x="0" y="0" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="700">অথবা সরাসরি কথা বলুন:</text>
        <rect y="15" width="350" height="48" fill="#F4F1E8" stroke="#183B35" stroke-width="1.5" rx="2"/>
        <text x="100" y="45" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">WhatsApp-এ আলাপ</text>
      </g>
    </g>
  </g>

  <!-- ========================================================= -->
  <!-- SCREEN 3: MOBILE NAVIGATION OVERLAY (390 x 844) -->
  <!-- ========================================================= -->
  <g transform="translate(1100, 100)">
    <rect width="390" height="844" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="2"/>
    <text x="0" y="-20" fill="#183B35" font-family="'Manrope', sans-serif" font-size="18" font-weight="700">03. মোবাইল মেনু ড্রয়ার (Mobile Navigation Drawer Overlay)</text>

    <!-- Top Bar with Close Button -->
    <rect width="390" height="72" fill="#F4F1E8"/>
    <text x="24" y="44" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">FLOWGRID</text>
    <rect x="310" y="14" width="56" height="44" fill="#183B35" rx="2"/>
    <text x="330" y="41" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">✕</text>
    <line x1="24" y1="72" x2="366" y2="72" stroke="#B8C2BA" stroke-width="1"/>

    <!-- Large Nav Links -->
    <g transform="translate(24, 120)">
      <text x="0" y="40" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="28" font-weight="700">আমাদের কাজ</text>
      <line x1="0" y1="65" x2="342" y2="65" stroke="#DEE7E2" stroke-width="1"/>

      <text x="0" y="115" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="28" font-weight="700">সেবাসমূহ</text>
      <line x1="0" y1="140" x2="342" y2="140" stroke="#DEE7E2" stroke-width="1"/>

      <text x="0" y="190" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="28" font-weight="700">কাজের পদ্ধতি</text>
      <line x1="0" y1="215" x2="342" y2="215" stroke="#DEE7E2" stroke-width="1"/>

      <text x="0" y="265" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="28" font-weight="700">স্টুডিও পরিচয়</text>
      <line x1="0" y1="290" x2="342" y2="290" stroke="#DEE7E2" stroke-width="1"/>

      <text x="0" y="340" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="28" font-weight="700">যোগাযোগ</text>
      <line x1="0" y1="365" x2="342" y2="365" stroke="#DEE7E2" stroke-width="1"/>
    </g>

    <!-- Language Selector Inside Menu -->
    <g transform="translate(24, 540)">
      <text x="0" y="0" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14">Language / ভাষা:</text>
      <rect y="10" width="180" height="48" fill="#DEE7E2" rx="2"/>
      <rect x="4" y="14" width="80" height="40" fill="#183B35" rx="2"/>
      <text x="25" y="39" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="600">বাংলা</text>
      <text x="115" y="39" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">EN</text>
    </g>

    <!-- Sibling Business Links -->
    <g transform="translate(24, 650)">
      <text x="0" y="0" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">অন্যান্য প্রতিষ্ঠান:</text>
      <text x="0" y="25" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14">রুমি’স ফ্যাশনেবল হাউজ (ভ্লগ) ↗</text>
      <text x="0" y="50" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14">অনেকটা প্রোডাক্ট (হোম অ্যাপ্লায়েন্স) ↗</text>
    </g>
  </g>
</svg>"""

with open('figma_svgs/04_mobile_bn.svg', 'w', encoding='utf-8') as f:
    f.write(svg_04)

print("Saved 04_mobile_bn.svg")
