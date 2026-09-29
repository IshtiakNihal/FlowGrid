# FlowGrid Design System Specification

**Stage 1 Production Delivery · 29 September 2026**  
**Figma File:** [FlowGrid — Design System & Responsive Experience](https://www.figma.com/design/eMRunQ80brYYvuTWkufV2o/FlowGrid-%E2%80%94-Design-System-%26-Responsive-Experience?node-id=0-1) (`eMRunQ80brYYvuTWkufV2o`)

---

## 1. Brand Identity & Logo System

The visual identity is reconstructed directly from the studio's official Facebook identity (`FlowGridBD`, Mirpur, Dhaka 1216):
- **Full Identity Lockup:** 6×6 architectural drafting grid with 45° diagonal line, calligraphic 'F' monogram in Deep Pine (`#16463C`), clean geometric sans wordmark `FlowGrid`, and tagline `Interior and design` (`#949492`).
- **Compact Monogram:** 'F' on 6×6 grid for responsive mobile headers and favicons.
- **Minimum Digital Sizes:** Full mark: 120 px width; Compact monogram: 24 px width; Favicon: 16/32/64 px.
- **Clear Space:** 0.25 × G (drafting grid width) on all four sides.

---

## 2. Semantic Color Palette

| Token Name | Hex Code | RGB | Role & Usage |
|---|---|---|---|
| `color.brand.pine` | `#16463C` | `22, 70, 60` | Primary brand color, monogram, active interactive states |
| `color.canvas.warm-paper`| `#F7F7F5` | `247, 247, 245`| Default background canvas, card surfaces |
| `color.grid.slate` | `#C6CBCB` | `198, 203, 203`| Drafting grid lines, architectural structural borders |
| `color.text.muted` | `#949492` | `148, 148, 146`| Subtitles, captions, metadata badges |
| `color.surface.mist` | `#DEE7E2` | `222, 231, 226`| Hover states, secondary pills, subtle container fills |
| `color.accent.clay` | `#895239` | `137, 82, 57` | Warm terracotta accents, highlights, balcony materials |
| `color.surface.deep-pine`| `#183B35` | `24, 59, 53` | Dark surfaces, contrast headers, hero backgrounds |

---

## 3. Typography Hierarchy

### Bengali (Noto Sans Bengali)
- **Display Hero:** 44px / Line-Height: 1.3 / Bold (`আপনার ঘর, আপনার মতো।`)
- **Section Heading:** 32px / Line-Height: 1.4 / SemiBold
- **Card Title / Project:** 22px / Line-Height: 1.5 / SemiBold
- **Body Regular:** 16px / Line-Height: 1.7 / Regular
- **Caption / Metadata:** 12px / Line-Height: 1.5 / Medium (`কনসেপ্ট ডিজাইন · মিরপুর, ঢাকা`)

### English (Inter / Geometric Modern Sans)
- **Display Hero:** 48px / Line-Height: 1.15 / SemiBold (`A home shaped around you.`)
- **Section Heading:** 32px / Line-Height: 1.3 / SemiBold
- **Card Title / Project:** 22px / Line-Height: 1.4 / SemiBold
- **Body Regular:** 15px / Line-Height: 1.6 / Regular
- **Caption / Metadata:** 12px / Line-Height: 1.4 / Medium (`Concept Design · Mirpur, Dhaka`)

---

## 4. Layout & Grid Standards

- **Desktop Master:** 1440 px canvas width. Max content container: 1200 px. 12-column grid, 24 px gutters, 120 px margins.
- **Mobile Master:** 390 px canvas width. Content container: 358 px. 4-column grid, 16 px gutters, 16 px margins.
- **Base Spacing System:** 8pt modular scale: `8, 16, 24, 32, 48, 64, 96, 128 px`.
- **Minimum Touch Targets:** 48 × 48 px on all mobile buttons, links, and form fields.

---

## 5. Reusable Component Inventory (Page 02)

1. `Button / Primary CTA` (`10:42`):
   - Variants: Default, Hover, Focused, Disabled.
   - Height: 50 px (Desktop) / 48 px (Mobile).
   - Radius: 4 px. Fill: `#16463C`.
2. `Control / Text Field` (`21:2599`):
   - Variants: Empty, Filled, Focused, Error.
   - Sizing: Hug vertical, 48 px min height. Accessible error states.
3. `Modal / Consultation Enquiry Card` (`10:43`):
   - Form fields: Name, Phone Number, Project Location, Project Type, Notes.
   - Connected states: Submitting (`18:403`) and Success Receipt (`18:407`).
4. `Navigation / Mobile Drawer` (`10:56`):
   - Slide-in sheet (320 px wide) with full bilingual navigation links and language switcher.
5. `Badge / Concept Disclosure` (`18:383`):
   - Clean, restrained label: `কনসেপ্ট ডিজাইন` / `Concept Design`.
   - All legacy AI disclaimers formally revoked and replaced.
