# Entity List

## 1. Master Entities

| Entity | Description |
|---|---|
| customer | Core insured party anchor |
| customer_address | Customer location and mailing details |
| business_customer | Business-specific customer profile |
| agent | Authorized sales representative |
| broker | External intermediary representing a customer or risk |
| branch | Organizational operating unit |
| underwriter | Risk authority responsible for approval |
| insurance_product | Commercial product offering |
| coverage_type | Standardized coverage catalog entry |

## 2. Sales & Quotation Entities

| Entity | Description |
|---|---|
| quote | Initial insurance quotation generated for a customer |
| quote_version | Version history of a quotation throughout the underwriting process |

## 3. Policy Entities

| Entity | Description |
|---|---|
| policy | Primary insurance contract record |
| policy_version | Versioned policy state over time |
| policy_transaction | Business events such as New Business, Renewal, Cancellation, Endorsement, and Reinstatement |
| policy_coverage | Coverage selection on a policy version |
| vehicle | Insured auto asset |
| property | Insured physical asset |

## 4. Financial Entities

| Entity | Description |
|---|---|
| premium | Premium obligation by policy and version |
| premium_payment | Payment received against premium due |

## 5. Claims Entities

| Entity | Description |
|---|---|
| fnol | First Notice of Loss captured before formal claim registration |
| claim | Loss event and claim case record |
| claim_note | Investigation notes and claim activity history |
| claim_reserve | Current estimated financial liability for a claim |
| claim_reserve_transaction | Historical reserve movements and reserve adjustments |
| claim_payment | Actual disbursement made against an approved claim |

## 6. Supporting Entities

| Entity | Description |
|---|---|
| policy_party_role | Defines the relationship between parties and policies (e.g., Policy Holder, Driver, Beneficiary, Business Contact) |
| rating_factor | Rating attributes used for premium calculation |
| lookup_tables | Controlled code sets such as status, frequency, payment methods, and policy types |
| reference_tables | Slowly changing reference values and business descriptors |
| audit_tables | Change history, audit trail, and operational traceability |

## Notes

This entity model represents a normalized enterprise Operational Data Model (OLTP) for a Property & Casualty (P&C) insurance company.

The model is designed to support future implementation using:

- PostgreSQL
- Apache Airflow
- Azure Data Lake Storage Gen2 (ADLS Gen2)
- Azure Databricks
- Unity Catalog
- Delta Lake
- Delta Live Tables (DLT)
- Databricks Workflows
- dbt
- Power BI

The design follows Third Normal Form (3NF) principles and is intended to support enterprise scalability, historical traceability, and compatibility with a Medallion Lakehouse Architecture.