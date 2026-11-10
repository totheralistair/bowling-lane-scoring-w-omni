# OMNI bug report: guide state can't move into project scope

**Date found:** 2026-11-09
**Tools:** `omni-ee guide-state` (skill bundle v0.9.1, build 2026-11-09), `omni start`

## What I was trying to do

I finished repository setup for a project and wanted to move the guide run out of the shared, per-machine state (`~/.omni-ee/guide-state.json`) and into the project. Then I could start a second OMNI project on the same Mac without the two sharing one guide state.

## What happens

- `omni-ee guide-state migrate` accepts only `--from-phase repo_readiness`. Any other source phase is refused: *"migration source must be repo_readiness"*.
- The guide run was in phase `pre_repo`. No command moves a run's phase from `pre_repo` to `repo_readiness`:
  - `bind-environment --phase repo_readiness` fails: *"loaded active state phase does not match requested placement"*.
  - `next-action --next-phase repo_readiness` sets only the next action; the phase stays `pre_repo`.
  - `record-intent` + `complete-step` (with result and validation refs) records the step; the phase stays `pre_repo`.
  - `omni start --no-launch` from the project folder records an audit entry; the phase stays `pre_repo`.
- After those, `migrate` (default phases) fails with *"loaded parked state does not match requested parked placement"*.
- The repository itself was ready: `repository-readiness.sh` exit 0, and `project-binding validate` status ready.

## What I expected

Once repository readiness passes, a supported command, or `omni start` itself, should advance the run to `repo_readiness` so that `guide-state migrate` can move it into the project.

## Impact

Only one OMNI guide run can exist per Mac. Running a second project means swapping `~/.omni-ee/guide-state.json` in and out by hand.

## Workaround in use

At the end of a session, copy `~/.omni-ee/guide-state.json` to `<project>/.omni-ee/guide-state-parked-YYYYMMDD.json`, then delete the original. At the start of a session, copy it back. The lock files are left alone.

## Also noticed

`omni-ee --check-update` reports *"update check failed: lookup latest release: HTTP 404 Not Found"*.
