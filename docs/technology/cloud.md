---
title: Cloud architecture
---

# Google Cloud architecture

The observed Release 8 topology uses a public Cloud Run web service and API, a private export worker, a migration job, Cloud SQL for PostgreSQL authority, and private object storage. Identity and provider calls cross explicit server-side boundaries.

<ArchitecturePanel image="/diagrams/06-google-cloud-topology.svg" title="Sanitized Google Cloud topology" caption="Web, API, worker, migration, database, storage, identity, and provider boundaries." />

## Evidence boundary

Release 8 was observed on the web, API, and export worker with a passing production smoke on 17 October 2026. That does not by itself establish broad load, disaster-recovery, alert-receipt, or penetration acceptance.

The [public web application](https://deckastra-web-794139896808.asia-south1.run.app/) is hosted on Cloud Run for the hackathon and was independently confirmed to return its HTML application shell. The separate API service is intentionally not presented as the web application.
