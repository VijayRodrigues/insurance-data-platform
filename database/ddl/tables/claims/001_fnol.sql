-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : claims
-- Table   : fnol
-- Purpose : Stores First Notice of Loss (FNOL) reported by customers.
-- ============================================================================

CREATE TABLE claims.fnol
(
    fnol_id                      BIGSERIAL PRIMARY KEY,

    fnol_reference               VARCHAR(30) NOT NULL UNIQUE,

    policy_id                    BIGINT NOT NULL,

    reported_by                  VARCHAR(100) NOT NULL,

    reported_date                TIMESTAMP NOT NULL,

    incident_date                TIMESTAMP NOT NULL,

    incident_location            VARCHAR(255),

    incident_description         TEXT,

    loss_type                    VARCHAR(50) NOT NULL,

    fnol_status                  VARCHAR(30) NOT NULL,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);