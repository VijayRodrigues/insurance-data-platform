# Database Standards

## Purpose

This document defines the database design standards for the Insurance Data Platform.

All PostgreSQL tables in this project must follow these standards to ensure consistency, maintainability, scalability, and enterprise-quality implementation.

---

# Database

| Standard | Value |
|----------|-------|
| Database | insurance_platform |
| Database Engine | PostgreSQL 17 |
| Character Encoding | UTF-8 |
| Naming Convention | lowercase_snake_case |

---

# Schemas

The project is organized into logical schemas.

| Schema | Purpose |
|---------|---------|
| master | Master and reference business entities |
| sales | Quotes and quotation process |
| policy | Policies and policy lifecycle |
| finance | Premiums and financial transactions |
| claims | Claims processing |
| reference | Lookup and reference data |
| audit | Audit and operational logging |

---

# Table Naming Standards

- Use lowercase.
- Use singular names.
- Use snake_case.
- Avoid prefixes like `tbl_`.
- Avoid abbreviations unless universally accepted.

### Examples

```
customer
policy
claim
premium_payment
vehicle
```

---

# Column Naming Standards

- Use lowercase.
- Use snake_case.
- Primary key format:

```
customer_id
policy_id
claim_id
```

- Foreign key must use the same column name as the referenced primary key.

Example:

```
customer.customer_id

↓

policy.customer_id
```

---

# Primary Keys

Every business table will use:

```sql
BIGSERIAL PRIMARY KEY
```

Example:

```sql
customer_id BIGSERIAL PRIMARY KEY
```

---

# Business Keys

Business identifiers are separate from internal primary keys.

Examples:

```
customer_number
policy_number
quote_number
claim_reference
```

Business keys must be unique.

---

# Audit Columns

Unless there is a strong business reason otherwise, every table should contain:

```sql
created_at
updated_at
created_by
updated_by
```

---

# Soft Delete

Business tables should support logical deletion.

```sql
is_deleted BOOLEAN DEFAULT FALSE
```

Physical deletion should be avoided whenever possible.

---

# Timestamp Standards

Use:

```sql
TIMESTAMP
```

Default:

```sql
CURRENT_TIMESTAMP
```

---

# Constraints

Use constraints wherever appropriate.

Examples:

- PRIMARY KEY
- UNIQUE
- NOT NULL
- CHECK
- FOREIGN KEY

Foreign keys will be created separately after all tables have been created.

---

# Indexing

Indexes will be managed separately.

Do not create indexes inside table creation scripts.

---

# Views

Views will be created separately.

---

# SQL File Standards

Every SQL file must begin with a standard header.

Example:

```sql
-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : master
-- Table   : customer
-- Purpose : Stores customer information.
-- ============================================================================
```

---

# Design Principles

The database follows:

- Third Normal Form (3NF)
- Enterprise naming conventions
- Separation of business keys and technical keys
- Historical traceability
- Maintainability
- Scalability
- Compatibility with PostgreSQL, Airflow, ADLS Gen2, Databricks, dbt, and Power BI