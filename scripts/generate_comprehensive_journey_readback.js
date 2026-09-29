// Generate comprehensive Figma Prototype Journey Readback with Destinations, Paths, Multi-Actions, Bound Variables & Components
(async () => {
    const pages = figma.root.children;
    const readback = {
        meta: {
            title: "FlowGrid — Complete Figma Prototype Journey & Native Binding Readback",
            timestamp: new Date().toISOString(),
            fileKey: "eMRunQ80brYYvuTWkufV2o",
            totalReactions: 0,
            journeysSummary: {
                journey1_exploration: 0,
                journey2_consultation: 0,
                journey3_language_and_nav: 0,
                journey4_archive_and_templates: 0
            }
        },
        journeys: {
            journey1_concept_exploration: [],
            journey2_consultation_booking_and_modal_states: [],
            journey3_global_navigation_and_language: [],
            journey4_concept_archive_and_templates: []
        },
        allReactions: [],
        boundVariablesSample: [],
        componentInstancesSample: []
    };

    function getPath(node) {
        const parts = [];
        let curr = node;
        while (curr && curr.type !== "DOCUMENT") {
            parts.unshift(curr.name);
            curr = curr.parent;
        }
        return parts.join(" > ");
    }

    function inspectReactions(node, pageName) {
        if (node.reactions && node.reactions.length > 0) {
            for (const r of node.reactions) {
                readback.meta.totalReactions++;
                const rawActions = r.actions || (r.action ? [r.action] : []);
                const actionsList = rawActions.map(a => {
                    let destName = null;
                    let destType = null;
                    let destPage = null;
                    if (a.destinationId) {
                        const dest = figma.getNodeById(a.destinationId);
                        if (dest) {
                            destName = dest.name;
                            destType = dest.type;
                            let p = dest.parent;
                            while (p && p.type !== "PAGE") p = p.parent;
                            destPage = p ? p.name : null;
                        } else {
                            destName = "NODE_NOT_FOUND";
                        }
                    }
                    return {
                        actionType: a.type || "UNKNOWN",
                        navigation: a.navigation || null,
                        destinationId: a.destinationId || null,
                        destinationName: destName,
                        destinationType: destType,
                        destinationPage: destPage,
                        url: a.url || null,
                        variableId: a.variableId || null,
                        transition: (a.transition ? a.transition.type : null),
                        duration: (a.transition ? a.transition.duration : null)
                    };
                });

                const primaryAction = actionsList[0] || {};
                const entry = {
                    page: pageName,
                    sourceId: node.id,
                    sourceName: node.name,
                    sourceType: node.type,
                    path: getPath(node),
                    trigger: r.trigger ? r.trigger.type : "UNKNOWN",
                    actions: actionsList,
                    actionType: primaryAction.actionType || "UNKNOWN",
                    navigation: primaryAction.navigation || null,
                    destinationId: primaryAction.destinationId || null,
                    destinationName: primaryAction.destinationName || null,
                    destinationType: primaryAction.destinationType || null,
                    destinationPage: primaryAction.destinationPage || null,
                    url: primaryAction.url || null,
                    transition: primaryAction.transition || null,
                    duration: primaryAction.duration || null
                };

                // Classify into journeys
                const isLang = entry.sourceName.includes("Language") || entry.sourceName.includes("Pill") || (primaryAction.url && primaryAction.url.includes("node-id"));
                const isArchiveOrFilter = entry.sourceName.includes("Tab") || entry.sourceName.includes("Archive") || entry.sourceName.includes("ধারণা সংগ্রহ") || (entry.destinationName && entry.destinationName.includes("Archive"));
                const isConsultation = entry.sourceName.includes("Modal") ||
                    entry.sourceName.includes("Consultation") ||
                    entry.sourceName.includes("CTA") ||
                    entry.sourceName.includes("Submit") ||
                    entry.sourceName.includes("Simulation") ||
                    entry.sourceName.includes("Done") ||
                    entry.sourceName.includes("Retry") ||
                    entry.sourceName.includes("Cancel") ||
                    entry.sourceName.includes("Close") ||
                    entry.sourceName.includes("Offline") ||
                    (primaryAction.navigation === "OVERLAY") ||
                    (primaryAction.actionType === "CLOSE") ||
                    (entry.destinationName && (entry.destinationName.includes("Overlay") || entry.destinationName.includes("Modal") || entry.destinationName.includes("Receipt") || entry.destinationName.includes("Submitting") || entry.destinationName.includes("Drawer")));

                if (isConsultation) {
                    readback.meta.journeysSummary.journey2_consultation++;
                    readback.journeys.journey2_consultation_booking_and_modal_states.push(entry);
                } else if (isLang) {
                    readback.meta.journeysSummary.journey3_language_and_nav++;
                    readback.journeys.journey3_global_navigation_and_language.push(entry);
                } else if (isArchiveOrFilter) {
                    readback.meta.journeysSummary.journey4_archive_and_templates++;
                    readback.journeys.journey4_concept_archive_and_templates.push(entry);
                } else if (
                    entry.sourceName.includes("Card") ||
                    entry.sourceName.includes("View Project") ||
                    entry.sourceName.includes("Angle") ||
                    entry.sourceName.includes("Dining") ||
                    entry.sourceName.includes("Joinery") ||
                    (entry.destinationName && entry.destinationName.includes("Detail"))
                ) {
                    readback.meta.journeysSummary.journey1_exploration++;
                    readback.journeys.journey1_concept_exploration.push(entry);
                } else {
                    readback.meta.journeysSummary.journey3_language_and_nav++;
                    readback.journeys.journey3_global_navigation_and_language.push(entry);
                }

                readback.allReactions.push(entry);
            }
        }

        if (node.children) {
            for (const child of node.children) {
                inspectReactions(child, pageName);
            }
        }
    }

    // Sample bound variables
    function inspectBoundVariables(node) {
        if (node.boundVariables) {
            const keys = Object.keys(node.boundVariables);
            if (keys.length > 0) {
                readback.boundVariablesSample.push({
                    nodeId: node.id,
                    nodeName: node.name,
                    nodeType: node.type,
                    bindings: keys.map(k => {
                        const binding = node.boundVariables[k];
                        let varName = "UNKNOWN";
                        if (binding && binding.id) {
                            const v = figma.variables.getVariableById(binding.id);
                            if (v) varName = v.name;
                        } else if (Array.isArray(binding) && binding[0] && binding[0].id) {
                            const v = figma.variables.getVariableById(binding[0].id);
                            if (v) varName = v.name;
                        }
                        return { property: k, variableName: varName };
                    })
                });
            }
        }
        if (node.children && readback.boundVariablesSample.length < 35) {
            for (const child of node.children) {
                inspectBoundVariables(child);
            }
        }
    }

    // Sample component instances
    function inspectInstances(node) {
        if (node.type === "INSTANCE") {
            const main = node.mainComponent;
            readback.componentInstancesSample.push({
                instanceId: node.id,
                instanceName: node.name,
                mainComponentId: main ? main.id : null,
                mainComponentName: main ? main.name : "UNKNOWN",
                componentSet: (main && main.parent && main.parent.type === "COMPONENT_SET") ? main.parent.name : null
            });
        }
        if (node.children && readback.componentInstancesSample.length < 35) {
            for (const child of node.children) {
                inspectInstances(child);
            }
        }
    }

    for (const page of pages) {
        inspectReactions(page, page.name);
        inspectBoundVariables(page);
        inspectInstances(page);
    }

    return readback;
})()
