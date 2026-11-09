# Atlas Core — Graph, Lineage, and Unified Discovery
Date: 2026-11-09
Status: IMPLEMENTATION IN REVIEW — OPEN DRAFT PR

## Repository implementation
- Application repository: `chaishillomnitech1/scrollverse-web-app`
- Feature branch: `feature/atlas-core-graph-lineage`
- Pull request: https://github.com/chaishillomnitech1/scrollverse-web-app/pull/7
- Latest observed head commit: `bbe267cd2a3d738f9a868b7116c352f955bc9c76`
- PR state: OPEN, DRAFT, mergeable at last inspection; not merged.

## Implemented in the feature branch
- MySQL/Drizzle `atlas_entities` and `atlas_relationships` tables.
- Source-aware evidence fields and provenance labels; optional links to `evidence_ledger`.
- Reviewed migration `drizzle/0049_atlas_core.sql`, journal entry, and schema snapshot.
- The migration also creates the `evidence_ledger` table introduced in the prior merged schema work, because the prior migration snapshot did not yet contain that table.
- Deterministic breadth-first traversal supports outgoing, incoming lineage, and bidirectional discovery, bounded to five hops.
- Five graph tests cover traversal order, incoming lineage, cycles, missing roots, and depth bounds.
- Public tRPC read endpoints expose only PUBLISHED + PUBLIC entities and relationships.
- Administrator-only create and publish procedures; new entities and edges begin DRAFT + PRIVATE.
- React explorer at `/atlas-core`, linked from the existing Creator Atlas page.
- `test:sovereign` includes both invariant and graph test suites.

## Validation evidence
- Run `42683605411`, commit `083481462b6f0aa5e8b1f84ba6bba8250361957a`: TypeScript check PASS; 2 test files PASS; 9 tests PASS.
- A later small change on the current head adds source URL and updated timestamp fields to the search result projection.
- Run `42683650557`, current head `bbe267cd2a3d738f9a868b7116c352f955bc9c76`: IN PROGRESS at last inspection. Do not mark the latest head validated until this run completes successfully.
- An earlier run failed on implicit-any callback types and a Map iterator target issue; these were corrected, and the subsequent run passed.

## Not yet done
- PR #7 has not been merged.
- No database migration has been applied to development or production.
- No Atlas records have been seeded or published.
- No production deployment or external ingestion has occurred.
- The graph engine is deterministic traversal over the current bounded public record set; it is not yet a cross-platform crawler, semantic inference engine, or autonomous archive importer.

## Next gates
1. Confirm CI on the latest PR head.
2. Review migration SQL, Drizzle snapshot, and authorization behavior.
3. Apply the migration only through the approved database change process.
4. Seed a small, source-backed Atlas collection with explicit provenance.
5. Verify list/search/lineage behavior against the migrated database.
6. Expand source ingestion and cross-project discovery only after the first records are auditable.

## Integrity rule
A relationship is a documented connection, not proof that two records are equivalent or that an external claim is true. Preserve source, interpretation, and verification state separately.
