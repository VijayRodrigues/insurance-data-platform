# Domain Model

## 1. Domain Boundaries
The logical model is organized into the following domains:

- Party and customer domain
- Distribution and organization domain
- Product and coverage domain
- Policy administration domain
- Billing and premium domain
- Claims domain
- Reference and audit domain

## 2. Core Concepts

### 2.1 Party and Customer
The party domain stores customer identity and address details. It distinguishes between individual customers and business customers while preserving a common customer anchor.

### 2.2 Distribution and Organization
Agents, brokers, branches, and underwriters represent the operating network that sells, approves, and services policies.

### 2.3 Product and Coverage
Products define the commercial offering. Coverage types define the insurable protection components that are assembled onto a policy.

### 2.4 Policy Administration
Policies are the central contractual object. Policy versions preserve history. Policy coverages define what is covered, at what limit, and under what deductible.

### 2.5 Billing and Premium
Premium and premium payment data support invoice-style financial tracking at the policy level.

### 2.6 Claims
Claims are the loss administration objects tied to policies and coverages. Claim reserves and claim payments provide financial control.

## 3. Conceptual Relationship Summary

| Source Concept | Related Concept | Relationship |
|---|---|---|
| Customer | Policy | One customer can own many policies |
| Policy | Policy Version | One policy can have many versions |
| Policy | Policy Coverage | One policy can have many coverages |
| Policy | Premium | One policy can have many premium records |
| Policy | Claim | One policy can have many claims |
| Claim | Claim Reserve | One claim can have many reserves |
| Claim | Claim Payment | One claim can have many payments |
| Branch | Policy | One branch can issue many policies |
| Underwriter | Policy | One underwriter can approve many policies |
| Agent/Broker | Policy | One intermediary can place many policies |

## 4. Entity Families

| Family | Included Entities |
|---|---|
| Party | customer, customer_address, business_customer |
| Organization | branch, agent, broker, underwriter |
| Product | insurance_product, coverage_type |
| Policy | policy, policy_version, policy_coverage |
| Asset/Risk | vehicle, property |
| Financial | premium, premium_payment, claim_reserve, claim_payment |
| Claims | claim |
| Reference | lookup tables, reference tables |
| Audit | audit tables |

