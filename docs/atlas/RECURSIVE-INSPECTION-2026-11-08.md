# Atlas Recursive Repository Inspection — 2026-11-08

**Inspection timestamp:** 2026-11-09T02:53:31.939Z  
**Scope:** Recursive default-branch Git tree inspection of five previously identified candidate repositories, plus targeted code searches and selected file reads.  
**Status:** Partial inspection snapshot. This is not a complete audit of all 96 repositories, all branches, or all history.

## Executive result

The recursive inspection found an existing browser-local Creator Atlas implementation in `scrollverse-web-app`, alongside multiple other Atlas-named portal pages and phase records. This is a meaningful existing application surface, but it is **not evidence that the proposed Atlas Core entity/relationship engine or original Phase 3 API seed exists**.

Targeted default-branch code searches in `scrollverse-web-app` for `AtlasEntity`, `AtlasRelationship`, and `atlas_phase3_api_seed.ts` returned no matches. Search indexing and default-branch scope limit what a negative result proves.

## Recursive tree results

| Repository | Default-branch tree paths | Atlas-related paths / result |
|---|---:|---|
| `omnitech1-portal` | 101 | No Atlas/seed/entity/relationship-named paths surfaced; root README and package manifest present |
| `scrollverse-platform` | 158 | No Atlas/seed/entity/relationship-named paths surfaced; package manifest present |
| `scrollverse-web-app` | 2,502 | Multiple Atlas pages, design records, and tests found; details below |
| `scrollverse-portal` | 4 | No Atlas/seed/entity/relationship-named paths surfaced; README and package manifest present |
| `scrollverse-master-ecosystem-hub` | 16 | Atlas handoff and inspection documentation found; no Atlas implementation files surfaced |

All five Git tree responses reported `truncated=false`. This describes the returned default-branch trees only.

## Existing Atlas surface found in scrollverse-web-app

### Direct implementation
- `client/src/pages/CreatorAtlas.tsx` — React page defining five discovery groups: Visual Worlds, Learn the System, Read the Work, Build With the Work, and Source and Continuity. It links to browser-local routes and labels some groups AVAILABLE NOW and one RESEARCH.
- `client/src/App.tsx` — search result confirms the CreatorAtlas module is imported as a lazy route module. The route registration should be checked directly before asserting the exact route path.
- `docs/phase403-scrollverse-atlas-structure.md` — describes a reader-directed Atlas with source context, operating state, local routes, and protected cross-link boundaries.
- `docs/phase591-connected-creator-atlas-design.md` — describes the five-group Creator Atlas design and browser-local orientation purpose.
- Related Atlas-named pages include `CreatorVisualIntakeAtlas.tsx`, `CryptoSystemsAtlas.tsx`, `FashionArtifactAtlas.tsx`, `InstitutionalSystemsAtlas.tsx`, `LegionSpecialistAtlas.tsx`, `OmnilandSourceAtlas.tsx`, `PlanningAtlas.tsx`, `ResearchAtlas.tsx`, and `ScrollVerseAtlas.tsx`.
- Related tests include `server/phase591.creatorAtlas.test.ts`, `server/phase837.creatorAtlasPresentation.test.ts`, and other phase-specific Atlas tests.

### What this does and does not establish
- **FOUND:** Existing UI and documentation called Creator Atlas / ScrollVerse Atlas.
- **FOUND:** Five discovery groups and route handoffs in the fetched CreatorAtlas component.
- **FOUND:** Atlas-related phase test files exist in the repository tree.
- **NOT ESTABLISHED:** That tests currently pass; no test command was run in this inspection.
- **NOT FOUND IN TARGETED SEARCH:** `AtlasEntity`, `AtlasRelationship`, and `atlas_phase3_api_seed.ts` in the default-branch code search for this repository.
- **NOT ESTABLISHED:** That a generalized Atlas Core graph engine, API, or the missing original seed exists elsewhere.

## Selected repository evidence

1. `scrollverse-web-app/client/src/pages/CreatorAtlas.tsx`  
   https://github.com/chaishillomnitech1/scrollverse-web-app/blob/2693f744a29d12e4a63784ae411d0e024c3bf074/client/src/pages/CreatorAtlas.tsx

