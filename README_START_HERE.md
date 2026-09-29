# FlowGrid — Stage 1 Deliverable & Handoff Package (Website-First Revision)

**Package Revision:** `FlowGrid_Stage1_Final_Deliverable` (Updated Post-Audit)  
**Date:** 29 September 2026  
**Status:** **WEBSITE FIGMA DESIGN & STILL-IMAGE HANDOFF COMPLETE — READY FOR CLAUDE CODE**  
**Role:** Antigravity Senior UI/UX Designer & Architectural Art Direction

---

## 1. Executive Direction: Website First

Per the owner's revised delivery order (`docs/FlowGrid_Stage1_Audit_and_Website_First_Corrections.md`):
1. **Website First:** All visual interface defects, brand integration gaps, copy meta-commentary, and malformed CSV data have been resolved directly on the live Figma canvas.
2. **Deferred Work:** The full apartment walkthrough, Google Flow video generation, scroll-scrubbing video animation, and 3D modeling are cleanly isolated in `apartment/DEFERRED_DEFECTS_AND_NEXT_STEPS.md` to be developed after the website is built.
3. **Claude Code Handoff:** Complete design system, 44 responsive layout exports (22 Desktop + 22 Mobile), 18 interactive overlays, verified brand assets, and clean CSVs are packaged and documented in `handoff/CLAUDE_CODE_HANDOFF.md`.

---

## 2. Primary Figma Access Links

