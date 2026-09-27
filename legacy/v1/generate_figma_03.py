"""
FlowGrid - Page 03: Desktop — BN (Bangla 1440px Templates) SVG Generator
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
img_bedroom = get_base64_image('concepts/concept_03_bedroom_dhaka.jpg')

svg_03 = f"""<svg width="4800" height="4200" viewBox="0 0 4800 4200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="4800" height="4200" fill="#E5E1D8"/>

  <!-- ========================================================= -->
  <!-- SCREEN 1: DESKTOP HOME (1440 x 3800) -->
  <!-- ========================================================= -->
  <g transform="translate(100, 100)">
    <!-- Canvas Frame -->
    <rect width="1440" height="3800" fill="#F4F1E8" rx="2"/>
    <text x="0" y="-20" fill="#183B35" font-family="'Manrope', sans-serif" font-size="20" font-weight="700">01. বাংলা ডেস্কটপ হোমপেজ (Desktop Home — BN · 1440px)</text>

    <!-- Header (88px) -->
    <rect width="1440" height="88" fill="#F4F1E8"/>
    <line x1="64" y1="88" x2="1376" y2="88" stroke="#B8C2BA" stroke-width="1"/>
    <text x="64" y="52" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="30" font-weight="700">FLOWGRID</text>
    <text x="64" y="70" fill="#56645E" font-family="'Manrope', sans-serif" font-size="11" letter-spacing="1">INTERIOR STUDIO</text>
    
    <text x="750" y="52" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">কাজ</text>
    <text x="830" y="52" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">সেবা</text>
    <text x="910" y="52" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">পদ্ধতি</text>
    <text x="1000" y="52" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">স্টুডিও</text>
    
    <text x="1100" y="52" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">বাংলা <tspan fill="#B8C2BA">|</tspan> EN</text>
    
    <rect x="1200" y="20" width="176" height="48" fill="#183B35" rx="2"/>
    <text x="1225" y="50" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="600">কথা বলুন</text>

    <!-- Hero Section (800px) -->
    <g transform="translate(64, 120)">
      <rect width="1312" height="740" fill="#183B35" rx="0"/>
      <!-- Embedded Living Image -->
      <image href="{img_living}" x="0" y="0" width="1312" height="740" preserveAspectRatio="xMidYMid slice" opacity="0.88"/>
      <!-- Subtle shadow vignette on left for typography readability -->
      <rect x="0" y="0" width="650" height="740" fill="url(#heroVignette)" opacity="0.7"/>

      <!-- Hero Text (Bangla) -->
      <text x="60" y="440" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="58" font-weight="700" line-height="1.3">আপনার জীবনের ছন্দে,</text>
      <text x="60" y="515" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="58" font-weight="700" line-height="1.3">আপনার ঘর।</text>
      <text x="60" y="575" fill="#DEE7E2" font-family="'Noto Sans Bengali', sans-serif" font-size="20" font-weight="400">আপনার প্রয়োজন, পছন্দ ও বাজেট বুঝে প্রতিটি কোণের সুচিন্তিত পরিকল্পনা।</text>
      
      <rect x="60" y="615" width="220" height="52" fill="#F4F1E8" rx="2"/>
      <text x="95" y="647" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="700">আমাদের কাজ দেখুন →</text>

      <!-- Honest Concept Tag -->
      <rect x="990" y="670" width="280" height="34" fill="#183B35" opacity="0.85" rx="2"/>
      <text x="1005" y="693" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="13" font-weight="600">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>
    </g>

    <!-- Studio Proposition Section (340px) -->
    <g transform="translate(64, 920)">
      <text x="0" y="40" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700" letter-spacing="1">THE FLOWGRID APPROACH</text>
      <text x="0" y="100" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="38" font-weight="600">একটি পরিশীলিত বাড়ি।</text>
      <text x="0" y="150" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="38" font-weight="600">একটি সুস্পষ্ট প্রক্রিয়া।</text>

      <text x="650" y="95" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="18" line-height="1.8">আমরা বিশ্বাস করি, ঘর কেবল সুন্দর দেখানোর জায়গা নয়—এটি আপনার প্রতিদিনের যাপনের স্বস্তি। আমরা শুরু করি আপনার পরিবার কীভাবে সময় কাটায়, কতটা সঞ্চয় ও স্টোরেজ প্রয়োজন, এবং আপনার বাজেট কতটুকু। কোনো অবাস্তব প্রতিশ্রুতি বা অতিরিক্ত খরচ ছাড়া, স্বচ্ছ পরিকল্পনায় তৈরি হয় আপনার আপন ঠিকানা।</text>
      <text x="650" y="195" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="700">আমাদের কাজের পদ্ধতি দেখুন →</text>
      <line x1="0" y1="240" x2="1312" y2="240" stroke="#B8C2BA" stroke-width="1"/>
    </g>

    <!-- Selected Projects Section (Asymmetrical 7/5 Grid) -->
    <g transform="translate(64, 1220)">
      <text x="0" y="30" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700" letter-spacing="1">SELECTED WORK</text>
      <text x="0" y="80" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="36" font-weight="600">উদ্দেশ্যপূর্ণ পরিকল্পনা, পরিমিত সৌন্দর্য</text>
      <text x="1180" y="80" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="700">সকল কাজ দেখুন →</text>

      <!-- Project 1 (7 cols: 755px) -->
      <g transform="translate(0, 130)">
        <rect width="755" height="520" fill="#DEE7E2"/>
        <image href="{img_living}" x="0" y="0" width="755" height="520" preserveAspectRatio="xMidYMid slice"/>
        <rect x="20" y="20" width="280" height="30" fill="#183B35" opacity="0.9" rx="2"/>
        <text x="32" y="41" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="13" font-weight="600">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>
        
        <text x="0" y="560" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="24" font-weight="600">অ্যাপার্টমেন্ট স্টাডি ০১ — পরিবার ও পরিসর</text>
        <text x="0" y="590" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="16">মিরপুর, ঢাকা · লিভিং, রিডিং কর্নার ও সিলিং-হাই স্টোরেজ</text>
        <text x="0" y="620" fill="#895239" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="600">বাস্তবায়িত প্রকল্প নয় — ডিজাইন কনসেপ্ট স্টাডি</text>
      </g>

      <!-- Project 2 (5 cols: 533px, offset down) -->
      <g transform="translate(779, 210)">
        <rect width="533" height="440" fill="#DEE7E2"/>
        <image href="{img_kitchen}" x="0" y="0" width="533" height="440" preserveAspectRatio="xMidYMid slice"/>
        <rect x="20" y="20" width="280" height="30" fill="#183B35" opacity="0.9" rx="2"/>
        <text x="32" y="41" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="13" font-weight="600">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>

        <text x="0" y="480" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="24" font-weight="600">কিচেন স্টাডি ০২ — নিত্যদিনের রান্না</text>
        <text x="0" y="510" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="16">ঢাকা অ্যাপার্টমেন্ট · তেল-মসলা সহনশীল গ্রানাইট ও এলপিজি ক্যাবিনেট</text>
        <text x="0" y="540" fill="#895239" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="600">বাস্তবায়িত প্রকল্প নয় — ডিজাইন কনসেপ্ট স্টাডি</text>
      </g>
    </g>

    <!-- Services Section (Ruled Rows) -->
    <g transform="translate(64, 2150)">
      <line x1="0" y1="0" x2="1312" y2="0" stroke="#B8C2BA" stroke-width="1"/>
      <text x="0" y="50" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700" letter-spacing="1">SERVICES</text>
      <text x="0" y="100" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="36" font-weight="600">আমাদের সেবাসমূহ</text>

      <!-- Row 1 -->
      <g transform="translate(0, 140)">
        <line x1="0" y1="0" x2="1312" y2="0" stroke="#B8C2BA" stroke-width="1"/>
        <text x="20" y="45" fill="#895239" font-family="'Bodoni Moda', serif" font-size="24">01</text>
        <text x="90" y="45" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="24" font-weight="600">গৃহ অভ্যন্তর পরিকল্পনা (Home Interiors)</text>
        <text x="500" y="45" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="16">সম্পূর্ণ ফ্ল্যাট বা একক রুমের লে-আউট, আলোকবিন্যাস ও কাস্টম ফার্নিচার ড্রয়িং।</text>
        <text x="1270" y="45" fill="#183B35" font-family="'Manrope', sans-serif" font-size="24">→</text>
        <line x1="0" y1="80" x2="1312" y2="80" stroke="#B8C2BA" stroke-width="1"/>
      </g>

      <!-- Row 2 -->
      <g transform="translate(0, 230)">
        <text x="20" y="45" fill="#895239" font-family="'Bodoni Moda', serif" font-size="24">02</text>
        <text x="90" y="45" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="24" font-weight="600">রান্নাঘর ও স্টোরেজ সলিউশন (Kitchens &amp; Storage)</text>
        <text x="500" y="45" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="16">নিত্যদিনের ভারী রান্নার সহনশীল কাউন্টারটপ, সিলিন্ডার স্পেস ও নিখুঁত ক্যাবিনেট্রি।</text>
        <text x="1270" y="45" fill="#183B35" font-family="'Manrope', sans-serif" font-size="24">→</text>
        <line x1="0" y1="80" x2="1312" y2="80" stroke="#B8C2BA" stroke-width="1"/>
      </g>

      <!-- Row 3 -->
      <g transform="translate(0, 320)">
        <text x="20" y="45" fill="#895239" font-family="'Bodoni Moda', serif" font-size="24">03</text>
        <text x="90" y="45" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="24" font-weight="600">রিনোভেশন ও রিমডেলিং (Renovation Planning)</text>
        <text x="500" y="45" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="16">পুরনো ফ্ল্যাটের দেয়াল বা পাইপলাইনের ক্ষতি না করে আধুনিক স্পেস ইউটিলাইজেশন।</text>
        <text x="1270" y="45" fill="#183B35" font-family="'Manrope', sans-serif" font-size="24">→</text>
        <line x1="0" y1="80" x2="1312" y2="80" stroke="#B8C2BA" stroke-width="1"/>
      </g>
    </g>

    <!-- Process Preview (5 Stages) -->
    <g transform="translate(64, 2630)">
      <rect width="1312" height="240" fill="#DEE7E2" rx="2"/>
      <text x="40" y="45" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700" letter-spacing="1">HOW WE WORK</text>
      <text x="40" y="85" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="28" font-weight="600">প্রথম আলাপ থেকে নকশা হস্তান্তর</text>

      <!-- 5 Steps -->
      <g transform="translate(40, 120)">
        <text x="0" y="25" fill="#895239" font-family="'Bodoni Moda', serif" font-size="18" font-weight="600">01</text>
        <text x="35" y="25" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">প্রাথমিক আলাপ</text>
        <text x="35" y="50" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="13">প্রয়োজন ও বাজেট</text>

        <text x="250" y="25" fill="#895239" font-family="'Bodoni Moda', serif" font-size="18" font-weight="600">02</text>
        <text x="285" y="25" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">স্থান পরিদর্শন</text>
        <text x="285" y="50" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="13">পরিমাপ ও বাস্তবতা</text>

        <text x="500" y="25" fill="#895239" font-family="'Bodoni Moda', serif" font-size="18" font-weight="600">03</text>
        <text x="535" y="25" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">ডিজাইন প্রণয়ন</text>
        <text x="535" y="50" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="13">লে-আউট ও ম্যাটেরিয়াল</text>

        <text x="750" y="25" fill="#895239" font-family="'Bodoni Moda', serif" font-size="18" font-weight="600">04</text>
        <text x="785" y="25" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">বাজেট অনুমোদন</text>
        <text x="785" y="50" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="13">স্পষ্ট আইটেমাইজেশন</text>

        <text x="1000" y="25" fill="#895239" font-family="'Bodoni Moda', serif" font-size="18" font-weight="600">05</text>
        <text x="1035" y="25" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">হস্তান্তর</text>
        <text x="1035" y="50" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="13">চূড়ান্ত তদারকি ও নথি</text>
      </g>
    </g>

    <!-- Studio / Trust Section (320px) -->
    <g transform="translate(64, 2940)">
      <text x="0" y="40" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700" letter-spacing="1">OUR STUDIO</text>
      <text x="0" y="90" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="34" font-weight="600">ঘরের প্রতিটি সিদ্ধান্তের পেছনে দায়িত্বশীল মুখ</text>
      
      <text x="0" y="140" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="17" line-height="1.8">FlowGrid মিরপুর, ঢাকায় অবস্থিত একটি পারিবারিক ইন্টেরিয়র ডিজাইন স্টুডিও। রুমি’স ফ্যাশনেবল হাউজ-এর দীর্ঘদিনের পারিবারিক ও ঘরোয়া কমিউনিটির অনুপ্রেরণায় আমাদের এই যাত্রা। আমরা প্রতিটি প্রজেক্টে স্বচ্ছতা, টেকসই উপকরণ ও বাস্তবসম্মত বাজেট রক্ষা করি। কোনো কাল্পনিক সংখ্যা বা অবাস্তব আন্তর্জাতিক মেগা-প্রজেক্ট নয়—আমরা সাধারণের অসাধারণ বাড়ি গড়ি।</text>
      
      <rect x="0" y="200" width="220" height="52" fill="#183B35" rx="2"/>
      <text x="40" y="232" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">স্টুডিও টিম দেখুন →</text>
    </g>

    <!-- Closing Enquiry Panel (Full Pine Panel) -->
    <g transform="translate(64, 3300)">
      <rect width="1312" height="260" fill="#183B35" rx="2"/>
      <text x="80" y="80" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="40" font-weight="700">আপনার ঘরের কথা বলুন।</text>
      <text x="80" y="125" fill="#DEE7E2" font-family="'Noto Sans Bengali', sans-serif" font-size="18">আপনার ফ্ল্যাটের পরিসর ও প্রয়োজন শেয়ার করুন। FlowGrid টিম আপনার সঙ্গে যোগাযোগ করবে।</text>

      <rect x="80" y="160" width="240" height="52" fill="#F4F1E8" rx="2"/>
      <text x="120" y="192" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="700">অনুরোধ পাঠান →</text>

      <text x="360" y="192" fill="#DEE7E2" font-family="'Noto Sans Bengali', sans-serif" font-size="16">অথবা সরাসরি কথা বলুন: <tspan fill="#FFFFFF" text-decoration="underline">WhatsApp</tspan> বা <tspan fill="#FFFFFF" text-decoration="underline">কল করুন</tspan></text>
    </g>

    <!-- Footer -->
    <g transform="translate(64, 3600)">
      <line x1="0" y1="0" x2="1312" y2="0" stroke="#B8C2BA" stroke-width="1"/>
      <text x="0" y="50" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">FLOWGRID</text>
      <text x="0" y="80" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">Mirpur, Dhaka, Bangladesh 1216 · © 2026 FlowGrid</text>

      <text x="500" y="50" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="600">সম্পর্কিত প্রতিষ্ঠানসমূহ:</text>
      <text x="500" y="80" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="13">রুমি’স ফ্যাশনেবল হাউজ (ভ্লগ ও গল্প) ↗ | অনেকটা প্রোডাক্ট (হোম অ্যাপ্লায়েন্স) ↗</text>

      <text x="1050" y="50" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">গোপনীয়তা নীতি | সেবার নীতিমালা</text>
    </g>
  </g>

  <!-- ========================================================= -->
  <!-- SCREEN 2: DESKTOP CASE STUDY DETAIL (1440 x 3600) -->
  <!-- ========================================================= -->
  <g transform="translate(1700, 100)">
    <rect width="1440" height="3600" fill="#F4F1E8" rx="2"/>
    <text x="0" y="-20" fill="#183B35" font-family="'Manrope', sans-serif" font-size="20" font-weight="700">02. প্রকল্প বিস্তারিত কেস স্টাডি (Project Case Study Detail — BN)</text>

    <!-- Header (88px) -->
    <rect width="1440" height="88" fill="#F4F1E8"/>
    <line x1="64" y1="88" x2="1376" y2="88" stroke="#B8C2BA" stroke-width="1"/>
    <text x="64" y="52" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="30" font-weight="700">FLOWGRID</text>
    <text x="1100" y="52" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">বাংলা <tspan fill="#B8C2BA">|</tspan> EN</text>
    <rect x="1200" y="20" width="176" height="48" fill="#183B35" rx="2"/>
    <text x="1225" y="50" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="600">কথা বলুন</text>

    <!-- Breadcrumb & Title Area -->
    <g transform="translate(64, 120)">
      <text x="0" y="25" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="15">আমাদের কাজ / <tspan fill="#183B35" font-weight="600">অ্যাপার্টমেন্ট স্টাডি ০১</tspan></text>
      
      <text x="0" y="80" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="46" font-weight="700">অ্যাপার্টমেন্ট স্টাডি ০১ · পারিবারিক লিভিং ও স্টোরেজ</text>
      
      <!-- Explicit Honest Status Tag -->
      <rect x="0" y="105" width="380" height="34" fill="#183B35" rx="2"/>
      <text x="16" y="128" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="600">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়</text>

      <!-- Factual Metadata Strip -->
      <g transform="translate(0, 160)">
        <rect width="1312" height="60" fill="#DEE7E2" rx="2"/>
        <text x="24" y="36" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">ধরন: <tspan fill="#183B35" font-weight="600">পারিবারিক ফ্ল্যাট</tspan></text>
        <text x="320" y="36" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">ফোকাস: <tspan fill="#183B35" font-weight="600">লিভিং, বুকশেলফ ও ব্যালকনি আলো</tspan></text>
        <text x="680" y="36" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">কাল্পনিক অবস্থান: <tspan fill="#183B35" font-weight="600">মিরপুর, ঢাকা</tspan></text>
        <text x="1000" y="36" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">স্ট্যাটাস: <tspan fill="#895239" font-weight="700">ডিজাইন স্টাডি</tspan></text>
      </g>
    </g>

    <!-- Master Hero Photo (16:9) -->
    <g transform="translate(64, 380)">
      <rect width="1312" height="740" fill="#DEE7E2"/>
      <image href="{img_living}" x="0" y="0" width="1312" height="740" preserveAspectRatio="xMidYMid slice"/>
      <text x="0" y="770" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">চিত্র ০১: ঢাকার আধুনিক ফ্ল্যাটের লিভিং স্পেস—সিলিং-হাই সেগুন কাঠের শেলফ এবং আলোযুক্ত ব্যালকনি বিন্যাস।</text>
    </g>

    <!-- Two-Column Brief & Space Intent -->
    <g transform="translate(64, 1200)">
      <text x="0" y="30" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700" letter-spacing="1">01 / THE BRIEF &amp; NEED</text>
      <text x="0" y="80" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="34" font-weight="600">দৈনন্দিন জীবনের স্থান,</text>
      <text x="0" y="125" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="34" font-weight="600">পরিপাটি স্টোরেজের মেলবন্ধন।</text>

      <text x="650" y="50" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="17" line-height="1.8">ঢাকার স্ট্যান্ডার্ড আবাসিক অ্যাপার্টমেন্টে সাধারণ সমস্যা হলো অতিরিক্ত সামগ্রী রাখার জায়গার অভাব এবং অপরিকল্পিত ক্যাবিনেটের কারণে ঘর অন্ধকার হয়ে যাওয়া। এই স্টাডিতে আমরা পরীক্ষা করেছি কীভাবে দেয়ালের উল্লম্ব স্থান ব্যবহার করে টিভি ইউনিট ও বুকশেলফকে একটি সমন্বিত আর্কিটেকচারাল উপাদানে রূপান্তর করা যায়, যাতে মেঝের চলাচলের পথ সম্পূর্ণ বাধাহীন থাকে।</text>
      <line x1="0" y1="180" x2="1312" y2="180" stroke="#B8C2BA" stroke-width="1"/>
    </g>

    <!-- 3 Key Space Decisions -->
    <g transform="translate(64, 1430)">
      <text x="0" y="30" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700" letter-spacing="1">02 / DESIGN DECISIONS</text>
      <text x="0" y="80" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="34" font-weight="600">নকশার তিনটি প্রধান সমাধান</text>

      <!-- Decision 1 -->
      <g transform="translate(0, 120)">
        <text x="20" y="35" fill="#895239" font-family="'Bodoni Moda', serif" font-size="22">01</text>
        <text x="80" y="35" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="22" font-weight="600">দেয়াল জুড়ে ইন-বিল্ট স্টোরেজ</text>
        <text x="80" y="70" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="16">আলাদা আলমারির পরিবর্তে কাঠামোগত শেলফ তৈরি করায় ঘরের মেঝের ৮০% জায়গা উন্মুক্ত থাকে।</text>
        <line x1="0" y1="95" x2="1312" y2="95" stroke="#DEE7E2" stroke-width="1"/>
      </g>

      <!-- Decision 2 -->
      <g transform="translate(0, 230)">
        <text x="20" y="35" fill="#895239" font-family="'Bodoni Moda', serif" font-size="22">02</text>
        <text x="80" y="35" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="22" font-weight="600">ব্যালকনি গ্রিল ও ভেন্টিলেশন সমন্বয়</text>
        <text x="80" y="70" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="16">ঢাকার আর্দ্র আবহাওয়ায় প্রাকৃতিক বাতাস ও বিকেলের আলো সরাসরি লিভিং রুম পর্যন্ত প্রবেশের পথ নিশ্চিত করা।</text>
        <line x1="0" y1="95" x2="1312" y2="95" stroke="#DEE7E2" stroke-width="1"/>
      </g>

      <!-- Decision 3 -->
      <g transform="translate(0, 340)">
        <text x="20" y="35" fill="#895239" font-family="'Bodoni Moda', serif" font-size="22">03</text>
        <text x="80" y="35" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="22" font-weight="600">সহজ পরিচর্যাযোগ্য দেশীয় উপাদান</text>
        <text x="80" y="70" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="16">সেগুন কাঠের ফিনিশ, হাতে বোনা বেত ও নিঃশ্বাসযোগ্য লাইম প্লাস্টার দেয়াল—যা সহজে পরিষ্কার রাখা যায়।</text>
        <line x1="0" y1="95" x2="1312" y2="95" stroke="#DEE7E2" stroke-width="1"/>
      </g>
    </g>

    <!-- Material Specifications & Details -->
    <g transform="translate(64, 1920)">
      <text x="0" y="30" fill="#895239" font-family="'Manrope', sans-serif" font-size="14" font-weight="700" letter-spacing="1">03 / MATERIAL PALETTE</text>
      <text x="0" y="80" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="34" font-weight="600">উপাদান ও রঙের সমন্বয়</text>

      <g transform="translate(0, 110)">
        <!-- Material 1 -->
        <rect x="0" y="0" width="310" height="180" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>
        <rect x="20" y="20" width="40" height="40" fill="#895239" rx="2"/>
        <text x="75" y="45" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="18" font-weight="600">সেগুন কাঠ (Teak)</text>
        <text x="20" y="90" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">ক্যাবিনেট্রি ও বুকশেলফে ব্যবহৃত ম্যাট ল্যাকার পলিশযুক্ত স্থানীয় কাষ্ঠল উপাদান।</text>

        <!-- Material 2 -->
        <rect x="334" y="0" width="310" height="180" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>
        <rect x="354" y="20" width="40" height="40" fill="#DEE7E2" rx="2"/>
        <text x="409" y="45" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="18" font-weight="600">হাতে বোনা বেত (Cane)</text>
        <text x="354" y="90" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">চেয়ার ও অ্যাকসেন্টে ব্যবহৃত ঐতিহ্যবাহী প্রাকৃতিক টেক্সচার।</text>

        <!-- Material 3 -->
        <rect x="668" y="0" width="310" height="180" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>
        <rect x="688" y="20" width="40" height="40" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1" rx="2"/>
        <text x="743" y="45" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="18" font-weight="600">লাইম প্লাস্টার (Plaster)</text>
        <text x="688" y="90" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">উষ্ণ পেপার টোনের দেয়াল ফিনিশ, যা নরম প্রাকৃতিক আলো প্রতিফলন করে।</text>

        <!-- Material 4 -->
        <rect x="1002" y="0" width="310" height="180" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="2"/>
        <rect x="1022" y="20" width="40" height="40" fill="#183B35" rx="2"/>
        <text x="1077" y="45" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="18" font-weight="600">অলিভ লিনেন (Textile)</text>
        <text x="1022" y="90" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">আরামদায়ক সোফার কভারিং, যা আবহাওয়ার জন্য উপযোগী ও স্বাস্থ্যকর।</text>
      </g>
    </g>

    <!-- Contextual Enquiry Banner -->
    <g transform="translate(64, 2250)">
      <rect width="1312" height="240" fill="#183B35" rx="2"/>
      <text x="80" y="80" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="34" font-weight="700">আপনার ঘরের জন্যও কি এমন সমাধান খুঁজছেন?</text>
      <text x="80" y="125" fill="#DEE7E2" font-family="'Noto Sans Bengali', sans-serif" font-size="17">আপনার ফ্ল্যাটের আকার ও প্রয়োজন জানান। FlowGrid টিম আলোচনা শুরু করতে প্রস্তুত।</text>
      <rect x="80" y="155" width="240" height="52" fill="#F4F1E8" rx="2"/>
      <text x="120" y="187" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="700">অনুরোধ পাঠান →</text>
    </g>

    <!-- Footer -->
    <g transform="translate(64, 2550)">
      <line x1="0" y1="0" x2="1312" y2="0" stroke="#B8C2BA" stroke-width="1"/>
      <text x="0" y="40" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="24" font-weight="700">FLOWGRID</text>
      <text x="0" y="70" fill="#56645E" font-family="'Manrope', sans-serif" font-size="13">© 2026 FlowGrid Interior Studio · Mirpur, Dhaka 1216</text>
    </g>
  </g>

  <!-- Gradient Defs -->
  <defs>
    <linearGradient id="heroVignette" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#183B35" stop-opacity="0.95"/>
      <stop offset="70%" stop-color="#183B35" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#183B35" stop-opacity="0"/>
    </linearGradient>
  </defs>
</svg>"""

with open('figma_svgs/03_desktop_bn.svg', 'w', encoding='utf-8') as f:
    f.write(svg_03)

print("Saved 03_desktop_bn.svg")
