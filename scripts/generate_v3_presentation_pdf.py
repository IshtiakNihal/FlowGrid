"""
FlowGrid - Customer Presentation Deck Generator v3 (16:9 Landscape PDF)
8 Deliberate Landscape Slides (1152 x 648 pt), True Visual Screen Displays,
Reconciled Contrast, Single Owner Fact Register, and Zero Text Cut-off.
"""
import os
import base64
import subprocess
import re

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

# High-resolution crops of actual rendered screens (replacing hand-coded mockups)
img_crop_desk_home = get_base64_image('figma_exports/crop_desktop_home.png')
img_crop_desk_arch = get_base64_image('figma_exports/crop_desktop_archive.png')
img_crop_desk_study = get_base64_image('figma_exports/crop_desktop_study.png')
img_crop_desk_serv = get_base64_image('figma_exports/crop_desktop_services.png')

img_crop_mob_home = get_base64_image('figma_exports/crop_mobile_home.png')
img_crop_mob_drawer = get_base64_image('figma_exports/crop_mobile_drawer.png')
img_crop_mob_study = get_base64_image('figma_exports/crop_mobile_study.png')
img_crop_mob_contact = get_base64_image('figma_exports/crop_mobile_contact.png')
img_crop_mob_form = get_base64_image('figma_exports/crop_mobile_form.png')

