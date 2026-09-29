# FlowGrid — Comprehensive Implementation & Handoff Guide for Claude Code

**Date:** 29 September 2026  
**Project:** FlowGrid — Architectural Interior Design Studio Website  
**Figma File:** [`eMRunQ80brYYvuTWkufV2o`](https://www.figma.com/design/eMRunQ80brYYvuTWkufV2o/FlowGrid-%E2%80%94-Design-System---Responsive-Experience)  
**Deliverable Status:** Stage 1 Figma Website Design & Assets Complete (Website-First Order)  
**Target Implementer:** Claude Code (Autonomous Full-Stack Builder)

---

## 1. Executive Summary & Delivery Order

### The Core Direction: Website First
As mandated by the owner's revised delivery order (superseding earlier video-first requirements):
1. **Antigravity has finished the website's Figma design, responsive layouts, brand identity, and still-image assets.** All visual interface bugs (blank CTAs, clipped 404 recovery buttons, partial-width headers, contact footer overlaps, and unclipped 16:9 detail hero images) have been resolved directly on the live Figma canvas and re-exported.
2. **Claude Code now builds the complete responsive website.** Deliver an interactive, fast, and accessible bilingual experience (Bengali & English) using the verified stills, clean CSV copy strings, and route map.
3. **The full apartment walkthrough, Google Flow video, and scroll-scrubbing playback are deferred.** Claude Code should prepare a designated hero / concept media container with a solid still fallback (`FG-APT-01_V04_living.jpg`), ensuring the website is completely functional and launch-ready without waiting for future video renders.

---

## 2. Brand Identity & Reconstructed Assets

All official brand assets have been reconstructed from official studio sources (`FlowGridBD`) and reside in `brand/`:

| Asset File | Format / Spec | Usage |
|---|---|---|
| `brand/flowgrid_logo_full_transparent.png` | 32-bit Transparent PNG | Primary header & footer logo across all desktop layouts (140 × 32 px). |
| `brand/flowgrid_logo_full.svg` | Scalable Vector Graphic | Resolution-independent desktop header wordmark & mark. |
| `brand/flowgrid_logo_compact_transparent.png` | 32-bit Transparent PNG | Mobile header monogram & compact wordmark (112 × 26 px). |
| `brand/flowgrid_logo_compact.svg` | Scalable Vector Graphic | Resolution-independent mobile header mark. |
| `brand/favicon.png` & `brand/favicon_32.png` | PNG Favicon Icons | Browser tab icon (16×16, 32×32, 192×192). |

---

## 3. Design Tokens & Styling Specifications

### A. Color Palette
```css
:root {
  /* Surfaces */
  --surface-page: #F4F1E8;         /* Warm Sand Page Background */
  --surface-clean: #FFFFFF;        /* Pure White Cards / Panels */
  --surface-mist: #DEE7E2;         /* Pale Mist Accent / Table Row */

  /* Text & Accents */
  --text-primary: #183B35;         /* Deep Forest Pine (High Contrast) */
  --text-secondary: #56645E;       /* Muted Charcoal Green */
  --accent-clay: #895239;          /* Rich Terracotta / Wood Accent */

  /* Interactive Actions */
  --action-primary: #183B35;       /* Primary CTA Background */
  --action-primary-hover: #102B26; /* Primary CTA Hover */
  --action-text: #FFFFFF;          /* Pure White on Dark Green */

  /* Borders & Focus */
  --border-subtle: #DEE7E2;        /* Card & Divider Border */
  --border-control: #B8C2BA;       /* Form Field Border */
  --focus-ring: #895239;           /* Accessible 2px Focus Outline */

  /* Status */
  --status-error: #9B302B;
  --status-error-bg: #FDF2F2;
  --status-success: #245C43;
  --status-success-bg: #EBF5F0;
}
```

### B. Typography
- **English Font:** `Inter`, sans-serif (Weights: 400 Regular, 500 Medium, 600 Semi-Bold, 700 Bold).
- **Bengali Font:** `Noto Sans Bengali`, sans-serif (Weights: 400 Regular, 500 Medium, 700 Bold).
- **Scale:**
  - Display / H1: 44px / 52px line-height (Desktop), 28px / 36px (Mobile).
  - H2: 32px / 40px (Desktop), 24px / 32px (Mobile).
  - H3: 20px / 28px (Desktop), 18px / 24px (Mobile).
  - Body: 16px / 26px (Desktop), 15px / 24px (Mobile).
  - Small / Badge / Metadata: 12px – 13px (All).

### C. Controls & Button Heights
- **Desktop Controls:** Height 52px, horizontal padding 24px, border-radius 2px (subtle architectural radius).
- **Mobile Controls:** Height 48px minimum touch target, full-width or minimum 160px.
- **Contrast Check:** All primary green buttons MUST feature crisp white text (`#FFFFFF` on `#183B35`, contrast ratio 8.2:1 — exceeds WCAG AAA).

---

## 4. Curated Concept Still Image Set

The audit identified spatial and continuity defects in the raw generated views. Claude Code must adhere to this curated set:

### Approved Launch Stills (Deploy in Website):
1. **`images/masters/FG-APT-01_V04_living.jpg`** (1376 × 768) — Primary Hero image on Desktop & Mobile Homepage and Concept Detail Hero.
2. **`images/masters/FG-APT-01_V08_kitchen.jpg`** (1376 × 768) — Secondary Angle on Homepage, Joinery Image Showcase, and Concept Study 02.
3. **`images/masters/FG-APT-01_V10_master_bed.jpg`** (1376 × 768) — Tertiary Angle on Homepage and Concept Study 03.
4. **`images/masters/FG-APT-01_V03_foyer.jpg`** (1376 × 768) — Handcrafted Burma Teak slatted partition screen and foyer millwork.
5. **`images/masters/FG-APT-01_V02_approach.jpg`** (1376 × 768) — Entrance doorway with Unit 4B plaque.
6. **`images/masters/FG-APT-01_V11_master_balcony.jpg`** (1376 × 768) — Master balcony sit-out paired with V10.
7. **`images/masters/FG-APT-01_V12_master_bath.jpg`** (1376 × 768) — Contemporary en-suite master bathroom.

### Excluded / Retired Views (DO NOT Display on Public Pages):
- **`V06` and `V07`:** Contain a duplicated handwash basin artifact (foreground basin + background duplicate). Excluded from launch.
- **`V01`:** Bird's-eye cutaway conflicts with plan geometry. Internal reference only.
- **`V05` & `V09`:** Door swing and corridor mismatches. Deferred to post-website 3D scene modeling.

---

## 5. Public Content & Truthfulness Guidelines

1. **Portfolio Framing:** Frame all work as **Concept Design / কনসেপ্ট ডিজাইন** for `FG-APT-01 (Dhaka Family Apartment)`. Do not claim completed client commissions or invent client testimonials.
2. **Apartment Target Area:** Represent strictly as **"approximately 1,500 sq ft" / "১,৫০০ বর্গফুট"** (do not publish the unverified 1,515 sq ft figure).
3. **Studio Location:** **Mirpur, Dhaka 1216, Bangladesh** (do not use placeholder Dhanmondi or Banani addresses).
4. **Zero AI Meta-Disclosures:** Remove all superseded labels ("AI Visualization", "Not a Built Project") and production commentary ("Authenticity & Credentials Policy"). Use natural architectural studio terminology.
5. **Primary Enquiry CTA:**
   - Bengali: `"আপনার পরিকল্পনা নিয়ে কথা বলুন"`
   - English: `"Discuss your space"`

---

## 6. Page Templates & Responsive Routing Matrix (44 Layouts)

Refer to `handoff/layout_register.csv` for the 1:1 mapping between Figma nodes and export PNGs:

### A. Desktop (1440px Viewport — 22 Templates)
- **Bengali (11 Screens):**
  - Homepage: `/bn/` (`figma_exports/phase3_desktop_home_bn.png`)
  - Concept Detail: `/bn/detail` (`figma_exports/phase3_desktop_detail_bn.png`)
  - Project Archive: `/bn/archive` (`figma_exports/phase3_desktop_archive_bn.png`)
  - Architectural Services: `/bn/services` (`figma_exports/phase3_desktop_services_bn.png`)
  - Custom Joinery: `/bn/joinery` (`figma_exports/phase3_desktop_joinery_bn.png`)
  - Process & Delivery: `/bn/process` (`figma_exports/phase3_desktop_process_bn.png`)
  - Studio Practice: `/bn/studio` (`figma_exports/phase3_desktop_studio_bn.png`)
  - Contact & Consultation: `/bn/contact` (`figma_exports/phase3_desktop_contact_bn.png`)
  - Privacy Policy: `/bn/privacy` (`figma_exports/phase3_desktop_privacy_bn.png`)
  - 404 Not Found: `/bn/404` (`figma_exports/phase3_desktop_404_bn.png`)
  - Built-Project Framework (Internal Reference): `/bn/framework` (`figma_exports/phase3_desktop_built_framework_bn.png`)
- **English (11 Screens):**
  - Corresponding English routes at `/en/`, `/en/detail`, `/en/archive`, etc.

### B. Mobile (390px Viewport — 22 Templates)
- Identical 11-template structure adapted for 390px screen width with 16px horizontal margins and full touch-target controls.

### C. Interactive Modals & Overlays (18 States)
- Consultation Request Modal (Full Name, Phone Number, Area, Scope, Notes)
- Submitting State (Spinner / Feedback)
- Success Confirmation Receipt
- Offline / Network Error Fallback
- Mobile Navigation Drawer

---

## 7. Delivery Files Checklist

All files are verified, formatted, and ready for immediate implementation:
- `brand/`: Official full & compact SVG and transparent PNG logos.
- `figma_exports/`: All 44 full-screen layout PNGs + 18 overlay state PNGs + verification contact sheets.
- `images/masters/`: High-resolution 1376 × 768 concept stills.
- `images/asset_manifest.csv`: 10-column properly quoted asset manifest with exact resolutions and status.
- `handoff/copy_bn_en.csv`: 5-column properly quoted bilingual copy strings.
- `handoff/layout_register.csv`: Complete layout registry mapping all 44 templates + overlays to file paths.
- `handoff/route_map.csv`: Prototype interaction map with verified destination nodes and URLs.
- `apartment/DEFERRED_DEFECTS_AND_NEXT_STEPS.md`: Architectural documentation for the future 3D tour.
