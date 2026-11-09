# Atlas Architecture Decision Record — Evolution Under Creator Atlas

**Recorded:** 2026-11-09T03:07:07.469Z  
**Decision status:** PROPOSED / READY FOR IMPLEMENTATION REVIEW  
**Scope:** Architecture synthesis of the Copilot roadmap with the independently inspected `scrollverse-web-app` repository. No application code changed in this record.

## Decision

Retain the existing `CreatorAtlas.tsx` as the user-facing **Atlas Explorer**. Design a separate Atlas Core domain layer beneath it for entities, relationships, lineage traversal, provenance, and evidence-aware queries.

The Creator Atlas is not replaced. It becomes a consumer of Atlas Core only after the core has a validated data model, test coverage, and source-backed records.

## Existing architecture observed

Repository: `chaishillomnitech1/scrollverse-web-app`  
Latest commit observed during inspection: `2693f744a29d12e4a63784ae411d0e024c3bf074` (2026-11-07T07:21:09Z).

Independently retrieved:
- `client/src/pages/CreatorAtlas.tsx`: five discovery groups and browser-local route links.
- `client/src/App.tsx`: Wouter route architecture; the Phase 591 test asserts registration at `/creator-atlas`.
- `server/routers.ts`: central tRPC `appRouter` composition.
- `server/routers/atlantisCatalog.ts`: existing router with an unrelated commerce/catalog domain. Its name is not evidence of an Atlas graph engine; do not repurpose it.
- `server/portalRouteRegistry.ts` and `server/routers/portalRouteRegistry.ts`: existing route metadata registry and admin-gated refresh pattern.
- `server/db.ts`: existing MySQL2 + Drizzle database access pattern.
- `server/phase591.creatorAtlas.test.ts` and `server/phase837.creatorAtlasPresentation.test.ts`: source-level Creator Atlas regression tests.
- `docs/phase403-scrollverse-atlas-structure.md` and `docs/phase591-connected-creator-atlas-design.md`: existing design context.

## Architecture boundary

```
CreatorAtlas.tsx (Atlas Explorer / presentation)
              |
              v
       Atlas tRPC API
              |
              v
       Atlas Core domain
       - entity registry
       - relationship registry
       - graph traversal
       - lineage queries
       - provenance/evidence validation
              |
              v
     Versioned source-backed data
```

This is a target design, not a description of currently deployed services.

## Initial implementation placement (proposed)

- `shared/atlas-types.ts` — shared entity, relationship, provenance, evidence, and query contracts.
- `data/atlas/` — versioned, source-backed records; do not populate canonical seed data from memory or unsourced handoff examples.
- `server/atlas/entities.ts` — entity validation and lookup.
- `server/atlas/relationships.ts` — relationship validation and traversal helpers.
- `server/atlas/lineage.ts` — bounded ancestor/descendant traversal with cycle protection.
- `server/atlas/graph.ts` — graph query orchestration.
- `server/routers/atlas.ts` — tRPC endpoints, composed through `server/routers.ts`.
- `client/src/pages/CreatorAtlas.tsx` — remains the Explorer; future graph view consumes typed API output.

Exact paths may be adjusted to match repository conventions during implementation.

## Storage decision

**Do not introduce a graph database in V1.** The inspected application already uses MySQL + Drizzle and a central tRPC API. First implement a deterministic, typed relationship registry and traversal layer over source-backed records. Evaluate persistence and graph-database needs only after query volume, mutation requirements, and provenance model are understood.

The Copilot roadmap's proposed `atlas-seed.json` is not authorized to become a canonical seed until its records have source references. The missing `atlas_phase3_api_seed.ts` remains NOT RECOVERED / BLOCKED. No reconstructed substitute may be labeled original.

## Data contract principles

Every entity should include:
- stable `id`
- `type`
- `title`
- optional description and tags
- source classification
- provenance references

Every relationship should include:
- stable `id`
- `fromEntityId`
- `toEntityId`
- typed relationship
- source/provenance reference
- confidence or review state where appropriate

A relationship label such as INSPIRED, EVOLVED, REFERENCED, MERGED, FORKED, DESCENDED, or CONNECTED is not proof by itself. It must be traceable to a source. Distinguish owner-authored assertions, repository facts, imported/pasted claims, and independently verified evidence.

## First API/query slice (proposed)

1. `atlas.listEntities` — bounded, filterable entity listing.
2. `atlas.getEntity` — one entity with source-backed relationships.
3. `atlas.getLineage` — ancestors and descendants with maximum depth, cycle protection, and relationship paths.
4. `atlas.findRelated` — typed relationship traversal.
5. `atlas.search` — title/description/tag search with evidence references.

Do not add a public graph visualization until these contracts and their tests are stable. No user-supplied future examples (e.g. Codex 43.7, Episode 44, Pattern Library) should enter canonical data without evidence.

## Required test gates

- schema validation for entity and relationship records
- missing endpoint rejection
- duplicate ID handling
- cycle protection and bounded traversal
- directionality of each relationship type
- lineage path correctness
- provenance required for canonical/exportable records
- no cross-tenant or private-record leakage if private scopes are later introduced
- existing Creator Atlas regression tests remain passing

No tests were run as part of this architecture inspection.

## Release and privacy gates

- Preserve all existing Creator Atlas files.
- No destructive rewrite or broad route refactor.
- No secret, credential, wallet seed phrase, private financial data, personal contact data, or private source material in public records.
- Public learning exports may use only explicitly approved, source-backed records.
- Treasury, token, royalty, deployment, pinning, and mint claims remain separate evidence domains and must not be inferred from Atlas relationships.
- No deployment, publication, pinning, or minting is authorized by this ADR.

## Current status

- Existing Atlas Explorer: FOUND.
- Existing tRPC + MySQL/Drizzle patterns: FOUND.
- Existing graph core / lineage API: NOT ESTABLISHED.
- Original Phase 3 seed: NOT RECOVERED / BLOCKED.
- Canonical seed dataset: NOT CREATED.
- Atlas Core implementation: NOT STARTED.
- This ADR: documentation only.

## Evidence references

- Creator Atlas: https://github.com/chaishillomnitech1/scrollverse-web-app/blob/2693f744a29d12e4a63784ae411d0e024c3bf074/client/src/pages/CreatorAtlas.tsx
- Phase 403: https://github.com/chaishillomnitech1/scrollverse-web-app/blob/main/docs/phase403-scrollverse-atlas-structure.md
- Phase 591: https://github.com/chaishillomnitech1/scrollverse-web-app/blob/main/docs/phase591-connected-creator-atlas-design.md
- tRPC composition: https://github.com/chaishillomnitech1/scrollverse-web-app/blob/main/server/routers.ts
- Existing unrelated Atlantis commerce router: https://github.com/chaishillomnitech1/scrollverse-web-app/blob/main/server/routers/atlantisCatalog.ts
- Portal route registry: https://github.com/chaishillomnitech1/scrollverse-web-app/blob/main/server/portalRouteRegistry.ts
- Database access: https://github.com/chaishillomnitech1/scrollverse-web-app/blob/main/server/db.ts
- Creator Atlas regression test: https://github.com/chaishillomnitech1/scrollverse-web-app/blob/main/server/phase591.creatorAtlas.test.ts
