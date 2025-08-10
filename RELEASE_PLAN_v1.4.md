# Release Plan — v1.4.0

## Milestones
- M1 Foundations — done
- M2 Ingest — done
- M3 ML Alpha — done
- M4 SOAR & EDR — done
- M5 Compliance & DLP — done
- M6 Polish & GA — in progress

## RC creation
1. `git checkout -b release/v1.4.0 develop`
2. `python scripts/version_bump.py 1.4.0-rc1`
3. Build + sign locally: `./scripts/release/release.sh 1.4.0-rc1`
4. Upload `signed_version.json` to staging `MANIFEST_URL` for RC
5. Create GitHub Release (RC) and attach installers + manifest

## GA
- Roll RC fixes into `release/v1.4.0`
- Tag `v1.4.0` on `main` and publish release notes
- Post-GA: merge release back to develop