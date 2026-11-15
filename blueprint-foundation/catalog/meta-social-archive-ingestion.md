# Meta Social Archive — Exhaustive Collection Specification

Created: 2026-11-14
Owning catalog: `scrollverse-master-ecosystem-hub/blueprint-foundation/catalog/`
Status: `SPECIFIED / SOURCE ACCOUNT ACCESS REQUIRED / NO META EXPORT INGESTED YET`

## Objective

Build one provenance-preserving master archive of the account owner's Facebook and Instagram publishing history and associated engagement records, then connect media and derivatives to their owning ScrollVerse repositories.

This specification covers organic account content. Paid-ad reporting is a separate dataset and must not be mixed with organic post history.

## Collection scope

### Published content
- Facebook Page posts, photos, videos, Reels, stories where exportable, albums, live-video records, captions, timestamps, permalinks, IDs, tags/mentions, location metadata where available, and attached media.
- Instagram posts, carousels, photos, videos, Reels, stories/highlights where exportable, captions, timestamps, permalinks, IDs, tags/mentions, collaborator data where available, and attached media.
- Original media bytes, platform-exported versions, thumbnails, captions, alt text, and available metadata.
- Deleted, archived, draft, or expired items only when the official account export or authorized source includes them. Absence from an export is not proof an item never existed.

### Engagement and relationship records
Capture each available category as its own record, including the actor and target when the platform export exposes them:
- Likes/reactions and reaction type.
- Comments, replies, timestamps, and author identifiers/names as exported.
- Shares/reposts and available destination/timestamp metadata.
- Saves/bookmarks only where the account's official export or authorized connector exposes them.
- Tags, mentions, collaborator invitations, and tagged-media references.
- Story replies, story interactions, and other engagement types only where included in the source export.
- Insights (reach, impressions, plays, watch time, saves, shares, comments, profile actions) stored separately from interaction-level records, with metric definitions and reporting windows.

Private or third-party information must be handled only within the account owner's authorized export and access scope. Do not attempt to bypass platform permissions or infer hidden engagement records.

## Authoritative sources and access

1. Prefer Meta Accounts Center's official Download Your Information export for the relevant Facebook and Instagram profiles, selecting the broadest available date range, media quality, content categories, and machine-readable format (JSON where offered; include HTML only as a readable companion).
2. Preserve the original downloaded archive unchanged. Record export request date, completion date, selected accounts, selected categories, date range, format, and any platform-reported omissions.
3. Use connected analytics providers only as supplemental sources. Their data coverage, historical retention, and metric definitions must be recorded; analytics connectors are not assumed to provide a complete media archive or every like/save/share/tag.
4. Never store passwords, access tokens, session cookies, recovery codes, or private keys in GitHub or the catalog.

## Record model

Every content item receives a stable archive ID and fields:
- platform, account/page identity label, platform object ID, permalink;
- content type, caption/text, original timestamp and timezone if supplied;
- source export filename/path and source archive checksum;
- media filename, MIME type, byte size, SHA-256, and media relationship;
- tags, mentions, collaborators, location metadata only when supplied;
- source method, export timestamp, collection date, and completeness notes;
- owning ScrollVerse repository, destination path, commit SHA, and direct GitHub URL;
- derivative-of relationship for resized, transcoded, edited, or designed outputs;
- rights/permission state, privacy classification, and publication approval;
- verification state and verifier timestamp.

Every engagement item receives a separate stable record:
- platform, engagement type, target content archive ID, platform interaction ID if supplied;
- actor identity only as provided by authorized export;
- interaction timestamp and content (for comments/replies);
- source export filename/path and extraction version;
- visibility/access limitations and completeness notes.

## Safe intake and archival sequence

1. Receive the official export or authorized connected-source data.
2. Inventory the archive before extraction; preserve the untouched original and compute SHA-256 for the complete export.
3. Parse each platform's JSON/HTML and enumerate every content and engagement record; record category totals and any gaps.
4. Extract media to a staging area, preserve original filenames and bytes, and compute SHA-256 per file.
5. Deduplicate by cryptographic hash without deleting duplicate source records; retain all platform relationships and source paths.
6. Classify each artifact and route it to the repository that owns the work. Cross-repo copies are derivatives or mirrors and must reference the canonical original.
7. Check destination paths and repository policies; add files only, never overwrite existing README, source, artwork, or prior archive entries.
8. Create per-item artifact/proof manifests and a master index; keep private or sensitive content out of public repositories.
9. Commit through dedicated branches and reviewable PRs. Fetch each committed file back and verify its content/hash.
10. Verify public live deployments independently from GitHub commits; record URL, deployment ID, observed time, and source commit where available.
11. Reconcile source totals against archived totals. Mark categories complete only when counts reconcile or documented platform limitations explain the difference.

## Completeness states

- `not_requested`: source export has not been requested.
- `awaiting_export`: account owner has not supplied the official export or authorized source.
- `received_uninspected`: archive received but not enumerated.
- `inventory_in_progress`: platform records and media being enumerated.
- `partially_archived`: some items processed; gaps remain.
- `reconciled`: exported records accounted for with documented exclusions.
- `verified_in_repository`: committed files fetched back and hashes match.
- `deployment_verified`: live deployment separately observed.
- `blocked_access`: required platform permissions or source data unavailable.

No claim of exhaustive collection is permitted until platform export scope, category counts, parsed totals, media totals, and exclusions have been reconciled.

## Current intake record

- Meta AI content supplied in chat: seven screenshot descriptions and associated textual transcription are preserved in the existing Infinite-Nexus PR #163 evidence record; this is a textual transcription, not the original seven binary screenshots.
- Additional SVG/image markers in the latest message: no SVG source bytes or separately attached image files were available to ingest from those markers alone.
- Facebook/Instagram account export: not connected or supplied in this turn.
- Posts/media/engagement fetched: 0.
- Per-item media hashes: 0.
- Live social content deployment: not applicable; platform permalinks will be recorded as source references when available.
- Current state: `awaiting_export`.

## Owner-provided source handoff

Provide the official Meta export ZIP(s) for the Facebook and Instagram account(s), or connect an authorized provider with clearly documented coverage. Do not send credentials or tokens. The archive will be preserved unchanged before extraction and then processed against this specification.
