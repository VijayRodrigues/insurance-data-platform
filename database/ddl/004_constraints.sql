-- ============================================================================
-- MASTER SCHEMA CONSTRAINTS
-- ============================================================================

ALTER TABLE master.customer_address
ADD CONSTRAINT fk_customer_address_customer
FOREIGN KEY (customer_id)
REFERENCES master.customer(customer_id);

ALTER TABLE master.business_customer
ADD CONSTRAINT fk_business_customer_customer
FOREIGN KEY (customer_id)
REFERENCES master.customer(customer_id);

ALTER TABLE master.agent
ADD CONSTRAINT fk_agent_branch
FOREIGN KEY (branch_id)
REFERENCES master.branch(branch_id);

ALTER TABLE master.underwriter
ADD CONSTRAINT fk_underwriter_branch
FOREIGN KEY (branch_id)
REFERENCES master.branch(branch_id);

ALTER TABLE master.coverage_type
ADD CONSTRAINT fk_coverage_type_product
FOREIGN KEY (insurance_product_id)
REFERENCES master.insurance_product(insurance_product_id);





-- ============================================================================
-- SALES SCHEMA CONSTRAINTS
-- ============================================================================

ALTER TABLE sales.quote
ADD CONSTRAINT fk_quote_customer
FOREIGN KEY (customer_id)
REFERENCES master.customer(customer_id);

ALTER TABLE sales.quote
ADD CONSTRAINT fk_quote_product
FOREIGN KEY (insurance_product_id)
REFERENCES master.insurance_product(insurance_product_id);

ALTER TABLE sales.quote
ADD CONSTRAINT fk_quote_branch
FOREIGN KEY (branch_id)
REFERENCES master.branch(branch_id);

ALTER TABLE sales.quote
ADD CONSTRAINT fk_quote_agent
FOREIGN KEY (agent_id)
REFERENCES master.agent(agent_id);

ALTER TABLE sales.quote
ADD CONSTRAINT fk_quote_broker
FOREIGN KEY (broker_id)
REFERENCES master.broker(broker_id);

ALTER TABLE sales.quote_version
ADD CONSTRAINT fk_quote_version_quote
FOREIGN KEY (quote_id)
REFERENCES sales.quote(quote_id);






-- ============================================================================
-- POLICY SCHEMA CONSTRAINTS - PART 1
-- ============================================================================

ALTER TABLE policy.policy
ADD CONSTRAINT fk_policy_customer
FOREIGN KEY (customer_id)
REFERENCES master.customer(customer_id);

ALTER TABLE policy.policy
ADD CONSTRAINT fk_policy_product
FOREIGN KEY (insurance_product_id)
REFERENCES master.insurance_product(insurance_product_id);

ALTER TABLE policy.policy
ADD CONSTRAINT fk_policy_quote
FOREIGN KEY (quote_id)
REFERENCES sales.quote(quote_id);

ALTER TABLE policy.policy
ADD CONSTRAINT fk_policy_branch
FOREIGN KEY (branch_id)
REFERENCES master.branch(branch_id);

ALTER TABLE policy.policy
ADD CONSTRAINT fk_policy_agent
FOREIGN KEY (agent_id)
REFERENCES master.agent(agent_id);

ALTER TABLE policy.policy
ADD CONSTRAINT fk_policy_broker
FOREIGN KEY (broker_id)
REFERENCES master.broker(broker_id);

ALTER TABLE policy.policy
ADD CONSTRAINT fk_policy_underwriter
FOREIGN KEY (underwriter_id)
REFERENCES master.underwriter(underwriter_id);









-- ============================================================================
-- POLICY SCHEMA CONSTRAINTS - PART 2
-- ============================================================================

ALTER TABLE policy.policy_version
ADD CONSTRAINT fk_policy_version_policy
FOREIGN KEY (policy_id)
REFERENCES policy.policy(policy_id);

ALTER TABLE policy.policy_transaction
ADD CONSTRAINT fk_policy_transaction_policy
FOREIGN KEY (policy_id)
REFERENCES policy.policy(policy_id);

ALTER TABLE policy.policy_transaction
ADD CONSTRAINT fk_policy_transaction_policy_version
FOREIGN KEY (policy_version_id)
REFERENCES policy.policy_version(policy_version_id);

ALTER TABLE policy.policy_coverage
ADD CONSTRAINT fk_policy_coverage_policy_version
FOREIGN KEY (policy_version_id)
REFERENCES policy.policy_version(policy_version_id);

ALTER TABLE policy.policy_coverage
ADD CONSTRAINT fk_policy_coverage_coverage_type
FOREIGN KEY (coverage_type_id)
REFERENCES master.coverage_type(coverage_type_id);

ALTER TABLE policy.vehicle
ADD CONSTRAINT fk_vehicle_policy
FOREIGN KEY (policy_id)
REFERENCES policy.policy(policy_id);

ALTER TABLE policy.property
ADD CONSTRAINT fk_property_policy
FOREIGN KEY (policy_id)
REFERENCES policy.policy(policy_id);








-- ============================================================================
-- FINANCE SCHEMA CONSTRAINTS
-- ============================================================================

ALTER TABLE finance.premium
ADD CONSTRAINT fk_premium_policy
FOREIGN KEY (policy_id)
REFERENCES policy.policy(policy_id);

ALTER TABLE finance.premium
ADD CONSTRAINT fk_premium_policy_version
FOREIGN KEY (policy_version_id)
REFERENCES policy.policy_version(policy_version_id);

ALTER TABLE finance.premium_payment
ADD CONSTRAINT fk_premium_payment_premium
FOREIGN KEY (premium_id)
REFERENCES finance.premium(premium_id);







-- ============================================================================
-- CLAIMS SCHEMA CONSTRAINTS
-- ============================================================================

ALTER TABLE claims.fnol
ADD CONSTRAINT fk_fnol_policy
FOREIGN KEY (policy_id)
REFERENCES policy.policy(policy_id);

ALTER TABLE claims.claim
ADD CONSTRAINT fk_claim_fnol
FOREIGN KEY (fnol_id)
REFERENCES claims.fnol(fnol_id);

ALTER TABLE claims.claim
ADD CONSTRAINT fk_claim_policy
FOREIGN KEY (policy_id)
REFERENCES policy.policy(policy_id);

ALTER TABLE claims.claim_note
ADD CONSTRAINT fk_claim_note_claim
FOREIGN KEY (claim_id)
REFERENCES claims.claim(claim_id);

ALTER TABLE claims.claim_reserve
ADD CONSTRAINT fk_claim_reserve_claim
FOREIGN KEY (claim_id)
REFERENCES claims.claim(claim_id);

ALTER TABLE claims.claim_reserve_transaction
ADD CONSTRAINT fk_claim_reserve_transaction_reserve
FOREIGN KEY (claim_reserve_id)
REFERENCES claims.claim_reserve(claim_reserve_id);

ALTER TABLE claims.claim_payment
ADD CONSTRAINT fk_claim_payment_claim
FOREIGN KEY (claim_id)
REFERENCES claims.claim(claim_id);