html_content = f"""<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="utf-8">
<title>FlowGrid — Design System &amp; Responsive Experience Presentation v3</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..700;1,6..96,400..700&family=Manrope:wght@400;500;600;700;800&family=Noto+Sans+Bengali:wght@400;500;600;700&display=swap');

  @page {{
    size: 16in 9in;
    margin: 0;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: 'Manrope', 'Noto Sans Bengali', sans-serif;
    background-color: #E5E1D8;
    color: #183B35;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  .slide {{
    width: 16in;
    height: 9in;
    page-break-after: always;
    position: relative;
    background-color: #F4F1E8;
    padding: 0.55in 0.75in;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  .slide-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-bottom: 1.5px solid #B8C2BA;
    padding-bottom: 12px;
    margin-bottom: 18px;
  }}

  .brand {{
    font-family: 'Bodoni Moda', serif;
    font-size: 26px;
    font-weight: 700;
    letter-spacing: 1px;
    color: #183B35;
  }}

  .brand-sub {{
    font-family: 'Manrope', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #895239;
    text-transform: uppercase;
    margin-top: 2px;
  }}

  .slide-num {{
    font-family: 'Bodoni Moda', serif;
    font-size: 24px;
    font-weight: 600;
    color: #895239;
  }}

  .slide-title-block {{
    margin-bottom: 16px;
  }}

  .slide-title {{
    font-family: 'Bodoni Moda', serif;
    font-size: 30px;
    font-weight: 700;
    color: #183B35;
    line-height: 1.15;
  }}

  .slide-subtitle {{
    font-family: 'Manrope', sans-serif;
    font-size: 14px;
    color: #56645E;
    margin-top: 4px;
  }}

  .slide-body {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }}

  .slide-footer {{
    border-top: 1px solid #B8C2BA;
    padding-top: 10px;
    display: flex;
    justify-content: space-between;
    font-size: 11px;
    color: #56645E;
    font-family: 'Manrope', sans-serif;
  }}

  .card {{
    background: #FFFFFF;
    border: 1px solid #B8C2BA;
    border-radius: 4px;
    padding: 16px 20px;
  }}

  .card-tinted {{
    background: #DEE7E2;
    border: 1px solid #B8C2BA;
    border-radius: 4px;
    padding: 16px 20px;
  }}

  .accent-label {{
    font-family: 'Manrope', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #895239;
    text-transform: uppercase;
    margin-bottom: 6px;
  }}

  .truth-tag {{
    display: inline-block;
    background: #183B35;
    color: #F4F1E8;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 8px;
    border-radius: 2px;
    font-family: 'Noto Sans Bengali', sans-serif;
  }}

  .grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }}

  .grid-3 {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
  }}

  .grid-4 {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 16px;
  }}

  .img-box {{
    width: 100%;
    overflow: hidden;
    background: #DEE7E2;
    border-radius: 2px;
  }}

  .img-box img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }}

  .table-custom {{
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
  }}

  .table-custom th {{
    background: #183B35;
    color: #F4F1E8;
    text-align: left;
    padding: 8px 10px;
    font-weight: 600;
  }}

  .table-custom td {{
    padding: 7px 10px;
    border-bottom: 1px solid #DEE7E2;
    color: #183B35;
  }}
</style>
</head>
<body>

  <!-- ============================================================== -->
  <!-- SLIDE 1: COVER                                                 -->
  <!-- ============================================================== -->
  <div class="slide" style="background-color: #183B35; color: #F4F1E8;">
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #2E5D4B; padding-bottom: 16px;">
      <div style="font-family: 'Manrope', sans-serif; font-size: 13px; letter-spacing: 2px; color: #DEE7E2;">
        FLOWGRID INTERIOR ARCHITECTURE STUDIO · MIRPUR, DHAKA 1216
      </div>
      <div style="font-family: 'Manrope', sans-serif; font-size: 13px; color: #DEE7E2;">
        VERIFIED DESIGN HANDOFF V3
      </div>
    </div>

    <div style="margin: auto 0;">
      <div style="font-family: 'Manrope', sans-serif; font-size: 15px; font-weight: 700; letter-spacing: 3px; color: #895239; margin-bottom: 14px; text-transform: uppercase;">
        Design System, Responsive Templates &amp; Architectural Concept Studies
      </div>
      <h1 style="font-family: 'Bodoni Moda', serif; font-size: 58px; font-weight: 700; line-height: 1.1; color: #F4F1E8; margin-bottom: 20px;">
        Room for Everyday Life<br>
        <span style="font-family: 'Noto Sans Bengali', sans-serif; font-size: 42px; font-weight: 600; color: #DEE7E2;">
          দৈনন্দিন জীবনের শান্ত ও সুবিন্যস্ত স্থাপত্য
        </span>
      </h1>
      <p style="font-family: 'Manrope', sans-serif; font-size: 16px; line-height: 1.6; color: #DEE7E2; max-width: 900px;">
        A comprehensive bilingual web experience and native design system tailored for urban apartment households in Dhaka, Bangladesh. Grounded in functional storage density, seasoned timber craftsmanship, and natural daylight.
      </p>
    </div>

    <div style="border-top: 1px solid #2E5D4B; padding-top: 16px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; font-size: 12px; color: #DEE7E2;">
      <div>
        <div style="color: #895239; font-weight: 700; margin-bottom: 4px;">LOCATION</div>
        <div>Mirpur-10, Dhaka 1216</div>
      </div>
      <div>
        <div style="color: #895239; font-weight: 700; margin-bottom: 4px;">MATERIAL PALETTE</div>
        <div>Burma Teak, Sylhet Cane, Lime, Granite</div>
      </div>
      <div>
        <div style="color: #895239; font-weight: 700; margin-bottom: 4px;">ACCESSIBILITY</div>
        <div>Measured 10.84:1 &amp; 48px Hit Areas</div>
      </div>
      <div>
        <div style="color: #895239; font-weight: 700; margin-bottom: 4px;">DISCLOSURE POLICY</div>
        <div>Strict Truth in AI Visualization</div>
      </div>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- SLIDE 2: THREE BUSINESSES & FACT REGISTER                      -->
  <!-- ============================================================== -->
  <div class="slide">
    <div class="slide-header">
      <div>
        <div class="brand">FLOWGRID</div>
        <div class="brand-sub">RESEARCH AUDIT &amp; GOVERNANCE</div>
      </div>
      <div class="slide-num">02 / 08</div>
    </div>

    <div class="slide-title-block">
      <div class="slide-title">Three Distinct Businesses &amp; Clear Governance Boundaries</div>
      <div class="slide-subtitle">Audit of live channels establishing strict entity boundaries and a single owner fact confirmation register.</div>
    </div>

    <div class="slide-body">
      <div class="grid-3" style="margin-bottom: 20px;">
        <div class="card">
          <div class="accent-label">CORE ENTITY · STUDIO</div>
          <h3 style="font-family: 'Bodoni Moda', serif; font-size: 20px; color: #183B35; margin-bottom: 8px;">1. FlowGrid</h3>
          <p style="font-size: 13px; line-height: 1.6; color: #56645E; margin-bottom: 10px;">
            Independent interior architecture studio in Mirpur, Dhaka. Specializes in bespoke joinery, family apartment space planning, and turnkey execution.
          </p>
          <div style="background: #F4F1E8; padding: 8px 12px; border-radius: 2px; font-size: 11px; color: #183B35; font-weight: 600;">
            Boundary Rule: Not an appliance retailer; not an influencer fan club; not a generic construction contractor.
          </div>
        </div>

        <div class="card">
          <div class="accent-label">COMMUNITY SIBLING · VLOGS</div>
          <h3 style="font-family: 'Bodoni Moda', serif; font-size: 20px; color: #183B35; margin-bottom: 8px;">2. Rumi's Fashionable House</h3>
          <p style="font-size: 13px; line-height: 1.6; color: #56645E; margin-bottom: 10px;">
            Verified YouTube community (140K subscribers, 2,368 videos, 36.6M views) focusing on lifestyle vlogs, home cooking, and family routines.
          </p>
          <div style="background: #F4F1E8; padding: 8px 12px; border-radius: 2px; font-size: 11px; color: #183B35; font-weight: 600;">
            Boundary Rule: Founder/community context. Strictly distinct from architectural licensure.
          </div>
        </div>

        <div class="card">
          <div class="accent-label">COMMERCE SIBLING · RETAIL</div>
          <h3 style="font-family: 'Bodoni Moda', serif; font-size: 20px; color: #183B35; margin-bottom: 8px;">3. Onekta Product</h3>
          <p style="font-size: 13px; line-height: 1.6; color: #56645E; margin-bottom: 10px;">
            Independent e-commerce seller of practical household essentials, small kitchen gadgets, and home accessories.
          </p>
          <div style="background: #F4F1E8; padding: 8px 12px; border-radius: 2px; font-size: 11px; color: #183B35; font-weight: 600;">
            Boundary Rule: FlowGrid does NOT host shopping carts or sell retail appliances. Outbound link only.
          </div>
        </div>
      </div>

      <!-- Single Owner Fact Register -->
      <div class="card-tinted">
        <div class="accent-label">OPERATIONAL AUDIT · SINGLE FACT REGISTER</div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; font-size: 12px; line-height: 1.5;">
          <div>
            <strong>Studio Address:</strong><br>Mirpur-10, Dhaka 1216 (provisional Facebook audit).
          </div>
          <div>
            <strong>Contact Telephone:</strong><br>+880 1700-000000 (placeholder; unverified FB 01712-402422).
          </div>
          <div>
            <strong>Production Domain:</strong><br>flowgrid-interiors.com (DNS confirmed pending setup).
          </div>
          <div>
            <strong>Concept Proof:</strong><br>All 3D visuals are strictly labelled as AI visual studies.
          </div>
        </div>
      </div>
    </div>

    <div class="slide-footer">
      <span>FlowGrid Design System Presentation · Slide 02 of 08</span>
      <span>Governance &amp; Entity Integrity</span>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- SLIDE 3: DESIGN FOUNDATIONS & ACCESSIBILITY                    -->
  <!-- ============================================================== -->
  <div class="slide">
    <div class="slide-header">
      <div>
        <div class="brand">FLOWGRID</div>
        <div class="brand-sub">DESIGN TOKENS &amp; SYSTEM FOUNDATIONS</div>
      </div>
      <div class="slide-num">03 / 08</div>
    </div>

    <div class="slide-title-block">
      <div class="slide-title">Design Foundations &amp; Authentic Material Register</div>
      <div class="slide-subtitle">Semantic color palette, reconciled mathematical contrast ratios, bilingual typography, and authentic materials.</div>
    </div>

    <div class="slide-body">
      <div class="grid-2" style="margin-bottom: 18px;">
        <!-- Left: Semantic Colors & Contrast -->
        <div class="card">
          <div class="accent-label">COLOR SYSTEM &amp; RECONCILED CONTRAST CHECKS</div>
          <table class="table-custom">
            <tr>
              <th>Color Token</th>
              <th>Hex Value</th>
              <th>Usage Context</th>
              <th>Measured Ratio</th>
              <th>Compliance</th>
            </tr>
            <tr>
              <td>Warm Paper</td>
              <td><code>#F4F1E8</code></td>
              <td>Canvas background</td>
              <td>Base Canvas</td>
              <td>N/A</td>
            </tr>
            <tr>
              <td>Deep Pine Ink</td>
              <td><code>#183B35</code></td>
              <td>Headings, body, primary CTAs (on #F4F1E8)</td>
              <td><strong>10.84 : 1</strong></td>
              <td>PASS (AAA)</td>
            </tr>
            <tr>
              <td>Muted Pine Slate</td>
              <td><code>#56645E</code></td>
              <td>Secondary text (on White #FFFFFF)</td>
              <td><strong>6.21 : 1</strong></td>
              <td>PASS (AA)</td>
            </tr>
            <tr>
              <td>Muted Pine Slate</td>
              <td><code>#56645E</code></td>
              <td>Secondary text (on Paper #F4F1E8)</td>
              <td><strong>5.50 : 1</strong></td>
              <td>PASS (AA)</td>
            </tr>
            <tr>
              <td>Terracotta Clay</td>
              <td><code>#895239</code></td>
              <td>Focus rings, category badges (on #F4F1E8)</td>
              <td><strong>5.58 : 1</strong></td>
              <td>PASS (AA)</td>
            </tr>
            <tr>
              <td>Dark Forest Teal</td>
              <td><code>#0D5C52</code></td>
              <td>WhatsApp action (on White #FFFFFF)</td>
              <td><strong>7.87 : 1</strong></td>
              <td>PASS (AAA)</td>
            </tr>
            <tr>
              <td>Soft Mist (Footer)</td>
              <td><code>#DEE7E2</code></td>
              <td>Dark footer links (on #183B35)</td>
              <td><strong>9.69 : 1</strong></td>
              <td>PASS (AAA)</td>
            </tr>
            <tr>
              <td>Light Slate (Footer)</td>
              <td><code>#C4D1CA</code></td>
              <td>Dark footer secondary (on #183B35)</td>
              <td><strong>7.76 : 1</strong></td>
              <td>PASS (AAA)</td>
            </tr>
            <tr>
              <td>Validation Crimson</td>
              <td><code>#9B302B</code></td>
              <td>Error text &amp; outline with icon (on #F4F1E8)</td>
              <td><strong>6.52 : 1</strong></td>
              <td>PASS (AA)</td>
            </tr>
          </table>
          <div style="font-size: 11px; color: #895239; margin-top: 8px;">
            * Slate on White measures 6.21:1 (AA). Light Slate on Pine measures 7.76:1 (AAA). Soft Mist on Pine measures 9.69:1 (AAA). All ratios mathematically verified from sRGB relative luminance.
          </div>
        </div>

        <!-- Right: Typography & Spatial Scale -->
        <div class="card">
          <div class="accent-label">BILINGUAL TYPOGRAPHY &amp; SPATIAL SCALE</div>
          <div style="margin-bottom: 12px;">
            <div style="font-family: 'Bodoni Moda', serif; font-size: 22px; color: #183B35; font-weight: 700;">
              Bodoni Moda (Display Serif) · 88px / 44px
            </div>
            <div style="font-size: 12px; color: #56645E;">
              Editorial monumental display for architectural titles and hero statements.
            </div>
          </div>
          <div style="margin-bottom: 12px;">
            <div style="font-family: 'Noto Sans Bengali', sans-serif; font-size: 18px; color: #183B35; font-weight: 600;">
              Noto Sans Bengali · 56px Hero / 17px Body (1.75 Line Height)
            </div>
            <div style="font-size: 12px; color: #56645E;">
              Ample vertical measure for Bengali ascenders, descenders, and vowel signs.
            </div>
          </div>
          <div style="background: #DEE7E2; padding: 12px; border-radius: 4px; font-size: 12px; color: #183B35;">
            <strong>Architectural Geometry Policy:</strong><br>
            • Media Radius: <strong>0px</strong> (Strict architectural squared edges).<br>
            • Control Radius: <strong>2px</strong> (Tactile softness, never pill-shaped).<br>
            • Touch Targets: Minimum <strong>48 × 48 px</strong> hit areas across all viewports.
          </div>
        </div>
      </div>

      <!-- Material Palette -->
      <div class="card-tinted" style="padding: 12px 20px;">
        <div class="accent-label">AUTHENTIC MATERIAL PALETTE REGISTER</div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; font-size: 12px;">
          <div>
            <strong>1. Burma Teak Wood:</strong><br>Seasoned timber with matte oil finish.
          </div>
          <div>
            <strong>2. Sylhet Woven Cane:</strong><br>Breathable panels for monsoon humidity.
          </div>
          <div>
            <strong>3. Natural Lime Plaster:</strong><br>Chuna Polish, glare-free breathable texture.
          </div>
          <div>
            <strong>4. Honed Gray Granite:</strong><br>20mm stain-resistant kitchen slab.
          </div>
        </div>
      </div>
    </div>

    <div class="slide-footer">
      <span>FlowGrid Design System Presentation · Slide 03 of 08</span>
      <span>Mathematical Contrast Verification &amp; Spatial Foundations</span>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- SLIDE 4: CONCEPT STUDY 01 — 3 COHERENT VIEWS                   -->
  <!-- ============================================================== -->
  <div class="slide">
    <div class="slide-header">
      <div>
        <div class="brand">FLOWGRID</div>
        <div class="brand-sub">CONCEPT STUDY 01 · GULSHAN LAKEVIEW RESIDENCE</div>
      </div>
      <div class="slide-num">04 / 08</div>
    </div>

    <div class="slide-title-block">
      <div class="slide-title">Gulshan Lakeview Residence — 3 Coherent Spatial Views</div>
      <div class="slide-subtitle">Contemporary family living space exploring daylighting, joinery density, and climate-resilient natural materials.</div>
    </div>

    <div class="slide-body">
      <div class="grid-3" style="margin-bottom: 14px;">
        <!-- View 1 -->
        <div class="card" style="padding: 12px;">
          <div style="height: 240px; margin-bottom: 10px;" class="img-box">
            <img src="{img_living_1}" alt="Gulshan Living Room Hero">
          </div>
          <div class="truth-tag">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত নয়</div>
          <h4 style="font-family: 'Bodoni Moda', serif; font-size: 16px; margin: 8px 0 4px; color: #183B35;">View 1: Living Hero &amp; Teak Media Wall</h4>
          <p style="font-size: 11px; color: #56645E; line-height: 1.5;">
            Floor-to-ceiling Burma teak media wall with horizontal timber slats, concealed cabling, and integrated low console.
          </p>
          <div style="font-size: 10px; color: #895239; margin-top: 4px; font-family: monospace;">Resolution: 1376 × 768 px</div>
        </div>

        <!-- View 2 -->
        <div class="card" style="padding: 12px;">
          <div style="height: 240px; margin-bottom: 10px;" class="img-box">
            <img src="{img_living_2}" alt="Gulshan Dining & Daylight">
          </div>
          <div class="truth-tag">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত নয়</div>
          <h4 style="font-family: 'Bodoni Moda', serif; font-size: 16px; margin: 8px 0 4px; color: #183B35;">View 2: Dining &amp; Veranda Daylight Angle</h4>
          <p style="font-size: 11px; color: #56645E; line-height: 1.5;">
            Dining table integration showing unobstructed sightlines, sheer linen drapery, and Dhaka natural afternoon daylight.
          </p>
          <div style="font-size: 10px; color: #895239; margin-top: 4px; font-family: monospace;">Resolution: 1376 × 768 px (Concept Variant)</div>
        </div>

        <!-- View 3 -->
        <div class="card" style="padding: 12px;">
          <div style="height: 240px; margin-bottom: 10px;" class="img-box">
            <img src="{img_living_3}" alt="Gulshan Joinery Detail">
          </div>
          <div class="truth-tag">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত নয়</div>
          <h4 style="font-family: 'Bodoni Moda', serif; font-size: 16px; margin: 8px 0 4px; color: #183B35;">View 3: Burma Teak Lap Joint &amp; Brass Inlay</h4>
          <p style="font-size: 11px; color: #56645E; line-height: 1.5;">
            Macro close-up of precision interlocking timber lap joint with polished brass inlay and matte organic oil finish.
          </p>
          <div style="font-size: 10px; color: #895239; margin-top: 4px; font-family: monospace;">Resolution: 1376 × 768 px</div>
        </div>
      </div>

      <div class="card-tinted" style="padding: 10px 16px; font-size: 11px; color: #183B35;">
        <strong>Documented Study Assumptions:</strong> Hypothetical 1,800–2,150 SFT apartment scenario for research and design exploration. Alternate angles are exploratory variants sharing material language, not photogrammetrically identical rooms.
      </div>
    </div>

    <div class="slide-footer">
      <span>FlowGrid Design System Presentation · Slide 04 of 08</span>
      <span>Living &amp; Storage Architecture Study</span>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- SLIDE 5: CONCEPT STUDIES 02 & 03                               -->
  <!-- ============================================================== -->
  <div class="slide">
    <div class="slide-header">
      <div>
        <div class="brand">FLOWGRID</div>
        <div class="brand-sub">CONCEPT STUDIES 02 &amp; 03 · KITCHEN &amp; BEDROOM</div>
      </div>
      <div class="slide-num">05 / 08</div>
    </div>

    <div class="slide-title-block">
      <div class="slide-title">High-Performance Kitchen &amp; Master Platform Bedroom</div>
      <div class="slide-subtitle">Purposeful architectural responses to intensive domestic cooking routines and quiet restful privacy.</div>
    </div>

    <div class="slide-body">
      <div class="grid-2">
        <!-- Kitchen Card -->
        <div class="card" style="padding: 16px;">
          <div style="height: 270px; margin-bottom: 12px;" class="img-box">
            <img src="{img_kitchen}" alt="Dhanmondi Kitchen Concept">
          </div>
          <div class="truth-tag">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত নয়</div>
          <div class="accent-label" style="margin-top: 8px;">CONCEPT 02 · RESILIENT DHAKA KITCHEN</div>
          <h3 style="font-family: 'Bodoni Moda', serif; font-size: 19px; color: #183B35; margin-bottom: 6px;">Resilient Kitchen, Pantry &amp; Galley Layout</h3>
          <p style="font-size: 12px; color: #56645E; line-height: 1.5; margin-bottom: 8px;">
            Honed 20mm dark granite countertops, open wall shelving, stainless steel fixtures, and compact galley kitchen configuration.
          </p>
          <div style="font-size: 10px; color: #895239; font-family: monospace;">Resolution: 1376 × 768 px · Assumed Study Constraint</div>
        </div>

        <!-- Bedroom Card -->
        <div class="card" style="padding: 16px;">
          <div style="height: 270px; margin-bottom: 12px;" class="img-box">
            <img src="{img_bedroom}" alt="Uttara Bedroom Concept">
          </div>
          <div class="truth-tag">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত নয়</div>
          <div class="accent-label" style="margin-top: 8px;">CONCEPT 03 · RESTFUL MASTER BEDROOM</div>
          <h3 style="font-family: 'Bodoni Moda', serif; font-size: 19px; color: #183B35; margin-bottom: 6px;">Master Platform Suite &amp; Acoustic Timber Slats</h3>
          <p style="font-size: 12px; color: #56645E; line-height: 1.5; margin-bottom: 8px;">
            Low-profile teak platform bed, slatted acoustic timber wall panelling, soft diffused lighting, and natural breathable finishes.
          </p>
          <div style="font-size: 10px; color: #895239; font-family: monospace;">Resolution: 1376 × 768 px · Assumed Study Constraint</div>
        </div>
      </div>
    </div>

    <div class="slide-footer">
      <span>FlowGrid Design System Presentation · Slide 05 of 08</span>
      <span>Culinary &amp; Restful Architectural Studies</span>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- SLIDE 6: DESKTOP EXPERIENCE SUITE (ACTUAL VISUAL SCREENS)      -->
  <!-- ============================================================== -->
  <div class="slide">
    <div class="slide-header">
      <div>
        <div class="brand">FLOWGRID</div>
        <div class="brand-sub">DESKTOP EXPERIENCE SUITE (1440PX)</div>
      </div>
      <div class="slide-num">06 / 08</div>
    </div>

    <div class="slide-title-block">
      <div class="slide-title">Desktop Experience Suite &amp; Complete Page Scope</div>
      <div class="slide-subtitle">Actual high-fidelity architectural page layouts across 11 templates in Bangla and English at 1440px master resolution.</div>
    </div>

    <div class="slide-body">
      <div class="grid-4" style="margin-bottom: 14px;">
        <!-- Visual Screen 1: Home -->
        <div class="card" style="padding: 10px;">
          <div class="accent-label">1. HOMEPAGE (/)</div>
          <div style="background: #F4F1E8; border: 1px solid #B8C2BA; border-radius: 2px; height: 260px; overflow: hidden; position: relative;">
            <img src="{img_crop_desk_home}" style="width: 100%; height: 100%; object-fit: cover; object-position: top; display: block;" alt="Desktop Homepage Screen Render">
          </div>
          <div style="font-size: 11px; color: #183B35; font-weight: 600; margin-top: 6px;">Master Bengali Homepage</div>
          <div style="font-size: 10px; color: #56645E;">Actual render from 1440px board</div>
        </div>

        <!-- Visual Screen 2: Projects Archive -->
        <div class="card" style="padding: 10px;">
          <div class="accent-label">2. PROJECTS ARCHIVE</div>
          <div style="background: #F4F1E8; border: 1px solid #B8C2BA; border-radius: 2px; height: 260px; overflow: hidden; position: relative;">
            <img src="{img_crop_desk_arch}" style="width: 100%; height: 100%; object-fit: cover; object-position: top; display: block;" alt="Projects Archive Screen Render">
          </div>
          <div style="font-size: 11px; color: #183B35; font-weight: 600; margin-top: 6px;">Filterable Concept Archive</div>
          <div style="font-size: 10px; color: #56645E;">Actual render from 1440px board</div>
        </div>

        <!-- Visual Screen 3: Case Study & Real-Project -->
        <div class="card" style="padding: 10px;">
          <div class="accent-label">3. 3-VIEW CASE STUDY</div>
          <div style="background: #F4F1E8; border: 1px solid #B8C2BA; border-radius: 2px; height: 260px; overflow: hidden; position: relative;">
            <img src="{img_crop_desk_study}" style="width: 100%; height: 100%; object-fit: cover; object-position: top; display: block;" alt="3-View Study Screen Render">
          </div>
          <div style="font-size: 11px; color: #183B35; font-weight: 600; margin-top: 6px;">3-View Case Study Template</div>
          <div style="font-size: 10px; color: #56645E;">Actual render from 1440px board</div>
        </div>

        <!-- Visual Screen 4: Services & Process -->
        <div class="card" style="padding: 10px;">
          <div class="accent-label">4. SERVICES &amp; JOINERY</div>
          <div style="background: #F4F1E8; border: 1px solid #B8C2BA; border-radius: 2px; height: 260px; overflow: hidden; position: relative;">
            <img src="{img_crop_desk_serv}" style="width: 100%; height: 100%; object-fit: cover; object-position: top; display: block;" alt="Services Screen Render">
          </div>
          <div style="font-size: 11px; color: #183B35; font-weight: 600; margin-top: 6px;">Dedicated Services &amp; Joinery</div>
          <div style="font-size: 10px; color: #56645E;">Actual render from 1440px board</div>
        </div>
      </div>

      <div class="card-tinted" style="padding: 10px 16px; font-size: 11px; color: #183B35;">
        <strong>Desktop Page Scope:</strong> 11 dedicated templates authored at 1440px master resolution in both Bengali and English (Total 22 Desktop page layouts across suite: Homepage, Projects Archive, 3-View Study, Built-Project Framework, Services, Millwork Detail, Process, Studio &amp; Team, Contact Form, Privacy, and 404).
      </div>
    </div>

    <div class="slide-footer">
      <span>FlowGrid Design System Presentation · Slide 06 of 08</span>
      <span>Desktop Experience Suite &amp; Template Matrix</span>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- SLIDE 7: MOBILE RESPONSIVE EXPERIENCE (ACTUAL SCREENS)         -->
  <!-- ============================================================== -->
  <div class="slide">
    <div class="slide-header">
      <div>
        <div class="brand">FLOWGRID</div>
        <div class="brand-sub">MOBILE RESPONSIVE SUITE (390PX)</div>
      </div>
      <div class="slide-num">07 / 08</div>
    </div>

    <div class="slide-title-block">
      <div class="slide-title">Mobile Experience &amp; Off-Canvas Navigation (390px)</div>
      <div class="slide-subtitle">Viewport previews, off-canvas navigation drawer, and fitted 4-field consultation enquiry form.</div>
    </div>

    <div class="slide-body">
      <div class="grid-4" style="margin-bottom: 14px;">
        <!-- Screen 1: Mobile Home -->
        <div class="card" style="padding: 10px;">
          <div class="accent-label">1. MOBILE HOME PREVIEW</div>
          <div style="background: #F4F1E8; border: 1px solid #B8C2BA; border-radius: 2px; height: 260px; overflow: hidden; position: relative;">
            <img src="{img_crop_mob_home}" style="width: 100%; height: 100%; object-fit: cover; object-position: top; display: block;" alt="Mobile Home Screen Render">
          </div>
          <div style="font-size: 11px; color: #183B35; font-weight: 600; margin-top: 6px;">Mobile Home Viewport Preview</div>
          <div style="font-size: 10px; color: #56645E;">Top-of-page render (390px)</div>
        </div>

        <!-- Screen 2: Mobile Drawer Overlay -->
        <div class="card" style="padding: 10px;">
          <div class="accent-label">2. OFF-CANVAS DRAWER</div>
          <div style="background: #183B35; border-radius: 2px; height: 260px; overflow: hidden; position: relative;">
            <img src="{img_crop_mob_drawer}" style="width: 100%; height: 100%; object-fit: cover; object-position: top; display: block;" alt="Mobile Drawer Screen Render">
          </div>
          <div style="font-size: 11px; color: #183B35; font-weight: 600; margin-top: 6px;">Off-Canvas Drawer Preview</div>
          <div style="font-size: 10px; color: #56645E;">Separate layer; zero footer overlap</div>
        </div>

        <!-- Screen 3: Mobile 3-View Case Study -->
        <div class="card" style="padding: 10px;">
          <div class="accent-label">3. CASE STUDY PREVIEW</div>
          <div style="background: #F4F1E8; border: 1px solid #B8C2BA; border-radius: 2px; height: 260px; overflow: hidden; position: relative;">
            <img src="{img_crop_mob_study}" style="width: 100%; height: 100%; object-fit: cover; object-position: top; display: block;" alt="Mobile 3-View Study Render">
          </div>
          <div style="font-size: 11px; color: #183B35; font-weight: 600; margin-top: 6px;">Case Study Viewport Preview</div>
          <div style="font-size: 10px; color: #56645E;">Top-of-study render (390px)</div>
        </div>

        <!-- Screen 4: 4-Field Enquiry Form States -->
        <div class="card" style="padding: 10px;">
          <div class="accent-label">4. COMPLETE 4-FIELD FORM</div>
          <div style="background: #F4F1E8; border: 1px solid #B8C2BA; border-radius: 2px; height: 260px; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center;">
            <img src="{img_crop_mob_form}" style="max-width: 100%; max-height: 100%; object-fit: contain; display: block;" alt="Complete Mobile Form Render">
          </div>
          <div style="font-size: 11px; color: #183B35; font-weight: 600; margin-top: 6px;">Complete 4-Field Form (Zero Cut-off)</div>
          <div style="font-size: 10px; color: #56645E;">All 4 required inputs &amp; 52px CTA visible</div>
        </div>
      </div>

      <div class="card-tinted" style="padding: 10px 16px; font-size: 11px; color: #183B35;">
        <strong>Mobile Suite Coverage:</strong> 11 dedicated mobile templates (390px) in Bengali and 11 in English (Total 22 mobile layouts + 2 off-canvas drawers). Previews 1–3 demonstrate viewport styling; Preview 4 fits the complete 4-field consultation enquiry form with 48px touch targets and 52px submission CTA without clipping.
      </div>
    </div>

    <div class="slide-footer">
      <span>FlowGrid Design System Presentation · Slide 07 of 08</span>
      <span>Mobile Architecture &amp; Touch Ergonomics</span>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- SLIDE 8: MOTION, ACCESSIBILITY & NEXT STEPS                    -->
  <!-- ============================================================== -->
  <div class="slide">
    <div class="slide-header">
      <div>
        <div class="brand">FLOWGRID</div>
        <div class="brand-sub">ENGINEERING HANDOFF &amp; CLIENT ACTIONS</div>
      </div>
      <div class="slide-num">08 / 08</div>
    </div>

    <div class="slide-title-block">
      <div class="slide-title">Motion Engineering, Verification Boundary &amp; Next Steps</div>
      <div class="slide-subtitle">Restrained kinetics, production CSS tokens, honest accessibility limits, and actionable client business questions.</div>
    </div>

    <div class="slide-body">
      <div class="grid-2" style="margin-bottom: 16px;">
        <!-- Left: Motion & CSS -->
        <div class="card">
          <div class="accent-label">RESTRAINED MOTION &amp; REDUCED-MOTION CSS</div>
          <ul style="font-size: 12px; line-height: 1.7; color: #56645E; padding-left: 18px; margin-bottom: 10px;">
            <li><strong>Hero Reveal (600ms):</strong> Center hairline split opens dual-wing horizontal mask wipe. Headline and CTAs immediately interactive (zero delayed usability).</li>
            <li><strong>Card Hover (360ms):</strong> Zero vertical lift (0px), zero shadow explosion. Subtle 1.015 image scale within strict 0px radius frame.</li>
            <li><strong>Drawer Kinetics:</strong> Unified 220ms enter / 160ms exit slide-out.</li>
          </ul>
          <div style="background: #183B35; color: #DEE7E2; padding: 10px; border-radius: 4px; font-family: monospace; font-size: 11px;">
            @media (prefers-reduced-motion: reduce) {{<br>
            &nbsp;&nbsp;*, *::before, *::after {{ animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }}<br>
            &nbsp;&nbsp;.hero-mask {{ clip-path: none !important; opacity: 1 !important; }}<br>
            }} /* Valid closing brace verified */
          </div>
        </div>

        <!-- Right: Actionable Client Questions -->
        <div class="card">
          <div class="accent-label">ACTIONABLE CLIENT BUSINESS QUESTIONS</div>
          <ol style="font-size: 11px; line-height: 1.6; color: #183B35; padding-left: 18px;">
            <li><strong>Vector Logo:</strong> Supply final SVG/AI for official wordmark.</li>
            <li><strong>Direct Hotline:</strong> Confirm public mobile number for calls &amp; WhatsApp.</li>
            <li><strong>Service Area:</strong> Confirm Dhaka metropolitan vs. nationwide coverage.</li>
            <li><strong>Commercial Model:</strong> Clarify design-only consultancy vs. turnkey joinery.</li>
            <li><strong>Site Visit Fee:</strong> Clarify if initial spatial consultation is complimentary.</li>
            <li><strong>Team Profiles:</strong> Provide verified names &amp; photos for Studio page.</li>
            <li><strong>Founder Statement:</strong> Authorize official wording for Rumi's context.</li>
            <li><strong>Domain Activation:</strong> Authorize DNS activation for flowgrid-interiors.com.</li>
          </ol>
        </div>
      </div>

      <!-- Final Status Banner with Explicit Status Taxonomy -->
      <div style="background: #183B35; color: #F4F1E8; padding: 12px 20px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center;">
        <div>
          <div style="font-weight: 700; font-size: 13px;">Verification Status: Implemented in Local SVGs/HTML · Verified via Headless Edge Renders</div>
          <div style="font-size: 11px; color: #DEE7E2;">All 44 page layouts authored in vector SVGs &amp; verified in PNGs · Read-only Figma tool boundary disclosed</div>
        </div>
        <div style="background: #895239; color: white; padding: 6px 14px; border-radius: 2px; font-weight: 600; font-size: 12px;">
          Figma File: eMRunQ80brYYvuTWkufV2o
        </div>
      </div>
    </div>

    <div class="slide-footer">
      <span>FlowGrid Design System Presentation · Slide 08 of 08</span>
      <span>Technical Handoff &amp; Verification Matrix</span>
    </div>
  </div>

</body>
</html>
"""

with open("presentation_v3.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved presentation_v3.html")

# Compile to PDF using Edge headless
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
html_abs = os.path.abspath("presentation_v3.html").replace("\\", "/")
pdf_abs = os.path.abspath("FlowGrid_Client_Presentation.pdf")

cmd = f'"{edge_path}" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="{pdf_abs}" "file:///{html_abs}"'
print("Running command:", cmd)
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print("Return code:", res.returncode)

if os.path.exists("FlowGrid_Client_Presentation.pdf"):
    size = os.path.getsize("FlowGrid_Client_Presentation.pdf")
    with open("FlowGrid_Client_Presentation.pdf", "rb") as f:
        content = f.read()
    mediaboxes = re.findall(rb'/MediaBox\s*\[\s*([0-9\.\s]+)\]', content)
    pages = re.findall(rb'/Type\s*/Page\b', content)
    print(f"Generated FlowGrid_Client_Presentation.pdf: {size} bytes, {len(pages)} pages, MediaBoxes: {mediaboxes[:3]}")
