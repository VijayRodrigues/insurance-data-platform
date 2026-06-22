# Indexing Strategy

## 1. Indexing Objectives
The indexing strategy supports:

- Fast policy lookup by policy_number and customer
- Fast claim lookup by claim_reference and policy
- Efficient premium due-date collections and payment searches
- Operational joins across policy, version, coverage, and claim entities
- Read-heavy analytics acceleration without denormalizing the source model

## 2. Recommended Logical Indexes

| Entity | Recommended Indexes |
|---|---|
| customer | customer_number, national_identifier, customer_type_code |
| customer_address | customer_id, address_type_code, postal_code |
| business_customer | customer_id, tax_identifier, industry_code |
| agent | agent_number, branch_id, agent_status_code |
| broker | broker_number, broker_status_code |
| branch | branch_number, region_code |
| underwriter | underwriter_number, branch_id |
| insurance_product | product_code, product_line_code, product_status_code |
| coverage_type | coverage_code, product_line_code, coverage_category_code |
| policy | policy_number, customer_id, branch_id, policy_status_code, policy_effective_date |
| policy_version | policy_id, policy_version_number, version_effective_date |
| policy_coverage | policy_version_id, coverage_type_id, vehicle_id, property_id |
| vehicle | vin, customer_id, registration_number |
| property | property_number, customer_id, postal_code |
| premium | policy_id, policy_version_id, due_date, premium_status_code |
| premium_payment | premium_id, payment_date, payment_reference |
| claim | claim_reference, policy_id, loss_date, claim_status_code |
| claim_reserve | claim_id, reserve_as_of_date, reserve_type_code |
| claim_payment | claim_id, payment_date, payment_reference |
| audit tables | source_table_name, source_record_key, change_timestamp |

## 3. Access Path Guidance

- Policy servicing primarily filters by policy_number, customer_id, and status.
- Claims operations primarily filter by claim_reference, policy_id, and loss date.
- Premium collections primarily filter by due_date and payment status.
- Reporting workloads should use curated analytical structures rather than forcing the operational model to serve ad hoc aggregates.

## 4. Indexing Notes

- Unique business keys should be indexed and enforced.
- Foreign key columns should be indexed to support joins and delete/update checks.
- Time-based predicates should have supporting indexes where operational search patterns justify them.
- Avoid over-indexing low-cardinality status fields unless they are paired with a selective business key or date filter.

