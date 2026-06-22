# Row Volume Estimates

## 1. Volume Assumptions
The estimates below represent a medium-sized P&C insurer with stable growth and a multi-year data retention horizon.

- Customers grow steadily through organic business and renewals
- Policies expand with product mix and cross-sell
- Claims volumes remain lower than policy counts but have high financial significance
- Audit rows grow faster than core entities because every change may create a record

## 2. Estimated Row Counts

| Entity | Estimated Current Rows | Estimated Annual Growth |
|---|---:|---:|
| customer | 500,000 | 8% |
| customer_address | 900,000 | 10% |
| business_customer | 80,000 | 12% |
| agent | 12,000 | 3% |
| broker | 4,000 | 4% |
| branch | 250 | 1% |
| underwriter | 1,500 | 5% |
| insurance_product | 4 | 0% |
| coverage_type | 75 | 5% |
| policy | 2,500,000 | 12% |
| policy_version | 4,500,000 | 15% |
| policy_coverage | 9,500,000 | 16% |
| vehicle | 850,000 | 11% |
| property | 420,000 | 10% |
| premium | 7,500,000 | 14% |
| premium_payment | 18,000,000 | 18% |
| claim | 180,000 | 9% |
| claim_reserve | 420,000 | 12% |
| claim_payment | 1,100,000 | 15% |
| lookup tables | 2,500 | 2% |
| reference tables | 1,200 | 2% |
| audit tables | 40,000,000 | 22% |

## 3. Interpretation

- Policy, premium, and audit volumes dominate storage and processing requirements.
- Claim volumes are smaller than policy volumes but require stronger operational integrity and traceability.
- Versioned policy data grows faster than the base policy table because endorsements and renewals create new states.

## 4. Planning Implications

- Operational storage should anticipate multi-year retention.
- Analytical workloads should isolate heavy historical scans from day-to-day servicing workloads.
- Audit data may require partitioning or lifecycle management in future physical implementation.

