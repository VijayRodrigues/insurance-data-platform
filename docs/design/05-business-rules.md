# Business Rules

## 1. Party and Customer Rules

| Rule | Description |
|---|---|
| BR-01 | One customer may own multiple policies. |
| BR-02 | A policy belongs to exactly one customer. |
| BR-03 | A customer may have multiple addresses. |
| BR-04 | A business customer must have a legal business name and tax identifier where applicable. |

## 2. Policy Rules

| Rule | Description |
|---|---|
| BR-05 | Every policy belongs to one insurance product. |
| BR-06 | Every policy is issued through an agent or broker. |
| BR-07 | Every policy is approved by an underwriter. |
| BR-08 | Every policy belongs to one branch. |
| BR-09 | A policy may have multiple versions. |
| BR-10 | A policy may renew into a successor policy. |
| BR-11 | A policy may expire at the end of term. |
| BR-12 | A policy may be cancelled before expiry. |

## 3. Coverage Rules

| Rule | Description |
|---|---|
| BR-13 | One policy may contain multiple coverages. |
| BR-14 | Coverage must be consistent with the policy product. |
| BR-15 | Auto policies require at least one vehicle. |
| BR-16 | Property policies require at least one property. |
| BR-17 | Coverage limit must be positive. |
| BR-18 | Deductible amount cannot be negative. |

## 4. Premium Rules

| Rule | Description |
|---|---|
| BR-19 | Premium frequency supports Monthly, Quarterly, Semi-Annual, and Annual. |
| BR-20 | Premium amounts must reference a policy version or issued policy state. |
| BR-21 | Premium payment totals should not exceed billed premium without explicit adjustment handling. |
| BR-22 | Outstanding premium must remain traceable by due date and policy. |

## 5. Claims Rules

| Rule | Description |
|---|---|
| BR-23 | One policy may have multiple claims. |
| BR-24 | Claims cannot occur before policy inception. |
| BR-25 | Claim reported date must be on or after loss date. |
| BR-26 | Claim amount cannot exceed policy coverage without exception handling. |
| BR-27 | One claim may have multiple reserves. |
| BR-28 | One claim may have multiple payments. |
| BR-29 | Claim payments must not exceed available reserve and approved settlement authority. |

## 6. Data Governance Rules

| Rule | Description |
|---|---|
| BR-30 | All operational entities require audit columns. |
| BR-31 | Reference data must be centrally managed and version-controlled where appropriate. |
| BR-32 | Business keys such as customer_number, policy_number, and claim_reference must be unique. |
| BR-33 | Status changes must be time-aware and traceable. |

