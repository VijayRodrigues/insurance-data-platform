-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : policy
-- Table   : policy_version
-- Purpose : Stores policy version history.
-- ============================================================================

CREATE TABLE policy.policy_version
(
    policy_version_id            BIGSERIAL PRIMARY KEY,

    policy_id                    BIGINT NOT NULL,

    version_number               INTEGER NOT NULL,

    effective_from               DATE NOT NULL,

    effective_to                 DATE,

    endorsement_reason           VARCHAR(255),

    version_status               VARCHAR(30) NOT NULL,

    remarks                      TEXT,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);