// FlowGrid: Comprehensive Repair of the Four Principal Bengali Screens
// Resolves FG-01, FG-02, FG-03, FG-04:
// 1. Bengali Homepage — 1440px Desktop (18:137)
// 2. Bengali Project Detail — 1440px Desktop (18:221)
// 3. Bengali Homepage — 390px Mobile (18:283)
// 4. Bengali Project Detail — 390px Mobile (18:339)

(async () => {
    console.log("Repairing 4 principal Bengali screens...");

    // 1. Ensure fonts
    const fonts = [
        { family: "Noto Sans Bengali", style: "Regular" },
        { family: "Noto Sans Bengali", style: "Bold" },
        { family: "Bodoni Moda", style: "Regular" },
        { family: "Bodoni Moda", style: "Bold" },
        { family: "Inter", style: "Regular" },
        { family: "Inter", style: "Bold" }
    ];
    for (const f of fonts) {
        try { await figma.loadFontAsync(f); } catch (e) {}
    }

    // 2. Map tokens
    const cols = figma.variables.getLocalVariableCollections();
    const varMap = {};
    for (const c of cols) {
        for (const vid of c.variableIds) {
            const v = figma.variables.getVariableById(vid);
            if (v) varMap[v.name] = v;
        }
    }

    function bindFill(node, varName) {
        const v = varMap[varName];
        if (!v) return;
        let p = { type: 'SOLID', color: { r: 1, g: 1, b: 1 } };
        p = figma.variables.setBoundVariableForPaint(p, 'color', v);
        node.fills = [p];
    }

    function bindStroke(node, varName, weight = 1) {
        const v = varMap[varName];
        if (!v) return;
        let p = { type: 'SOLID', color: { r: 0, g: 0, b: 0 } };
        p = figma.variables.setBoundVariableForPaint(p, 'color', v);
        node.strokes = [p];
        node.strokeWeight = weight;
    }

    function bindCornerRadius(node, varName) {
        const v = varMap[varName];
        if (!v) return;
        node.setBoundVariable('cornerRadius', v);
    }

    const styles = figma.getLocalTextStyles();
    const styleMap = {};
    for (const s of styles) styleMap[s.name] = s;

    function createStyledText(text, styleName, fillVar, options = {}) {
        const t = figma.createText();
        const style = styleMap[styleName];
        if (style) {
            t.textStyleId = style.id;
        } else {
            t.fontName = { family: "Noto Sans Bengali", style: "Regular" };
            t.fontSize = 14;
        }
        t.characters = text;
        if (fillVar) bindFill(t, fillVar);
        if (options.align) t.textAlignHorizontal = options.align;
        // CRITICAL FOR ZERO TEXT CLIPPING:
        if (options.hug) {
            t.textAutoResize = "WIDTH_AND_HEIGHT";
        } else {
            t.layoutAlign = "STRETCH";
            t.textAutoResize = "HEIGHT";
        }
        return t;
    }

    function createImageRect(imageHash, w, h, radiusVar = 'radius/none') {
        const rect = figma.createRectangle();
        rect.name = "Architectural Photo";
        rect.resize(w, h);
        rect.fills = [{
            type: 'IMAGE',
            scaleMode: 'FILL',
            imageHash: imageHash
        }];
        if (radiusVar && varMap[radiusVar]) {
            bindCornerRadius(rect, radiusVar);
        }
        return rect;
    }

    // Image hashes
    const imgOverviewHash = "9e6c1225ff649790c89d5a011ce12a7bb25d9e9c";
    const imgAltHash = "a50d4991b590cc05dbb7cd34750d69293c60594f";
    const imgJoineryHash = "dcca525e8ca800bc1e178890630b346c99b2a149";

    const compPage = figma.root.children.find(p => p.name === "02 Components");
    const desktopBnPage = figma.root.children.find(p => p.name === "03 Desktop — BN");
    const mobileBnPage = figma.root.children.find(p => p.name === "04 Mobile — BN");

    const defaultBtnComp = compPage.children.find(c => c.name === "Button / Primary CTA")?.children[0];
    function getBtn(label) {
        const inst = defaultBtnComp.createInstance();
        if (label) {
            const txt = inst.children.find(c => c.type === "TEXT");
            if (txt) txt.characters = label;
        }
        return inst;
    }

    // =========================================================================
    // 1. REPAIR BENGALI HOMEPAGE — 1440px DESKTOP (Node #18:137)
    // =========================================================================
    console.log("Repairing Bengali Homepage 1440px Desktop...");
    const homeDt = desktopBnPage.children.find(c => c.name === "Bengali Homepage — 1440px Desktop");
    homeDt.resize(1440, 100);
    homeDt.layoutMode = "VERTICAL";
    homeDt.primaryAxisSizingMode = "AUTO";
    homeDt.counterAxisSizingMode = "FIXED";
    bindFill(homeDt, 'surface/page');

    // Remove old children to reconstruct cleanly with flawless Auto Layout
    while (homeDt.children.length > 0) {
        homeDt.children[0].remove();
    }

    // Header
    const hDt = figma.createFrame();
    hDt.name = "Header / Global Navigation";
    hDt.layoutMode = "HORIZONTAL";
    hDt.primaryAxisAlignItems = "SPACE_BETWEEN";
    hDt.counterAxisAlignItems = "CENTER";
    hDt.layoutAlign = "STRETCH";
    hDt.resize(1440, 88);
    hDt.paddingLeft = 48;
    hDt.paddingRight = 48;
    bindFill(hDt, 'surface/page');
    bindStroke(hDt, 'border/decorative', 1);

    const brandDt = figma.createText();
    brandDt.textStyleId = styleMap["Typography / Latin / Brand Display"]?.id;
    brandDt.characters = "FlowGrid";
    brandDt.textAutoResize = "WIDTH_AND_HEIGHT";
    bindFill(brandDt, 'text/primary');
    hDt.appendChild(brandDt);

    const navLinksDt = figma.createFrame();
    navLinksDt.name = "Nav Links";
    navLinksDt.layoutMode = "HORIZONTAL";
    navLinksDt.counterAxisAlignItems = "CENTER";
    navLinksDt.itemSpacing = 32;
    navLinksDt.fills = [];
    const dtLinks = [
        { name: "ধারণা সংগ্রহ", id: "navArchive" },
        { name: "সেবাসমূহ", id: "navServices" },
        { name: "পদ্ধতি", id: "navProcess" },
        { name: "স্টুডিও", id: "navStudio" },
        { name: "যোগাযোগ", id: "navContact" }
    ];
    dtLinks.forEach(l => {
        const lt = figma.createText();
        lt.textStyleId = styleMap["Typography / Bengali / Body Regular"]?.id;
        lt.characters = l.name;
        lt.textAutoResize = "WIDTH_AND_HEIGHT";
        bindFill(lt, 'text/primary');
        navLinksDt.appendChild(lt);
    });
    hDt.appendChild(navLinksDt);

    const navActsDt = figma.createFrame();
    navActsDt.name = "Nav Actions";
    navActsDt.layoutMode = "HORIZONTAL";
    navActsDt.counterAxisAlignItems = "CENTER";
    navActsDt.itemSpacing = 16;
    navActsDt.fills = [];

    const langPillDt = figma.createFrame();
    langPillDt.name = "Language Pill";
    langPillDt.layoutMode = "HORIZONTAL";
    langPillDt.paddingLeft = 14;
    langPillDt.paddingRight = 14;
    langPillDt.paddingTop = 6;
    langPillDt.paddingBottom = 6;
    bindFill(langPillDt, 'surface/mist');
    bindCornerRadius(langPillDt, 'radius/pill');
    const langTxt = figma.createText();
    langTxt.textStyleId = styleMap["Typography / Latin / Meta Small"]?.id;
    langTxt.characters = "EN";
    langTxt.textAutoResize = "WIDTH_AND_HEIGHT";
    bindFill(langTxt, 'text/primary');
    langPillDt.appendChild(langTxt);
    navActsDt.appendChild(langPillDt);

    const ctaHead = getBtn("পরামর্শ শুরু করুন");
    ctaHead.name = "Header Consultation CTA";
    navActsDt.appendChild(ctaHead);
    hDt.appendChild(navActsDt);
    homeDt.appendChild(hDt);

    // Hero Section
    const heroSec = figma.createFrame();
    heroSec.name = "Section / Hero Architectural Showcase";
    heroSec.layoutMode = "VERTICAL";
    heroSec.layoutAlign = "STRETCH";
    heroSec.paddingLeft = 48;
    heroSec.paddingRight = 48;
    heroSec.paddingTop = 64;
    heroSec.paddingBottom = 64;
    heroSec.itemSpacing = 32;
    bindFill(heroSec, 'surface/page');

    const heroBadge = createStyledText("ধারণা স্টাডি ০১ · ধানমন্ডি, ঢাকা", "Typography / Bengali / Label Bold", 'accent/clay');
    heroSec.appendChild(heroBadge);

    const heroTitle = createStyledText("প্রকৃতি, আলো ও কাঠের সুষম মেলবন্ধন", "Typography / Bengali / Display H1", 'text/primary');
    heroSec.appendChild(heroTitle);

    const heroLead = createStyledText(
        "একটি অ্যাপার্টমেন্টের সৌন্দর্য কেবল আসবাবে নয়, বরং এর সামগ্রিক অনুভূতিতে নিহিত। ঢাকার আবহাওয়ায় প্রাকৃতিক বাতাস ও উষ্ণ আলোর প্রতিফলন নিশ্চিত করে একটি প্রশান্ত পরিবেশ তৈরির স্থানিক পরিকল্পনা।",
        "Typography / Bengali / Body Large",
        'text/secondary'
    );
    heroSec.appendChild(heroLead);

    // Hero Actions row
    const heroActs = figma.createFrame();
    heroActs.name = "Hero Action Buttons";
    heroActs.layoutMode = "HORIZONTAL";
    heroActs.itemSpacing = 16;
    heroActs.fills = [];
    const heroCta1 = getBtn("পরামর্শের আবেদন করুন →");
    heroCta1.name = "Hero Primary CTA";
    heroActs.appendChild(heroCta1);
    const heroSecBtn = figma.createFrame();
    heroSecBtn.name = "Button / Secondary View Project";
    heroSecBtn.layoutMode = "HORIZONTAL";
    heroSecBtn.primaryAxisAlignItems = "CENTER";
    heroSecBtn.counterAxisAlignItems = "CENTER";
    heroSecBtn.paddingLeft = 24;
    heroSecBtn.paddingRight = 24;
    heroSecBtn.resize(180, 52);
    bindFill(heroSecBtn, 'surface/clean');
    bindStroke(heroSecBtn, 'border/control', 1);
    bindCornerRadius(heroSecBtn, 'radius/control');
    const secBtnTxt = figma.createText();
    secBtnTxt.textStyleId = styleMap["Typography / Bengali / Body Regular"]?.id;
    secBtnTxt.characters = "প্রজেক্ট বিস্তারিত দেখুন";
    secBtnTxt.textAutoResize = "WIDTH_AND_HEIGHT";
    bindFill(secBtnTxt, 'text/primary');
    heroSecBtn.appendChild(secBtnTxt);
    heroActs.appendChild(heroSecBtn);
    heroSec.appendChild(heroActs);

    // Hero Main Image
    const heroImg = createImageRect(imgOverviewHash, 1344, 600, 'radius/media');
    heroImg.layoutAlign = "STRETCH";
    heroSec.appendChild(heroImg);
    homeDt.appendChild(heroSec);

    // Narrative Section: 2-Column Multi-Angle Showcase (FG-03 fix)
    const narSec = figma.createFrame();
    narSec.name = "Section / Spatial Sequence & Material Craft";
    narSec.layoutMode = "VERTICAL";
    narSec.paddingLeft = 48;
    narSec.paddingRight = 48;
    narSec.paddingTop = 64;
    narSec.paddingBottom = 64;
    narSec.itemSpacing = 40;
    bindFill(narSec, 'surface/page');
    homeDt.appendChild(narSec);
    narSec.layoutAlign = "STRETCH";
    try { narSec.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const narHead = figma.createFrame();
    narHead.name = "Narrative Header";
    narHead.layoutMode = "VERTICAL";
    narHead.itemSpacing = 12;
    narHead.fills = [];
    narSec.appendChild(narHead);
    narHead.layoutAlign = "STRETCH";
    try { narHead.layoutSizingHorizontal = "FILL"; } catch(e) {}
    const narBadge = createStyledText("স্থানিক বিন্যাস ও ম্যাটেরিয়াল স্টাডি · ARCHITECTURAL NARRATIVE", "Typography / Bengali / Label Bold", 'accent/clay');
    const narTitle = createStyledText("বসবাসের স্বাচ্ছন্দ্য, আলো ও জয়েনারি খুঁটিনাটি", "Typography / Bengali / Section H2", 'text/primary');
    narHead.appendChild(narBadge);
    narHead.appendChild(narTitle);

    // 2-Column Gallery Grid (explicit 660px cards, 420px height photos)
    const galleryRow = figma.createFrame();
    galleryRow.name = "Multi-Angle Visual Grid";
    galleryRow.layoutMode = "HORIZONTAL";
    galleryRow.itemSpacing = 24;
    galleryRow.fills = [];
    narSec.appendChild(galleryRow);
    galleryRow.layoutAlign = "STRETCH";
    try { galleryRow.layoutSizingHorizontal = "FILL"; } catch(e) {}
    galleryRow.counterAxisSizingMode = "AUTO";

    // Card 1: Dining
    const card1 = figma.createFrame();
    card1.name = "Angle 02 / Dining Interaction";
    card1.layoutMode = "VERTICAL";
    card1.itemSpacing = 16;
    card1.paddingLeft = 24;
    card1.paddingRight = 24;
    card1.paddingTop = 24;
    card1.paddingBottom = 24;
    bindFill(card1, 'surface/clean');
    bindStroke(card1, 'border/decorative', 1);
    bindCornerRadius(card1, 'radius/control');
    galleryRow.appendChild(card1);
    card1.layoutGrow = 1;
    try { card1.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const img1 = createImageRect(imgAltHash, 612, 380, 'radius/control');
    card1.appendChild(img1);
    img1.layoutAlign = "STRETCH";
    try { img1.layoutSizingHorizontal = "FILL"; } catch(e) {}
    const cap1 = createStyledText("ডাইনিং ও বারান্দার খোলামেলা সংযোগ", "Typography / Bengali / Card H3", 'text/primary');
    const desc1 = createStyledText("স্বাভাবিক আলো ও ছায়ার পরিশীলিত ভারসাম্য বজায় রেখে উন্মুক্ত স্থানিক অনুভূতি তৈরি।", "Typography / Bengali / Body Regular", 'text/secondary');
    card1.appendChild(cap1);
    card1.appendChild(desc1);

    // Card 2: Joinery Detail
    const card2 = figma.createFrame();
    card2.name = "Angle 03 / Joinery Detail";
    card2.layoutMode = "VERTICAL";
    card2.itemSpacing = 16;
    card2.paddingLeft = 24;
    card2.paddingRight = 24;
    card2.paddingTop = 24;
    card2.paddingBottom = 24;
    bindFill(card2, 'surface/clean');
    bindStroke(card2, 'border/decorative', 1);
    bindCornerRadius(card2, 'radius/control');
    galleryRow.appendChild(card2);
    card2.layoutGrow = 1;
    try { card2.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const img2 = createImageRect(imgJoineryHash, 612, 380, 'radius/control');
    card2.appendChild(img2);
    img2.layoutAlign = "STRETCH";
    try { img2.layoutSizingHorizontal = "FILL"; } catch(e) {}
    const cap2 = createStyledText("কাস্টম কাঠের সূক্ষ্ম কারুকাজ", "Typography / Bengali / Card H3", 'text/primary');
    const desc2 = createStyledText("স্থানীয় কাঠের মিস্ত্রিদের ঐতিহ্যবাহী দক্ষতার সাথে আধুনিক আর্কিটেকচারাল ফিনিশের সমন্বয়।", "Typography / Bengali / Body Regular", 'text/secondary');
    card2.appendChild(cap2);
    card2.appendChild(desc2);

    // Architectural Specifications Matrix (4 distinct horizontal cards)
    const specRow = figma.createFrame();
    specRow.name = "Architectural Specifications Matrix";
    specRow.layoutMode = "HORIZONTAL";
    specRow.itemSpacing = 20;
    specRow.fills = [];
    narSec.appendChild(specRow);
    specRow.layoutAlign = "STRETCH";
    try { specRow.layoutSizingHorizontal = "FILL"; } catch(e) {}
    specRow.counterAxisSizingMode = "AUTO";

    const specs = [
        { label: "উপাদান ও ফিনিশ", val: "সিজনড মেহগনি কাঠ, প্রাকৃতিক ম্যাট পলিশ ও কোয়ার্টজ পৃষ্ঠ।" },
        { label: "আলোকসজ্জা ও ফিক্সচার", val: "২৭০০K উষ্ণ আর্কিটেকচারাল কোভ লাইটিং, ৯৫+ CRI কালার রেন্ডারিং।" },
        { label: "স্থানিক পরিমাপ", val: "২,৪০০ বর্গফুট (৩ বেডরুম ও স্টুডিও এলাকা)।" },
        { label: "নকশা দর্শন", val: "বায়োফিলিক ব্যালেন্স ও টেকসই দেশীয় উপাদানের প্রয়োগ।" }
    ];

    specs.forEach(sp => {
        const sc = figma.createFrame();
        sc.name = "Spec: " + sp.label;
        sc.layoutMode = "VERTICAL";
        sc.itemSpacing = 8;
        sc.paddingLeft = 20;
        sc.paddingRight = 20;
        sc.paddingTop = 20;
        sc.paddingBottom = 20;
        bindFill(sc, 'surface/clean');
        bindStroke(sc, 'border/decorative', 1);
        bindCornerRadius(sc, 'radius/control');
        specRow.appendChild(sc);
        sc.layoutGrow = 1;
        try { sc.layoutSizingHorizontal = "FILL"; } catch(e) {}

        const sTitle = createStyledText(sp.label, "Typography / Bengali / Label Bold", 'accent/clay');
        const sVal = createStyledText(sp.val, "Typography / Bengali / Body Small", 'text/primary');
        sc.appendChild(sTitle);
        sc.appendChild(sVal);
    });

    // Services Section: 3-Column Studio Practice Cards (FG-03 fix)
    const svcSec = figma.createFrame();
    svcSec.name = "Section / Studio Services & Practice";
    svcSec.layoutMode = "VERTICAL";
    svcSec.paddingLeft = 48;
    svcSec.paddingRight = 48;
    svcSec.paddingTop = 64;
    svcSec.paddingBottom = 64;
    svcSec.itemSpacing = 40;
    bindFill(svcSec, 'surface/page');
    homeDt.appendChild(svcSec);
    svcSec.layoutAlign = "STRETCH";
    try { svcSec.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const svcHead = figma.createFrame();
    svcHead.name = "Services Header";
    svcHead.layoutMode = "VERTICAL";
    svcHead.itemSpacing = 12;
    svcHead.fills = [];
    svcSec.appendChild(svcHead);
    svcHead.layoutAlign = "STRETCH";
    try { svcHead.layoutSizingHorizontal = "FILL"; } catch(e) {}
    const svcBadge = createStyledText("সেবাসমূহ · SERVICES", "Typography / Bengali / Label Bold", 'accent/clay');
    const svcTitle = createStyledText("আমাদের স্থাপত্য ও ইন্টেরিয়র কর্মক্ষেত্র", "Typography / Bengali / Section H2", 'text/primary');
    svcHead.appendChild(svcBadge);
    svcHead.appendChild(svcTitle);

    const svcGrid = figma.createFrame();
    svcGrid.name = "Services 3-Column Grid";
    svcGrid.layoutMode = "HORIZONTAL";
    svcGrid.itemSpacing = 24;
    svcGrid.fills = [];
    svcSec.appendChild(svcGrid);
    svcGrid.layoutAlign = "STRETCH";
    try { svcGrid.layoutSizingHorizontal = "FILL"; } catch(e) {}
    svcGrid.counterAxisSizingMode = "AUTO";

    const svcCards = [
        { num: "০১", title: "ইন্টেরিয়র আর্কিটেকচার", desc: "পূর্ণাঙ্গ স্পেস প্ল্যানিং, কাস্টম দেয়াল পার্টিশন, ক্যাবিনেটরি এবং আন্তর্জাতিক মানসম্পন্ন লাইটিং নকশা।" },
        { num: "০২", title: "কাস্টম মিলওয়ার্ক ও জয়েনারি", desc: "সিজনড মেহগনি ও সেগুন কাঠে নির্মিত মেঝে-থেকে-ছাদ স্টোরেজ ও টেকসই আর্কিটেকচারাল আসবাব।" },
        { num: "০৩", title: "স্পেস প্ল্যানিং ও BOQ শিট", desc: "স্বচ্ছ বাজারদরভিত্তিক নির্মাণ সামগ্রীর বাজেট বিবরণী এবং সার্বক্ষণিক সাইট তদারকি।" }
    ];

    svcCards.forEach(c => {
        const sc = figma.createFrame();
        sc.name = "Service Card " + c.num;
        sc.layoutMode = "VERTICAL";
        sc.itemSpacing = 16;
        sc.paddingLeft = 32;
        sc.paddingRight = 32;
        sc.paddingTop = 32;
        sc.paddingBottom = 32;
        bindFill(sc, 'surface/clean');
        bindStroke(sc, 'border/decorative', 1);
        bindCornerRadius(sc, 'radius/control');
        svcGrid.appendChild(sc);
        sc.layoutGrow = 1;
        try { sc.layoutSizingHorizontal = "FILL"; } catch(e) {}

        const numTxt = createStyledText(c.num, "Typography / Bengali / Label Bold", 'accent/clay');
        const titTxt = createStyledText(c.title, "Typography / Bengali / Card H3", 'text/primary');
        const descTxt = createStyledText(c.desc, "Typography / Bengali / Body Regular", 'text/secondary');
        sc.appendChild(numTxt);
        sc.appendChild(titTxt);
        sc.appendChild(descTxt);
    });

    // Consultation Practice Banner
    const consultSec = figma.createFrame();
    consultSec.name = "Section / Consultation Practice Banner";
    consultSec.layoutMode = "VERTICAL";
    consultSec.paddingLeft = 48;
    consultSec.paddingRight = 48;
    consultSec.paddingTop = 48;
    consultSec.paddingBottom = 48;
    bindFill(consultSec, 'surface/page');
    homeDt.appendChild(consultSec);
    consultSec.layoutAlign = "STRETCH";
    try { consultSec.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const consultCard = figma.createFrame();
    consultCard.name = "Consultation Card";
    consultCard.layoutMode = "HORIZONTAL";
    consultCard.primaryAxisAlignItems = "SPACE_BETWEEN";
    consultCard.counterAxisAlignItems = "CENTER";
    consultCard.paddingLeft = 48;
    consultCard.paddingRight = 48;
    consultCard.paddingTop = 40;
    consultCard.paddingBottom = 40;
    bindFill(consultCard, 'surface/mist');
    bindStroke(consultCard, 'border/control', 1);
    bindCornerRadius(consultCard, 'radius/modal');
    consultSec.appendChild(consultCard);
    consultCard.layoutAlign = "STRETCH";
    try { consultCard.layoutSizingHorizontal = "FILL"; } catch(e) {}
    consultCard.counterAxisSizingMode = "AUTO";

    const cTextWrap = figma.createFrame();
    cTextWrap.name = "CTA Text";
    cTextWrap.layoutMode = "VERTICAL";
    cTextWrap.itemSpacing = 8;
    cTextWrap.fills = [];
    consultCard.appendChild(cTextWrap);
    cTextWrap.layoutGrow = 1;
    try { cTextWrap.layoutSizingHorizontal = "FILL"; } catch(e) {}
    const cTitle = createStyledText("আপনার স্থানিক স্বপ্নের বাস্তব রূপ দিতে প্রস্তুত?", "Typography / Bengali / Card H3", 'text/primary');
    const cSub = createStyledText("ঢাকায় আমাদের প্রধান স্থপতিদের সাথে সরাসরি স্থানিক আলোচনা শুরু করুন।", "Typography / Bengali / Body Regular", 'text/secondary');
    cTextWrap.appendChild(cTitle);
    cTextWrap.appendChild(cSub);

    const cBtn = getBtn("পরামর্শের আবেদন করুন →");
    cBtn.name = "Consultation Action Button";
    consultCard.appendChild(cBtn);

    // Footer / Colophon: Full 1440px wide (FG-03 fix)
    const ftDt = figma.createFrame();
    ftDt.name = "Footer / Colophon";
    ftDt.layoutMode = "HORIZONTAL";
    ftDt.primaryAxisAlignItems = "SPACE_BETWEEN";
    ftDt.counterAxisAlignItems = "CENTER";
    ftDt.paddingLeft = 48;
    ftDt.paddingRight = 48;
    ftDt.paddingTop = 32;
    ftDt.paddingBottom = 32;
    bindFill(ftDt, 'text/primary');
    homeDt.appendChild(ftDt);
    ftDt.layoutAlign = "STRETCH";
    try { ftDt.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const bTxt = figma.createText();
    bTxt.textStyleId = styleMap["Typography / Latin / Brand Display"]?.id;
    bTxt.characters = "FlowGrid Architectural Studio";
    bTxt.textAutoResize = "WIDTH_AND_HEIGHT";
    bindFill(bTxt, 'surface/page');
    ftDt.appendChild(bTxt);

    const cTxt = figma.createText();
    cTxt.textStyleId = styleMap["Typography / Bengali / Body Small"]?.id;
    cTxt.characters = "© ২০২৬ FlowGrid Architectural Studio. বনানী, ঢাকা, বাংলাদেশ। সর্বস্বত্ব সংরক্ষিত।";
    cTxt.textAutoResize = "WIDTH_AND_HEIGHT";
    bindFill(cTxt, 'surface/mist');
    ftDt.appendChild(cTxt);


    // =========================================================================
    // 2. REPAIR BENGALI PROJECT DETAIL — 1440px DESKTOP (Node #18:221)
    // =========================================================================
    console.log("Repairing Bengali Project Detail 1440px Desktop...");
    const detailDt = desktopBnPage.children.find(c => c.name === "Bengali Project Detail — 1440px Desktop");
    detailDt.resize(1440, 100);
    detailDt.layoutMode = "VERTICAL";
    detailDt.primaryAxisSizingMode = "AUTO";
    detailDt.counterAxisSizingMode = "FIXED";
    bindFill(detailDt, 'surface/page');

    while (detailDt.children.length > 0) {
        detailDt.children[0].remove();
    }

    // Detail Header (cloned structure from home)
    const hDetail = hDt.clone();
    detailDt.appendChild(hDetail);

    // Detail Hero & Overview
    const dtHeroSec = figma.createFrame();
    dtHeroSec.name = "Section / Project Narrative & Specs";
    dtHeroSec.layoutMode = "VERTICAL";
    dtHeroSec.layoutAlign = "STRETCH";
    dtHeroSec.paddingLeft = 48;
    dtHeroSec.paddingRight = 48;
    dtHeroSec.paddingTop = 64;
    dtHeroSec.paddingBottom = 64;
    dtHeroSec.itemSpacing = 32;
    bindFill(dtHeroSec, 'surface/page');

    const dBadge = createStyledText("ধারণা স্টাডি ০১ · ধানমন্ডি, ঢাকা", "Typography / Bengali / Label Bold", 'accent/clay');
    const dTitle = createStyledText("ধানমন্ডি রেসিডেনশিয়াল অ্যাপার্টমেন্ট: প্রাকৃতিক আলো ও কাঠের পরিশীলিত বিন্যাস", "Typography / Bengali / Display H1", 'text/primary');
    const dStory = createStyledText(
        "ঢাকার ঘনবসতিপূর্ণ নাগরিক জীবনে শান্তি ও প্রশান্তির আবহ তৈরি করাই ছিল এই প্রকল্পের মূল দর্শন। লিভিং এবং ডাইনিং স্পেসের মধ্যে অপ্রয়োজনীয় দেয়ালের বাধা দূর করে প্রাকৃতিক বাতাসের চলাচলের অবাধ পথ সুগম করা হয়েছে। সিজনড মেহগনি কাঠের তৈরি ক্যাবিনেটরি এবং আধুনিক বায়োফিলিক উপাদানের মেলবন্ধনে একটি টেকসই ও মার্জিত স্থাপত্য পরিবেশ রচিত হয়েছে।",
        "Typography / Bengali / Body Large",
        'text/secondary'
    );
    dtHeroSec.appendChild(dBadge);
    dtHeroSec.appendChild(dTitle);
    dtHeroSec.appendChild(dStory);

    const dMainPhoto = createImageRect(imgOverviewHash, 1344, 600, 'radius/media');
    dMainPhoto.layoutAlign = "STRETCH";
    dtHeroSec.appendChild(dMainPhoto);
    detailDt.appendChild(dtHeroSec);

    // Secondary Views Grid (FG-04 fix: 660px cards, 440px photo height)
    const secViewsSec = figma.createFrame();
    secViewsSec.name = "Section / Secondary Spatial Perspectives";
    secViewsSec.layoutMode = "VERTICAL";
    secViewsSec.paddingLeft = 48;
    secViewsSec.paddingRight = 48;
    secViewsSec.paddingTop = 32;
    secViewsSec.paddingBottom = 64;
    secViewsSec.itemSpacing = 24;
    bindFill(secViewsSec, 'surface/page');
    detailDt.appendChild(secViewsSec);
    secViewsSec.layoutAlign = "STRETCH";
    try { secViewsSec.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const svGrid = figma.createFrame();
    svGrid.name = "Secondary Views & Joinery Craft";
    svGrid.layoutMode = "HORIZONTAL";
    svGrid.itemSpacing = 24;
    svGrid.fills = [];
    secViewsSec.appendChild(svGrid);
    svGrid.layoutAlign = "STRETCH";
    try { svGrid.layoutSizingHorizontal = "FILL"; } catch(e) {}
    svGrid.counterAxisSizingMode = "AUTO";

    // View 1
    const vCard1 = figma.createFrame();
    vCard1.name = "View / Dining Interaction";
    vCard1.layoutMode = "VERTICAL";
    vCard1.itemSpacing = 16;
    vCard1.paddingLeft = 24;
    vCard1.paddingRight = 24;
    vCard1.paddingTop = 24;
    vCard1.paddingBottom = 24;
    bindFill(vCard1, 'surface/clean');
    bindStroke(vCard1, 'border/decorative', 1);
    bindCornerRadius(vCard1, 'radius/control');
    svGrid.appendChild(vCard1);
    vCard1.layoutGrow = 1;
    try { vCard1.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const vImg1 = createImageRect(imgAltHash, 612, 440, 'radius/control');
    vCard1.appendChild(vImg1);
    vImg1.layoutAlign = "STRETCH";
    try { vImg1.layoutSizingHorizontal = "FILL"; } catch(e) {}
    const vCap1 = createStyledText("চিত্র ০২: ডাইনিং জোন ও লিভিং স্পেসের দৃশ্যমান মেলবন্ধন", "Typography / Bengali / Card H3", 'text/primary');
    const vDesc1 = createStyledText("উন্মুক্ত সার্কুলেশন করিডোর ডাইনিং এলাকাকে সরাসরি ব্যালকনির প্রাকৃতিক আলোর সাথে সংযুক্ত করে।", "Typography / Bengali / Body Regular", 'text/secondary');
    vCard1.appendChild(vCap1);
    vCard1.appendChild(vDesc1);

    // View 2
    const vCard2 = figma.createFrame();
    vCard2.name = "View / Joinery Craft";
    vCard2.layoutMode = "VERTICAL";
    vCard2.itemSpacing = 16;
    vCard2.paddingLeft = 24;
    vCard2.paddingRight = 24;
    vCard2.paddingTop = 24;
    vCard2.paddingBottom = 24;
    bindFill(vCard2, 'surface/clean');
    bindStroke(vCard2, 'border/decorative', 1);
    bindCornerRadius(vCard2, 'radius/control');
    svGrid.appendChild(vCard2);
    vCard2.layoutGrow = 1;
    try { vCard2.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const vImg2 = createImageRect(imgJoineryHash, 612, 440, 'radius/control');
    vCard2.appendChild(vImg2);
    vImg2.layoutAlign = "STRETCH";
    try { vImg2.layoutSizingHorizontal = "FILL"; } catch(e) {}
    const vCap2 = createStyledText("চিত্র ০৩: কাস্টম মিলওয়ার্ক ও সিজনড কাঠের নিপুণ সংযোগ", "Typography / Bengali / Card H3", 'text/primary');
    const vDesc2 = createStyledText("উচ্চ আর্দ্রতা প্রতিরোধক স্থানীয় কাঠের সঠিক ট্রিটমেন্ট এবং লুকায়িত মেকানিক্যাল জয়েন্ট।", "Typography / Bengali / Body Regular", 'text/secondary');
    vCard2.appendChild(vCap2);
    vCard2.appendChild(vDesc2);

    // Material Specifications Schedule (FG-04 fix)
    const matSec = figma.createFrame();
    matSec.name = "Material Schedule & Joinery Craft";
    matSec.layoutMode = "VERTICAL";
    matSec.paddingLeft = 48;
    matSec.paddingRight = 48;
    matSec.paddingTop = 48;
    matSec.paddingBottom = 64;
    matSec.itemSpacing = 24;
    bindFill(matSec, 'surface/page');
    detailDt.appendChild(matSec);
    matSec.layoutAlign = "STRETCH";
    try { matSec.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const matTitle = createStyledText("ম্যাটেরিয়াল স্পেসিফিকেশন ও নির্মাণ বিবরণী", "Typography / Bengali / Section H2", 'text/primary');
    matSec.appendChild(matTitle);

    const matTable = figma.createFrame();
    matTable.name = "Material Table";
    matTable.layoutMode = "VERTICAL";
    matTable.itemSpacing = 12;
    matTable.fills = [];
    matSec.appendChild(matTable);
    matTable.layoutAlign = "STRETCH";
    try { matTable.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const matItems = [
        { name: "কাঠের কাঠামো", spec: "সিজনড মেহগনি ও বার্মা সেগুন কাঠ, আর্দ্রতার মাত্রা ১২%-এ নিয়ন্ত্রিত।" },
        { name: "পৃষ্ঠতলের ফিনিশ", spec: "ইকো-ফ্রেন্ডলি জিরো-VOC ন্যাচারাল ম্যাট পলিউরেথেন কোটিং, দাগ-প্রতিরোধী ও টেকসই।" },
        { name: "লাইটিং সিস্টেম", spec: "২৭০০K উষ্ণ আর্কিটেকচারাল LED কোভ লাইটিং, ৯৫+ CRI কালার রেন্ডারিং ইনডেক্স।" },
        { name: "হার্ডওয়্যার ও ফিটিংস", spec: "জার্মান প্রযুক্তির হেভি ডিউটি কনসিল্ড কব্জা এবং সফট-ক্লোজ ড্রয়ার চ্যানেল।" }
    ];

    matItems.forEach(mi => {
        const row = figma.createFrame();
        row.name = "Row / " + mi.name;
        row.layoutMode = "HORIZONTAL";
        row.paddingLeft = 24;
        row.paddingRight = 24;
        row.paddingTop = 20;
        row.paddingBottom = 20;
        row.itemSpacing = 24;
        bindFill(row, 'surface/clean');
        bindStroke(row, 'border/decorative', 1);
        bindCornerRadius(row, 'radius/control');
        matTable.appendChild(row);
        row.layoutAlign = "STRETCH";
        try { row.layoutSizingHorizontal = "FILL"; } catch(e) {}
        row.counterAxisSizingMode = "AUTO";

        const col1 = createStyledText(mi.name, "Typography / Bengali / Label Bold", 'accent/clay', { hug: true });
        col1.resize(220, 24);

        const col2 = createStyledText(mi.spec, "Typography / Bengali / Body Regular", 'text/primary');

        row.appendChild(col1);
        row.appendChild(col2);
        col1.layoutGrow = 0;
        col2.layoutGrow = 1;
        try {
            col1.layoutSizingHorizontal = "FIXED";
            col2.layoutSizingHorizontal = "FILL";
        } catch(e) {}
    });

    // Bottom CTA & Footer
    const dtBottomCta = consultSec.clone();
    detailDt.appendChild(dtBottomCta);
    dtBottomCta.layoutAlign = "STRETCH";
    try { dtBottomCta.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const dtBottomFt = ftDt.clone();
    detailDt.appendChild(dtBottomFt);
    dtBottomFt.layoutAlign = "STRETCH";
    try { dtBottomFt.layoutSizingHorizontal = "FILL"; } catch(e) {}


    // =========================================================================
    // 3. REPAIR BENGALI HOMEPAGE — 390px MOBILE (Node #18:283)
    // =========================================================================
    console.log("Repairing Bengali Homepage 390px Mobile...");
    const homeMb = mobileBnPage.children.find(c => c.name.startsWith("Bengali Homepage"));
    homeMb.resize(390, 100);
    homeMb.layoutMode = "VERTICAL";
    homeMb.primaryAxisSizingMode = "AUTO";
    homeMb.counterAxisSizingMode = "FIXED";
    bindFill(homeMb, 'surface/page');

    while (homeMb.children.length > 0) {
        homeMb.children[0].remove();
    }

    // Mobile Header
    const hMb = figma.createFrame();
    hMb.name = "Header / Navigation";
    hMb.layoutMode = "HORIZONTAL";
    hMb.primaryAxisAlignItems = "SPACE_BETWEEN";
    hMb.counterAxisAlignItems = "CENTER";
    hMb.layoutAlign = "STRETCH";
    hMb.resize(390, 64);
    hMb.paddingLeft = 16;
    hMb.paddingRight = 16;
    bindFill(hMb, 'surface/page');
    bindStroke(hMb, 'border/decorative', 1);

    const bMbLogo = figma.createText();
    bMbLogo.textStyleId = styleMap["Typography / Latin / Brand Display"]?.id;
    bMbLogo.characters = "FlowGrid";
    bMbLogo.textAutoResize = "WIDTH_AND_HEIGHT";
    bindFill(bMbLogo, 'text/primary');
    hMb.appendChild(bMbLogo);

    const burgerMb = figma.createFrame();
    burgerMb.name = "Hamburger Button";
    burgerMb.resize(48, 48);
    burgerMb.layoutMode = "HORIZONTAL";
    burgerMb.primaryAxisAlignItems = "CENTER";
    burgerMb.counterAxisAlignItems = "CENTER";
    bindFill(burgerMb, 'surface/clean');
    bindStroke(burgerMb, 'border/control', 1);
    bindCornerRadius(burgerMb, 'radius/control');
    const bIcon = figma.createText();
    bIcon.fontName = { family: "Inter", style: "Bold" };
    bIcon.fontSize = 18;
    bIcon.characters = "☰";
    bindFill(bIcon, 'text/primary');
    burgerMb.appendChild(bIcon);
    hMb.appendChild(burgerMb);
    homeMb.appendChild(hMb);

    // Mobile Hero Section (FG-01 fix: full textAutoResize = HEIGHT, no clipping)
    const mbHeroSec = figma.createFrame();
    mbHeroSec.name = "Section / Hero Architectural Showcase";
    mbHeroSec.layoutMode = "VERTICAL";
    mbHeroSec.layoutAlign = "STRETCH";
    mbHeroSec.paddingLeft = 16;
    mbHeroSec.paddingRight = 16;
    mbHeroSec.paddingTop = 32;
    mbHeroSec.paddingBottom = 40;
    mbHeroSec.itemSpacing = 20;
    bindFill(mbHeroSec, 'surface/page');

    const mbBadge = createStyledText("ধারণা স্টাডি ০১ · ধানমন্ডি, ঢাকা", "Typography / Bengali / Label Bold", 'accent/clay');
    const mbTitle = createStyledText("প্রকৃতি, আলো ও কাঠের সুষম মেলবন্ধন", "Typography / Bengali / Display H1", 'text/primary');
    const mbLead = createStyledText(
        "একটি অ্যাপার্টমেন্টের সৌন্দর্য কেবল আসবাবে নয়, বরং এর সামগ্রিক অনুভূতিতে নিহিত। ঢাকার আবহাওয়ায় প্রাকৃতিক বাতাস ও উষ্ণ আলোর প্রতিফলন নিশ্চিত করে একটি প্রশান্ত পরিবেশ তৈরির স্থানিক পরিকল্পনা।",
        "Typography / Bengali / Body Regular",
        'text/secondary'
    );
    mbHeroSec.appendChild(mbBadge);
    mbHeroSec.appendChild(mbTitle);
    mbHeroSec.appendChild(mbLead);

    const mbHeroImg = createImageRect(imgOverviewHash, 358, 220, 'radius/control');
    mbHeroImg.layoutAlign = "STRETCH";
    mbHeroSec.appendChild(mbHeroImg);

    const mbCtaBtn = getBtn("পরামর্শের আবেদন করুন →");
    mbCtaBtn.name = "Hero Mobile CTA";
    mbCtaBtn.layoutAlign = "STRETCH";
    mbHeroSec.appendChild(mbCtaBtn);
    homeMb.appendChild(mbHeroSec);

    // Mobile Narrative Section
    const mbNarSec = figma.createFrame();
    mbNarSec.name = "Section / Spatial Sequence & Material Craft";
    mbNarSec.layoutMode = "VERTICAL";
    mbNarSec.layoutAlign = "STRETCH";
    mbNarSec.paddingLeft = 16;
    mbNarSec.paddingRight = 16;
    mbNarSec.paddingTop = 32;
    mbNarSec.paddingBottom = 40;
    mbNarSec.itemSpacing = 20;
    bindFill(mbNarSec, 'surface/page');

    const mbNarHead = createStyledText("বসবাসের স্বাচ্ছন্দ্য ও স্থানিক বিন্যাস", "Typography / Bengali / Section H2", 'text/primary');
    mbNarSec.appendChild(mbNarHead);

    // Card 1
    const mbC1 = figma.createFrame();
    mbC1.name = "Card / Angle 02";
    mbC1.layoutMode = "VERTICAL";
    mbC1.layoutAlign = "STRETCH";
    mbC1.itemSpacing = 12;
    mbC1.paddingLeft = 16;
    mbC1.paddingRight = 16;
    mbC1.paddingTop = 16;
    mbC1.paddingBottom = 16;
    bindFill(mbC1, 'surface/clean');
    bindStroke(mbC1, 'border/decorative', 1);
    bindCornerRadius(mbC1, 'radius/control');

    const mbImg1 = createImageRect(imgAltHash, 326, 200, 'radius/control');
    mbImg1.layoutAlign = "STRETCH";
    mbC1.appendChild(mbImg1);
    const mbCap1 = createStyledText("ডাইনিং ও বারান্দার খোলামেলা সংযোগ", "Typography / Bengali / Card H3", 'text/primary');
    const mbDesc1 = createStyledText("স্বাভাবিক আলো ও ছায়ার পরিশীলিত ভারসাম্য বজায় রেখে উন্মুক্ত স্থানিক অনুভূতি তৈরি।", "Typography / Bengali / Body Small", 'text/secondary');
    mbC1.appendChild(mbCap1);
    mbC1.appendChild(mbDesc1);
    mbNarSec.appendChild(mbC1);

    // Card 2
    const mbC2 = figma.createFrame();
    mbC2.name = "Card / Angle 03";
    mbC2.layoutMode = "VERTICAL";
    mbC2.layoutAlign = "STRETCH";
    mbC2.itemSpacing = 12;
    mbC2.paddingLeft = 16;
    mbC2.paddingRight = 16;
    mbC2.paddingTop = 16;
    mbC2.paddingBottom = 16;
    bindFill(mbC2, 'surface/clean');
    bindStroke(mbC2, 'border/decorative', 1);
    bindCornerRadius(mbC2, 'radius/control');

    const mbImg2 = createImageRect(imgJoineryHash, 326, 200, 'radius/control');
    mbImg2.layoutAlign = "STRETCH";
    mbC2.appendChild(mbImg2);
    const mbCap2 = createStyledText("কাস্টম কাঠের সূক্ষ্ম কারুকাজ", "Typography / Bengali / Card H3", 'text/primary');
    const mbDesc2 = createStyledText("স্থানীয় কাঠের মিস্ত্রিদের ঐতিহ্যবাহী দক্ষতার সাথে আধুনিক আর্কিটেকচারাল ফিনিশের সমন্বয়।", "Typography / Bengali / Body Small", 'text/secondary');
    mbC2.appendChild(mbCap2);
    mbC2.appendChild(mbDesc2);
    mbNarSec.appendChild(mbC2);
    homeMb.appendChild(mbNarSec);

    // Mobile Services Section
    const mbSvcSec = figma.createFrame();
    mbSvcSec.name = "Section / Studio Services";
    mbSvcSec.layoutMode = "VERTICAL";
    mbSvcSec.layoutAlign = "STRETCH";
    mbSvcSec.paddingLeft = 16;
    mbSvcSec.paddingRight = 16;
    mbSvcSec.paddingTop = 32;
    mbSvcSec.paddingBottom = 40;
    mbSvcSec.itemSpacing = 16;
    bindFill(mbSvcSec, 'surface/page');

    const mbSvcHead = createStyledText("আমাদের স্থাপত্য সেবাসমূহ", "Typography / Bengali / Section H2", 'text/primary');
    mbSvcSec.appendChild(mbSvcHead);

    svcCards.forEach(c => {
        const sc = figma.createFrame();
        sc.name = "Mobile Service " + c.num;
        sc.layoutMode = "VERTICAL";
        sc.layoutAlign = "STRETCH";
        sc.itemSpacing = 8;
        sc.paddingLeft = 16;
        sc.paddingRight = 16;
        sc.paddingTop = 16;
        sc.paddingBottom = 16;
        bindFill(sc, 'surface/clean');
        bindStroke(sc, 'border/decorative', 1);
        bindCornerRadius(sc, 'radius/control');

        const numTxt = createStyledText(c.num, "Typography / Bengali / Label Bold", 'accent/clay');
        const titTxt = createStyledText(c.title, "Typography / Bengali / Card H3", 'text/primary');
        const descTxt = createStyledText(c.desc, "Typography / Bengali / Body Small", 'text/secondary');
        sc.appendChild(numTxt);
        sc.appendChild(titTxt);
        sc.appendChild(descTxt);
        mbSvcSec.appendChild(sc);
    });
    homeMb.appendChild(mbSvcSec);

    // Mobile Footer
    const mbFt = figma.createFrame();
    mbFt.name = "Footer / Colophon";
    mbFt.layoutMode = "VERTICAL";
    mbFt.layoutAlign = "STRETCH";
    mbFt.paddingLeft = 16;
    mbFt.paddingRight = 16;
    mbFt.paddingTop = 24;
    mbFt.paddingBottom = 24;
    mbFt.itemSpacing = 8;
    bindFill(mbFt, 'text/primary');

    const mbFtTitle = createStyledText("FlowGrid Architectural Studio", "Typography / Latin / Card H3", 'surface/page');
    const mbFtCopy = createStyledText("© ২০২৬ FlowGrid Architectural Studio. বনানী, ঢাকা, বাংলাদেশ।", "Typography / Bengali / Body Small", 'surface/mist');
    mbFt.appendChild(mbFtTitle);
    mbFt.appendChild(mbFtCopy);
    homeMb.appendChild(mbFt);


    // =========================================================================
    // 4. REPAIR BENGALI PROJECT DETAIL — 390px MOBILE (Node #18:339)
    // =========================================================================
    console.log("Repairing Bengali Project Detail 390px Mobile...");
    const detailMb = mobileBnPage.children.find(c => c.name.startsWith("Bengali Project Detail"));
    detailMb.resize(390, 100);
    detailMb.layoutMode = "VERTICAL";
    detailMb.primaryAxisSizingMode = "AUTO";
    detailMb.counterAxisSizingMode = "FIXED";
    bindFill(detailMb, 'surface/page');

    while (detailMb.children.length > 0) {
        detailMb.children[0].remove();
    }

    // Detail Header
    const mbDetailH = hMb.clone();
    detailMb.appendChild(mbDetailH);

    // Detail Content (FG-02 fix: textAutoResize = HEIGHT, no clipped specs)
    const mbDetSec = figma.createFrame();
    mbDetSec.name = "Section / Project Narrative & Specs";
    mbDetSec.layoutMode = "VERTICAL";
    mbDetSec.layoutAlign = "STRETCH";
    mbDetSec.paddingLeft = 16;
    mbDetSec.paddingRight = 16;
    mbDetSec.paddingTop = 32;
    mbDetSec.paddingBottom = 40;
    mbDetSec.itemSpacing = 20;
    bindFill(mbDetSec, 'surface/page');

    const mdBadge = createStyledText("ধারণা স্টাডি ০১ · ধানমন্ডি, ঢাকা", "Typography / Bengali / Label Bold", 'accent/clay');
    const mdTitle = createStyledText("ধানমন্ডি রেসিডেনশিয়াল অ্যাপার্টমেন্ট", "Typography / Bengali / Section H2", 'text/primary');
    const mdLead = createStyledText(
        "প্রাকৃতিক আলো ও বাতাসের সঞ্চালন বাড়িয়ে একটি শান্ত ও আরামদায়ক পরিবেশ তৈরি করা হয়েছে। কাঠের সূক্ষ্ম কারুকাজ এবং খোলামেলা স্থানিক বিন্যাসের মাধ্যমে পরিবেশবান্ধব নকশার প্রতিফলন।",
        "Typography / Bengali / Body Regular",
        'text/secondary'
    );
    mbDetSec.appendChild(mdBadge);
    mbDetSec.appendChild(mdTitle);
    mbDetSec.appendChild(mdLead);

    const mdMainPhoto = createImageRect(imgOverviewHash, 358, 220, 'radius/control');
    mdMainPhoto.layoutAlign = "STRETCH";
    mbDetSec.appendChild(mdMainPhoto);
    detailMb.appendChild(mbDetSec);

    // Mobile Gallery Cards
    const mbGalSec = figma.createFrame();
    mbGalSec.name = "Section / Multi-Angle Visuals";
    mbGalSec.layoutMode = "VERTICAL";
    mbGalSec.layoutAlign = "STRETCH";
    mbGalSec.paddingLeft = 16;
    mbGalSec.paddingRight = 16;
    mbGalSec.paddingTop = 16;
    mbGalSec.paddingBottom = 32;
    mbGalSec.itemSpacing = 16;
    bindFill(mbGalSec, 'surface/page');

    // Photo 1
    const gp1 = createImageRect(imgAltHash, 358, 220, 'radius/control');
    gp1.layoutAlign = "STRETCH";
    const gp1Cap = createStyledText("চিত্র ০২: ডাইনিং জোন ও লিভিং স্পেসের সমন্বয়", "Typography / Bengali / Card H3", 'text/primary');
    mbGalSec.appendChild(gp1);
    mbGalSec.appendChild(gp1Cap);

    // Photo 2
    const gp2 = createImageRect(imgJoineryHash, 358, 220, 'radius/control');
    gp2.layoutAlign = "STRETCH";
    const gp2Cap = createStyledText("চিত্র ০৩: কাস্টম কাঠের আসবাব ও ফিনিশ", "Typography / Bengali / Card H3", 'text/primary');
    mbGalSec.appendChild(gp2);
    mbGalSec.appendChild(gp2Cap);
    detailMb.appendChild(mbGalSec);

    // Mobile Specs List (FG-02 fix: clean full-width cards with textAutoResize = HEIGHT)
    const mbSpecSec = figma.createFrame();
    mbSpecSec.name = "Section / Architectural Specifications";
    mbSpecSec.layoutMode = "VERTICAL";
    mbSpecSec.layoutAlign = "STRETCH";
    mbSpecSec.paddingLeft = 16;
    mbSpecSec.paddingRight = 16;
    mbSpecSec.paddingTop = 16;
    mbSpecSec.paddingBottom = 32;
    mbSpecSec.itemSpacing = 12;
    bindFill(mbSpecSec, 'surface/page');

    const specSecTitle = createStyledText("প্রকল্পের বিস্তারিত বিবরণী", "Typography / Bengali / Section H2", 'text/primary');
    mbSpecSec.appendChild(specSecTitle);

    matItems.forEach(mi => {
        const sc = figma.createFrame();
        sc.name = "Spec Card / " + mi.name;
        sc.layoutMode = "VERTICAL";
        sc.layoutAlign = "STRETCH";
        sc.itemSpacing = 6;
        sc.paddingLeft = 16;
        sc.paddingRight = 16;
        sc.paddingTop = 14;
        sc.paddingBottom = 14;
        bindFill(sc, 'surface/clean');
        bindStroke(sc, 'border/decorative', 1);
        bindCornerRadius(sc, 'radius/control');

        const col1 = createStyledText(mi.name, "Typography / Bengali / Label Bold", 'accent/clay');
        const col2 = createStyledText(mi.spec, "Typography / Bengali / Body Small", 'text/primary');
        sc.appendChild(col1);
        sc.appendChild(col2);
        mbSpecSec.appendChild(sc);
    });
    detailMb.appendChild(mbSpecSec);

    // Mobile Detail Bottom CTA
    const mbDetCtaSec = figma.createFrame();
    mbDetCtaSec.name = "Mobile Detail CTA";
    mbDetCtaSec.layoutMode = "VERTICAL";
    mbDetCtaSec.layoutAlign = "STRETCH";
    mbDetCtaSec.paddingLeft = 16;
    mbDetCtaSec.paddingRight = 16;
    mbDetCtaSec.paddingTop = 16;
    mbDetCtaSec.paddingBottom = 32;
    mbDetCtaSec.itemSpacing = 12;
    bindFill(mbDetCtaSec, 'surface/page');

    const mbDetCta = getBtn("এই কনসেপ্টের ভিত্তিতে পরামর্শ নিন →");
    mbDetCta.layoutAlign = "STRETCH";
    mbDetCtaSec.appendChild(mbDetCta);
    detailMb.appendChild(mbDetCtaSec);

    // Mobile Footer
    const mbDetFt = mbFt.clone();
    detailMb.appendChild(mbDetFt);

    console.log("Four principal screens repaired successfully!");
    return {
        ok: true,
        homeDesktopId: homeDt.id,
        detailDesktopId: detailDt.id,
        homeMobileId: homeMb.id,
        detailMobileId: detailMb.id
    };
})()
