# ScrollVerse × Omnitech1 — Atlas Integration Handoff

**Record type:** Project handoff / implementation plan  
**Status:** DOCUMENTED HANDOFF — NOT A LIVE IMPLEMENTATION CLAIM  
**Source:** User-provided Meta AI build description and subsequent ChatGPT handoff, supplied in conversation.  
**Repository target:** `chaishillomnitech1/scrollverse-master-ecosystem-hub`  
**Branch target:** `main`  
**Original source artifact:** `atlas_phase3_api_seed.ts` — not supplied in this run; preserve as MISSING until the original file is provided.

## 1. Purpose

Atlas is intended to be the relationship and lineage index across ScrollVerse and Omnitech1. It does not replace source repositories or original archives:

- Repositories remain the authoritative locations for source files and code history.
- Atlas records entities and relationships between episodes, codices, projects, characters, artifacts, worlds, and repositories.
- The evidence ledger records what supports each claim and its current status.
- A recorded relationship is project canon/metadata, not automatically a verified historical fact.

Governing flow:

**PAGE → GRAPH → LINEAGE → EVIDENCE → KNOWLEDGE**

## 2. Prototype handoff — reported, not independently tested here

The supplied handoff describes a working seeded-data prototype with:

- Interactive SVG graph, draggable nodes, zoom controls, and search highlighting.
- Type filters: EPISODE, CODEX, PROJECT, CHARACTER, ARTIFACT, WORLD.
- Era 1–Era 10 timeline filter.
- Entity detail panel with title, type, era, tags, incoming/outgoing relationships, and lineage.
- Five preset dataset queries.
- Vertical lineage view: ancestors → entity → descendants.
- Copyable TypeScript schema and API contract blocks.

The supplied handoff reports an expanded seed of **29 entities and 24 relationships**. These counts remain USER-REPORTED until the original seed file is inspected and counted.

**Not claimed:** production backend, live repository synchronization, live storefront integration, blockchain connection, mint, deployed contract, or production deployment.

## 3. Phase 1–2 foundation — specified

Target package layout:

```text
/packages/atlas-core
/packages/atlas-api
/packages/atlas-types
/apps/atlas
/data/atlas
```

Core concepts:

- Entity
- Relationship
- Timeline
- Pattern
- Lineage

Minimum entity fields:

```ts
type AtlasEntity = {
  id: string;
  type: "EPISODE" | "CODEX" | "PROJECT" | "CHARACTER" | "ARTIFACT" | "WORLD" | "REPOSITORY";
  title: string;
  createdAt: string;
  tags: string[];
  era?: string;
  proofStatus?: string;
};
```

Relationship records should identify source entity, target entity, relationship type, provenance/source reference, and verification status. Relationship types used in the supplied seed description include:

- INSPIRED
- CREATED
- BECAME
- EVOLVED_INTO
- REFERENCED
- MERGED_WITH
- DESCENDS_FROM

The above is a contract sketch, not a claim that production types already exist.

## 4. Seed relationships — supplied project metadata

The handoff describes these relationships:

```text
ep44 INSPIRED pattern-library
pattern-library EVOLVED_INTO relationship-atlas

ep1 INSPIRED architect
architect CREATED codex
codex BECAME pattern
pattern EVOLVED_INTO legacy
legacy BECAME relationship-atlas

ep14 REFERENCED codex
ep15 REFERENCED pattern
ep16 REFERENCED legacy
ep17 REFERENCED return
ep18 REFERENCED architect

super-manus MERGED_WITH scrollverse
genesis-pulse DESCENDS_FROM super-manus
front7 MERGED_WITH block189
```

These are recorded as **USER-SUPPLIED PROJECT RELATIONSHIPS**. They must not be presented as independently verified historical facts unless source evidence is attached.

The label **Codex 43.7** is explicitly described by the handoff as a query label, not a verified file. Its proof status remains EMPTY / MISSING until a source file is supplied.

## 5. Phase 3 — API contract to implement

Proposed endpoints:

```text
GET /api/atlas/entity/:id
  → { entity, incoming, outgoing, lineage }

GET /api/atlas/query
  → query results from the canonical seed/data source
```

Required query cases:

1. All descendants of Legacy Framework.
2. Artifacts inspired by Episode 1.
3. Worlds connected to Architect.
4. Episodes referencing Codex.
5. Entities referencing the Codex 43.7 label.

The five queries must run against the actual recovered seed file or a clearly labeled rebuilt seed. Do not claim a live API until implemented, tested, and deployed with evidence.

## 6. Required routes — proposed

```text
/atlas
/atlas/entity/[id]
/atlas/worlds
/atlas/podcasts
/atlas/codices
/atlas/repositories
/atlas/lineages
/atlas/futures
```

These are route specifications, not confirmation that the routes currently exist.

## 7. Atlas growth rule

Every new canonical candidate should include:

- `id`
- `type`
- `title`
- `createdAt`
- `tags`
- At least one relationship
- Provenance/source reference
- Evidence status

