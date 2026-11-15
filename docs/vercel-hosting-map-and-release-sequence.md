# Vercel Hosting Map — Portfolio Snapshot

**Snapshot:** 2026-11-14  
**Team scope:** `chaishillomnitech1-d2ca6004`  
**Projects inspected:** 20  
**Machine-readable registry:** `registry/vercel-hosting-map.v1.json`

## Observed inventory

| Vercel latest deployment state | Projects |
|---|---:|
| READY | 11 |
| ERROR | 4 |
| No deployment observed | 5 |
| Total | 20 |

- 19 projects have SSO protection enabled; the `chaishillomnitech1` project now has SSO disabled.
- No custom domains are attached to this Vercel team.
- Every project returned `live=false`, including projects whose latest deployment state is READY.
- A READY deployment is not an HTTP reachability test and does not establish that the public website is operational.
- The account returned HTTP 402 `resource_creation_blocked` for a new production deployment because the Vercel team is suspended pending a valid payment method.

## Exact repository mappings

The machine-readable registry records the project ID, project name, GitHub repository, branch, commit SHA, latest deployment ID/state/URL, SSO state, and duplicate relationship for each project.

### Duplicate project groups

- `scrollverse_commerce`: two Vercel projects, both linked to the same GitHub repository and same main commit; both latest deployments are ERROR.
- `nextjs-commerce`: two Vercel projects, both linked to the same repository and same main commit; both latest deployments are ERROR.
- `Expansion-`: three Vercel projects linked to the same repository and same main commit; all three latest deployments are READY.
- `nextjs-boilerplate`: four Vercel projects linked to the same repository and same main commit; all four latest deployments are READY.
- `Chaishillomnitech1`: two Vercel projects linked to the same repository and same main commit; both latest deployments are READY. SSO was disabled only on the `chaishillomnitech1` project.

Duplicate project records are not deleted or consolidated by this snapshot. The primary project and custom-domain owner must be confirmed before consolidation.

## Missing production mapping

`scrollverse-web-app` did not appear as a GitHub-linked project in the 20-project Vercel team inventory. It therefore needs a deliberate Vercel project mapping after the team is reactivated. No custom domain is attached to this team, so `scrollverse.co` is not currently routed through this Vercel inventory.

## Release sequence

1. Reactivate the Vercel team through its billing flow; do not bypass the HTTP 402 restriction.
2. Establish one canonical Vercel project per application repository and record the exact GitHub link.
3. Link `scrollverse-web-app` to its own Vercel project with the intended root directory and production branch.
4. Re-run the merged commerce build and publish to the canonical commerce project.
5. Attach and verify the intended custom domain only after the correct application and production route are confirmed.
6. Keep preview and non-public projects protected; make only approved customer-facing production domains public.
7. Verify HTTP reachability, route behavior, SSL, checkout, and customer-facing terms after deployment.

## Evidence and limitations

The registry is based on direct Vercel project and deployment metadata reads. It is a project-to-repository mapping snapshot, not a full audit of every deployment, alias, GitHub branch, custom DNS record, external hosting account, or live HTTP response. The Manus-hosted `scrollverse.co` billing and DNS state is outside this Vercel team inventory.
