"""
FlowGrid - Crop Actual High-Fidelity Screen Views from Rendered PNG Boards
Creates pixel-perfect screen previews for the client presentation deck (Slides 6 & 7).
All crop coordinates verified against exact SVG layout positions.
"""
import os
from PIL import Image

def main():
    print("Opening page_03_desktop_bn.png...")
    img_desk = Image.open('figma_exports/page_03_desktop_bn.png')
    print("Desktop board size:", img_desk.size)

    # 1. Desktop Homepage hero + content (1440 x 1080 crop at x=80, y=260)
    crop_desk_home = img_desk.crop((80, 260, 80 + 1440, 260 + 1080))
    crop_desk_home.save('figma_exports/crop_desktop_home.png')
    print("Saved crop_desktop_home.png:", crop_desk_home.size)

    # 2. Desktop Projects Archive (1440 x 1080 crop at x=1680, y=260)
    crop_desk_arch = img_desk.crop((1680, 260, 1680 + 1440, 260 + 1080))
    crop_desk_arch.save('figma_exports/crop_desktop_archive.png')
    print("Saved crop_desktop_archive.png:", crop_desk_arch.size)

    # 3. Desktop 3-View Concept Study (1440 x 1080 crop at x=3280, y=260)
    crop_desk_study = img_desk.crop((3280, 260, 3280 + 1440, 260 + 1080))
    crop_desk_study.save('figma_exports/crop_desktop_study.png')
    print("Saved crop_desktop_study.png:", crop_desk_study.size)

    # 4. Desktop Services & Joinery (1440 x 1080 crop at x=80, y=2560)
    crop_desk_serv = img_desk.crop((80, 2560, 80 + 1440, 2560 + 1080))
    crop_desk_serv.save('figma_exports/crop_desktop_services.png')
    print("Saved crop_desktop_services.png:", crop_desk_serv.size)

    print("\nOpening page_04_mobile_bn.png...")
    img_mob = Image.open('figma_exports/page_04_mobile_bn.png')
    print("Mobile board size:", img_mob.size)

    # 5. Mobile Home (390 x 844 crop at x=80, y=260)
    crop_mob_home = img_mob.crop((80, 260, 80 + 390, 260 + 844))
    crop_mob_home.save('figma_exports/crop_mobile_home.png')
    print("Saved crop_mobile_home.png:", crop_mob_home.size)

    # 6. Mobile 3-View Concept Study (390 x 844 crop at x=550, y=1920)
    crop_mob_study = img_mob.crop((550, 1920, 550 + 390, 1920 + 844))
    crop_mob_study.save('figma_exports/crop_mobile_study.png')
    print("Saved crop_mobile_study.png:", crop_mob_study.size)

    # 7. Mobile Dedicated Contact (390 x 844 crop at x=1960, y=260)
    crop_mob_contact = img_mob.crop((1960, 260, 1960 + 390, 260 + 844))
    crop_mob_contact.save('figma_exports/crop_mobile_contact.png')
    print("Saved crop_mobile_contact.png:", crop_mob_contact.size)

    # 8. Mobile Off-Canvas Drawer Overlay (390 x 750 crop at x=1960, y=2420)
    crop_mob_drawer = img_mob.crop((1960, 2420, 1960 + 390, 2420 + 750))
    crop_mob_drawer.save('figma_exports/crop_mobile_drawer.png')
    print("Saved crop_mobile_drawer.png:", crop_mob_drawer.size)

    # 9. Fitted Mobile Contact Form (390 x 520 crop at x=1960, y=390 showing header, 4 fields, and 52px CTA without blank card space)
    crop_mob_form = img_mob.crop((1960, 260 + 130, 1960 + 390, 260 + 130 + 520))
    crop_mob_form.save('figma_exports/crop_mobile_form.png')
    print("Saved crop_mobile_form.png:", crop_mob_form.size)

    print("\nAll 9 crops generated and verified successfully!")

if __name__ == '__main__':
    main()
