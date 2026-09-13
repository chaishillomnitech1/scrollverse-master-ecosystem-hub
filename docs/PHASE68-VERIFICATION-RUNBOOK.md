# Phase 68 Verification Runbook

**Purpose:** move the Phase 68 registry from recorded design state toward reproducible verification without inflating claims.

## Evidence states

1. **PROPOSAL_ONLY** — design intent exists; implementation is not established.
2. **IMPLEMENTED** — artifact exists and is readable in the inspected workspace.
3. **GIT_RECORDED** — artifact is committed to Git history at a known commit.
4. **DEPLOYED** — the intended public endpoint is reachable and the relevant artifact can be identified there.
5. **INDEPENDENTLY_VERIFIED** — an external verification step confirms the stated property.

These states are cumulative evidence labels, not synonyms.

## Current baseline

- Phase: `PHASE_68_BASELINE`
- Baseline diagnostic commit: `1c7c635e21b72706bfa6ed23c2d88ce0a6a2784e`
- Repository: `chaishillomnitech1/scrollverse-master-ecosystem-hub`
- Current hardening commits include the machine-readable schema and mock verifier tests.
- Independent verification remains `PENDING` unless a separate run produces evidence.

## Execution order

```text
PING WORKSPACE
    ↓
RUN REPOSITORY STATE VERIFIER
    ↓
VALIDATE REGISTRY AGAINST JSON SCHEMA
    ↓
REVIEW PROVENANCE LOG
    ↓
COMMIT INTENTIONAL CHANGES
    ↓
CREATE RELEASE
    ↓
VERIFY RELEASE INTEGRITY
    ↓
VERIFY DEPLOYMENT
    ↓
INDEPENDENT AUDIT
```

## Mock path test

`tests/test_ping_script_paths.py` creates temporary workspaces and verifies two cases:

- missing critical dependencies → non-zero exit and `MISALIGNED`
- all critical dependencies present → zero exit and `READY FOR EXECUTION`

This test validates the verifier's behavior without making any statement about a particular developer machine.

## Release integrity

For a GitHub immutable release, enable release immutability before publishing the release intended to be locked. GitHub states that immutable releases lock the associated tag and release assets and automatically generate a cryptographically verifiable release attestation.

After publication, verify with:

```bash
gh release verify RELEASE-TAG
```

For a local release asset:

```bash
gh release verify-asset RELEASE-TAG ARTIFACT-PATH
```

## Zero-inflation rule

Never upgrade a state merely because a file says that the state is verified. Verification status must be derived from an actual observation or an explicitly identified external source.

In particular:

- a Git commit proves the commit exists;
- a file hash proves the bytes hashed at the time of hashing;
- a release proves the release exists;
- an immutable release protects the published tag and assets;
- a reachable endpoint establishes reachability at the time checked;
- none of these alone proves real-world deployment, adoption, financial performance, scientific validity, or ownership.

## Governing statement

> **Nothing erased. Nothing inflated. Nothing hidden. Everything contextualized.**

`PENDING` is a valid and intentional state. It is not a defect in the archive.
