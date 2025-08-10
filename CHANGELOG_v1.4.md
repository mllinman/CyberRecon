# Changelog — v1.4.0

## Highlights
- Compliance uplift: **NIST CSF, NIST 800-53** mappings, multi-framework reports (GDPR/HIPAA/PCI/ISO).
- Cloud connectors: **AWS CloudTrail/GuardDuty**, **Azure Activity/Security**, **GCP Audit** (initial).
- Endpoint: Agent-based deployer (light telemetry), process/file/network audit.
- SIEM/EDR UX: unified timeline, MITRE ATT&CK overlays, rule packs.
- SOAR: built-in playbooks (block IP, isolate host, disable user, quarantine file, open ticket) + approvals/dry-run.
- ML: baseline anomaly models + explainer panels.
- DLP: USB/file exfil monitoring, PII/PCI detectors (tunable).
- Pentesters tab: curated OSS tools with on/off and auto-update controls.
- Offline mode: full operation + offline updates.
- Integrity: CLI and UI verifier; auto first-launch check.

## Notes
- Feature flags default OFF for ML/SOAR/EDR until GA.
- New `config/settings.json` keys may require migration.