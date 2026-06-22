# insurance-data-platform Design Documentation

## Purpose
This documentation package defines the logical business and data design for **insurance-data-platform**, a flagship enterprise Property & Casualty (P&C) insurance portfolio project.

The design is intentionally technology-aware but implementation-neutral. It is written for senior data engineers, solution architects, and technical interviewers who need a rigorous view of the business domain, operational data model, and analytical architecture.

## Scope
This design covers only the following P&C products:

- Auto Insurance
- Home Insurance
- Commercial Property Insurance
- General Liability Insurance

Out of scope:

- Life Insurance
- Health Insurance
- Reinsurance
- Marine Insurance
- Aviation Insurance
- Pension
- Wealth Management
- Investment Products

## Document Map

| File | Purpose |
|---|---|
| [01-business-overview.md](./01-business-overview.md) | Business context, goals, and operating model |
| [02-business-process.md](./02-business-process.md) | End-to-end policy, premium, and claims processes |
| [03-domain-model.md](./03-domain-model.md) | Domain boundaries and major business concepts |
| [04-entity-list.md](./04-entity-list.md) | Entity inventory with concise descriptions |
| [05-business-rules.md](./05-business-rules.md) | Enterprise business rules and policy constraints |
| [06-logical-data-model.md](./06-logical-data-model.md) | 3NF logical data model for all entities |
| [07-table-dependencies.md](./07-table-dependencies.md) | Parent-child and dependency sequencing |
| [08-indexing-strategy.md](./08-indexing-strategy.md) | Logical indexing and access-path guidance |
| [09-row-volume-estimates.md](./09-row-volume-estimates.md) | Volume assumptions and annual growth |
| [10-future-scalability.md](./10-future-scalability.md) | Scalability, extensibility, and platform alignment |
| [architecture/architecture-overview.md](./architecture/architecture-overview.md) | High-level architecture direction |
| [architecture/source-systems.md](./architecture/source-systems.md) | Source system landscape and data ownership |
| [architecture/medallion-architecture.md](./architecture/medallion-architecture.md) | Medallion architecture mapping |
| [architecture/analytics-layer.md](./architecture/analytics-layer.md) | Curated analytics and reporting layer concepts |

## Design Principles

- 3NF operational design with no unnecessary denormalization
- Enterprise naming conventions using business language
- Clear separation of master, transactional, and audit data
- Support for policy lifecycle, renewals, claims, reserves, and payments
- Technology-neutral logical model compatible with PostgreSQL and lakehouse analytics
- Medallion architecture alignment for downstream processing

## Cross-Reference Guidance

- Start with [01-business-overview.md](./01-business-overview.md) for the operating model.
- Use [05-business-rules.md](./05-business-rules.md) to validate entity behavior.
- Use [06-logical-data-model.md](./06-logical-data-model.md) as the primary schema reference.
- Use [09-row-volume-estimates.md](./09-row-volume-estimates.md) to understand scale assumptions.
- Use the files under [architecture/](./architecture) for implementation planning across PostgreSQL, ADLS Gen2, Databricks, Delta Lake, DLT, dbt, and Power BI.

