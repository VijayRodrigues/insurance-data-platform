-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : master
-- Table   : underwriter
-- Purpose : Stores underwriter information.
-- ============================================================================

CREATE TABLE master.underwriter
(
    underwriter_id               BIGSERIAL PRIMARY KEY,

    underwriter_number           VARCHAR(20) NOT NULL UNIQUE,

    first_name                   VARCHAR(100) NOT NULL,

    last_name                    VARCHAR(100) NOT NULL,

    email_address                VARCHAR(255),

    mobile_number                VARCHAR(20),

    underwriting_authority       VARCHAR(100),

    branch_id                    BIGINT NOT NULL,

    underwriter_status           VARCHAR(30) NOT NULL,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);