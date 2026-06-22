# Business Overview

## 1. Executive Summary
The **insurance-data-platform** initiative models the core operational data needs of a medium-sized Property & Casualty insurer. The platform supports policy administration, underwriting, billing, and claims operations for a constrained but realistic product portfolio.

The objective is to design a stable enterprise data foundation that can support:

- Policy origination and lifecycle management
- Premium calculation and payment tracking
- Claim intake, reserve management, and claim payment processing
- Customer and business customer management
- Agent, broker, branch, and underwriter accountability
- Operational auditability and downstream analytics

## 2. Business Goals

- Maintain a single logical view of customer, policy, claim, and payment data
- Support P&C products without mixing in life, health, or investment concepts
- Preserve operational integrity through 3NF modeling
- Enable reliable reporting, analytics, and data quality controls
- Prepare the data model for lakehouse implementation and future scale

## 3. Operating Context
The insurer operates through multiple distribution channels and underwriting controls.

Key operating participants include:

- Customers and business customers
- Agents and brokers
- Branches
- Underwriters
- Finance and claims operations

The business expects policies to be issued through an authorized intermediary or direct channel equivalent represented through agent or broker relationships. Claims and premiums must retain traceability back to the originating policy, product, and coverage structure.

## 4. Core Business Outcomes

| Outcome | Description |
|---|---|
| Policy control | Track issued, renewed, cancelled, and expired policies |
| Financial control | Track billed, collected, and outstanding premium amounts |
| Claims control | Track reported losses, reserves, payments, and closures |
| Channel control | Attribute business to agent, broker, and branch |
| Underwriting control | Track underwriting approval and accountability |
| Customer insight | Maintain a durable view of individuals and business customers |

## 5. Product Scope

| Product | Typical Use Case |
|---|---|
| Auto Insurance | Personal or commercial vehicle coverage |
| Home Insurance | Owner-occupied or tenant-related property protection |
| Commercial Property Insurance | Coverage for business-owned buildings and contents |
| General Liability Insurance | Liability coverage for business operations |

## 6. Key Enterprise Assumptions

- A customer may hold multiple policies across products.
- Policies are versioned to preserve lifecycle history.
- Coverages are attached to policies through policy coverage records.
- Claims are tied to policies and evaluated against covered exposures.
- Claims may have multiple reserves and multiple payments over time.
- Policy premiums may be billed on recurring schedules.
- Auditability is a design requirement, not an optional enhancement.

## 7. Design Boundaries
This project intentionally excludes:

- Reinsurance treaties and ceded accounting
- Life and health underwriting concepts
- Wealth, pension, and investment products
- Marine and aviation exposure structures

Those exclusions keep the model focused and prevent inappropriate cross-domain contamination.

