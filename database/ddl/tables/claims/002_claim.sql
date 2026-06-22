-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : claims
-- Table   : claim
-- Purpose : Stores insurance claims.
-- ============================================================================

CREATE TABLE claims.claim
(
    claim_id                     BIGSERIAL PRIMARY KEY,

    claim_reference              VARCHAR(30) NOT NULL UNIQUE,

    fnol_id                      BIGINT NOT NULL,

    policy_id                    BIGINT NOT NULL,

    claim_type                   VARCHAR(50) NOT NULL,

    claim_status                 VARCHAR(30) NOT NULL,

    loss_date                    DATE NOT NULL,

    reported_date                DATE NOT NULL,

    claim_amount                 NUMERIC(18,2),

    approved_amount              NUMERIC(18,2),

    settlement_date              DATE,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);