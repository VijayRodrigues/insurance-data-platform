# Table Dependencies

## 1. Dependency Principles
Dependency order is driven by parent-child integrity and lookup/reference prerequisites.

## 2. Load Sequence

| Sequence | Entity Group | Dependency Notes |
|---|---|---|
| 1 | lookup tables, reference tables | Must exist before transactional records |
| 2 | branch, insurance_product, coverage_type | Foundational operating and product setup |
| 3 | customer | Root party entity |
| 4 | customer_address, business_customer | Depend on customer |
| 5 | agent, broker, underwriter | Depend on branch and reference data |
| 6 | vehicle, property | Depend on customer |
| 7 | policy | Depends on customer, product, distribution, and underwriting entities |
| 8 | policy_version | Depends on policy |
| 9 | policy_coverage | Depends on policy_version and coverage_type |
| 10 | premium | Depends on policy and policy_version |
| 11 | premium_payment | Depends on premium |
| 12 | claim | Depends on policy and policy_coverage |
| 13 | claim_reserve, claim_payment | Depend on claim |
| 14 | audit tables | Capture changes after upstream entities exist |

## 3. Relationship Dependency Detail

| Child | Parent | Dependency Reason |
|---|---|---|
| customer_address | customer | An address cannot exist without a customer |
| business_customer | customer | Business profile extends customer |
| agent | branch | Agent organizational assignment |
| underwriter | branch | Underwriter organizational assignment |
| policy | customer, branch, product, underwriter | Core issuance dependencies |
| policy_version | policy | Version history cannot precede policy creation |
| policy_coverage | policy_version, coverage_type | Coverage must attach to a policy state and valid coverage code |
| premium | policy, policy_version | Billing derives from issued policy state |
| claim | policy, policy_coverage | Loss must reference a valid policy and applicable coverage |
| claim_reserve | claim | Reserve only exists after claim initiation |
| claim_payment | claim | Payment only exists after claim acceptance and settlement controls |

## 4. Referential Integrity Considerations

- Foreign keys should be enforced for all core transactional relationships.
- Business key uniqueness should be maintained at the entity level.
- Soft changes, such as status or effective date updates, should create new versioned records rather than overwrite historical facts where the business context requires traceability.

