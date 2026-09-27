"""
FlowGrid - Page 02: Reusable Components SVG Generator
"""
import os

svg_02 = f"""<svg width="2400" height="2400" viewBox="0 0 2400 2400" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="2400" height="2400" fill="#F4F1E8"/>
  
  <!-- Banner -->
  <rect x="80" y="80" width="2240" height="140" fill="#183B35" rx="4"/>
  <text x="120" y="145" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="36" font-weight="600">FlowGrid — Reusable Component Library</text>
  <text x="120" y="185" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="18">Atomic components, interactive states (Default, Hover, Focus, Error, Loading), navigation, cards, form inputs, and footer</text>

  <!-- Row 1: Buttons & Interactive Controls -->
  <rect x="80" y="260" width="2240" height="360" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="260" width="2240" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="293" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">01. Buttons &amp; Action States (52px Minimum Touch Height, 2px Radius)</text>

  <!-- Button State: Default Primary -->
  <g transform="translate(120, 340)">
    <text x="0" y="-15" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Primary (Default)</text>
    <rect width="220" height="52" fill="#183B35" rx="2"/>
    <text x="35" y="32" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="16" font-weight="600">আমাদের কাজ দেখুন →</text>
  </g>

  <!-- Button State: Hover -->
  <g transform="translate(380, 340)">
    <text x="0" y="-15" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Primary (Hover #102B26)</text>
    <rect width="220" height="52" fill="#102B26" rx="2"/>
    <text x="35" y="32" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="16" font-weight="600">আমাদের কাজ দেখুন →</text>
  </g>

  <!-- Button State: Focus Ring -->
  <g transform="translate(640, 340)">
    <text x="0" y="-15" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Primary (Keyboard Focus)</text>
    <rect x="-4" y="-4" width="228" height="60" fill="none" stroke="#895239" stroke-width="2" rx="4"/>
    <rect width="220" height="52" fill="#183B35" rx="2"/>
    <text x="35" y="32" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="16" font-weight="600">আমাদের কাজ দেখুন →</text>
  </g>

  <!-- Button State: Loading/Busy -->
  <g transform="translate(900, 340)">
    <text x="0" y="-15" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Primary (Loading State)</text>
    <rect width="220" height="52" fill="#183B35" opacity="0.8" rx="2"/>
    <circle cx="45" cy="26" r="8" fill="none" stroke="#F4F1E8" stroke-width="2" stroke-dasharray="16 8"/>
    <text x="65" y="32" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="15">পাঠানো হচ্ছে...</text>
  </g>

  <!-- Button State: Disabled -->
  <g transform="translate(1160, 340)">
    <text x="0" y="-15" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Primary (Disabled)</text>
    <rect width="220" height="52" fill="#B8C2BA" rx="2"/>
    <text x="45" y="32" fill="#FFFFFF" font-family="'Noto Sans Bengali', sans-serif" font-size="16">অনুরোধ পাঠান</text>
  </g>

  <!-- Secondary Outlined Button -->
  <g transform="translate(120, 470)">
    <text x="0" y="-15" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Secondary (Outlined)</text>
    <rect width="220" height="52" fill="#F4F1E8" stroke="#718178" stroke-width="1.5" rx="2"/>
    <text x="40" y="32" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">বিস্তারিত জানুন</text>
  </g>

  <!-- Direct WhatsApp Channel Button (Restrained Pine, not neon) -->
  <g transform="translate(380, 470)">
    <text x="0" y="-15" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">WhatsApp Channel (Restrained)</text>
    <rect width="220" height="52" fill="#F4F1E8" stroke="#183B35" stroke-width="1.5" rx="2"/>
    <circle cx="40" cy="26" r="10" fill="#183B35"/>
    <text x="36" y="30" fill="#FFFFFF" font-family="'Manrope', sans-serif" font-size="12" font-weight="700">W</text>
    <text x="60" y="32" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">WhatsApp-এ আলাপ</text>
  </g>

  <!-- Direct Phone Call Button -->
  <g transform="translate(640, 470)">
    <text x="0" y="-15" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Direct Phone Call</text>
    <rect width="220" height="52" fill="#183B35" rx="2"/>
    <path d="M40 20 C42 22, 45 25, 45 28 C45 31, 38 33, 38 33" stroke="#F4F1E8" stroke-width="2" fill="none"/>
    <text x="60" y="32" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="600">সরাসরি কল করুন</text>
  </g>

  <!-- Language Switch Control -->
  <g transform="translate(900, 470)">
    <text x="0" y="-15" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Bilingual Toggle</text>
    <rect width="180" height="52" fill="#DEE7E2" rx="2"/>
    <rect x="6" y="6" width="80" height="40" fill="#183B35" rx="2"/>
    <text x="30" y="31" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="600">বাংলা</text>
    <text x="120" y="31" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">EN</text>
  </g>

  <!-- Row 2: Navigation Headers (Desktop & Mobile) -->
  <rect x="80" y="650" width="2240" height="340" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="650" width="2240" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="683" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">02. Navigation Bars (Desktop 88px, Mobile 72px)</text>

  <!-- Desktop Header Frame -->
  <g transform="translate(120, 720)">
    <text x="0" y="-10" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Desktop Global Navigation (1440px Canvas, 88px Height, Solid Paper Surface)</text>
    <rect width="2160" height="88" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    
    <!-- Wordmark -->
    <text x="40" y="48" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="28" font-weight="700" letter-spacing="1">FLOWGRID</text>
    <text x="40" y="68" fill="#56645E" font-family="'Manrope', sans-serif" font-size="11" letter-spacing="1.5">INTERIOR STUDIO · DHAKA</text>

    <!-- Nav Links (Bangla) -->
    <text x="900" y="52" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">কাজ</text>
    <text x="1000" y="52" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">সেবা</text>
    <text x="1100" y="52" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">পদ্ধতি</text>
    <text x="1210" y="52" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">স্টুডিও</text>

    <!-- Lang -->
    <text x="1680" y="52" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">বাংলা <tspan fill="#B8C2BA">|</tspan> EN</text>

    <!-- Primary CTA -->
    <rect x="1860" y="18" width="240" height="52" fill="#183B35" rx="2"/>
    <text x="1900" y="50" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">আপনার ঘর নিয়ে কথা বলি</text>
  </g>

  <!-- Mobile Header Frame -->
  <g transform="translate(120, 850)">
    <text x="0" y="-10" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Mobile Navigation Header (390px Canvas, 72px Height)</text>
    <rect width="600" height="72" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    <text x="24" y="44" fill="#183B35" font-family="'Bodoni Moda', serif" font-size="22" font-weight="700">FLOWGRID</text>
    <text x="440" y="44" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">EN</text>
    <rect x="490" y="14" width="86" height="44" fill="#183B35" rx="2"/>
    <text x="515" y="42" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="600">মেনু</text>
  </g>

  <!-- Row 3: Cards, Service Rows & Form Controls -->
  <rect x="80" y="1020" width="2240" height="980" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>
  <rect x="80" y="1020" width="2240" height="50" fill="#183B35" rx="4 4 0 0"/>
  <text x="110" y="1053" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="18" font-weight="600">03. Project Cards (with Explicit Status), 3-Row Service Structure &amp; Form Fields</text>

  <!-- Project Card (Concept Study Example) -->
  <g transform="translate(120, 1100)">
    <text x="0" y="-10" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Project / Concept Card (Truthful Status Label)</text>
    <rect width="480" height="400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    
    <!-- Image Box -->
    <rect x="0" y="0" width="480" height="260" fill="#DEE7E2"/>
    <text x="150" y="135" fill="#56645E" font-family="'Manrope', sans-serif" font-size="15">[4:3 Ratio Architectural Image]</text>
    
    <!-- Concept Label Pill (Visible, not hidden) -->
    <rect x="20" y="20" width="280" height="32" fill="#183B35" opacity="0.9" rx="2"/>
    <text x="32" y="42" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="13" font-weight="600">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</text>

    <!-- Card Content -->
    <text x="24" y="300" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="22" font-weight="600">অ্যাপার্টমেন্ট স্টাডি ০১</text>
    <text x="24" y="325" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="15">মিরপুর, ঢাকা · লিভিং ও মাল্টিফাংশনাল স্টোরেজ</text>
    <text x="24" y="355" fill="#895239" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="600">বাস্তবায়িত প্রকল্প নয় — ডিজাইন স্টাডি</text>
    <text x="24" y="380" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="700">বিস্তারিত কেস স্টাডি দেখুন →</text>
  </g>

  <!-- 3-Row Ruled Service Component -->
  <g transform="translate(640, 1100)">
    <text x="0" y="-10" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Ruled Service Component (No Cluttered Bento Cards)</text>
    <rect width="680" height="400" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>
    
    <!-- Row 1 -->
    <g transform="translate(24, 30)">
      <line x1="0" y1="0" x2="632" y2="0" stroke="#B8C2BA" stroke-width="1"/>
      <text x="10" y="40" fill="#895239" font-family="'Bodoni Moda', serif" font-size="20">01</text>
      <text x="60" y="40" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="20" font-weight="600">গৃহ অভ্যন্তর পরিকল্পনা (Home Interiors)</text>
      <text x="60" y="70" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="15">লে-আউট, ফার্নিচার বিন্যাস, আলো ও ম্যাটেরিয়াল নির্বাচন।</text>
      <text x="600" y="45" fill="#183B35" font-family="'Manrope', sans-serif" font-size="22">→</text>
      <line x1="0" y1="100" x2="632" y2="100" stroke="#B8C2BA" stroke-width="1"/>
    </g>

    <!-- Row 2 -->
    <g transform="translate(24, 150)">
      <text x="10" y="40" fill="#895239" font-family="'Bodoni Moda', serif" font-size="20">02</text>
      <text x="60" y="40" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="20" font-weight="600">রান্নাঘর ও স্টোরেজ সলিউশন (Kitchens &amp; Storage)</text>
      <text x="60" y="70" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="15">নিত্যদিনের রান্না, সিলিন্ডার ও সামগ্রীর দীর্ঘস্থায়ী বিন্যাস।</text>
      <text x="600" y="45" fill="#183B35" font-family="'Manrope', sans-serif" font-size="22">→</text>
      <line x1="0" y1="100" x2="632" y2="100" stroke="#B8C2BA" stroke-width="1"/>
    </g>

    <!-- Row 3 -->
    <g transform="translate(24, 270)">
      <text x="10" y="40" fill="#895239" font-family="'Bodoni Moda', serif" font-size="20">03</text>
      <text x="60" y="40" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="20" font-weight="600">সংস্কার ও রিনোভেশন পরিকল্পনা (Renovation Planning)</text>
      <text x="60" y="70" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="15">পুরনো ফ্ল্যাটের কাঠামোগত ক্ষতি ছাড়া আধুনিকায়ন।</text>
      <text x="600" y="45" fill="#183B35" font-family="'Manrope', sans-serif" font-size="22">→</text>
      <line x1="0" y1="100" x2="632" y2="100" stroke="#B8C2BA" stroke-width="1"/>
    </g>
  </g>

  <!-- Complete Enquiry Form Controls & Validation States -->
  <g transform="translate(1360, 1100)">
    <text x="0" y="-10" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Form Controls &amp; Error Validation States (52px Input Height)</text>
    <rect width="900" height="850" fill="#F4F1E8" stroke="#B8C2BA" stroke-width="1"/>

    <!-- Field 1: Name (Idle) -->
    <g transform="translate(40, 30)">
      <text x="0" y="0" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="600">আপনার নাম <tspan fill="#9B302B">*</tspan></text>
      <rect y="10" width="400" height="52" fill="#FFFFFF" stroke="#718178" stroke-width="1.5" rx="2"/>
      <text x="16" y="42" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="15">যেমন: তানভীর আহমেদ</text>
    </g>

    <!-- Field 2: Phone (Focus state with +880) -->
    <g transform="translate(470, 30)">
      <text x="0" y="0" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="600">মোবাইল নম্বর <tspan fill="#9B302B">*</tspan></text>
      <rect y="10" width="390" height="52" fill="#FFFFFF" stroke="#895239" stroke-width="2" rx="2"/>
      <text x="16" y="42" fill="#183B35" font-family="'Manrope', sans-serif" font-size="15" font-weight="600">01712-345678</text>
    </g>

    <!-- Field 3: City / Area (Error State) -->
    <g transform="translate(40, 120)">
      <text x="0" y="0" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="600">এলাকা বা শহর <tspan fill="#9B302B">*</tspan></text>
      <rect y="10" width="400" height="52" fill="#FFFFFF" stroke="#9B302B" stroke-width="2" rx="2"/>
      <text x="16" y="42" fill="#9B302B" font-family="'Noto Sans Bengali', sans-serif" font-size="14">এলাকার নাম উল্লেখ করুন (যেমন: মিরপুর, উত্তরা)</text>
      <text x="0" y="80" fill="#9B302B" font-family="'Noto Sans Bengali', sans-serif" font-size="13">ত্রুটি: এই তথ্যটি পূরণ করা আবশ্যক</text>
    </g>

    <!-- Field 4: Service Need Dropdown -->
    <g transform="translate(470, 120)">
      <text x="0" y="0" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="15" font-weight="600">কী ধরনের কাজ প্রয়োজন? <tspan fill="#9B302B">*</tspan></text>
      <rect y="10" width="390" height="52" fill="#FFFFFF" stroke="#718178" stroke-width="1.5" rx="2"/>
      <text x="16" y="42" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="15">গৃহ অভ্যন্তর পরিকল্পনা (Home Interiors)</text>
      <text x="350" y="42" fill="#56645E" font-family="'Manrope', sans-serif" font-size="16">▼</text>
    </g>

    <!-- Optional Fields Disclosure -->
    <g transform="translate(40, 230)">
      <rect width="820" height="50" fill="#DEE7E2" rx="2"/>
      <text x="20" y="32" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="16" font-weight="600">+ আরও তথ্য দিন (ঐচ্ছিক: ফ্ল্যাটের আয়তন, বাজেট ও বার্তা)</text>
    </g>

    <!-- Expanded Optional Fields -->
    <g transform="translate(40, 310)">
      <text x="0" y="0" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="600">আনুমানিক আয়তন (বর্গফুট)</text>
      <rect y="10" width="390" height="52" fill="#FFFFFF" stroke="#718178" stroke-width="1.5" rx="2"/>
      <text x="16" y="42" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">যেমন: ১৪৫০ বর্গফুট</text>
    </g>

    <g transform="translate(470, 310)">
      <text x="0" y="0" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="600">বাজেট ধারণা (ঐচ্ছিক)</text>
      <rect y="10" width="390" height="52" fill="#FFFFFF" stroke="#718178" stroke-width="1.5" rx="2"/>
      <text x="16" y="42" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">আলোচনা সাপেক্ষে</text>
    </g>

    <!-- Message Area -->
    <g transform="translate(40, 400)">
      <text x="0" y="0" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14" font-weight="600">আপনার ঘরের কথা বলুন (ঐচ্ছিক)</text>
      <rect y="10" width="820" height="120" fill="#FFFFFF" stroke="#718178" stroke-width="1.5" rx="2"/>
      <text x="16" y="42" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="14">আপনার পরিবারের প্রয়োজন ও ঘরের বিশেষ চাহিদা সম্পর্কে সংক্ষেপে লিখুন...</text>
    </g>

    <!-- Form Submission Button & Privacy Notice -->
    <g transform="translate(40, 560)">
      <rect width="820" height="54" fill="#183B35" rx="2"/>
      <text x="340" y="34" fill="#F4F1E8" font-family="'Noto Sans Bengali', sans-serif" font-size="18" font-weight="600">অনুরোধ পাঠান</text>
      <text x="0" y="85" fill="#56645E" font-family="'Noto Sans Bengali', sans-serif" font-size="13">আপনার সঙ্গে যোগাযোগের জন্যই কেবল এই তথ্য ব্যবহার করা হবে। <tspan text-decoration="underline">গোপনীয়তা নীতি</tspan></text>
    </g>

    <!-- Submission Confirmation Banner (State: Received) -->
    <g transform="translate(40, 680)">
      <rect width="820" height="110" fill="#DEE7E2" stroke="#245C43" stroke-width="1.5" rx="4"/>
      <circle cx="45" cy="55" r="18" fill="#245C43"/>
      <text x="38" y="62" fill="#FFFFFF" font-family="'Manrope', sans-serif" font-size="20" font-weight="700">✓</text>
      <text x="80" y="45" fill="#245C43" font-family="'Noto Sans Bengali', sans-serif" font-size="18" font-weight="700">আপনার অনুরোধ সফলভাবে গৃহীত হয়েছে।</text>
      <text x="80" y="75" fill="#183B35" font-family="'Noto Sans Bengali', sans-serif" font-size="14">FlowGrid টিম আপনার তথ্য পর্যালোচনা করে শীঘ্রই ফোনে বা WhatsApp-এ যোগাযোগ করবে।</text>
    </g>
  </g>

  <!-- Row 4: Footer Component -->
  <g transform="translate(120, 2040)">
    <text x="0" y="-15" fill="#56645E" font-family="'Manrope', sans-serif" font-size="14" font-weight="600">Global Footer Component (Verified Links &amp; Clear Boundaries)</text>
    <rect width="2160" height="260" fill="#183B35" rx="4"/>
    
    <text x="60" y="70" fill="#F4F1E8" font-family="'Bodoni Moda', serif" font-size="32" font-weight="700">FLOWGRID</text>
    <text x="60" y="105" fill="#DEE7E2" font-family="'Noto Sans Bengali', sans-serif" font-size="15">আপনার জীবনের ছন্দে, আপনার ঘর।</text>
    <text x="60" y="140" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="14">Mirpur, Dhaka, Bangladesh 1216</text>
    <text x="60" y="170" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="14">WhatsApp &amp; Call Consultation Available</text>

    <!-- Navigation links -->
    <text x="650" y="70" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Studio Links</text>
    <text x="650" y="105" fill="#DEE7E2" font-family="'Noto Sans Bengali', sans-serif" font-size="14">আমাদের কাজ (Projects)</text>
    <text x="650" y="135" fill="#DEE7E2" font-family="'Noto Sans Bengali', sans-serif" font-size="14">সেবাসমূহ (Services)</text>
    <text x="650" y="165" fill="#DEE7E2" font-family="'Noto Sans Bengali', sans-serif" font-size="14">কাজের পদ্ধতি (Process)</text>
    <text x="650" y="195" fill="#DEE7E2" font-family="'Noto Sans Bengali', sans-serif" font-size="14">যোগাযোগ (Contact)</text>

    <!-- Sibling Business Gateways -->
    <text x="1150" y="70" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Related Businesses</text>
    <text x="1150" y="105" fill="#DEE7E2" font-family="'Noto Sans Bengali', sans-serif" font-size="14">রুমি'র ফ্যাশনেবল হাউজ (Rumi's Story / Portfolio) ↗</text>
    <text x="1150" y="135" fill="#DEE7E2" font-family="'Noto Sans Bengali', sans-serif" font-size="14">অনেকটা প্রোডাক্ট — হোম অ্যাপ্লায়েন্স (Onekta Product) ↗</text>
    <text x="1150" y="180" fill="#B8C2BA" font-family="'Manrope', sans-serif" font-size="12">FlowGrid does not sell appliances or retail merchandise.</text>

    <!-- Legal & Attribution -->
    <text x="1700" y="70" fill="#F4F1E8" font-family="'Manrope', sans-serif" font-size="16" font-weight="700">Policies &amp; Trust</text>
    <text x="1700" y="105" fill="#DEE7E2" font-family="'Noto Sans Bengali', sans-serif" font-size="14">গোপনীয়তা নীতি (Privacy Policy)</text>
    <text x="1700" y="135" fill="#DEE7E2" font-family="'Noto Sans Bengali', sans-serif" font-size="14">সেবার শর্তাবলী (Terms &amp; Service Info)</text>
    <text x="1700" y="195" fill="#DEE7E2" font-family="'Manrope', sans-serif" font-size="13">© 2026 FlowGrid Interior Studio. All rights reserved.</text>
  </g>
</svg>"""

with open('figma_svgs/02_components.svg', 'w', encoding='utf-8') as f:
    f.write(svg_02)

print("Saved 02_components.svg")
