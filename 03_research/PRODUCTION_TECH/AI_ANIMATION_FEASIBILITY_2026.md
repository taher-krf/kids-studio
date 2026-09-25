# AI-assisted animation feasibility: 2026 desk research

Status: RESEARCH / NO STACK SELECTION, configuration, purchase or production asset. Accessed 2026-09-25. Metadata: [SOURCE_REGISTER](../SOURCE_REGISTER.md).

## Question and method

Can current generative tools support recurring, legible, safe character comedy? Reviewed current official capability documentation: [Veo 3.1](https://ai.google.dev/gemini-api/docs/veo?hl=en), [Runway Gen-4 References](https://help.runwayml.com/hc/en-us/articles/40042718905875-Creating-with-Gen-4-Image-References), [Adobe Firefly image-guided video](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html), and [OpenAI Sora discontinuation notice](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation). These are vendor capability statements, not independent Kids Studio quality tests. Rejected vendor demo clips as evidence of reliable 50-episode continuity and third-party leaderboard rankings lacking repeatable test conditions.

## Capability vs show need

| Need | Documented capability | What remains unproved |
| --- | --- | --- |
| Reference-conditioned identity and backgrounds | Veo accepts up to three reference images; Runway's References workflows aim to preserve characters/scenes [S38](https://ai.google.dev/gemini-api/docs/veo?hl=en), [S39](https://help.runwayml.com/hc/en-us/articles/40042718905875-Creating-with-Gen-4-Image-References). | Pip/Nimbus silhouette, expression and colors across shots, orientations, weather states and 50 episodes. |
| First/last-frame and image-to-video control | Veo and Firefly document image input and first/last-frame guidance [S38](https://ai.google.dev/gemini-api/docs/veo?hl=en), [S40](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html). | In-between causality, prop contact, timing and exact end pose; endpoints do not guarantee physically coherent motion. |
| Short clips / editing | Veo documentation describes short generated clips; Adobe supports clip generation with constraints on combined settings [S38](https://ai.google.dev/gemini-api/docs/veo?hl=en), [S40](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/generate-videos-using-images.html). | Assembly into a continuous episode, camera continuity, audio edits and consistent lighting. |
| Multi-character acting and lip sync | Runway documents multi-character workflow with separate performances [Runway Act-Two](https://help.runwayml.com/hc/en-us/articles/41748090660499-Creating-Multi-Character-Dialogues-with-Act-Two). | Child-safe stylized expressions, simultaneous interactions and lip sync in this concept. Sparse dialogue reduces one burden but does not solve acting. |
| OpenAI video candidate | Official notice says Sora web/app experiences ended 2026-04-26 [S41](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation). | Do not treat Sora as a stable current option. Research any future replacement only when available. |

## Likely strengths, failures and production split

**LIKELY AI STRENGTHS — MEDIUM / PRIMARY vendor capability + INFERENCE:** exploratory backgrounds, mood studies, broad motion sketches, isolated short reaction shots, alternate staging concepts. **LIKELY FAILURE MODES — LOW / INFERENCE until benchmark:** silhouette drift, fluctuating cloud volume, weather effects disconnected from cause, disappearing props, inconsistent hands/contact, wrong camera direction, multi-character identity swap, audio mismatch, accidental uncanny or unsafe content. Vendors do not quantify these rates for Kids Studio.

**GENERATIVE CANDIDATES:** exploratory concepts and nonessential background/motion options after rights review. **DETERMINISTIC CANDIDATES:** final character rigs or model sheets, close prop contact, on-screen causal action, exact timing/pause/callback, recurring locations, safety-critical weather action, typography, final edit/audio mix. Hybrid 2D/3D/AI compositing is a candidate architecture only. Blender, FFmpeg, Remotion and ComfyUI are possible tools noted in project state; no current installation or production selection is asserted.

## Benchmark required before stack decision

Create a rights-cleared, disposable pilot benchmark only after owner approves moving beyond this research phase: same two-character shot across five camera angles; repeated identity under rain/wind; a prop handed between characters; a three-beat escalating action with exact continuity; expressive silent emotion; one limited-dialogue take; return to same background; safety review of every frame; editability, time and cost per accepted second. Compare generative, deterministic and hybrid versions. Decide by accepted-quality yield and editorial control, not vendor demos. No service was subscribed to or integrated in this sprint.
