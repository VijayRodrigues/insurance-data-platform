-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : finance
-- Table   : premium
-- Purpose : Stores premium obligations for insurance policies.
-- ============================================================================

CREATE TABLE finance.premium
(
    premium_id                   BIGSERIAL PRIMARY KEY,

    premium_number               VARCHAR(30) NOT NULL UNIQUE,

    policy_id                    BIGINT NOT NULL,

    policy_version_id            BIGINT NOT NULL,

    premium_frequency            VARCHAR(30) NOT NULL,

    premium_amount               NUMERIC(18,2) NOT NULL,

    tax_amount                   NUMERIC(18,2) DEFAULT 0,

    total_amount                 NUMERIC(18,2) NOT NULL,

    due_date                     DATE NOT NULL,

    premium_status               VARCHAR(30) NOT NULL,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);