2. `scrollverse-web-app/docs/phase403-scrollverse-atlas-structure.md`  
   https://github.com/chaishillomnitech1/scrollverse-web-app/blob/main/docs/phase403-scrollverse-atlas-structure.md

3. `scrollverse-web-app/docs/phase591-connected-creator-atlas-design.md`  
   https://github.com/chaishillomnitech1/scrollverse-web-app/blob/main/docs/phase591-connected-creator-atlas-design.md

4. Latest commit observed for `scrollverse-web-app` during this inspection:  
   `2693f744a29d12e4a63784ae411d0e024c3bf074` — 2026-11-07T07:21:09Z  
   https://github.com/chaishillomnitech1/scrollverse-web-app/commit/2693f744a29d12e4a63784ae411d0e024c3bf074

5. Existing master-repo handoff and prior inspection report remain documented separately under `docs/atlas/`.

## Evidence ledger entries

| Timestamp | Source | Result | Evidence reference |
|---|---|---|---|
| 2026-11-09T02:53:31.939Z | GitHub recursive Git tree API, default branch | `omnitech1-portal`: 101 paths; no Atlas/seed/entity/relationship-named paths surfaced | https://api.github.com/repos/chaishillomnitech1/omnitech1-portal/git/trees/HEAD?recursive=1 |
| 2026-11-09T02:53:31.939Z | GitHub recursive Git tree API, default branch | `scrollverse-platform`: 158 paths; no Atlas/seed/entity/relationship-named paths surfaced | https://api.github.com/repos/chaishillomnitech1/scrollverse-platform/git/trees/HEAD?recursive=1 |
| 2026-11-09T02:53:31.939Z | GitHub recursive Git tree API, default branch | `scrollverse-web-app`: 2,502 paths; Atlas pages, docs, and tests found | https://api.github.com/repos/chaishillomnitech1/scrollverse-web-app/git/trees/HEAD?recursive=1 |
| 2026-11-09T02:53:31.939Z | GitHub recursive Git tree API, default branch | `scrollverse-portal`: 4 paths; no Atlas/seed/entity/relationship-named paths surfaced | https://api.github.com/repos/chaishillomnitech1/scrollverse-portal/git/trees/HEAD?recursive=1 |
| 2026-11-09T02:53:31.939Z | GitHub recursive Git tree API, default branch | `scrollverse-master-ecosystem-hub`: 16 paths; Atlas documentation found, no implementation paths surfaced | https://api.github.com/repos/chaishillomnitech1/scrollverse-master-ecosystem-hub/git/trees/HEAD?recursive=1 |
| 2026-11-09T02:53:31.939Z | GitHub default-branch code search in `scrollverse-web-app` | No matches returned for `AtlasEntity`, `AtlasRelationship`, or `atlas_phase3_api_seed.ts` | https://github.com/chaishillomnitech1/scrollverse-web-app |
| 2026-11-09T02:53:31.939Z | GitHub file retrieval | CreatorAtlas component and Phase 403 / Phase 591 design records retrieved | https://github.com/chaishillomnitech1/scrollverse-web-app/blob/2693f744a29d12e4a63784ae411d0e024c3bf074/client/src/pages/CreatorAtlas.tsx |

## Gates still open

1. Original `atlas_phase3_api_seed.ts`: **NOT RECOVERED / BLOCKED**. Do not reconstruct or relabel a substitute as original.
2. Full 96-repository commit/README inventory: **IN PROGRESS**. This report does not complete the remaining 90 checks described in the prior handoff.
3. Candidate app code review: **PARTIAL**. Tree-level recursive inspection completed for five candidates; detailed review of all potentially relevant files and route wiring remains.
4. Test execution: **NOT RUN** in this inspection.
5. Secret scan: **NOT RUN**. No secrets were printed or copied.
6. Privacy review of the two repositories previously flagged as public: **OPEN**. No visibility or content changes made.
7. Atlas Core implementation, five query tests, provenance wiring, evidence-ledger runtime, deployment, pinning, and minting: **NOT PERFORMED**.

## Next safe step

Review the existing CreatorAtlas route and the related Atlas page/data structures in `scrollverse-web-app` before designing a separate Atlas Core package. Preserve the existing app as-is. If the original seed is supplied later, archive it unchanged and work only on a separate copy.
