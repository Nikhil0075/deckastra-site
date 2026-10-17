---
title: Scalability
---

# Scalability, isolation, and present constraints

## Implemented today

- Stateless Cloud Run web and API services.
- Cloud SQL as the stateful PostgreSQL authority.
- Export jobs isolated from interactive requests.
- Job leasing, retries, idempotency, and structured failure states.
- Private object storage with lifecycle controls.
- Provider quotes, credit reservations, daily limits, and an AI-only spend stop.

## Current limits

- The small hackathon shape is intended for demos and a handful of people, not broad production traffic.
- Capacity, recovery, alert receipt, and security acceptance are not complete.
- Provider availability and quotas remain external dependencies.
- The current web application has no verified public URL for this documentation site to link.

## Future scaling work

Load-test representative authoring and export journeys, rehearse recovery with measured objectives, validate alert delivery, keep workers independently scalable, and increase database capacity only with evidence.

<ArchitecturePanel image="/diagrams/08-scaling-failure-cost-controls.svg" title="Scaling, failure, and cost controls" caption="Interactive services, background work, persistence, and provider cost fail along different boundaries." />
