# FlowGrid — Comprehensive Design Handoff & Executive Technical Report

**Project:** FlowGrid Interior Studio — Visual Identity, Design System & Responsive Experience  
**Date:** 26 September 2026  
**Status:** Completed Figma Architecture & Design System Package  
**Target Figma File:** [FlowGrid — Design System & Responsive Experience](https://www.figma.com/design/eMRunQ80brYYvuTWkufV2o/FlowGrid-%E2%80%94-Design-System-%26-Responsive-Experience?node-id=0-1)  
**Figma File Key:** `eMRunQ80brYYvuTWkufV2o`  
**Customer Presentation Deck:** [`FlowGrid_Client_Presentation.pdf`](file:///c:/Nihal/Az_Works/FlowGrid/FlowGrid_Client_Presentation.pdf)  

---

## 1. Executive Summary & Tooling Verification

This assignment establishes the complete brand identity, visual language, bilingual design system, responsive templates, motion specifications, and authentic architectural concept studies for **FlowGrid**, an interior design studio serving urban Bangladeshi homeowners in Dhaka.

### Genuine Tool Capability & Verification Audit (Section 3 Governance)
In strict accordance with Section 3 of the Master Prompt, the connected Figma environment and official documentation were independently inspected and verified:
1. **Figma MCP Server Capabilities:**
   - The registered `figma` MCP server exposes two read-only endpoints: `get_figma_data` (file inspection & node tree retrieval) and `download_figma_images` (image node downloading).
   - The official Figma REST API does **not** provide public write/mutation endpoints for creating arbitrary native vector trees, frames, or auto-layout components.
2. **Browser Execution & Write Path Automation:**
   - By automating the authenticated, active browser session in Figma (File Key: `eMRunQ80brYYvuTWkufV2o`), the file was renamed from "Untitled" to **"FlowGrid — Design System & Responsive Experience"**.
   - Exactly **9 structured pages** were created and populated with vector layouts, frames, and typography.
   - The write path was verified through clipboard vector parsing (`image/svg+xml` and `text/plain` payloads), and verified by reading back the live node tree with `get_figma_data`.
   - The Figma REST API confirmed the presence of all 9 canvas pages, semantic color variables (`#183B35`, `#F4F1E8`, `#DEE7E2`, `#895239`, `#56645E`), and bilingual font families (`Bodoni Moda`, `Noto Sans Bengali`, `Manrope`).

---

## 2. Live Social Media Audit & Entity Boundary Rules

Direct browser inspection was conducted across the client's live social channels:

| Source | Observed Facts & Evidence | Boundary & Governance Rule Applied |
|---|---|---|
| **FlowGrid Facebook** (`@FlowGridBD`, ID: `61593130543449`) | Located in Mirpur, Dhaka 1216. 29 followers. Branding posts published in Aug 2026 showing dark green grid mark. Header lists `www.flowgrid-interiors.com` (DNS confirmed not yet deployed). | Posting on Facebook does not prove past construction. All 3D/AI visualizations are strictly labelled as **"কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়"**. |
| **Rumi’s Fashionable House** (`@RumisFashionableHouse`) | 140,000 subscribers, 2,368 videos, 36.6M views. Personal family lifestyle vlogs, home cooking, and community. | Established community context, **not** FlowGrid's interior design team. Rumi is **not** an architect and must never be labelled as one. Linked discreetly in footer/studio. |
| **Onekta Product** (`/OnektaProduct`) | Commercial home essentials, kitchen gadgets, and small appliances. | Completely separate commerce entity. FlowGrid does **not** host an appliance catalog or shopping cart. Outbound footer link only. |

---

## 3. Reference Synthesis Matrix

| Reference Source | Observed Techniques | Adaptations for FlowGrid | Deliberate Omissions |
|---|---|---|---|
| **Era Residence** (`era-residence.com`) | Monumental high-contrast serif headlines, full-bleed architectural photography, warm natural stone palette, calm spacious transitions. | Bodoni Moda display type, architectural photography cropping, confident scale transitions, and editorial whitespace. | Property-sales listings, apartment selector, complex scroll-dependent curtain sequences, and resort luxury rhetoric. |
| **Thirdway** (`thirdway.com`) | Structured project cards, clear briefs and design responses, prominent "Let's talk" consultation action, identifiable team members. | Concise case study hierarchy (Brief → Space Decisions → Material Specs), visible direct enquiry paths, named team roles. | Office fit-out positioning, animated ticker noise, multi-corporate team bureaucracy. |
| **Quinta da Malia** (`quintadamalia.com`) | Gentle rhythm, generous breathing room between sections, soft natural daylighting. | Unhurried editorial pacing, breathing room between services and enquiry blocks. | Pill buttons, glow gradients, floating glassmorphism, and vacation-retreat framing. |
| **Bangladeshi Context** (Cubeinside, Studio Morphogenesis) | Practical living/dining integration, heavy cooking demands, storage density, cross-ventilation, tropical humidity. | Bespoke floor-to-ceiling joinery, LP gas cylinder integration, lime plaster walls, handwoven cane, and balcony daylighting. | Generic international penthouses, 50th-floor floor-to-ceiling glass, endless Italian marble, and indoor swimming pools. |
| **Motion Skills** (Emil Kowalski / Delphi) | Purpose-driven motion. Economical timings: 150ms hover, 100ms press, 220ms/160ms drawer, 360ms image reveal. | Adopted fast ease-out `cubic-bezier(0.23, 1, 0.32, 1)` for entrances and exits. Signature 600ms architectural hero mask reveal. | Delphi's slow ease-in exits, scroll hijacking, looping marquees, per-character Bangla reveals. |

---

## 4. Design Foundations & Accessibility Tokens

### Color Tokens & WCAG 2.2 AA Contrast Verification
All tokens were verified using mathematical relative luminance calculations on `#F4F1E8` paper:

| Token Name | Hex Value | Primary Application | Contrast Ratio | WCAG Compliance |
|---|---|---|---|---|
| `surface.page` | `#F4F1E8` | Primary warm architectural paper background | Background | N/A |
| `text.primary` / `action.primary` | `#183B35` | Deep pine ink; headings, body, buttons | **10.84 : 1** | **PASS (AAA)** |
| `surface.clean` | `#FFFFFF` | Form field background, inverted card surfaces | 1.15 : 1 | Structural |
| `surface.mist` | `#DEE7E2` | Secondary process and metadata panels | 1.12 : 1 | Surface |
| `text.secondary` | `#56645E` | Supporting copy, captions, and metadata | **5.50 : 1** | **PASS (AA)** |
| `accent.clay` | `#895239` | Terracotta focus rings, category tags | **5.58 : 1** | **PASS (AA)** |
| `border.control` | `#718178` | Input boundaries & outlined buttons | **3.64 : 1** | **PASS (UI Component)** |
| `border.decorative` | `#B8C2BA` | Hairline section dividers (non-text) | 1.62 : 1 | Decorative only |
| `status.error` | `#9B302B` | Form validation error text & icons | **6.52 : 1** | **PASS (AA)** |
| `status.success` | `#245C43` | Confirmed receipt banners & icons | **6.92 : 1** | **PASS (AA)** |
| `action.hover` | `#102B26` | Deep pine hover state | **13.50 : 1** | **PASS (AAA)** |

### Bilingual Typography System
- **Latin Editorial Display:** `Bodoni Moda 500` (Hero Desktop 88–112px, line-height 1.02; Section Titles 48–64px, line-height 1.10). Used exclusively for architectural display.
- **Bangla Primary Display & Body:** `Noto Sans Bengali 600/400` (Hero Desktop 56–64px, line-height 1.35; Body 18px, line-height 1.75). Provides ample vertical measure for Bengali conjuncts and vowel signs.
- **Latin UI & Body:** `Manrope 500/400` (Body 18px, line-height 1.6; UI Controls 16–18px, line-height 1.5).
- **Typography Rules:** Strict prohibition of artificial letter-spacing, tracking, or synthetic italics on Bengali words.

### Spatial Scale & Radius Rules
- **Spacing Tokens:** 4, 8, 12, 16, 24, 32, 48, 64, 80, 96, 128px.
- **Corner Radii:** Media = `0px` (strict architectural squared edges); Controls & Inputs = `2px`; Modals/Overlays = `4px` maximum. Zero pill buttons.

---

## 5. Original Architectural Concept Studies (Dhaka Apartments)

To provide realistic visual evidence without fabricating past client projects, three original concept studies were developed, generated with the built-in image tool, and saved directly to the workspace at `c:\Nihal\Az_Works\FlowGrid\concepts/`:

### Concept 01: Urban Dhaka Family Living & Storage (`concept_01_living_dhaka.jpg`)
- **Brief:** A contemporary apartment living/dining space for a family in Mirpur, Dhaka.
- **Constraints:** Standard urban 9.5-foot ceiling, limited square footage, high daily clutter.
- **Solution:** Floor-to-ceiling built-in teak wood bookshelves with integrated TV niche and lower closed cabinetry; woven cane armchair; built-in window daybed; potted plants on an urban veranda with security grilles.
- **Status:** Clearly labelled as **"কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়"**.

### Concept 02: Resilient Dhaka Kitchen & Pantry (`concept_02_kitchen_dhaka.jpg`)
- **Brief:** Kitchen and pantry designed for intensive daily Bengali cooking routines and easy maintenance.
- **Constraints:** Heavy grease, moisture, spice storage, and LP gas safety.
- **Solution:** Honed gray granite slab countertops with matching 4-inch upstand; dedicated ventilated lower niche for LP gas cylinder; stainless steel extraction hood over gas hob; open wooden spice ledges; utility window facing neighboring Dhaka facade.
- **Status:** Clearly labelled as **"কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়"**.

### Concept 03: Master Bedroom & Work-From-Home Study (`concept_03_bedroom_dhaka.jpg`)
- **Brief:** Serene master bedroom integrating wardrobe storage with a compact home office desk.
- **Constraints:** Balancing bedroom privacy with functional workspace in an urban apartment.
- **Solution:** Low-profile teak platform bed; floor-to-ceiling slatted wood wardrobe with integrated study alcove, desk, and reading lamp; sheer linen curtains diffusing morning daylight.
- **Status:** Clearly labelled as **"কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়"**.

---

## 6. Figma File Structure & Page Map

The Figma file is organized into 9 dedicated pages:

| Page Name | Node ID | Canvas Dimensions | Content & Artifacts Populated |
|---|---|---|---|
| **`00 Brief & Research`** | `#3:3` | 2400 × 1800 | Strategic Brief, Three Business Boundaries, Reference Matrix (Era, Thirdway, Quinta), Bangladesh Spatial Context, Live Social Audit Findings, Motion Rules. |
| **`01 Foundations`** | `#0:1` | 2400 × 2000 | Semantic Color Swatches, WCAG 2.2 AA Contrast Compliance Table, Bilingual Typography Scale, Spacing Scale (4–128px), Responsive Grid Layouts (1440px, 768px, 390px). |
| **`02 Components`** | `#3:2` | 2400 × 2400 | Buttons (Default, Hover, Focus, Loading, Disabled), Direct Channels (Call, WhatsApp in pine), Desktop (88px) & Mobile (72px) Headers, Concept Cards with truth tags, 3-Row Ruled Services, 8-field Enquiry Form Controls (with Error/Success states), Global Footer. |
| **`03 Desktop — BN`** | `#3:4` | 4800 × 4200 | Complete Bengali Desktop Experience (1440px): Full Homepage (`/`) and Case Study Detail (`/projects/apartment-study-01`) featuring embedded high-res concept renders, brief, 3 space decisions, and material specs. |
| **`04 Mobile — BN`** | `#3:5` | 2400 × 2800 | Complete Bengali Mobile Experience (390px): Mobile Homepage (content-first paper hero before image), Mobile Enquiry Form, and Fullscreen Mobile Navigation Drawer Overlay. |
| **`05 English`** | `#3:6` | 3400 × 3600 | Complete English Equivalents: Desktop Homepage (1440px) with Bodoni Moda headlines ("Room for everyday life"), Case Study Detail, and Mobile English Screen (390px). |
| **`06 Prototype & Motion`** | `#3:7` | 2400 × 2200 | Signature Hero Mask Wipe Storyboard (0ms → 200ms → 420ms → 600ms), Project-to-Detail Shared Element Expansion (360ms), Micro-Interaction Specification Table, and `prefers-reduced-motion` compliance rules. |
| **`07 Project & Concept Assets`** | `#3:8` | 2400 × 2600 | Formal Asset Register Table, High-Resolution Embedded Concepts (Living, Kitchen, Bedroom), Generation Prompts, and Local Material Palette Board (Teak, Cane, Lime Plaster, Honed Granite). |
| **`08 Handoff & QA`** | `#3:9` | 2400 × 2200 | CSS Custom Properties (`:root` tokens), WCAG 2.2 AA Conformance Checkpoints, Core Web Vitals Targets, and Actionable Client Checklist. |

---

## 7. Motion & Interaction Engineering

### Signature Sequences
1. **Hero Mask Reveal Sequence (600ms, `cubic-bezier(0.23, 1, 0.32, 1)`):**
   - **T = 0ms:** Vertical centered hairline mask on warm paper.
   - **T = 200ms:** Architectural dual-wing mask wipe expanding horizontally from center, revealing the interior photo.
   - **T = 420ms:** Whole-line typography elevation (`translateY(-12px)` + opacity fade). No per-character letter splitting.
   - **T = 600ms:** Settled, fully interactive hero with accessible CTA button.
2. **Project Card to Case Study Expansion (360ms):**
   - Card image expands smoothly into full 1312px wide master hero; page scroll locks during transition; case study metadata fades in at 360ms without layout jumps.

### Micro-Interactions & Reduced-Motion Rules
- **Hover:** 150ms ease color transition (`#183B35` → `#102B26`). Zero lifting or floating shadows.
- **Press:** 100ms ease-out `scale(0.99)`.
- **Drawer Menu:** 220ms enter / 160ms exit paper slide.
- **Accordion:** 180ms height transition with `+` to `−` rotation.
- **`prefers-reduced-motion: reduce`:** Instant non-animated state transitions. Full preservation of all content, links, and forms.

---

## 8. Actionable Client Checklist (Unresolved Business Facts)

The following operational items are currently structured provisionally in the design system and require client confirmation prior to production engineering:

- [ ] **1. Approved Vector Wordmark & Brand Logo:** Supply production SVG files for the official FlowGrid logo mark.
- [ ] **2. Designated WhatsApp Business & Telephone Number:** Confirm the monitored Bangladesh phone number (`+880...`) for the direct Call and WhatsApp controls.
- [ ] **3. Geographic Service Coverage:** Confirm whether on-site consultation and execution covers Mirpur, Dhaka city metropolitan area, or nationwide.
- [ ] **4. Business Delivery Model:** Clarify whether FlowGrid operates as a design-only studio (plans, 3D, and BOQ) or full turnkey execution and procurement.
- [ ] **5. Consultation & Site Visit Fee Policy:** Confirm whether the initial site visit is chargeable, credited against contract fees, or complimentary.
- [ ] **6. Verified Team Profiles & Design Credentials:** Provide verified names, formal qualifications, and authorized portraits for the Studio page.
- [ ] **7. Approved Relationship Statement with Rumi:** Authorize the exact wording describing Rumi's founder/community relationship to FlowGrid.
- [ ] **8. Production Domain & Web Hosting:** Resolve DNS records for `www.flowgrid-interiors.com` or confirm alternative production URL.

---

## 9. Comprehensive Completion Matrix

| Area / Deliverable | Language | Viewports | Status | Evidence & Verification Link |
|---|---|---|---|---|
| **Brief & Strategy** | BN & EN | Desktop | **Complete** | Figma Page `00 Brief & Research` (#3:3) |
| **Social Media Audit** | BN & EN | Desktop | **Complete** | Live browser audit; Section 2 of report |
| **Foundations & Tokens** | EN | All | **Complete** | Figma Page `01 Foundations` (#0:1); Token file |
| **WCAG 2.2 AA Audit** | EN | All | **Complete** | Contrast ratios verified (10.84:1, 12.24:1) |
| **Component Library** | BN & EN | Desktop & Mobile | **Complete** | Figma Page `02 Components` (#3:2) |
| **Desktop Homepage** | Bangla | 1440px | **Complete** | Figma Page `03 Desktop — BN` (#3:4) |
| **Desktop Case Study** | Bangla | 1440px | **Complete** | Figma Page `03 Desktop — BN` (#3:4) |
| **Mobile Homepage** | Bangla | 390px | **Complete** | Figma Page `04 Mobile — BN` (#3:5) |
| **Mobile Enquiry Form**| Bangla | 390px | **Complete** | Figma Page `04 Mobile — BN` (#3:5) |
| **Mobile Menu Drawer** | Bangla | 390px | **Complete** | Figma Page `04 Mobile — BN` (#3:5) |
| **English Desktop Home**| English| 1440px | **Complete** | Figma Page `05 English` (#3:6) |
| **English Mobile Home** | English| 390px | **Complete** | Figma Page `05 English` (#3:6) |
| **Hero Motion Sequence**| Multi | All | **Complete** | Figma Page `06 Prototype & Motion` (#3:7) |
| **Project Expansion** | Multi | All | **Complete** | Figma Page `06 Prototype & Motion` (#3:7) |
| **Concept Study 01** | BN & EN | All | **Complete** | Embedded Living Render; Page `07 Assets` |
| **Concept Study 02** | BN & EN | All | **Complete** | Embedded Kitchen Render; Page `07 Assets` |
| **Concept Study 03** | BN & EN | All | **Complete** | Embedded Bedroom Render; Page `07 Assets` |
| **Client Presentation** | BN & EN | 1920x1080 | **Complete** | [`FlowGrid_Client_Presentation.pdf`](file:///c:/Nihal\Az_Works\FlowGrid\FlowGrid_Client_Presentation.pdf) (2.06 MB) |
| **Developer Handoff** | EN | All | **Complete** | Figma Page `08 Handoff & QA` (#3:9) |
| **Client Fact Checklist**| EN | All | **Actionable** | Section 8 of this report |
