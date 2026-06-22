# Business Process

## 1. End-to-End Process View
The platform supports a simplified but enterprise-realistic P&C lifecycle:

1. Customer onboarding
2. Risk capture and quote initiation
3. Underwriting review and approval
4. Policy issuance
5. Premium billing and collection
6. Policy maintenance and renewal
7. Loss notification and claim intake
8. Reserve setup and adjustment
9. Claim payment processing
10. Policy expiration, cancellation, or renewal closure

## 2. Policy Lifecycle

### 2.1 Quote and Underwriting
- A quote is captured against a customer and a product.
- Risk data is reviewed by an underwriter.
- The underwriter approves, declines, or requests changes.
- Approved quotations become issued policies.

### 2.2 Policy Issuance
- A policy is created for exactly one customer.
- The policy is associated with one product, one branch, and one underwriting decision.
- The policy is routed through one agent or broker relationship.
- One policy may contain multiple coverages.

### 2.3 Policy Maintenance
- Policies may be endorsed through new versions.
- Each version preserves the state of the policy at a point in time.
- Mid-term changes may alter coverages, insured values, or premium amounts.
- Policies may be renewed into a successor policy.
- Policies may expire naturally or cancel early.

## 3. Premium and Billing Process
- Premium is calculated from product, rating factors, and coverage selections.
- Premium amounts may be billed monthly, quarterly, semi-annually, or annually.
- Payments are captured against premium obligations.
- Outstanding balances remain visible for collection and aging analysis.

## 4. Claims Process

### 4.1 First Notice of Loss
- A claim is created after a loss event occurs.
- The claim must reference a valid in-force policy period.
- Loss details are recorded with loss date, report date, and cause of loss.

### 4.2 Reserve Management
- A claim may have one or more reserves.
- Reserves track expected future cost by type, such as indemnity or expense.
- Reserve amounts may be adjusted as claim knowledge changes.

### 4.3 Claim Payment
- One claim may produce multiple payments.
- Payments may be issued in installments.
- Payments must link back to the claim and the payment purpose.

## 5. Customer and Channel Process
- Individual and business customers are managed separately but share common relationship principles.
- Agents and brokers represent the distribution channel.
- Branches provide geographic and operational accountability.
- Underwriters provide risk approval and control.

## 6. Control Points

| Control Point | Description |
|---|---|
| Customer validation | Ensure customer identity and relationship completeness |
| Policy approval | Confirm underwriting decision prior to issuance |
| Coverage validation | Confirm product-specific coverage rules |
| Claim validation | Confirm claim date is within policy eligibility window |
| Financial validation | Reconcile premiums, reserves, and payments |
| Audit validation | Preserve who changed what and when |