- **Main Figma Design File:**  
  [FlowGrid — Design System & Responsive Experience](https://www.figma.com/design/eMRunQ80brYYvuTWkufV2o/FlowGrid-%E2%80%94-Design-System-%26-Responsive-Experience?node-id=0-1)  
  *File Key: `eMRunQ80brYYvuTWkufV2o`*

- **Interactive Prototype Start Links (Verified Native Journeys):**
  1. **[Bengali Desktop Experience (1440px)](https://www.figma.com/proto/eMRunQ80brYYvuTWkufV2o/FlowGrid-%E2%80%94-Design-System-%26-Responsive-Experience?node-id=24-8034&starting-point-node-id=24%3A8034)** — Flow Starting Point `24:8034`
  2. **[English Desktop Experience (1440px)](https://www.figma.com/proto/eMRunQ80brYYvuTWkufV2o/FlowGrid-%E2%80%94-Design-System-%26-Responsive-Experience?node-id=24-8456&starting-point-node-id=24%3A8456)** — Flow Starting Point `24:8456`
  3. **[Bengali Mobile Experience (390px)](https://www.figma.com/proto/eMRunQ80brYYvuTWkufV2o/FlowGrid-%E2%80%94-Design-System-%26-Responsive-Experience?node-id=24-8890&starting-point-node-id=24%3A8890)** — Flow Starting Point `24:8890`
  4. **[English Mobile Experience (390px)](https://www.figma.com/proto/eMRunQ80brYYvuTWkufV2o/FlowGrid-%E2%80%94-Design-System-%26-Responsive-Experience?node-id=24-9221&starting-point-node-id=24%3A9221)** — Flow Starting Point `24:9221`

---

## 3. Summary of Resolved Stage 1 Audit Items

| Audit Item | Issue Identified | Correction Implemented & Verified |
|---|---|---|
| **W1: Brand Logo on Customer Screens** | Previous exports retained plain serif text wordmark. | Official reconstructed FlowGrid logo (`brand/flowgrid_logo_full_transparent.png`) installed across all 44 desktop/mobile headers and footers with 1440px / 390px full-width alignment. |
| **W2: Blank Button Labels** | English Desktop & Mobile primary CTA buttons exported with blank labels. | Font override bug resolved by loading `Inter Medium` on Latin text nodes. Text `"Discuss your space"` now renders with full white glyphs (confirmed by pixel readback: 2,521 white px). |
| **W2: Mobile 404 Text Clipping** | Recovery buttons had 100px fixed width constraint, clipping recovery text. | Sized `Row / Recovery Buttons` to 358px full width; text centered with zero clipping for both EN (`"Return to Homepage →"`) and BN (`"মূল পাতায় ফিরে যান →"`). |
| **W2: Mobile Contact Clearance** | Submit button collided with footer edge. | Added 24px bottom padding on consultation card, expanded frame to 1140px, giving 24px+ clearance above footer. |
| **W2: Detail Hero Clipping** | English Concept Detail hero image was clipped to a 300px thin strip. | Removed 300px fixed height; expanded hero section to 880px, displaying full 1344 × 580 px 16:9 hero image (`V04`). |
| **W2: Joinery Empty Media Region** | Oversized blank media area preceded specification cards. | Filled `Photo / Joinery Macro Detail AST-03` with master image `V08` (Burma teak cabinetry and island) on both EN and BN joinery pages. |
| **W3: Public Copy & Policy Cleanup** | Mobile Studio contained internal "Authenticity & Credentials Policy" meta-commentary; dummy phone numbers in contact. | Replaced internal commentary with natural studio commitment copy; studio address set to **Mirpur, Dhaka 1216**; standardized enquiry CTA to `"আপনার পরিকল্পনা নিয়ে কথা বলুন"` / `"Discuss your space"`. |
| **W4: Layout Coverage** | Only 42 main layout exports provided (missing BN/EN mobile privacy). | All 44 main template layouts + 18 overlays exported fresh from Figma to `figma_exports/`. Verified 1:1 mapping in `handoff/layout_register.csv`. |
| **W4: Prototype Routing** | Archive Card 02 routed to internal built-project framework (`23:503` -> `18:1624` and `23:579` -> `18:1160`). | Updated all archive card study buttons to navigate directly to Concept Detail (`18:221` for BN, `18:1139` for EN). Updated URL language toggles with real `/en/...` and `/bn/...` routes. |
| **W5: CSV Formatting** | Unquoted commas split rows in `asset_manifest.csv` and `copy_bn_en.csv`; incorrect 1920x1080 dimensions. | Re-exported both CSVs with Python `csv.writer(quoting=csv.QUOTE_MINIMAL)`. Corrected master image dimensions to **1376 × 768** (~1.792 aspect ratio). All rows verified to have consistent column counts. |

---

## 4. Key Deliverable Directories

```
FlowGrid/
├── README_START_HERE.md                 # This executive summary
├── verification.md                      # Audit item verification details
├── brand/                               # Reconstructed official brand assets
│   ├── flowgrid_logo_full.svg           # Desktop vector SVG
│   ├── flowgrid_logo_compact.svg        # Mobile vector SVG
│   ├── flowgrid_logo_full_transparent.png # High-res transparent PNG
│   ├── flowgrid_logo_compact_transparent.png # Monogram transparent PNG
│   └── brand_guidelines.md              # Clear-space, sizing, and color standards
├── figma_exports/                       # 44 verified full-screen layout PNGs + 18 overlay PNGs
│   ├── phase3_desktop_home_en.png       # English desktop home (verified buttons & logo)
│   ├── phase3_desktop_detail_en.png     # English desktop detail (unclipped 16:9 hero)
│   ├── phase3_mobile_home_en.png        # English mobile home (verified button & logo)
│   ├── phase3_mobile_404_en.png         # English mobile 404 (unclipped recovery buttons)
│   ├── phase3_mobile_contact_en.png     # English mobile contact (clearance verified)
│   ├── phase3_mobile_privacy_bn.png     # Previously missing BN mobile privacy
│   ├── phase3_mobile_privacy_en.png     # Previously missing EN mobile privacy
│   └── verification_contact_sheets/     # Scannable visual proof sheets
├── images/
│   ├── masters/                         # 12 Master architectural concept stills (1376x768)
│   └── asset_manifest.csv               # Corrected 10-column manifest with launch status
├── handoff/
│   ├── CLAUDE_CODE_HANDOFF.md           # Master technical implementation guide for Claude Code
│   ├── layout_register.csv              # 44 layouts + 18 overlays mapped to export paths
│   ├── copy_bn_en.csv                   # Properly quoted 5-column bilingual copy manifest
│   └── route_map.csv                    # In-prototype interaction map & URL targets
└── apartment/
    └── DEFERRED_DEFECTS_AND_NEXT_STEPS.md # Architectural plan defects & post-website 3D plan
```
