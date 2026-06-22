# Source Systems

## 1. Source Landscape
The platform assumes the following classes of source systems:

| Source System Type | Role |
|---|---|
| Policy administration system | Holds policy, customer, underwriting, and coverage data |
| Billing system | Manages premium invoicing and payment receipt data |
| Claims system | Manages loss intake, reserves, and claim payments |
| Reference/master data system | Maintains code sets and enterprise reference values |
| Organization directory | Maintains branches, users, and organizational assignments |

## 2. Source Ownership

| Domain | Primary Source Ownership |
|---|---|
| Customer | Policy administration system |
| Addresses | Policy administration system |
| Business customer | Policy administration system or customer master |
| Agent and broker | Distribution master or policy administration system |
| Branch and underwriter | Organization or underwriting master |
| Product and coverage | Product catalog or product governance system |
| Policy and versions | Policy administration system |
| Premium and payments | Billing system |
| Claims, reserves, and claim payments | Claims system |
| Lookup and reference data | Master data management or reference repository |

## 3. Integration Considerations

- Source systems may use different identifiers for the same real-world party.
- Business keys must be standardized during conformance.
- Effective dating is critical for policy and claim history.
- Source-to-target lineage must be preserved for auditability.

## 4. Ingestion Expectations

- Scheduled extracts for stable operational data
- Incremental change capture where available
- Reference and lookup refreshes on a controlled cadence
- Validation of required business keys before promotion to curated layers

