-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : policy
-- Table   : policy_transaction
-- Purpose : Stores policy lifecycle transactions.
-- ============================================================================

CREATE TABLE policy.policy_transaction
(
    policy_transaction_id        BIGSERIAL PRIMARY KEY,

    policy_id                    BIGINT NOT NULL,

    policy_version_id            BIGINT,

    transaction_type             VARCHAR(50) NOT NULL,

    transaction_date             DATE NOT NULL,

    transaction_status           VARCHAR(30) NOT NULL,

    transaction_amount           NUMERIC(18,2),

    remarks                      TEXT,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);