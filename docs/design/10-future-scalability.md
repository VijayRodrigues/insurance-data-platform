# Future Scalability

## 1. Scalability Objectives
The design is intended to support future evolution without forcing a redesign of the core business model.

- Scale from operational serving to analytical lakehouse processing
- Maintain consistent business keys across platforms
- Support late-arriving changes and historical reconstruction
- Enable domain-oriented data ownership and quality controls

## 2. PostgreSQL Readiness

- The logical design is normalized and suitable for transactional storage.
- Business keys and foreign keys are explicit.
- Versioned records preserve historical state without overwriting prior values.
- Audit tables support operational traceability.

## 3. Lakehouse Readiness
The same logical model can be mapped into a lakehouse pattern:

- Raw landing for source-aligned ingestion
- Cleansed conformed datasets for business entities
- Curated analytical layers for reporting and semantic models

## 4. Medallion Architecture Fit

- Bronze layer: ingest source extracts with minimal transformation
- Silver layer: standardize keys, types, code values, and history logic
- Gold layer: produce business-ready analytical marts and subject-area views

## 5. Future Compatibility Targets

| Technology | Compatibility Notes |
|---|---|
| PostgreSQL | Suitable for operational master and transaction data |
| Apache Airflow | Suitable for orchestration of ingestion, validation, and refresh tasks |
| Azure Data Lake Storage Gen2 | Suitable for storage of staged and curated files |
| Azure Databricks | Suitable for transformation, quality, and analytic processing |
| Unity Catalog | Suitable for governance, access control, and lineage |
| Delta Lake | Suitable for historical, transactional, and analytical storage patterns |
| Delta Live Tables | Suitable for managed pipeline logic and quality constraints |
| Databricks Workflows | Suitable for multi-step orchestration |
| dbt | Suitable for transformation modeling and documentation in the analytics layer |
| Power BI | Suitable for semantic reporting and executive dashboards |

## 6. Scaling Principles

- Preserve 3NF in the operational layer.
- Add curated analytical structures rather than compromising source integrity.
- Keep business keys stable across processing layers.
- Design for policy, premium, and claims history growth as the main drivers of scale.

