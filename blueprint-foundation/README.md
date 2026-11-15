# Machine-readable ScrollVerse foundation

This directory defines additive, versioned record shapes for the production-factory blueprint. It is a schema foundation, not a running agent system, event database, deployment, or legal determination.

## Schemas

- `signal.schema.json` — observations entering the signal-to-work pipeline. Keeps observation separate from interpretation.
- `agent-task.schema.json` — scoped work assigned to an independently identified agent, including permissions, model provenance, outputs, and review state.
- `canon-event.schema.json` — append-only canon lifecycle: proposal, review, authorized decree, propagation, correction, or rejection.
- `artifact-manifest.schema.json` — creator/source lineage, file hashes, generation metadata, rights status, preservation evidence, and publication state.
- `proof-record.schema.json` — claims linked to dated evidence and an explicit verification status.

## Governing rules

1. Preserve source records. Corrections create new records and link to the superseded record; do not rewrite history.
2. A screenshot is snapshot evidence. Prefer independently resolvable commits, CI runs, deployment IDs, transaction hashes, provider records, and storage proofs.
3. Distinguish observed facts from interpretation, estimates, pending work, and claims supplied by a source.
4. Agent identity and authorship remain attributable. Coordination does not merge independent identities.
5. Permissions are explicit and least-privilege. A task record is not authorization to execute a restricted action.
6. Production deployment, public release, financial actions, payouts, token operations, custody, and regulated ownership claims require separate authorization and evidence.
7. A content hash proves byte identity, not authorship, rights, availability, or persistence. A CID alone does not prove pinning or archival durability.

## Versioning

These files are initial schema version `1.0.0`. Breaking changes require a new versioned schema or a reviewed compatibility plan. Store instance records separately from schema definitions; do not put secrets or private credentials in records.

## Status

Schema definitions only. Validation fixtures, an append-only event store, CI enforcement, dashboards, and runtime adapters are subsequent implementation stages.
