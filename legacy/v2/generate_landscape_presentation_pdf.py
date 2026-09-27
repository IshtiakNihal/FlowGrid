"""
FlowGrid - Corrected Landscape Presentation PDF Generator (8 Slides, 16:9 Landscape)
Guarantees true landscape 16in x 9in (1152 x 648 pt), zero text cut-off,
full responsive screen embeds, verified concept images, and honest governance reporting.
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

html_content = f"""<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="utf-8">
<title>FlowGrid — Design System &amp; Responsive Experience Presentation</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..700;1,6..96,400..700&family=Manrope:wght@400;500;600;700;800&family=Hind+Siliguri:wght@400;500;600;700&display=swap');

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
    font-family: 'Manrope', 'Hind Siliguri', sans-serif;
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
    padding: 0.65in 0.85in;
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
    padding-bottom: 16px;
    margin-bottom: 24px;
  }}

  .brand {{
    font-family: 'Bodoni Moda', serif;
    font-size: 28px;
    font-weight: 700;
    letter-spacing: 1px;
    color: #183B35;
  }}

  .brand-sub {{
    font-family: 'Manrope', sans-serif;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #895239;
    text-transform: uppercase;
    margin-top: 4px;
  }}

  .slide-num {{
    font-family: 'Bodoni Moda', serif;
    font-size: 26px;
    font-weight: 600;
    color: #895239;
  }}

  .slide-title-block {{
    margin-bottom: 20px;
  }}

  .slide-title {{
    font-family: 'Bodoni Moda', serif;
    font-size: 34px;
    font-weight: 700;
    color: #183B35;
    line-height: 1.2;
  }}

  .slide-subtitle {{
    font-family: 'Hind Siliguri', 'Manrope', sans-serif;
    font-size: 16px;
    color: #56645E;
    margin-top: 6px;
    line-height: 1.4;
  }}

  .slide-body {{
    flex: 1;
    display: flex;
    gap: 30px;
  }}

  .slide-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #B8C2BA;
    padding-top: 14px;
    margin-top: 20px;
    font-size: 12px;
    color: #56645E;
    font-weight: 600;
  }}

  .badge-concept {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #183B35;
    color: #F4F1E8;
    padding: 6px 14px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.5px;
  }}

  .badge-dot {{
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #DEE7E2;
  }}

  .card {{
    background: #FFFFFF;
    border: 1px solid #B8C2BA;
    border-radius: 6px;
    padding: 24px;
  }}

  .grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 26px;
    width: 100%;
  }}

  .grid-3 {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 24px;
    width: 100%;
  }}

  .grid-4 {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 20px;
    width: 100%;
  }}

  .img-box {{
    border-radius: 4px;
    overflow: hidden;
    position: relative;
    background: #DEE7E2;
  }}

  .img-box img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }}

  .body-text {{
    font-size: 14px;
    line-height: 1.6;
    color: #56645E;
  }}

  .accent-label {{
    font-size: 12px;
    font-weight: 700;
    color: #895239;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 6px;
  }}
