# v1.4 Merge Checklist (2025-08-09)

## Code complete checks
- [ ] All planned features toggled behind **feature flags**.
- [ ] Config schema updated in `config/settings.json` (default flags set).
- [ ] CI green on release branch (Linux/Windows builds + signed manifest).
- [ ] SBOM generated (if applicable) and dependencies audited.

## Security & Compliance
- [ ] Updater public key matches signing private key in CI secrets.
- [ ] Compliance: NIST CSF, 800-53, GDPR/HIPAA/PCI mappings reviewed.
- [ ] `docs/compliance/Compliance_Control_Matrix.(csv|pdf|html)` updated.

## UX & Docs
- [ ] Help → Documentation submenu lists all docs.
- [ ] Roadmap updated for v1.4 scope and v1.5 preview.
- [ ] Tutorial & Runbook included in `docs/`.
- [ ] Integrity verifier present and working.

## Packaging
- [ ] PyInstaller build OK, `hash_manifest.json` generated.
- [ ] `signed_version.json` created by local release script.
- [ ] Inno/WiX installers build and (optionally) codesign completes.

## Release steps
- [ ] Bump version to `1.4.0-rcN` on `release/v1.4.0`.
- [ ] Tag RC; verify installers + manifest.
- [ ] Merge to `main`; tag `v1.4.0` when ready.