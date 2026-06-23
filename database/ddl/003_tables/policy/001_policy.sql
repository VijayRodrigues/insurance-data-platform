-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : policy
-- Table   : policy
-- Purpose : Stores insurance policy master records.
-- ============================================================================

CREATE TABLE policy.policy
(
    policy_id                    BIGSERIAL PRIMARY KEY,

    policy_number                VARCHAR(30) NOT NULL UNIQUE,

    customer_id                  BIGINT NOT NULL,

    insurance_product_id         BIGINT NOT NULL,

    quote_id                     BIGINT,

    branch_id                    BIGINT NOT NULL,

    agent_id                     BIGINT,

    broker_id                    BIGINT,

    underwriter_id               BIGINT NOT NULL,

    policy_effective_date        DATE NOT NULL,

    policy_expiry_date           DATE NOT NULL,

    policy_issue_date            DATE NOT NULL,

    policy_status                VARCHAR(30) NOT NULL,

    total_sum_insured            NUMERIC(18,2) NOT NULL,

    total_premium                NUMERIC(18,2) NOT NULL,

    currency_code                VARCHAR(10) NOT NULL,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);