# Architecture Overview

## 1. Architecture Summary
The target architecture is a hybrid operational and analytics platform for a Property & Casualty insurer.

It is designed to support:

- Transactional policy administration in an operational database
- Batch and near-real-time ingestion from source systems
- Historical storage and transformation in a lakehouse
- Subject-area analytics for reporting and decision support

## 2. Logical Layers

| Layer | Purpose |
|---|---|
| Source systems | Operational systems of record and external inputs |
| Bronze | Raw landed data with minimal transformation |
| Silver | Conformed and quality-controlled data |
| Gold | Business-ready analytical structures |
| Semantic layer | BI-friendly measures and reporting models |

## 3. Architectural Design Goals

- Protect the integrity of operational data
- Provide clear lineage from source to report
- Separate ingestion, transformation, and consumption concerns
- Support governance and access control
- Minimize duplication of business logic across tools

## 4. Core Design Tenets

- Operational source-of-truth remains normalized
- Analytical structures are derived, not manually maintained
- History is preserved for policy, claim, and financial events
- Data quality rules are enforced as early as practical

