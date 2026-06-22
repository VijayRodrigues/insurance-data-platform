-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : master
-- Table   : branch
-- Purpose : Stores insurance company branch information.
-- ============================================================================

CREATE TABLE master.branch
(
    branch_id                    BIGSERIAL PRIMARY KEY,

    branch_code                  VARCHAR(20) NOT NULL UNIQUE,

    branch_name                  VARCHAR(200) NOT NULL,

    address_line_1               VARCHAR(255),

    address_line_2               VARCHAR(255),

    city                         VARCHAR(100),

    state                        VARCHAR(100),

    postal_code                  VARCHAR(20),

    country                      VARCHAR(100),

    phone_number                 VARCHAR(20),

    email_address                VARCHAR(255),

    branch_status                VARCHAR(30) NOT NULL,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);