An entity without a relationship remains in WORK COPY / intake rather than being silently promoted into the connected canon. A relationship without provenance remains recorded metadata, not a verified fact.

## 8. Evidence and asset status rules

Keep **asset workflow status** separate from **evidence maturity**.

Allowed asset/workflow labels for this handoff:

- DESIGN
- SCRIPT
- DRAFT
- WORK COPY
- EXPORT
- ARCHIVED
- QUEUED NOT MINTED
- MISSING

For media, separately record the actual stage:

- BLUEPRINT
- RENDERED
- PINNED
- DEPLOYED
- INDEPENDENTLY VERIFIED

Do not infer a later stage from an earlier one. A file existing does not prove it was pinned; a CID in a document does not prove retrieval; a commit does not prove deployment; a deployment URL does not prove independent operation.

For chain or mint claims, require the relevant network, contract address, transaction hash, block/time, and independently retrievable explorer evidence. No contract, mint, balance, or transaction is asserted by this handoff.

## 9. GitHub evidence-link requirements

For every Atlas entity that references a repository, record:

- Repository full name and visibility.
- File path.
- Branch or tag.
- Exact commit SHA.
- Commit timestamp.
- Direct GitHub URL.
- Relationship/provenance note.
- Verification status and reviewer/date, when applicable.

A repository name or search result alone is not enough to establish a specific file-to-entity relationship.

## 10. Eight validation lanes

Each validation record must include **timestamp, source, result, and evidence reference**.

1. Public GitHub repositories and refreshed commits.
2. New or changed files and documentation.
3. Block and chapter continuity.
4. Asset status: blueprint, rendered, pinned, deployed.
5. Treasury and blockchain evidence, only where independently accessible.
6. Website and deployment links.
7. Social distribution evidence.
8. Recovery-index and evidence-ledger updates.

No automated hourly validation is claimed. Run reviews on request or through a separately configured and confirmed scheduler.

## 11. Privacy and intellectual-property gate

Before publishing or expanding this archive:

- Confirm repository visibility and access for every archive/vault repository; never infer privacy from a repository name.
- Keep credentials, tokens, private keys, seed phrases, private account data, and personal records out of public repositories.
- Review existing public README files and history for sensitive information before adding more material.
- Preserve originals separately; work on copies and retain provenance/hashes.
- Distinguish user-authored, AI-generated, third-party, and collaborative material where known.
- Check licenses, permissions, trademarks, contributor rights, and third-party content before public release or commercialization.
- Do not treat public availability as proof of ownership or permission to reuse.

## 12. Recovery and implementation gates

| Work item | Status in this handoff | Evidence needed to advance |
|---|---|---|
| Original `atlas_phase3_api_seed.ts` | MISSING — not supplied in this run | Original file bytes and provenance |
| Prototype UI | USER-REPORTED BUILT | Original artifact/source and reproducible inspection |
| Seed dataset (29 entities / 24 relationships) | USER-REPORTED | Original seed file and independent count |
| Atlas core packages | SPECIFIED / NOT VERIFIED IMPLEMENTED | Repository paths, code, tests, commit |
| API endpoints | SPECIFIED / NOT VERIFIED IMPLEMENTED | Route source, query tests, commit |
| Repository integration | NOT IMPLEMENTED / NOT VERIFIED | Actual repo/file/commit references |
| Storefront integration | NOT CLAIMED | Integration code and test evidence |
| Blockchain integration / mint | NOT CLAIMED | Contract, network, transaction, explorer evidence |
| Public deployment | NOT CLAIMED | Live URL and deployment evidence |
| Independent verification | PENDING | Reproducible independent checks |

## 13. Recommended execution order

1. Recover and preserve the original `atlas_phase3_api_seed.ts`; do not reconstruct it and call it original.
2. Inspect the target repository structure and existing Atlas-related files before creating or replacing implementation code.
3. Add tests for schema validation, graph traversal, cycles, missing nodes, and the five required queries.
4. Implement core/types and seed loading against the recovered source.
5. Implement API routes and connect the UI to the API.
6. Add repository/commit provenance to entities.
7. Add the evidence ledger and validation records.
8. Review privacy, licensing, and public-release readiness before publishing learning resources.

## 14. Episode and publication continuity

The supplied creative handoff includes:

- Episode 18 — The Architect Returns.
- Episode 19 — The Next Expression.
- Episode 21 — The Handoff.

These are creative/editorial assets from the handoff, not evidence of published or distributed episodes. Merch Drop 002 and 003 are design drafts; no live inventory, prices, orders, mint, or product photographs are claimed. Era 10 is described as the Atlas becoming the memory, with the rule: one node, one relationship, one proof.

Public learning resources should show the source, build steps, test results, limitations, attribution, and evidence status. Publish only material that passes the privacy and rights review.

---

**Seal statement:** This document records the supplied Atlas handoff and its implementation gates in Git history. It does not certify that the prototype, backend, routes, chain, storefront, media, or deployments are live. Originals remain authoritative; unknowns remain explicitly unresolved.
