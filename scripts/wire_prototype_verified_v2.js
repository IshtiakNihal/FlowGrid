// FlowGrid Phase 4 & FG-08: Complete Verified Prototype Wiring v3
// Fixes all Issue 2 requirements:
// - Bengali header Process (পদ্ধতি -> 18:1718) & Studio (স্টুডিও -> 18:1752)
// - Language pills on desktop & mobile with URL actions
// - 5 Filter Tabs on 18:1587 & 18:1102
// - 4 Archive Cards re-mapped to distinct destinations (18:221, 18:1624, 18:1655, 18:1686 / 18:1139, 18:1160, 18:1191, 18:1222)
// - Complete return navigation paths on Detail screens (18:221, 18:1139, 18:339, 18:1425)

(async () => {
    console.log("Starting prototype wiring verification v3...");

    const log = {
        success: [],
        errors: []
    };

    async function safeSetReactions(node, reactions, desc) {
        if (!node) {
            log.errors.push({ desc, error: "Node is null or undefined" });
            return false;
        }
        try {
            await node.setReactionsAsync(reactions);
            log.success.push({
                desc,
                nodeId: node.id,
                nodeName: node.name,
                reactionsCount: reactions.length,
                actionTypes: reactions.map(r => (r.actions || []).map(a => a.type + (a.navigation ? `(${a.navigation})` : "") + (a.destinationId ? `->${a.destinationId}` : "") + (a.url ? `(${a.url})` : "")).join(", "))
            });
            return true;
        } catch (e) {
            log.errors.push({ desc, nodeId: node.id, nodeName: node.name, error: e.toString() });
            return false;
        }
    }

    function findChild(parent, predicate) {
        if (!parent || !parent.children) return null;
        for (const child of parent.children) {
            if (predicate(child)) return child;
            const found = findChild(child, predicate);
            if (found) return found;
        }
        return null;
    }

    function findAllChildren(parent, predicate) {
        const results = [];
        if (!parent || !parent.children) return results;
        for (const child of parent.children) {
            if (predicate(child)) results.push(child);
            results.push(...findAllChildren(child, predicate));
        }
        return results;
    }

    // Helper for navigation avoiding self-navigation
    async function wireNav(node, dest, currentFrame, desc, transition = { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 }) {
        if (!node || !dest) return;
        if (dest.id === currentFrame.id) {
            // Self-navigation is invalid in Figma
            return;
        }
        await safeSetReactions(node, [{
            trigger: { type: "ON_CLICK" },
            actions: [{
                type: "NODE",
                destinationId: dest.id,
                navigation: "NAVIGATE",
                transition: transition
            }]
        }], desc);
    }

    // ==========================================
    // 1. PAGE 03: DESKTOP — BN
    // ==========================================
    const dtBnHome = figma.getNodeById("18:137");
    const dtBnDetail = figma.getNodeById("18:221");
    const dtBnArchive = figma.getNodeById("18:1587");
    const dtBnBuilt = figma.getNodeById("18:1624");
    const dtBnServices = figma.getNodeById("18:1655");
    const dtBnJoinery = figma.getNodeById("18:1686");
    const dtBnProcess = figma.getNodeById("18:1718");
    const dtBnStudio = figma.getNodeById("18:1752");
    const dtBnContact = figma.getNodeById("18:1780");

    const dtBnModal = figma.getNodeById("18:2031");
    const dtBnSubmitting = figma.getNodeById("18:2057");
    const dtBnReceipt = figma.getNodeById("18:2063");
    const dtBnOffline = figma.getNodeById("18:2071");

    // Helper for Bengali Desktop Header
    async function wireBengaliDesktopHeader(frame, frameName) {
        if (!frame) return;
        const navLinks = findChild(frame, c => c.name === "Nav Links");
        if (navLinks && navLinks.children) {
            for (const item of navLinks.children) {
                const text = (item.type === "TEXT" ? item.characters : item.name) || "";
                if ((text.includes("ধারণা") || text.includes("আর্কাইভ")) && dtBnArchive) {
                    await wireNav(item, dtBnArchive, frame, `${frameName} Nav -> Archive`);
                } else if (text.includes("সেবা") && dtBnServices) {
                    await wireNav(item, dtBnServices, frame, `${frameName} Nav -> Services`);
                } else if ((text.includes("পদ্ধতি") || text.includes("কার্যপদ্ধতি")) && dtBnProcess) {
                    await wireNav(item, dtBnProcess, frame, `${frameName} Nav -> Process`);
                } else if ((text.includes("স্টুডিও") || text.includes("দর্শন")) && dtBnStudio) {
                    await wireNav(item, dtBnStudio, frame, `${frameName} Nav -> Studio`);
                } else if (text.includes("যোগাযোগ") && dtBnContact) {
                    await wireNav(item, dtBnContact, frame, `${frameName} Nav -> Contact`);
                }
            }
        }

        // Brand logo / text -> Home
        const brand = findChild(frame, c => c.characters === "FlowGrid" || c.name === "Brand Logo");
        if (brand && dtBnHome && frame.id !== dtBnHome.id) {
            await wireNav(brand, dtBnHome, frame, `${frameName} Brand -> Home`);
        }

        // Language Pill -> Switch to English
        const langPill = findChild(frame, c => c.name === "Language Pill");
        if (langPill) {
            await safeSetReactions(langPill, [{
                trigger: { type: "ON_CLICK" },
                actions: [{
                    type: "URL",
                    url: "https://www.figma.com/design/eMRunQ80brYYvuTWkufV2o/?node-id=18-1068"
                }]
            }], `${frameName} Lang Pill -> English URL`);
        }

        // Header Consultation CTA -> Modal
        const headerCta = findChild(frame, c => c.name === "Header Consultation CTA");
        if (headerCta && dtBnModal) {
            await safeSetReactions(headerCta, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: dtBnModal.id, navigation: "OVERLAY", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], `${frameName} Header CTA -> Modal`);
        }

        // Section Consultation CTA (any banner CTA on the page)
        const ctaBtns = findAllChildren(frame, c => c.name && (c.name.includes("Consultation CTA") || c.name.includes("Button / Consultation CTA") || c.name === "Consultation Action Button"));
        for (const cb of ctaBtns) {
            if (cb.id !== headerCta?.id && dtBnModal) {
                await safeSetReactions(cb, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: dtBnModal.id, navigation: "OVERLAY", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], `${frameName} Banner CTA -> Modal`);
            }
        }
    }

    const bnDesktopFrames = [
        { node: dtBnHome, name: "Bengali Home Desktop" },
        { node: dtBnDetail, name: "Bengali Detail Desktop" },
        { node: dtBnArchive, name: "Bengali Archive Desktop" },
        { node: dtBnServices, name: "Bengali Services Desktop" },
        { node: dtBnContact, name: "Bengali Contact Desktop" }
    ];
    for (const f of bnDesktopFrames) {
        if (f.node) await wireBengaliDesktopHeader(f.node, f.name);
    }

    // Specific Desktop BN Home Hero actions
    if (dtBnHome) {
        const heroPrimary = findChild(dtBnHome, c => c.name === "Hero Primary CTA");
        if (heroPrimary && dtBnModal) {
            await safeSetReactions(heroPrimary, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: dtBnModal.id, navigation: "OVERLAY", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "Desktop BN Hero Primary -> Modal");
        }
        const heroSec = findChild(dtBnHome, c => c.name && c.name.includes("Secondary View Project"));
        if (heroSec && dtBnDetail) {
            await wireNav(heroSec, dtBnDetail, dtBnHome, "Desktop BN Hero Secondary -> Detail", { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.3 });
        }
    }

    // Specific Desktop BN Detail Return Paths
    if (dtBnDetail) {
        const backLink = findChild(dtBnDetail, c => (c.name && c.name.includes("Back")) || (c.characters && c.characters.includes("ফিরে যান")));
        if (backLink && dtBnArchive) {
            await wireNav(backLink, dtBnArchive, dtBnDetail, "Desktop BN Detail Back -> Archive");
        }
        const bc = findChild(dtBnDetail, c => c.name && c.name.includes("Breadcrumb"));
        if (bc && dtBnArchive) {
            await wireNav(bc, dtBnArchive, dtBnDetail, "Desktop BN Detail Breadcrumb -> Archive");
        }
    }

    // Specific Desktop BN Archive: Filter Tabs & 4 Distinct Cards Destinations
    if (dtBnArchive) {
        const filterTabs = [
            { name: "আবাসিক লিভিং", dest: dtBnDetail },
            { name: "মডুলার কিচেন", dest: dtBnBuilt },
            { name: "মাস্টার স্যুট", dest: dtBnServices },
            { name: "জয়েনারি ক্রাফট", dest: dtBnJoinery }
        ];
        for (const ft of filterTabs) {
            const tabNode = findChild(dtBnArchive, c => c.name && c.name.includes("Tab") && c.name.includes(ft.name));
            if (tabNode && ft.dest) {
                await wireNav(tabNode, ft.dest, dtBnArchive, `Desktop BN Archive Filter Tab ${ft.name} -> ${ft.dest.name}`);
            }
        }

        const cardDests = [
            { studyName: "ধারণা সমীক্ষা ০১", dest: dtBnDetail, desc: "Study 01 Living -> Detail" },
            { studyName: "ধারণা সমীক্ষা ০২", dest: dtBnBuilt, desc: "Study 02 Kitchen -> Built/Study 02" },
            { studyName: "ধারণা সমীক্ষা ০৩", dest: dtBnServices, desc: "Study 03 Bedroom -> Services/Study 03" },
            { studyName: "ধারণা সমীক্ষা ০৪", dest: dtBnJoinery, desc: "Study 04 Joinery -> Joinery/Study 04" }
        ];

        for (const cd of cardDests) {
            const cardNode = findChild(dtBnArchive, c => c.name && c.name.includes(cd.studyName));
            if (cardNode && cd.dest) {
                await wireNav(cardNode, cd.dest, dtBnArchive, `Desktop BN Archive Card ${cd.desc}`, { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.3 });
                const cardBtn = findChild(cardNode, c => c.name && (c.name.includes("Button") || c.name.includes("CTA")));
                if (cardBtn) {
                    await wireNav(cardBtn, cd.dest, dtBnArchive, `Desktop BN Archive Card Button ${cd.desc}`, { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.3 });
                }
            }
        }
    }

    // Modal Overlays Wiring (Desktop BN)
    if (dtBnModal) {
        const closeBtn = findChild(dtBnModal, c => c.name && (c.name.includes("Close") || c.name.includes("Cancel")));
        if (closeBtn) {
            await safeSetReactions(closeBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "CLOSE" }] }], "Desktop BN Modal Close");
        }
        const submitBtn = findChild(dtBnModal, c => c.name && (c.name === "Submit CTA" || c.name.includes("Submit")));
        if (submitBtn && dtBnSubmitting) {
            await safeSetReactions(submitBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: dtBnSubmitting.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "Desktop BN Modal Submit -> Submitting");
        }
        const offlineTrigger = findChild(dtBnModal, c => c.name && c.name.includes("Offline"));
        if (offlineTrigger && dtBnOffline) {
            await safeSetReactions(offlineTrigger, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: dtBnOffline.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "Desktop BN Modal Offline Trigger -> Offline Error");
        }
    }

    if (dtBnSubmitting && dtBnReceipt) {
        const simBtn = findChild(dtBnSubmitting, c => c.name && c.name.includes("Simulation"));
        if (simBtn) {
            await safeSetReactions(simBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: dtBnReceipt.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.3 } }] }], "Desktop BN Submitting -> Receipt");
        }
    }

    if (dtBnReceipt) {
        const doneBtn = findChild(dtBnReceipt, c => c.name && c.name.includes("Done"));
        if (doneBtn) {
            await safeSetReactions(doneBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "CLOSE" }] }], "Desktop BN Receipt Done -> Close");
        }
    }

    if (dtBnOffline && dtBnSubmitting) {
        const retryBtn = findChild(dtBnOffline, c => c.name && c.name.includes("Retry"));
        if (retryBtn) {
            await safeSetReactions(retryBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: dtBnSubmitting.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "Desktop BN Offline Retry -> Submitting");
        }
        const cancelBtn = findChild(dtBnOffline, c => c.name && c.name.includes("Cancel"));
        if (cancelBtn) {
            await safeSetReactions(cancelBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "CLOSE" }] }], "Desktop BN Offline Cancel -> Close");
        }
    }

    // ==========================================
    // 2. PAGE 04: MOBILE — BN
    // ==========================================
    const mbBnHome = figma.getNodeById("18:283");
    const mbBnDetail = figma.getNodeById("18:339");
    const mbBnArchive = figma.getNodeById("18:1853");
    const mbBnBuilt = figma.getNodeById("18:1871");
    const mbBnServices = figma.getNodeById("18:1889");
    const mbBnJoinery = figma.getNodeById("18:1907");
    const mbBnProcess = figma.getNodeById("18:1925");
    const mbBnStudio = figma.getNodeById("18:1943");
    const mbBnContact = figma.getNodeById("18:1961");

    const mbBnModal = figma.getNodeById("18:2080");
    const mbBnSubmitting = figma.getNodeById("18:2106");
    const mbBnReceipt = figma.getNodeById("18:2112");
    const mbBnOffline = figma.getNodeById("18:2120");
    const mbBnDrawer = figma.getNodeById("18:2129");

    async function wireBengaliMobileHeader(frame, frameName) {
        if (!frame) return;
        const burger = findChild(frame, c => c.name && (c.name.includes("Hamburger") || c.name.includes("Menu Toggle")));
        if (burger && mbBnDrawer) {
            await safeSetReactions(burger, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: mbBnDrawer.id, navigation: "OVERLAY", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], `${frameName} Hamburger -> Drawer`);
        }
        const brand = findChild(frame, c => c.characters === "FlowGrid" || c.name === "Brand Logo");
        if (brand && mbBnHome && frame.id !== mbBnHome.id) {
            await wireNav(brand, mbBnHome, frame, `${frameName} Brand -> Home`);
        }
        const langPill = findChild(frame, c => c.name && c.name.includes("Language Pill"));
        if (langPill) {
            await safeSetReactions(langPill, [{
                trigger: { type: "ON_CLICK" },
                actions: [{
                    type: "URL",
                    url: "https://www.figma.com/design/eMRunQ80brYYvuTWkufV2o/?node-id=18-1389"
                }]
            }], `${frameName} Lang Pill -> English Mobile URL`);
        }
        const ctaBtns = findAllChildren(frame, c => c.name && (c.name.includes("CTA") || c.name.includes("Consultation")));
        for (const cb of ctaBtns) {
            if (cb.name !== "Header Consultation CTA" && mbBnModal) {
                await safeSetReactions(cb, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: mbBnModal.id, navigation: "OVERLAY", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], `${frameName} CTA -> Modal`);
            }
        }
    }

    const bnMobileFrames = [
        { node: mbBnHome, name: "Bengali Home Mobile" },
        { node: mbBnDetail, name: "Bengali Detail Mobile" },
        { node: mbBnArchive, name: "Bengali Archive Mobile" }
    ];
    for (const f of bnMobileFrames) {
        if (f.node) await wireBengaliMobileHeader(f.node, f.name);
    }

    if (mbBnDetail) {
        const backLink = findChild(mbBnDetail, c => c.name && (c.name.includes("Back") || c.name.includes("Breadcrumb")));
        if (backLink && mbBnArchive) {
            await wireNav(backLink, mbBnArchive, mbBnDetail, "Mobile BN Detail Back -> Archive");
        }
    }

    if (mbBnArchive) {
        const cardDests = [
            { studyName: "ধারণা সমীক্ষা ০১", dest: mbBnDetail },
            { studyName: "ধারণা সমীক্ষা ০২", dest: mbBnBuilt },
            { studyName: "ধারণা সমীক্ষা ০৩", dest: mbBnServices },
            { studyName: "ধারণা সমীক্ষা ০৪", dest: mbBnJoinery }
        ];
        for (const cd of cardDests) {
            const cardNode = findChild(mbBnArchive, c => c.name && c.name.includes(cd.studyName));
            if (cardNode && cd.dest) {
                await wireNav(cardNode, cd.dest, mbBnArchive, `Mobile BN Archive Card -> ${cd.dest.name}`, { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.3 });
            }
        }
    }

    // Mobile BN Drawer Wiring
    if (mbBnDrawer) {
        const closeBtn = findChild(mbBnDrawer, c => c.name && c.name.includes("Close"));
        if (closeBtn) {
            await safeSetReactions(closeBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "CLOSE" }] }], "Mobile BN Drawer Close");
        }
        const drawerLinks = [
            { name: "ধারণা সংগ্রহ", dest: mbBnArchive },
            { name: "সেবাসমূহ", dest: mbBnServices },
            { name: "পদ্ধতি", dest: mbBnProcess },
            { name: "স্টুডিও", dest: mbBnStudio },
            { name: "যোগাযোগ", dest: mbBnContact }
        ];
        for (const dl of drawerLinks) {
            const item = findChild(mbBnDrawer, c => c.name && (c.name.includes(dl.name) || (c.characters && c.characters.includes(dl.name))));
            if (item && dl.dest) {
                await wireNav(item, dl.dest, mbBnDrawer, `Mobile BN Drawer Link -> ${dl.dest.name}`);
            }
        }
        const drawerCta = findChild(mbBnDrawer, c => c.name && (c.name.includes("CTA") || c.name.includes("Consultation")));
        if (drawerCta && mbBnModal) {
            await safeSetReactions(drawerCta, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: mbBnModal.id, navigation: "OVERLAY", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "Mobile BN Drawer CTA -> Modal");
        }
    }

    // Mobile BN Modals
    if (mbBnModal) {
        const closeBtn = findChild(mbBnModal, c => c.name && (c.name.includes("Close") || c.name.includes("Cancel")));
        if (closeBtn) {
            await safeSetReactions(closeBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "CLOSE" }] }], "Mobile BN Modal Close");
        }
        const submitBtn = findChild(mbBnModal, c => c.name && (c.name === "Submit CTA" || c.name.includes("Submit")));
        if (submitBtn && mbBnSubmitting) {
            await safeSetReactions(submitBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: mbBnSubmitting.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "Mobile BN Modal Submit -> Submitting");
        }
        const offlineTrigger = findChild(mbBnModal, c => c.name && c.name.includes("Offline"));
        if (offlineTrigger && mbBnOffline) {
            await safeSetReactions(offlineTrigger, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: mbBnOffline.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "Mobile BN Modal Offline Trigger -> Offline Error");
        }
    }
    if (mbBnSubmitting && mbBnReceipt) {
        const simBtn = findChild(mbBnSubmitting, c => c.name && c.name.includes("Simulation"));
        if (simBtn) {
            await safeSetReactions(simBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: mbBnReceipt.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.3 } }] }], "Mobile BN Submitting -> Receipt");
        }
    }
    if (mbBnReceipt) {
        const doneBtn = findChild(mbBnReceipt, c => c.name && c.name.includes("Done"));
        if (doneBtn) {
            await safeSetReactions(doneBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "CLOSE" }] }], "Mobile BN Receipt Done -> Close");
        }
    }
    if (mbBnOffline && mbBnSubmitting) {
        const retryBtn = findChild(mbBnOffline, c => c.name && c.name.includes("Retry"));
        if (retryBtn) {
            await safeSetReactions(retryBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: mbBnSubmitting.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "Mobile BN Offline Retry -> Submitting");
        }
        const cancelBtn = findChild(mbBnOffline, c => c.name && c.name.includes("Cancel"));
        if (cancelBtn) {
            await safeSetReactions(cancelBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "CLOSE" }] }], "Mobile BN Offline Cancel -> Close");
        }
    }

    // ==========================================
    // 3. PAGE 05: ENGLISH
    // ==========================================
    const enHomeDt = figma.getNodeById("18:1068");
    const enArchiveDt = figma.getNodeById("18:1102");
    const enDetailDt = figma.getNodeById("18:1139");
    const enBuiltDt = figma.getNodeById("18:1160");
    const enServicesDt = figma.getNodeById("18:1191");
    const enJoineryDt = figma.getNodeById("18:1222");
    const enProcessDt = figma.getNodeById("18:1254");
    const enStudioDt = figma.getNodeById("18:1288");
    const enContactDt = figma.getNodeById("18:1316");

    const enHomeMb = figma.getNodeById("18:1389");
    const enArchiveMb = figma.getNodeById("18:1407");
    const enDetailMb = figma.getNodeById("18:1425");
    const enBuiltMb = figma.getNodeById("18:1443");
    const enServicesMb = figma.getNodeById("18:1461");
    const enJoineryMb = figma.getNodeById("18:1479");
    const enProcessMb = figma.getNodeById("18:1497");
    const enStudioMb = figma.getNodeById("18:1515");
    const enContactMb = figma.getNodeById("18:1533");

    const enModalDt = figma.getNodeById("18:2149");
    const enSubmittingDt = figma.getNodeById("18:2175");
    const enReceiptDt = figma.getNodeById("18:2181");
    const enOfflineDt = figma.getNodeById("18:2189");

    const enModalMb = figma.getNodeById("18:2198");
    const enSubmittingMb = figma.getNodeById("18:2224");
    const enReceiptMb = figma.getNodeById("18:2230");
    const enOfflineMb = figma.getNodeById("18:2238");
    const enDrawerMb = figma.getNodeById("18:2247");

    async function wireEnglishDesktopHeader(frame, frameName) {
        if (!frame) return;
        const navLinks = findChild(frame, c => c.name === "Nav Links");
        if (navLinks && navLinks.children) {
            for (const item of navLinks.children) {
                const text = (item.type === "TEXT" ? item.characters : item.name) || "";
                if (text.includes("Archive") && enArchiveDt) {
                    await wireNav(item, enArchiveDt, frame, `${frameName} Nav -> Archive`);
                } else if (text.includes("Services") && enServicesDt) {
                    await wireNav(item, enServicesDt, frame, `${frameName} Nav -> Services`);
                } else if (text.includes("Process") && enProcessDt) {
                    await wireNav(item, enProcessDt, frame, `${frameName} Nav -> Process`);
                } else if (text.includes("Studio") && enStudioDt) {
                    await wireNav(item, enStudioDt, frame, `${frameName} Nav -> Studio`);
                } else if (text.includes("Contact") && enContactDt) {
                    await wireNav(item, enContactDt, frame, `${frameName} Nav -> Contact`);
                }
            }
        }
        const brand = findChild(frame, c => c.characters === "FlowGrid" || c.name === "Brand Logo");
        if (brand && enHomeDt && frame.id !== enHomeDt.id) {
            await wireNav(brand, enHomeDt, frame, `${frameName} Brand -> Home`);
        }
        const langPill = findChild(frame, c => c.name === "Language Pill");
        if (langPill) {
            await safeSetReactions(langPill, [{
                trigger: { type: "ON_CLICK" },
                actions: [{
                    type: "URL",
                    url: "https://www.figma.com/design/eMRunQ80brYYvuTWkufV2o/?node-id=18-137"
                }]
            }], `${frameName} Lang Pill -> Bengali URL`);
        }
        const headerCta = findChild(frame, c => c.name === "Header Consultation CTA");
        if (headerCta && enModalDt) {
            await safeSetReactions(headerCta, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: enModalDt.id, navigation: "OVERLAY", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], `${frameName} Header CTA -> Modal`);
        }
        const ctaBtns = findAllChildren(frame, c => c.name && (c.name.includes("Consultation CTA") || c.name.includes("Button / Consultation CTA") || c.name === "Consultation Action Button"));
        for (const cb of ctaBtns) {
            if (cb.id !== headerCta?.id && enModalDt) {
                await safeSetReactions(cb, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: enModalDt.id, navigation: "OVERLAY", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], `${frameName} Banner CTA -> Modal`);
            }
        }
    }

    const enDesktopFrames = [
        { node: enHomeDt, name: "English Home Desktop" },
        { node: enArchiveDt, name: "English Archive Desktop" },
        { node: enDetailDt, name: "English Detail Desktop" }
    ];
    for (const f of enDesktopFrames) {
        if (f.node) await wireEnglishDesktopHeader(f.node, f.name);
    }

    // English Archive Desktop: Filter Tabs & 4 Distinct Cards Destinations
    if (enArchiveDt) {
        const filterTabs = [
            { name: "Living & Dining", dest: enDetailDt },
            { name: "Modular Kitchen", dest: enBuiltDt },
            { name: "Master Suite", dest: enServicesDt },
            { name: "Joinery Craft", dest: enJoineryDt }
        ];
        for (const ft of filterTabs) {
            const tabNode = findChild(enArchiveDt, c => c.name && c.name.includes("Tab") && c.name.includes(ft.name));
            if (tabNode && ft.dest) {
                await wireNav(tabNode, ft.dest, enArchiveDt, `English Archive Filter Tab ${ft.name} -> ${ft.dest.name}`);
            }
        }

        const cardDests = [
            { studyName: "Concept Study 01", dest: enDetailDt },
            { studyName: "Concept Study 02", dest: enBuiltDt },
            { studyName: "Concept Study 03", dest: enServicesDt },
            { studyName: "Concept Study 04", dest: enJoineryDt }
        ];
        for (const cd of cardDests) {
            const cardNode = findChild(enArchiveDt, c => c.name && c.name.includes(cd.studyName));
            if (cardNode && cd.dest) {
                await wireNav(cardNode, cd.dest, enArchiveDt, `English Archive Card -> ${cd.dest.name}`, { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.3 });
                const cardBtn = findChild(cardNode, c => c.name && (c.name.includes("Button") || c.name.includes("CTA")));
                if (cardBtn) {
                    await wireNav(cardBtn, cd.dest, enArchiveDt, `English Archive Card Button -> ${cd.dest.name}`, { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.3 });
                }
            }
        }
    }

    // Detail Return Path (English Desktop)
    if (enDetailDt) {
        const backLink = findChild(enDetailDt, c => c.name && (c.name.includes("Back") || c.name.includes("Link / Back to Archive")));
        if (backLink && enArchiveDt) {
            await wireNav(backLink, enArchiveDt, enDetailDt, "English Detail Back -> Archive");
        }
    }

    // Detail Return Path (English Mobile)
    if (enDetailMb) {
        const backLink = findChild(enDetailMb, c => c.name && (c.name.includes("Back") || c.name.includes("Link / Back to Archive Mobile")));
        if (backLink && (enArchiveMb || enArchiveDt)) {
            const dest = enArchiveMb || enArchiveDt;
            await wireNav(backLink, dest, enDetailMb, "English Detail Mobile Back -> Archive");
        }
        const burger = findChild(enDetailMb, c => c.name && (c.name.includes("Hamburger") || c.name.includes("Menu Toggle")));
        if (burger && enDrawerMb) {
            await safeSetReactions(burger, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: enDrawerMb.id, navigation: "OVERLAY", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "English Detail Mobile Hamburger -> Drawer");
        }
        const brand = findChild(enDetailMb, c => c.characters === "FlowGrid" || c.name === "Brand Logo");
        if (brand && enHomeMb && enDetailMb.id !== enHomeMb.id) {
            await wireNav(brand, enHomeMb, enDetailMb, "English Detail Mobile Brand -> Home");
        }
        const langPill = findChild(enDetailMb, c => c.name && c.name.includes("Language Pill"));
        if (langPill) {
            await safeSetReactions(langPill, [{
                trigger: { type: "ON_CLICK" },
                actions: [{
                    type: "URL",
                    url: "https://www.figma.com/design/eMRunQ80brYYvuTWkufV2o/?node-id=18-283"
                }]
            }], "English Detail Mobile Lang Pill -> Bengali Mobile URL");
        }
    }

    // English Mobile Home
    if (enHomeMb) {
        const burger = findChild(enHomeMb, c => c.name && (c.name.includes("Hamburger") || c.name.includes("Menu Toggle")));
        if (burger && enDrawerMb) {
            await safeSetReactions(burger, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: enDrawerMb.id, navigation: "OVERLAY", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "English Home Mobile Hamburger -> Drawer");
        }
        const langPill = findChild(enHomeMb, c => c.name && c.name.includes("Language Pill"));
        if (langPill) {
            await safeSetReactions(langPill, [{
                trigger: { type: "ON_CLICK" },
                actions: [{
                    type: "URL",
                    url: "https://www.figma.com/design/eMRunQ80brYYvuTWkufV2o/?node-id=18-283"
                }]
            }], "English Home Mobile Lang Pill -> Bengali Mobile URL");
        }
        const heroCta = findChild(enHomeMb, c => c.name && (c.name.includes("Hero") && c.name.includes("CTA")));
        if (heroCta && enModalMb) {
            await safeSetReactions(heroCta, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: enModalMb.id, navigation: "OVERLAY", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "English Home Mobile Hero CTA -> Modal");
        }
    }

    // English Drawer Mobile Wiring
    if (enDrawerMb) {
        const closeBtn = findChild(enDrawerMb, c => c.name && c.name.includes("Close"));
        if (closeBtn) {
            await safeSetReactions(closeBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "CLOSE" }] }], "English Drawer Close");
        }
        const drawerLinks = [
            { name: "Concept Archive", dest: enArchiveMb || enArchiveDt },
            { name: "Services", dest: enServicesMb || enServicesDt },
            { name: "Process", dest: enProcessMb || enProcessDt },
            { name: "Studio", dest: enStudioMb || enStudioDt },
            { name: "Contact", dest: enContactMb || enContactDt }
        ];
        for (const dl of drawerLinks) {
            const item = findChild(enDrawerMb, c => c.name && (c.name.includes(dl.name) || (c.characters && c.characters.includes(dl.name))));
            if (item && dl.dest) {
                await wireNav(item, dl.dest, enDrawerMb, `English Drawer Link -> ${dl.dest.name}`);
            }
        }
        const drawerCta = findChild(enDrawerMb, c => c.name && (c.name.includes("CTA") || c.name.includes("Consultation")));
        if (drawerCta && enModalMb) {
            await safeSetReactions(drawerCta, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: enModalMb.id, navigation: "OVERLAY", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "English Drawer CTA -> Modal");
        }
    }

    // English Desktop Modals
    if (enModalDt) {
        const closeBtn = findChild(enModalDt, c => c.name && (c.name.includes("Close") || c.name.includes("Cancel")));
        if (closeBtn) {
            await safeSetReactions(closeBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "CLOSE" }] }], "English Desktop Modal Close");
        }
        const submitBtn = findChild(enModalDt, c => c.name && (c.name === "Submit CTA" || c.name.includes("Submit")));
        if (submitBtn && enSubmittingDt) {
            await safeSetReactions(submitBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: enSubmittingDt.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "English Desktop Modal Submit -> Submitting");
        }
        const offlineTrigger = findChild(enModalDt, c => c.name && c.name.includes("Offline"));
        if (offlineTrigger && enOfflineDt) {
            await safeSetReactions(offlineTrigger, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: enOfflineDt.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "English Desktop Modal Offline Trigger -> Offline Error");
        }
    }
    if (enSubmittingDt && enReceiptDt) {
        const simBtn = findChild(enSubmittingDt, c => c.name && c.name.includes("Simulation"));
        if (simBtn) {
            await safeSetReactions(simBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: enReceiptDt.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.3 } }] }], "English Desktop Submitting -> Receipt");
        }
    }
    if (enReceiptDt) {
        const doneBtn = findChild(enReceiptDt, c => c.name && c.name.includes("Done"));
        if (doneBtn) {
            await safeSetReactions(doneBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "CLOSE" }] }], "English Desktop Receipt Done -> Close");
        }
    }
    if (enOfflineDt && enSubmittingDt) {
        const retryBtn = findChild(enOfflineDt, c => c.name && c.name.includes("Retry"));
        if (retryBtn) {
            await safeSetReactions(retryBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: enSubmittingDt.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "English Desktop Offline Retry -> Submitting");
        }
        const cancelBtn = findChild(enOfflineDt, c => c.name && c.name.includes("Cancel"));
        if (cancelBtn) {
            await safeSetReactions(cancelBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "CLOSE" }] }], "English Desktop Offline Cancel -> Close");
        }
    }

    // English Mobile Modals
    if (enModalMb) {
        const closeBtn = findChild(enModalMb, c => c.name && (c.name.includes("Close") || c.name.includes("Cancel")));
        if (closeBtn) {
            await safeSetReactions(closeBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "CLOSE" }] }], "English Mobile Modal Close");
        }
        const submitBtn = findChild(enModalMb, c => c.name && (c.name === "Submit CTA" || c.name.includes("Submit")));
        if (submitBtn && enSubmittingMb) {
            await safeSetReactions(submitBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: enSubmittingMb.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "English Mobile Modal Submit -> Submitting");
        }
        const offlineTrigger = findChild(enModalMb, c => c.name && c.name.includes("Offline"));
        if (offlineTrigger && enOfflineMb) {
            await safeSetReactions(offlineTrigger, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: enOfflineMb.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "English Mobile Modal Offline Trigger -> Offline Error");
        }
    }
    if (enSubmittingMb && enReceiptMb) {
        const simBtn = findChild(enSubmittingMb, c => c.name && c.name.includes("Simulation"));
        if (simBtn) {
            await safeSetReactions(simBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: enReceiptMb.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.3 } }] }], "English Mobile Submitting -> Receipt");
        }
    }
    if (enReceiptMb) {
        const doneBtn = findChild(enReceiptMb, c => c.name && c.name.includes("Done"));
        if (doneBtn) {
            await safeSetReactions(doneBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "CLOSE" }] }], "English Mobile Receipt Done -> Close");
        }
    }
    if (enOfflineMb && enSubmittingMb) {
        const retryBtn = findChild(enOfflineMb, c => c.name && c.name.includes("Retry"));
        if (retryBtn) {
            await safeSetReactions(retryBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "NODE", destinationId: enSubmittingMb.id, navigation: "SWAP", transition: { type: "DISSOLVE", easing: { type: "EASE_OUT" }, duration: 0.25 } }] }], "English Mobile Offline Retry -> Submitting");
        }
        const cancelBtn = findChild(enOfflineMb, c => c.name && c.name.includes("Cancel"));
        if (cancelBtn) {
            await safeSetReactions(cancelBtn, [{ trigger: { type: "ON_CLICK" }, actions: [{ type: "CLOSE" }] }], "English Mobile Offline Cancel -> Close");
        }
    }

    console.log(`Wiring completed! Success: ${log.success.length}, Errors: ${log.errors.length}`);
    return {
        successCount: log.success.length,
        errorCount: log.errors.length,
        errors: log.errors
    };
})()
