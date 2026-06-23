-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : claims
-- Table   : claim_reserve
-- Purpose : Stores the current reserve maintained for each claim.
-- ============================================================================

CREATE TABLE claims.claim_reserve
(
    claim_reserve_id             BIGSERIAL PRIMARY KEY,

    claim_id                     BIGINT NOT NULL,

    reserve_amount               NUMERIC(18,2) NOT NULL,

    reserve_status               VARCHAR(30) NOT NULL,

    last_review_date             DATE,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);