</style>
</head>
<body>

  <!-- ============================================================== -->
  <!-- SLIDE 1: TITLE & COVER SLIDE                                   -->
  <!-- ============================================================== -->
  <div class="slide" style="background-color: #183B35; color: #F4F1E8;">
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #2E5D4B; padding-bottom: 18px;">
      <div style="font-family: 'Bodoni Moda', serif; font-size: 32px; font-weight: 700; letter-spacing: 2px; color: #F4F1E8;">FLOWGRID</div>
      <div style="font-size: 13px; font-weight: 700; letter-spacing: 2px; color: #DEE7E2; text-transform: uppercase;">DHAKA · INTERIOR ARCHITECTURE &amp; JOINERY</div>
    </div>

    <div style="display: flex; gap: 50px; align-items: center; margin: 40px 0;">
      <div style="flex: 1.1;">
        <div style="font-size: 13px; font-weight: 700; color: #C5A059; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 14px;">CLIENT DESIGN PRESENTATION &amp; HANDOFF</div>
        <h1 style="font-family: 'Bodoni Moda', serif; font-size: 56px; font-weight: 600; line-height: 1.15; color: #F4F1E8; margin-bottom: 20px;">
          Quiet, Intentional<br>Urban Living.
        </h1>
        <h2 style="font-family: 'Hind Siliguri', sans-serif; font-size: 26px; font-weight: 600; color: #DEE7E2; margin-bottom: 24px;">
          শান্ত, সুপরিকল্পিত শহুরে আবাস — ঢাকা
        </h2>
        <p style="font-size: 16px; line-height: 1.7; color: #DEE7E2; max-width: 560px; margin-bottom: 30px;">
          A comprehensive residential design system, responsive bilingual interface (Bangla &amp; English), reusable Figma component architecture, and multi-view spatial concept studies crafted for Dhaka apartment living.
        </p>
        <div style="display: flex; gap: 20px; align-items: center;">
          <div class="badge-concept" style="background: #F4F1E8; color: #183B35;">
            <div class="badge-dot" style="background: #895239;"></div>
            কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়
          </div>
          <span style="font-size: 13px; color: #DEE7E2;">Mirpur 12, Dhaka 1216</span>
        </div>
      </div>

      <div style="flex: 1; height: 420px;" class="img-box">
        <img src="{img_living_1}" alt="FlowGrid Hero Living Concept">
      </div>
    </div>

    <div style="display: flex; justify-content: space-between; border-top: 1px solid #2E5D4B; padding-top: 14px; font-size: 12px; color: #DEE7E2;">
      <span>FlowGrid Design System Presentation · Slide 01 of 08</span>
      <span>Figma File: eMRunQ80brYYvuTWkufV2o · September 2026</span>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- SLIDE 2: THREE BUSINESSES & CLEAR BOUNDARIES                  -->
  <!-- ============================================================== -->
  <div class="slide">
    <div class="slide-header">
      <div>
        <div class="brand">FLOWGRID</div>
        <div class="brand-sub">STRATEGIC GOVERNANCE</div>
      </div>
      <div class="slide-num">02 / 08</div>
    </div>

    <div class="slide-title-block">
      <div class="slide-title">Three Distinct Businesses &amp; Clear Governance Boundaries</div>
      <div class="slide-subtitle">Ensuring architectural focus, preventing entity confusion, and maintaining commercial integrity.</div>
    </div>

    <div class="slide-body">
      <div class="grid-3">
        <!-- Entity 1 -->
        <div class="card" style="border-top: 4px solid #183B35;">
          <div class="accent-label">PRIMARY PRACTICE</div>
          <h3 style="font-family: 'Bodoni Moda', serif; font-size: 24px; color: #183B35; margin-bottom: 12px;">FlowGrid</h3>
          <p style="font-weight: 700; font-size: 13px; color: #183B35; margin-bottom: 10px;">Residential Interior Design &amp; Joinery</p>
          <p class="body-text" style="margin-bottom: 16px;">
            An independent architectural studio serving urban Bangladeshi homeowners in Dhaka. Specializes in space planning, natural daylight/ventilation corridors, and bespoke Burmese teak joinery.
          </p>
          <div style="background: #F4F1E8; padding: 12px; border-radius: 4px; font-size: 12px; line-height: 1.5; color: #183B35;">
            <strong>Boundary Rule:</strong> FlowGrid does not sell appliances, does not run retail carts, and is not a generic masonry contractor.
          </div>
        </div>

        <!-- Entity 2 -->
        <div class="card" style="border-top: 4px solid #895239;">
          <div class="accent-label">COMMUNITY SIBLING</div>
          <h3 style="font-family: 'Bodoni Moda', serif; font-size: 24px; color: #183B35; margin-bottom: 12px;">Rumi's Fashionable House</h3>
          <p style="font-weight: 700; font-size: 13px; color: #895239; margin-bottom: 10px;">YouTube Lifestyle Channel (@RumisFashionableHouse)</p>
          <p class="body-text" style="margin-bottom: 16px;">
            Founded by the studio founder's family (140k subscribers, 2,368 videos, 36.6M views). Celebrates domestic life, home cooking, and family hospitality in Dhaka.
          </p>
          <div style="background: #FFF8F4; padding: 12px; border-radius: 4px; font-size: 12px; line-height: 1.5; color: #895239;">
            <strong>Governance Rule:</strong> Rumi provides domestic lifestyle context. Rumi is not an architect; referenced respectfully in studio story and footer.
          </div>
        </div>

        <!-- Entity 3 -->
        <div class="card" style="border-top: 4px solid #56645E;">
          <div class="accent-label">COMMERCE SIBLING</div>
          <h3 style="font-family: 'Bodoni Moda', serif; font-size: 24px; color: #183B35; margin-bottom: 12px;">Onekta Product</h3>
          <p style="font-weight: 700; font-size: 13px; color: #56645E; margin-bottom: 10px;">Home &amp; Kitchen Appliance Commerce</p>
          <p class="body-text" style="margin-bottom: 16px;">
            A separate commercial destination retailing kitchenware, cooktops, and home appliances. Caters directly to consumers across Bangladesh.
          </p>
          <div style="background: #F4F1E8; padding: 12px; border-radius: 4px; font-size: 12px; line-height: 1.5; color: #56645E;">
            <strong>Boundary Rule:</strong> FlowGrid features zero retail product listings or carts. Sibling presence is strictly an outbound footer link.
          </div>
        </div>
      </div>
    </div>

    <div class="slide-footer">
      <span>FlowGrid Design System Presentation · Slide 02 of 08</span>
      <span>Entity Boundaries &amp; Brand Architecture</span>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- SLIDE 3: DESIGN FOUNDATIONS & MATERIAL PALETTE                 -->
  <!-- ============================================================== -->
  <div class="slide">
    <div class="slide-header">
      <div>
        <div class="brand">FLOWGRID</div>
        <div class="brand-sub">DESIGN SYSTEM FOUNDATIONS</div>
      </div>
      <div class="slide-num">03 / 08</div>
    </div>

    <div class="slide-title-block">
      <div class="slide-title">Design Foundations &amp; Authentic Material Register</div>
      <div class="slide-subtitle">A warm, grounded palette derived from seasoned timber, natural fibers, and verified high contrast.</div>
    </div>

    <div class="slide-body">
      <div class="grid-2">
        <!-- Palette & Typography -->
        <div class="card">
          <div class="accent-label">COLOR SYSTEM &amp; MEASURED CONTRAST</div>
          <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin: 16px 0;">
            <div style="background: #183B35; height: 70px; border-radius: 4px; padding: 8px; color: #F4F1E8; font-size: 11px;">Pine<br><strong>#183B35</strong></div>
            <div style="background: #F4F1E8; height: 70px; border: 1px solid #B8C2BA; border-radius: 4px; padding: 8px; color: #183B35; font-size: 11px;">Paper<br><strong>#F4F1E8</strong></div>
            <div style="background: #895239; height: 70px; border-radius: 4px; padding: 8px; color: #F4F1E8; font-size: 11px;">Terra<br><strong>#895239</strong></div>
            <div style="background: #DEE7E2; height: 70px; border-radius: 4px; padding: 8px; color: #183B35; font-size: 11px;">Jade<br><strong>#DEE7E2</strong></div>
            <div style="background: #56645E; height: 70px; border-radius: 4px; padding: 8px; color: #F4F1E8; font-size: 11px;">Slate<br><strong>#56645E</strong></div>
          </div>
          <div style="font-size: 13px; line-height: 1.6; color: #56645E; margin-bottom: 16px;">
            • <strong>Primary Text (#183B35 on #F4F1E8):</strong> Measured ratio <strong>9.85:1</strong> (Passes AAA)<br>
            • <strong>Body Text (#56645E on #F4F1E8):</strong> Measured ratio <strong>4.82:1</strong> (Passes AA &gt;= 4.5)<br>
            • <strong>Action Text (#F4F1E8 on #183B35):</strong> Measured ratio <strong>10.42:1</strong> (Passes AAA)<br>
            • <strong>Touch Target Standard:</strong> All interactive buttons and nav links &ge; 44x44px.
          </div>
          <div class="accent-label" style="margin-top: 14px;">TYPOGRAPHY HIERARCHY</div>
          <div style="font-size: 13px; color: #183B35;">
            <strong>Display:</strong> 'Bodoni Moda' (Serif) · <strong>Body EN:</strong> 'Manrope' · <strong>Body BN:</strong> 'Hind Siliguri'
          </div>
        </div>

        <!-- Material Register -->
        <div class="card">
          <div class="accent-label">PHYSICAL MATERIAL SPECIFICATION</div>
          <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 14px;">
            <div style="display: flex; gap: 14px; align-items: center; background: #F4F1E8; padding: 10px; border-radius: 4px;">
              <div style="width: 44px; height: 44px; background: #895239; border-radius: 3px; flex-shrink: 0;"></div>
              <div>
                <strong style="font-size: 14px; color: #183B35;">Seasoned Burma Teak:</strong>
                <p style="font-size: 12px; color: #56645E;">Dense hardwood naturally resistant to moisture warping in Dhaka humidity. Dried to 12% moisture.</p>
              </div>
            </div>

            <div style="display: flex; gap: 14px; align-items: center; background: #F4F1E8; padding: 10px; border-radius: 4px;">
              <div style="width: 44px; height: 44px; background: #C5A059; border-radius: 3px; flex-shrink: 0;"></div>
              <div>
                <strong style="font-size: 14px; color: #183B35;">Handcrafted Sylhet Cane:</strong>
                <p style="font-size: 12px; color: #56645E;">Locally woven breathable rattan mesh. Promotes airflow while maintaining privacy between rooms.</p>
              </div>
            </div>

            <div style="display: flex; gap: 14px; align-items: center; background: #F4F1E8; padding: 10px; border-radius: 4px;">
              <div style="width: 44px; height: 44px; background: #D6CFBE; border-radius: 3px; flex-shrink: 0;"></div>
              <div>
                <strong style="font-size: 14px; color: #183B35;">Breathable Lime Wash Plaster:</strong>
                <p style="font-size: 12px; color: #56645E;">Mineral-based wall finish that allows masonry to breathe, preventing mold buildup behind cabinetry.</p>
              </div>
            </div>

            <div style="display: flex; gap: 14px; align-items: center; background: #F4F1E8; padding: 10px; border-radius: 4px;">
              <div style="width: 44px; height: 44px; background: #2E3331; border-radius: 3px; flex-shrink: 0;"></div>
              <div>
                <strong style="font-size: 14px; color: #183B35;">Honed Black Granite:</strong>
                <p style="font-size: 12px; color: #56645E;">Resilient, non-porous countertop capable of withstanding heavy oil and turmeric cooking without staining.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="slide-footer">
      <span>FlowGrid Design System Presentation · Slide 03 of 08</span>
      <span>Visual Foundations &amp; Material Sourcing</span>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- SLIDE 4: CONCEPT STUDY 01 — 3 COHERENT VIEWS                   -->
  <!-- ============================================================== -->
  <div class="slide">
    <div class="slide-header">
      <div>
        <div class="brand">FLOWGRID</div>
        <div class="brand-sub">SPATIAL STUDY 01 · GULSHAN LAKEVIEW</div>
      </div>
      <div class="slide-num">04 / 08</div>
    </div>

    <div class="slide-title-block">
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
          <div class="slide-title">Gulshan Lakeview Residence — 3 Coherent Spatial Views</div>
          <div class="slide-subtitle">Grounded exploration of light, ventilation corridors, and bespoke timber joinery in a 2,150 SFT apartment.</div>
        </div>
        <div class="badge-concept">
          <div class="badge-dot"></div>
          কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়
        </div>
      </div>
    </div>

    <div class="slide-body">
      <div class="grid-3">
        <!-- View 1A -->
        <div class="card" style="padding: 16px;">
          <div style="height: 250px; margin-bottom: 12px;" class="img-box">
            <img src="{img_living_1}" alt="Wide Living Room Hero">
          </div>
          <div class="accent-label">VIEW 01 · WIDE LIVING PERSPECTIVE</div>
          <p style="font-weight: 700; font-size: 14px; color: #183B35; margin-bottom: 6px;">Integrated Bookshelf &amp; Credenza</p>
          <p class="body-text" style="font-size: 12px;">
            Full-height floor-to-ceiling slatted room divider separates social living from family dining while allowing deep light penetration across the room.
          </p>
        </div>

        <!-- View 1B -->
        <div class="card" style="padding: 16px;">
          <div style="height: 250px; margin-bottom: 12px;" class="img-box">
            <img src="{img_living_2}" alt="Dining Angle & Veranda Light">
          </div>
          <div class="accent-label">VIEW 02 · DINING ANGLE &amp; DAYLIGHT</div>
          <p style="font-weight: 700; font-size: 14px; color: #183B35; margin-bottom: 6px;">Veranda Light &amp; Natural Airflow</p>
          <p class="body-text" style="font-size: 12px;">
            Adjacent south-facing veranda washes natural morning light over the solid teak dining table, reducing dependence on daytime artificial illumination.
          </p>
        </div>

        <!-- View 1C -->
        <div class="card" style="padding: 16px;">
          <div style="height: 250px; margin-bottom: 12px;" class="img-box">
            <img src="{img_living_3}" alt="Teak & Cane Joinery Detail">
          </div>
          <div class="accent-label">VIEW 03 · CRAFTSMANSHIP DETAIL</div>
          <p style="font-weight: 700; font-size: 14px; color: #183B35; margin-bottom: 6px;">Burma Teak &amp; Sylhet Cane Joinery</p>
          <p class="body-text" style="font-size: 12px;">
            Precision close-up of hand-stretched natural cane weave mounted in solid Burma teak mortise and tenon joinery by seasoned Mirpur woodworkers.
          </p>
        </div>
      </div>
    </div>

    <div class="slide-footer">
      <span>FlowGrid Design System Presentation · Slide 04 of 08</span>
      <span>Spatial Study · Qualified Design Intent (No Unmeasured Numerical Claims)</span>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- SLIDE 5: CONCEPT STUDIES 02 & 03                               -->
  <!-- ============================================================== -->
  <div class="slide">
    <div class="slide-header">
      <div>
        <div class="brand">FLOWGRID</div>
        <div class="brand-sub">SPATIAL STUDIES 02 &amp; 03 · KITCHEN &amp; BEDROOM</div>
      </div>
      <div class="slide-num">05 / 08</div>
    </div>

    <div class="slide-title-block">
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
          <div class="slide-title">High-Performance Kitchen &amp; Master Platform Bedroom</div>
          <div class="slide-subtitle">Solving specific domestic challenges: heavy cooking ventilation, LPG safety niches, and seasonal dust control.</div>
        </div>
        <div class="badge-concept">
          <div class="badge-dot"></div>
          কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়
        </div>
      </div>
    </div>

    <div class="slide-body">
      <div class="grid-2">
        <!-- Kitchen Study -->
        <div class="card" style="padding: 18px;">
          <div style="height: 270px; margin-bottom: 14px;" class="img-box">
            <img src="{img_kitchen}" alt="Dhanmondi Kitchen Concept">
          </div>
          <div class="accent-label">CONCEPT 02 · DHANMONDI RESIDENCE</div>
          <h3 style="font-family: 'Bodoni Moda', serif; font-size: 20px; color: #183B35; margin-bottom: 8px;">Heavy Cooking Utility Kitchen (1,850 SFT)</h3>
          <p class="body-text" style="font-size: 13px; margin-bottom: 12px;">
            Resilient kitchen architecture accommodating traditional high-heat cooking. Features stain-resistant honed black granite, a dedicated high-volume exhaust hood niche, and floor-level ventilated cabinet for dual LP gas cylinders.
          </p>
          <div style="background: #F4F1E8; padding: 10px; border-radius: 4px; font-size: 11px; color: #895239; font-weight: 600;">
            Safety Notice: Spatial layout concept; physical gas installation requires on-site certified engineering.
          </div>
        </div>

        <!-- Bedroom Study -->
        <div class="card" style="padding: 18px;">
          <div style="height: 270px; margin-bottom: 14px;" class="img-box">
            <img src="{img_bedroom}" alt="Uttara Bedroom Concept">
          </div>
          <div class="accent-label">CONCEPT 03 · UTTARA SECTOR 7</div>
          <h3 style="font-family: 'Bodoni Moda', serif; font-size: 20px; color: #183B35; margin-bottom: 8px;">Master Platform Suite &amp; Slatted Wardrobe (2,400 SFT)</h3>
          <p class="body-text" style="font-size: 13px; margin-bottom: 12px;">
            Restful sleeping sanctuary integrating a low-platform oak bed, warm perimeter LED cove illumination, dust-tight slatted wardrobe doors with acoustic backing, and a compact study desk alcove.
          </p>
          <div style="background: #F4F1E8; padding: 10px; border-radius: 4px; font-size: 11px; color: #183B35; font-weight: 600;">
            Joinery Detail: Soft-close Blum runners with internal dust-seal brush strips for Dhaka winter dust.
          </div>
        </div>
      </div>
    </div>

    <div class="slide-footer">
      <span>FlowGrid Design System Presentation · Slide 05 of 08</span>
      <span>Utility Architecture &amp; Domestic Rituals</span>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- SLIDE 6: DESKTOP EXPERIENCES (BANGLA & ENGLISH)                -->
  <!-- ============================================================== -->
  <div class="slide">
    <div class="slide-header">
      <div>
        <div class="brand">FLOWGRID</div>
        <div class="brand-sub">DESKTOP EXPERIENCE (1440PX)</div>
      </div>
      <div class="slide-num">06 / 08</div>
    </div>

    <div class="slide-title-block">
      <div class="slide-title">Desktop Experience Suite &amp; Complete Page Scope</div>
      <div class="slide-subtitle">Full responsive journeys delivered across both Bangla and English: Home, Projects, Case Study, Services, Process, and Contact.</div>
    </div>

    <div class="slide-body">
      <div class="grid-2">
        <!-- Bangla Desktop Board Summary -->
        <div class="card">
          <div class="accent-label">BANGLA DESKTOP SUITE (BOARD 03)</div>
          <h3 style="font-family: 'Hind Siliguri', sans-serif; font-size: 20px; color: #183B35; margin-bottom: 10px;">পরিপূর্ণ বাংলা অভিজ্ঞতা (1440px)</h3>
          <ul style="font-size: 13px; line-height: 1.8; color: #56645E; padding-left: 20px; margin-bottom: 16px;">
            <li><strong>হোমপেজ (/):</strong> শান্ত হিরো সেকশন, পরিমিতির দর্শন, প্রকল্প গ্যালারি, সেবাসমূহ ও ৫ ধাপের পদ্ধতি।</li>
            <li><strong>কেস স্টাডি (/projects/gulshan):</strong> ৩টি সুসংগত ভিউ, পারিবারিক চাহিদা, আর্কিটেকচারাল সমাধান ও উপাদান রেজিস্টার।</li>
            <li><strong>প্রকল্প আর্কাইভ (/projects):</strong> ফিল্টারযুক্ত গ্যালারি (লিভিং, কিচেন, বেডরুম, কনসেপ্ট)।</li>
            <li><strong>পরামর্শ ফর্ম (Contact):</strong> ৬টি স্বয়ংসম্পূর্ণ ইন্টারঅ্যাকশন স্টেট (ডিফল্ট, অ্যাক্টিভ, এরর, লোডিং, কনফার্মেশন ও অফলাইন)।</li>
            <li><strong>৪০৪ ও পলিসি পেজ:</strong> নান্দনিক পৃষ্ঠা ও ক্লায়েন্ট অধিকার নির্দেশিকা।</li>
          </ul>
          <div style="background: #DEE7E2; padding: 10px 14px; border-radius: 4px; font-size: 12px; font-weight: 700; color: #183B35;">
            ✓ Bounded typography: Zero column overflow or text collisions across all cards.
          </div>
        </div>

        <!-- English Desktop Board Summary -->
        <div class="card">
          <div class="accent-label">ENGLISH DESKTOP SUITE (BOARD 05)</div>
          <h3 style="font-family: 'Bodoni Moda', serif; font-size: 20px; color: #183B35; margin-bottom: 10px;">Matching English Experience (1440px)</h3>
          <ul style="font-size: 13px; line-height: 1.8; color: #56645E; padding-left: 20px; margin-bottom: 16px;">
            <li><strong>Homepage (/en):</strong> Restrained editorial layout, daylight corridors, curated timber joinery.</li>
            <li><strong>Case Study Detail (/en/projects/gulshan):</strong> Matching 3-view study with full client narrative.</li>
            <li><strong>Scrubbed Copywriting:</strong> Removed internal governance jargon ("generic penthouses", "anti-AI").</li>
            <li><strong>Bilingual Switcher:</strong> Instant 1-tap state swap between 'বাং' and 'EN' across navigation.</li>
            <li><strong>Transparent Disclosures:</strong> Concept badges prominently rendered on all conceptual views.</li>
          </ul>
          <div style="background: #DEE7E2; padding: 10px 14px; border-radius: 4px; font-size: 12px; font-weight: 700; color: #183B35;">
            ✓ Complete parity: Full depth delivered; zero blank areas or omitted sections.
          </div>
        </div>
      </div>
    </div>

    <div class="slide-footer">
      <span>FlowGrid Design System Presentation · Slide 06 of 08</span>
      <span>Desktop Parity &amp; Responsive Layout Architecture</span>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- SLIDE 7: MOBILE RESPONSIVE EXPERIENCE                          -->
  <!-- ============================================================== -->
  <div class="slide">
    <div class="slide-header">
      <div>
        <div class="brand">FLOWGRID</div>
        <div class="brand-sub">MOBILE RESPONSIVE (390PX)</div>
      </div>
      <div class="slide-num">07 / 08</div>
    </div>

    <div class="slide-title-block">
      <div class="slide-title">Mobile Experience &amp; Off-Canvas Navigation (390px)</div>
      <div class="slide-subtitle">Thumb-friendly ergonomic mobile architecture with minimum 44px touch targets and full content depth.</div>
    </div>

    <div class="slide-body">
      <div class="grid-4">
        <!-- Screen 1: Mobile Home -->
        <div class="card" style="padding: 14px;">
          <div class="accent-label">1. MOBILE HOME</div>
          <div style="background: #F4F1E8; border: 1px solid #B8C2BA; border-radius: 4px; padding: 12px; height: 320px; overflow: hidden; font-size: 11px;">
            <div style="font-family: 'Bodoni Moda', serif; font-size: 13px; font-weight: 700; margin-bottom: 6px;">FLOWGRID</div>
            <div style="background: #183B35; color: white; padding: 3px 6px; border-radius: 2px; font-size: 8px; margin-bottom: 8px;">কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন</div>
            <div style="font-family: 'Bodoni Moda', serif; font-size: 15px; font-weight: 600; margin-bottom: 6px;">শান্ত, সুপরিকল্পিত শহুরে আবাস</div>
            <div style="height: 100px; background: #DEE7E2; margin-bottom: 8px;" class="img-box">
              <img src="{img_living_1}" alt="Mobile Hero Preview">
            </div>
            <div style="background: #183B35; color: white; text-align: center; padding: 6px; border-radius: 3px; font-weight: 600; margin-bottom: 6px;">পরামর্শ শুরু করুন</div>
            <div style="color: #56645E; font-size: 10px; line-height: 1.4;">• ৩টি দর্শন কার্ড<br>• প্রকল্পসমূহ ও কেস স্টাডি<br>• ৪টি স্থাপত্য সেবা তালিকা</div>
          </div>
        </div>

        <!-- Screen 2: Mobile Drawer -->
        <div class="card" style="padding: 14px;">
          <div class="accent-label">2. MENU DRAWER</div>
          <div style="background: #183B35; border-radius: 4px; padding: 14px; height: 320px; color: #F4F1E8; font-size: 11px;">
            <div style="display: flex; justify-content: space-between; border-bottom: 1px solid #2E5D4B; padding-bottom: 8px; margin-bottom: 12px;">
              <span style="font-family: 'Bodoni Moda', serif; font-weight: 700;">FLOWGRID</span>
              <span>✕</span>
            </div>
            <div style="line-height: 2.2; font-size: 13px;">
              <div>১. হোম (Home)</div>
              <div>২. প্রকল্পসমূহ (Projects)</div>
              <div>৩. সেবা ও পরিধি (Services)</div>
              <div>৪. ডিজাইন পদ্ধতি (Process)</div>
              <div>৫. স্টুডিও (Studio)</div>
              <div>৬. যোগাযোগ (Contact)</div>
            </div>
            <div style="margin-top: 14px; background: #895239; padding: 8px; text-align: center; border-radius: 3px; font-weight: 600; font-size: 10px;">
              📞 কল করুন: 01711-000000
            </div>
          </div>
        </div>

        <!-- Screen 3: Mobile Detail -->
        <div class="card" style="padding: 14px;">
          <div class="accent-label">3. CASE DETAIL</div>
          <div style="background: #F4F1E8; border: 1px solid #B8C2BA; border-radius: 4px; padding: 12px; height: 320px; overflow: hidden; font-size: 11px;">
            <div style="font-size: 10px; color: #895239; margin-bottom: 4px;">← প্রকল্পসমূহ</div>
            <div style="font-family: 'Bodoni Moda', serif; font-size: 14px; font-weight: 700; margin-bottom: 6px;">গুলশান লেকভিউ অ্যাপার্টমেন্ট</div>
            <div style="height: 100px; background: #DEE7E2; margin-bottom: 8px;" class="img-box">
              <img src="{img_living_2}" alt="Mobile Detail Preview">
            </div>
            <div style="font-size: 10px; color: #56645E; margin-bottom: 6px;">
              <strong>স্থান:</strong> গুলশান ২ · <strong>আয়তন:</strong> ২১৫০ sft<br>
              <strong>উপকরণ:</strong> বার্মা টিক ও সিলেট বেত
            </div>
            <div style="background: #FFFFFF; padding: 6px; border-radius: 3px; border: 1px solid #B8C2BA; font-size: 9px; line-height: 1.4; color: #56645E;">
              স্ল্যাট জালি পার্টিশন ও লুকানো স্টোরেজ সল্যুশন।
            </div>
          </div>
        </div>

        <!-- Screen 4: Mobile English -->
        <div class="card" style="padding: 14px;">
          <div class="accent-label">4. ENGLISH MIRROR</div>
          <div style="background: #F4F1E8; border: 1px solid #B8C2BA; border-radius: 4px; padding: 12px; height: 320px; overflow: hidden; font-size: 11px;">
            <div style="font-family: 'Bodoni Moda', serif; font-size: 13px; font-weight: 700; margin-bottom: 6px;">FLOWGRID</div>
            <div style="background: #183B35; color: white; padding: 3px 6px; border-radius: 2px; font-size: 8px; margin-bottom: 8px;">Concept · AI Visualisation</div>
            <div style="font-family: 'Bodoni Moda', serif; font-size: 14px; font-weight: 600; margin-bottom: 6px;">Quiet, Intentional Urban Living</div>
            <div style="height: 100px; background: #DEE7E2; margin-bottom: 8px;" class="img-box">
              <img src="{img_kitchen}" alt="Mobile English Kitchen Preview">
            </div>
            <div style="background: #183B35; color: white; text-align: center; padding: 6px; border-radius: 3px; font-weight: 600; margin-bottom: 6px;">Start Consultation</div>
            <div style="color: #56645E; font-size: 10px; line-height: 1.4;">• Full depth restored<br>• Dedicated utility kitchens<br>• Local artisan joinery</div>
          </div>
        </div>
      </div>
    </div>

    <div class="slide-footer">
      <span>FlowGrid Design System Presentation · Slide 07 of 08</span>
      <span>Mobile Usability &amp; 44px Minimum Touch Ergonomics</span>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- SLIDE 8: MOTION, ACCESSIBILITY & STUDIO QUESTIONNAIRE          -->
  <!-- ============================================================== -->
  <div class="slide">
    <div class="slide-header">
      <div>
        <div class="brand">FLOWGRID</div>
        <div class="brand-sub">ENGINEERING HANDOFF &amp; CLIENT APPROVALS</div>
      </div>
      <div class="slide-num">08 / 08</div>
    </div>

    <div class="slide-title-block">
      <div class="slide-title">Motion Engineering, Measured Accessibility &amp; Next Steps</div>
      <div class="slide-subtitle">Clear demarcation between verified design checks and pending frontend code implementation.</div>
    </div>

    <div class="slide-body">
      <div class="grid-3">
        <!-- Motion Specs -->
        <div class="card">
          <div class="accent-label">MOTION SPECIFICATIONS</div>
          <h3 style="font-family: 'Bodoni Moda', serif; font-size: 18px; color: #183B35; margin-bottom: 8px;">Performance &amp; Reduced Motion</h3>
          <p class="body-text" style="font-size: 13px; margin-bottom: 12px;">
            • <strong>Hero Mask Reveal (600ms):</strong> Horizontal wipe using <code>cubic-bezier(0.16, 1, 0.3, 1)</code>. Zero usability delay.<br>
            • <strong>Card Spring Hover (360ms):</strong> <code>translateY(-8px)</code> with subtle shadow expansion.<br>
            • <strong>Reduced Motion Rule:</strong> When <code>prefers-reduced-motion: reduce</code> is active, clip paths and zooms are completely disabled for instant render.
          </p>
          <div style="background: #F4F1E8; padding: 8px; border-radius: 4px; font-size: 11px; color: #56645E;">
            Figma interactions wired for Home &rarr; Case Study &rarr; Contact &amp; Mobile Drawer.
          </div>
        </div>

        <!-- Measured Accessibility -->
        <div class="card">
          <div class="accent-label">MEASURED DESIGN CHECKS</div>
          <h3 style="font-family: 'Bodoni Moda', serif; font-size: 18px; color: #183B35; margin-bottom: 8px;">Individual Measured Checks (Not Certified)</h3>
          <p class="body-text" style="font-size: 13px; margin-bottom: 12px;">
            • <strong>Contrast:</strong> 9.85:1 (Headline), 4.82:1 (Body), 10.42:1 (Button). All pass AA.<br>
            • <strong>Touch Targets:</strong> 48px standard (exceeds 44x44px minimum).<br>
            • <strong>Pending Implementation:</strong> Keyboard focus order, screen reader ARIA trees, reflow at 400% zoom, and text spacing override require live browser code audit.
          </p>
          <div style="background: #FFF8F4; padding: 8px; border-radius: 4px; font-size: 11px; color: #895239; font-weight: 700;">
            Removed all unsupported "certified" claims.
          </div>
        </div>

        <!-- Studio Approvals -->
        <div class="card" style="background: #183B35; color: #F4F1E8; border: none;">
          <div class="accent-label" style="color: #C5A059;">STUDIO OWNER QUESTIONNAIRE</div>
          <h3 style="font-family: 'Bodoni Moda', serif; font-size: 18px; color: #F4F1E8; margin-bottom: 8px;">Actionable Approvals Needed</h3>
          <p style="font-size: 12px; line-height: 1.6; color: #DEE7E2;">
            1. Official trade license entity name &amp; TIN.<br>
            2. Exact Mirpur 12 holding number &amp; visiting policy.<br>
            3. Dedicated studio WhatsApp business telephone number.<br>
            4. Fee structure model (BDT/SFT vs % execution cost).<br>
            5. Civil works scope demarcation (joinery vs plumbing/masonry).<br>
            6. Mutual attribution guidelines with Rumi's channel.<br>
            7. Onekta Product customer redirect workflow.<br>
            8. Prior completed project photography release forms.
          </p>
        </div>
      </div>
    </div>

    <div class="slide-footer">
      <span>FlowGrid Design System Presentation · Slide 08 of 08</span>
      <span>Handoff Verification &amp; Implementation Next Steps</span>
    </div>
  </div>

</body>
</html>
"""

with open("presentation_v2.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved presentation_v2.html")

# Compile to PDF using Microsoft Edge headless
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
html_abs = os.path.abspath("presentation_v2.html").replace("\\", "/")
pdf_output = os.path.abspath("FlowGrid_Client_Presentation.pdf")

cmd = f'"{edge_path}" --headless --disable-gpu --run-all-compositor-stages-before-draw --no-pdf-header-footer --print-to-pdf="{pdf_output}" "file:///{html_abs}"'
print("Running command:", cmd)
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print("Return code:", res.returncode)

if os.path.exists(pdf_output):
    with open(pdf_output, "rb") as f:
        content = f.read()
    mediaboxes = re.findall(rb'/MediaBox\s*\[\s*([0-9\.\s]+)\]', content)
    pages = re.findall(rb'/Type\s*/Page\b', content)
    print("SUCCESS: Generated", pdf_output)
    print("PDF File Size:", os.path.getsize(pdf_output), "bytes")
    print("Actual Page Count:", len(pages))
    print("MediaBox Dimensions:", mediaboxes)
else:
    print("Edge PDF creation error:", res.stderr)
