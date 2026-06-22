# Medallion Architecture

## 1. Bronze Layer
The bronze layer stores source-aligned data with minimal manipulation.

### Characteristics
- Raw or lightly structured ingestion
- Source timestamps and file or batch metadata retained
- Minimal business transformation
- Duplicate control handled through ingestion metadata

### Intended Use
- Reprocessing
- Replay
- Audit and lineage

## 2. Silver Layer
The silver layer standardizes and conforms data.

### Characteristics
- Business key normalization
- Reference code mapping
- Deduplication and history alignment
- Data quality validation
- Conformed customer, policy, claim, and premium entities

### Intended Use
- Operational reconciliation
- Curated downstream transformation
- Analytics-ready standardized facts and dimensions

## 3. Gold Layer
The gold layer provides business-ready outputs.

### Characteristics
- Subject-area structures
- Reporting-friendly metrics
- Aggregations by product, branch, channel, and time
- Consistent measure definitions

### Intended Use
- Executive dashboards
- Claims performance analysis
- Policy growth reporting
- Premium collection reporting

## 4. Governance Alignment

- Unity Catalog can govern the logical zones and access permissions.
- Delta Lake can preserve historical versions and transactional consistency.
- Delta Live Tables can enforce pipeline quality logic.
- Databricks Workflows can orchestrate incremental processing across layers.

