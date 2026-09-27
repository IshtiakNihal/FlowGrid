"""
FlowGrid - Page 00: Brief & Research Generator (v3)
Strict XML escaping, single owner fact register, clear entity boundaries.
"""
import os
from svg_utils import wrap_text, escape_xml, validate_svg_file

def generate_board_00():
    w, h = 2400, 1950
    svg = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{w}" height="{h}" fill="#F4F1E8"/>')
    
    # Header Banner
    svg.append('<rect x="80" y="80" width="2240" height="140" fill="#183B35" rx="4"/>')
    svg.append('<text x="120" y="145" fill="#F4F1E8" font-family="\'Bodoni Moda\', serif" font-size="36" font-weight="600">FlowGrid — Strategic Foundations &amp; Research Audit (v3)</text>')
    svg.append('<text x="120" y="185" fill="#DEE7E2" font-family="\'Manrope\', sans-serif" font-size="18">Visual direction, architectural references, live social media audit, and local Bangladeshi design context</text>')

    # Col 1: Three Entities & Boundary Governance
    svg.append('<rect x="80" y="260" width="700" height="780" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<rect x="80" y="260" width="700" height="60" fill="#183B35" rx="4 4 0 0"/>')
    svg.append('<text x="110" y="300" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="20" font-weight="600">01. Three Entities &amp; Boundary Governance</text>')
    
    svg.append('<text x="110" y="355" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="17" font-weight="700">1. FlowGrid (Interior Architecture Studio)</text>')
    t1, _ = wrap_text("• Core Scope: Space planning, bespoke joinery, family living solutions, and design consultation.", 110, 385, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    t2, _ = wrap_text("• Identity: Independent studio serving urban Bangladeshi homeowners with custom joinery.", 110, 435, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    t3, _ = wrap_text("• Studio Location: Mirpur, Dhaka 1216 (provisional/observed on Facebook).", 110, 485, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    t4, _ = wrap_text("• Boundary Rule: Not an appliance retailer; not an influencer fan club; not a construction contractor.", 110, 535, 68, 22, "'Manrope', sans-serif", 14, "#895239", 600)
    svg.extend([t1, t2, t3, t4])

    svg.append('<text x="110" y="600" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="17" font-weight="700">2. Rumi\'s Fashionable House (Community Sibling)</text>')
    t5, _ = wrap_text("• Presence: 140,000 subscribers, 2,368 videos, 36.6M views on YouTube (verified).", 110, 630, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    t6, _ = wrap_text("• Audience Focus: Family lifestyle vlogs, home cooking, and community trust.", 110, 680, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    t7, _ = wrap_text("• Boundary Rule: Rumi is a lifestyle vlogger/founder context, NOT an architect. Do NOT imply architectural credentials or lack thereof.", 110, 730, 68, 22, "'Manrope', sans-serif", 14, "#895239", 600)
    svg.extend([t5, t6, t7])

    svg.append('<text x="110" y="800" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="17" font-weight="700">3. Onekta Product (Retail Sibling)</text>')
    t8, _ = wrap_text("• Focus: Small appliances, practical household tools, and consumer kitchen items.", 110, 830, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    t9, _ = wrap_text("• Boundary Rule: Completely separate commerce entity. FlowGrid does NOT host shopping carts or sell appliances.", 110, 880, 68, 22, "'Manrope', sans-serif", 14, "#895239", 600)
    t10, _ = wrap_text("• Integration: Mentioned strictly as a trusted household resource link in studio/footer.", 110, 950, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    svg.extend([t8, t9, t10])

    # Col 2: Reference Synthesis Matrix
    svg.append('<rect x="850" y="260" width="700" height="780" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<rect x="850" y="260" width="700" height="60" fill="#183B35" rx="4 4 0 0"/>')
    svg.append('<text x="880" y="300" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="20" font-weight="600">02. Design Reference Synthesis Matrix</text>')

    svg.append('<text x="880" y="355" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="17" font-weight="700">Era Residence (era-residence.com)</text>')
    r1, _ = wrap_text("• Adopted: Warm paper background, Bodoni Moda serif headlines, generous architectural whitespace.", 880, 385, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    r2, _ = wrap_text("• Omitted: Commercial apartment-sales listings, apartment selector tools, luxury resort rhetoric.", 880, 440, 68, 22, "'Manrope', sans-serif", 14, "#895239")
    svg.extend([r1, r2])

    svg.append('<text x="880" y="510" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="17" font-weight="700">Thirdway (thirdway.com)</text>')
    r3, _ = wrap_text("• Adopted: Clear structured project briefs (Brief → Decisions → Specs), identifiable team roles, visible contact.", 880, 540, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    r4, _ = wrap_text("• Omitted: Corporate office fit-out positioning, animated ticker noise, multi-corporate bureaucracy.", 880, 600, 68, 22, "'Manrope', sans-serif", 14, "#895239")
    svg.extend([r3, r4])

    svg.append('<text x="880" y="670" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="17" font-weight="700">Quinta da Malia (quintadamalia.com)</text>')
    r5, _ = wrap_text("• Adopted: Restrained unhurried pacing, soft natural daylighting, calm editorial rhythm.", 880, 700, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    r6, _ = wrap_text("• Omitted: Pill buttons, glow gradients, floating glassmorphism, vacation retreat framing.", 880, 755, 68, 22, "'Manrope', sans-serif", 14, "#895239")
    svg.extend([r5, r6])

    svg.append('<text x="880" y="830" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="17" font-weight="700">Local Architectural Precedents (Cubeinside / Morphogenesis)</text>')
    r7, _ = wrap_text("• Adopted: Teak wood joinery, woven cane panels, resilient granite, cross-ventilation, balcony plants.", 880, 860, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    r8, _ = wrap_text("• Omitted: 50th-floor floor-to-ceiling glass walls, cold glass/steel, indoor pools.", 880, 920, 68, 22, "'Manrope', sans-serif", 14, "#895239")
    svg.extend([r7, r8])

    # Col 3: Bangladesh Cultural & Spatial Realities
    svg.append('<rect x="1620" y="260" width="700" height="780" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<rect x="1620" y="260" width="700" height="60" fill="#183B35" rx="4 4 0 0"/>')
    svg.append('<text x="1650" y="300" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="20" font-weight="600">03. Dhaka Spatial &amp; Cultural Realities</text>')

    svg.append('<text x="1650" y="355" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="17" font-weight="700">Urban Apartment Ceilings &amp; Storage Density</text>')
    s1, _ = wrap_text("• Standard 9.5-foot structural slab height limits suspended ceilings; prioritized vertical joinery.", 1650, 385, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    s2, _ = wrap_text("• Intense storage requirements: seasonal quilts, suitcases, books, and crockery need closed floor-to-ceiling millwork.", 1650, 440, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    svg.extend([s1, s2])

    svg.append('<text x="1650" y="520" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="17" font-weight="700">Kitchen &amp; Culinary Demands</text>')
    s3, _ = wrap_text("• Heavy daily Bengali cooking involves turmeric, mustard oil, and spices requiring stain-resistant surfaces.", 1650, 550, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    s4, _ = wrap_text("• Liquid Petroleum Gas (LPG) cylinder integration requires dedicated lower ventilated cabinetry.", 1650, 605, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    svg.extend([s3, s4])

    svg.append('<text x="1650" y="680" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="17" font-weight="700">Dhaka Climate &amp; Monsoon Humidity</text>')
    s5, _ = wrap_text("• High relative humidity requires breathable woven cane inserts and moisture-resistant finishes.", 1650, 710, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    s6, _ = wrap_text("• Veranda grilles and natural daylighting integration are central to urban apartment living.", 1650, 765, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    svg.extend([s5, s6])

    svg.append('<text x="1650" y="840" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="17" font-weight="700">Family Multi-Generational Living</text>')
    s7, _ = wrap_text("• Living and dining areas must comfortably seat extended family gatherings and prayer routines.", 1650, 870, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    s8, _ = wrap_text("• Acoustically isolated bedroom study alcoves support quiet work-from-home focus in compact apartments.", 1650, 925, 68, 22, "'Manrope', sans-serif", 14, "#56645E")
    svg.extend([s7, s8])

    # Bottom Row: Single Owner Fact Register & Restrained Motion Principles
    svg.append('<rect x="80" y="1080" width="1100" height="780" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<rect x="80" y="1080" width="1100" height="60" fill="#183B35" rx="4 4 0 0"/>')
    svg.append('<text x="110" y="1120" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="20" font-weight="600">04. Single Owner Fact &amp; Operational Register</text>')
    
    facts = [
        ("Studio Location", "Mirpur, Dhaka 1216 (provisional: Mirpur-10 observed on Facebook). Requires owner confirmation."),
        ("Contact Telephone", "Provisional placeholder: +880 1700-000000 (observed FB: 01712-402422 pending owner verification)."),
        ("Studio Email", "hello@flowgrid-interiors.com (provisional placeholder pending production domain setup)."),
        ("Production Domain", "www.flowgrid-interiors.com (DNS confirmed not yet active; pending client hosting setup)."),
        ("Wordmark & Logo", "Proposed typographic wordmark (Bodoni Moda / Noto Sans Bengali). Final vector asset pending owner."),
        ("Commercial Model", "Design consultancy, custom joinery fabrication, and turnkey supervision (pending contract scope review)."),
        ("Initial Site Visit", "Provisional spatial assessment (pricing policy pending owner confirmation)."),
        ("Rumi Context", "Founder / community lifestyle connection. Strictly distinct from architectural licensure.")
    ]
    cur_y = 1170
    for title, desc in facts:
        svg.append(f'<text x="110" y="{cur_y}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="15" font-weight="700">{escape_xml(title)}:</text>')
        td, _ = wrap_text(desc, 310, cur_y, 75, 20, "'Manrope', sans-serif", 14, "#56645E")
        svg.append(td)
        cur_y += 72

    # Restrained Motion Guidance
    svg.append('<rect x="1220" y="1080" width="1100" height="780" fill="#FFFFFF" stroke="#B8C2BA" stroke-width="1" rx="4"/>')
    svg.append('<rect x="1220" y="1080" width="1100" height="60" fill="#183B35" rx="4 4 0 0"/>')
    svg.append('<text x="1250" y="1120" fill="#F4F1E8" font-family="\'Manrope\', sans-serif" font-size="20" font-weight="600">05. Restrained Architectural Motion Guidance</text>')

    motion_rules = [
        ("Hero Reveal Sequence (600ms)", "Center hairline split opens dual-wing horizontal mask wipe (cubic-bezier(0.23, 1, 0.32, 1)). Headline text and primary CTA remain immediately visible and interactive to ensure zero delayed usability."),
        ("Calm Project Card Hover (360ms)", "Zero vertical lift (0px), zero shadow explosion. Subtle 1.015 image scale within strict squared 0px radius frame. Easing: cubic-bezier(0.23, 1, 0.32, 1)."),
        ("Tactile Button Micro-Interactions", "150ms background color shift (#183B35 -> #102B26). 100ms press scale(0.99). High-contrast focus outline (2px #895239 with 2px offset)."),
        ("Mobile Navigation Drawer (220ms / 160ms)", "220ms smooth ease-out slide-in from right; 160ms ease-in slide-out. Backdrop opacity 0.5 pine overlay."),
        ("Accordion Expand/Collapse (180ms)", "180ms ease-in-out height transition. Icon rotates 90 degrees (+ to -)."),
        ("Accessible Reduced Motion Architecture", "@media (prefers-reduced-motion: reduce) collapses all animation durations to 0ms. Essential content, navigation, and enquiry forms render instantly without transitions.")
    ]
    cur_y = 1175
    for title, desc in motion_rules:
        svg.append(f'<text x="1250" y="{cur_y}" fill="#183B35" font-family="\'Manrope\', sans-serif" font-size="16" font-weight="700">{escape_xml(title)}</text>')
        cur_y += 24
        td, th = wrap_text(desc, 1250, cur_y, 90, 22, "'Manrope', sans-serif", 14, "#56645E")
        svg.append(td)
        cur_y += th + 30

    svg.append('</svg>')
    
    out_path = 'figma_svgs_v3/00_brief_and_research.svg'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    
    valid, err = validate_svg_file(out_path)
    print(f'Board 00: {out_path} -> Valid XML? {valid} ({err})')

if __name__ == '__main__':
    generate_board_00()
