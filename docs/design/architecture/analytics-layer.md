# Analytics Layer

## 1. Purpose
The analytics layer is the consumption-facing part of the platform. It exists to support business intelligence, operational reporting, and trend analysis without placing reporting pressure on the operational model.

## 2. Subject Areas

| Subject Area | Key Questions |
|---|---|
| Policy | How many policies were written, renewed, cancelled, or expired? |
| Customer | How many customers are active by product and branch? |
| Premium | What premium was billed, collected, or outstanding? |
| Claims | How many claims were reported, paid, reserved, or closed? |
| Distribution | Which agents, brokers, and branches drive business volume? |
| Underwriting | Which underwriters approve the most business? |

## 3. Recommended Analytical Structures

- Policy performance mart
- Premium billing and collections mart
- Claims performance mart
- Customer 360 reporting view
- Distribution channel performance mart

## 4. Reporting Principles

- Use conformed dimensions for customer, product, branch, and time.
- Keep measures aligned with business definitions.
- Avoid mixing operational transaction detail with executive-level reporting logic.
- Preserve traceability back to the underlying source keys.

## 5. Power BI Fit

- Power BI semantic models can consume curated Gold-layer outputs.
- Measures should be defined consistently for premium written, premium collected, claim incurred, and policy counts.
- RLS can be applied by branch, role, or distribution channel where needed.

