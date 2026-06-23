-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : policy
-- Table   : policy_coverage
-- Purpose : Stores coverage selected for each policy version.
-- ============================================================================

CREATE TABLE policy.policy_coverage
(
    policy_coverage_id           BIGSERIAL PRIMARY KEY,

    policy_version_id            BIGINT NOT NULL,

    coverage_type_id             BIGINT NOT NULL,

    coverage_limit_amount        NUMERIC(18,2) NOT NULL,

    deductible_amount            NUMERIC(18,2),

    premium_amount               NUMERIC(18,2) NOT NULL,

    coverage_status              VARCHAR(30) NOT NULL,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);