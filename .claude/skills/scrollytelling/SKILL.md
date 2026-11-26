---
name: scrollytelling
description: Build client-specific scroll-driven interactive landing pages and scrollytelling experiences for any suitable product, service, place, event, organization, or campaign. Use when a brief asks for scroll-linked animation, cinematic product storytelling, interactive web experiences, or immersive landing pages.
---

# Scroll-Driven Interactive Landing Pages (Scrollytelling)

## Core principle

Build the experience around the **client's actual brief, audience, brand, content, assets, and conversion goal**. This is an industry-agnostic capability, not a car-site template. A car is only one possible subject. Never assume the subject, visual style, scene sequence, or 3D requirement before reviewing the client brief.

Possible client categories include (not limited to):
- Physical products: electronics, furniture, fashion, cosmetics, appliances, food packaging.
- Services: consulting, education, finance (only permissible services), software, healthcare information, travel.
- Places and experiences: hotels, destinations, architecture, museums, events.
- Organizations and campaigns: startups, nonprofits, institutions, launches, portfolios.

Reject or escalate work that conflicts with the client's stated ethical/religious constraints. Do not create deceptive claims, fake testimonials, misleading product demonstrations, or unlicensed brand/celebrity likenesses.

## Phase 1 — Understand the brief before choosing technology

Identify:
1. Client, industry, product/service, target audience, and primary conversion action.
2. Story/message and the single most important takeaway.
3. Required sections, copy, languages, CTA, and destination links.
4. Brand guidelines: logo, colors, typography, tone, references.
5. Available assets: photos, video, 3D models (GLB/GLTF/USDZ), product renders, illustrations, fonts, audio, and proof of usage rights.
6. Target devices, browsers, geographic audience, accessibility needs, deadline, and budget.
7. Whether the experience truly needs 3D, or can be achieved better with video, still imagery, SVG, CSS, or 2D motion.

If essential information is missing, ask one concise clarification at a time. Do not invent product specifications, prices, certifications, performance claims, or client facts. Use clearly marked placeholders only when the client authorizes them.

## Phase 2 — Choose the simplest suitable visual approach

Choose per brief, not by habit:

- **CSS scroll-driven animations** for lightweight transitions and progressive enhancement where browser support is adequate. Provide a non-scroll-linked fallback.
- **GSAP + ScrollTrigger** for precise timelines, pinned scenes, scrubbed animation, sequencing, and broad production control.
- **Three.js / React Three Fiber** when an actual interactive 3D scene materially improves understanding or storytelling.
- **Video/image sequence** when the client supplies suitable rendered footage or frame sequences and deterministic cinematic playback is preferable.
- **SVG / Canvas / Lottie / 2D assets** for diagrams, maps, charts, icons, and lightweight motion.
- **Spline or another authoring tool** only when its workflow, export, licensing, performance, and hosting fit the brief.

Do not add Three.js, a large 3D model, or a heavy animation library merely to make the site look impressive. Prefer the lightest approach that meets the creative and business goal.

Official technical references:
- GSAP ScrollTrigger: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- Three.js documentation: https://threejs.org/docs/
- React Three Fiber: https://r3f.docs.pmnd.rs/
- MDN scroll-driven animations: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations

## Phase 3 — Plan the story

Create a scene/section outline before coding. For each scene define:
- Narrative purpose and key message.
- What changes as the visitor scrolls (position, scale, camera, crop, opacity, typography, diagram state).
- Required assets and their source/rights.
- Text and CTA.
- Mobile adaptation and reduced-motion alternative.

A common structure (adapt it; do not force every project into it):
1. Hero: clear value proposition and opening visual.
2. Context/problem or product introduction.
3. Key features/benefits, each supported by evidence.
4. Detail/exploded view/process/demo where relevant.
5. Trust/proof: real specifications, case studies, or verified facts.
6. CTA and useful footer.

## Phase 4 — Build requirements

- Make the page responsive; design mobile intentionally rather than shrinking desktop scenes.
- Keep body content readable and navigation/CTA usable even if animation fails.
- Ensure scroll does not trap the visitor. Avoid excessive pinning and very long forced scroll distances.
- Respect `prefers-reduced-motion`; provide a calm static or low-motion experience.
- Support keyboard navigation, semantic HTML, visible focus, meaningful alt text, contrast, and accessible controls.
- Avoid scroll-jacking. Normal browser scrolling must remain predictable.
- Load large models, textures, fonts, and video progressively; use compressed assets, responsive image sizes, lazy loading, and sensible fallbacks.
- Optimize 3D geometry, draw calls, texture sizes, and memory. Pause or reduce rendering when off-screen or the tab is inactive where practical.
- Avoid autoplay audio. If sound is used, require a clear user action and provide controls.
- Test touch, trackpad, mouse wheel, narrow viewports, orientation changes, and slow connections.
- Keep SEO-critical copy in semantic HTML; do not hide the whole story inside a canvas.
- Track only necessary analytics and respect applicable consent/privacy requirements.

## Phase 5 — Quality assurance

Before presenting the result:
1. Run the project build, lint, and tests that exist; report exact outcomes.
2. Check desktop and mobile layouts, including a narrow phone viewport.
3. Test the whole page from top to bottom, reverse scrolling, refresh at a mid-page position, and direct anchor navigation.
4. Test with reduced motion enabled and with WebGL unavailable or failed.
5. Check console errors, loading states, broken assets, text overflow, CTA destinations, and keyboard access.
6. Verify all assets and fonts are licensed for the intended client/commercial use.
7. Confirm factual claims against client-provided or authoritative evidence.
8. Provide a concise handoff: what was built, how to run it, known limitations, assets still needed, and test results.

Never claim the site is complete, deployed, or tested unless the relevant action actually succeeded and was verified.

## Client approval and delivery controls

- Prepare proposals and drafts, but do not contact leads or clients without the user's explicit approval.
- Do not purchase assets, subscribe to services, deploy, publish, connect analytics, or change client systems without separate approval.
- Obtain approval for the storyboard, material design direction, paid assets, final build, and delivery.
- Protect client files and credentials; never commit secrets or private customer data.
- Do not use copyrighted music, footage, models, logos, fonts, or photography without appropriate rights.
