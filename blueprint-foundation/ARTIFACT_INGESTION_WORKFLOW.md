# ScrollVerse artifact-to-GitHub intake workflow

## Purpose

Make every eligible HTML artifact, lookbook, and published site created across the ScrollVerse workstreams discoverable from the correct GitHub repository, with original files and provenance preserved.

This is an additive archival and traceability workflow. It does not move or delete source material, claim ownership, publish a site, or authorize a production deployment.

## Intake classes

1. **HTML artifacts** — standalone pages, interactive prototypes, microsites, dashboards, explainers, and generated HTML deliverables.
2. **Lookbooks and visual collections** — PDF/HTML lookbooks, source artwork, thumbnails, image sequences, and supporting metadata.
3. **Websites and site builds** — source repository, route map, build output where appropriate, deployment references, and observed public URL.
4. **Media and creative packages** — video, audio, image, 3D, and associated source/project files.

## Required record for each artifact

Create one artifact manifest using `schemas/artifact-manifest.schema.json` and one proof record using `schemas/proof-record.schema.json`. Capture, where available:

- Original title and exact source conversation/artifact identifier.
- Creation date, creator/agent attribution, and generation or production tool/version.
- Original source location and original filename; never replace the source with a derivative.
- Target repository selected by the artifact's actual subject and function.
- Destination path, commit SHA, branch, and GitHub file URL.
- SHA-256 of each archived file; record derivative relationships explicitly.
- Rights/permission status and any restrictions; unknown means unknown, not cleared.
- For a website: canonical URL, route scope, observed-at timestamp, source commit, build/test result, and deployment identifier if actually available.
- For a lookbook: source images, layout/source project, export format, thumbnail, and any image-level provenance available.
- Verification state: `pending`, `verified`, `failed`, or `unknown`, with verifier and timestamp.

## Repository routing

- Put the artifact in the repository that owns the product, site, collection, or technical system.
- Keep cross-project indexes and shared standards in `scrollverse-master-ecosystem-hub`.
- If an artifact spans multiple repositories, keep one canonical source copy and add lightweight links/references in related repositories. Do not create uncontrolled duplicate binaries.
- For the repository identity initiative, follow the protected identity blueprint specification in [issue #1](https://github.com/chaishillomnitech1/scrollverse-master-ecosystem-hub/issues/1).

## Safe ingestion sequence

1. Inventory source artifacts and record their original names, locations, dates, and identifiers.
2. Inspect file type, size, completeness, provenance, rights, and sensitive content.
3. Select the owning repository and a non-colliding destination path.
4. Copy additively; preserve the original source and existing README, artwork, code, and history.
5. Generate SHA-256 and a manifest; never treat a hash as proof of authorship, rights, or persistence.
6. Commit on a dedicated branch. Add a direct GitHub file link and a short catalog entry to the owning repository's README or artifact index without replacing existing content.
7. Open a PR for review. Run the relevant format, link, accessibility, build, or asset checks.
8. After merge, verify the exact GitHub URL resolves. For public sites, separately inspect the live URL and record the observed timestamp; a committed file does not prove deployment.
9. Update the master artifact catalog with repository, path, commit, source, hash, and verification state.

## Status vocabulary

- `inventoried`: source identified, not yet copied.
- `archived`: file committed to a repository; URL resolves.
- `validated`: required file/schema/build checks passed.
- `published`: public endpoint observed at a timestamp.
- `verified`: evidence requirements for the artifact's class are met.
- `blocked`: explicit reason recorded.
- `unknown`: evidence unavailable; do not infer success.

## Batch rollout

Process the backlog in batches by source collection or project. Start with existing HTML artifacts, lookbooks, and site deliverables that already have a known source and destination. Keep a manifest row for every item, including blocked items, so nothing disappears from the inventory. Do not claim “all artifacts archived” until the source inventory is complete and every item has a recorded disposition.

## Release boundaries

No production deployment, domain/DNS change, public media release, payment activation, financial action, token operation, legal/ownership assertion, or secret handling is authorized by an artifact-intake record. Obtain the separate approvals and evidence required for those actions.
