-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : claims
-- Table   : claim_reserve_transaction
-- Purpose : Stores reserve adjustment history.
-- ============================================================================

CREATE TABLE claims.claim_reserve_transaction
(
    claim_reserve_transaction_id BIGSERIAL PRIMARY KEY,

    claim_reserve_id             BIGINT NOT NULL,

    transaction_date             TIMESTAMP NOT NULL,

    previous_amount              NUMERIC(18,2) NOT NULL,

    new_amount                   NUMERIC(18,2) NOT NULL,

    adjustment_reason            VARCHAR(255),

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);