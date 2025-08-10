# CyberRecon Suite — v1.4 Branching Plan

## Branch strategy
- `main` — stable, tagged releases only.
- `develop` — integration branch for upcoming minor versions.
- `release/v1.4.0` — stabilization branch for v1.4 (bug fixes & docs only).
- `feature/*` — short-lived feature branches (squash-merge into develop).

## Commands (reference)
```bash
# Create release branch from develop
git checkout develop
git pull
git checkout -b release/v1.4.0

# Freeze features, allow only: bug fixes, docs, perf
# Update version
python scripts/version_bump.py 1.4.0-rc1
git commit -am "chore: bump to 1.4.0-rc1"

# Tag RC (optional)
git tag v1.4.0-rc1
git push origin release/v1.4.0 --tags
```

## After GA
```bash
# Merge release -> main
git checkout main
git merge --no-ff release/v1.4.0
git tag v1.4.0
git push origin main --tags

# Back-merge to develop (to keep history in sync)
git checkout develop
git merge --no-ff release/v1.4.0
git push origin develop
```