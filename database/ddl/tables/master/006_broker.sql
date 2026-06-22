-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : master
-- Table   : broker
-- Purpose : Stores broker organization information.
-- ============================================================================

CREATE TABLE master.broker
(
    broker_id                    BIGSERIAL PRIMARY KEY,

    broker_number                VARCHAR(20) NOT NULL UNIQUE,

    broker_name                  VARCHAR(255) NOT NULL,

    registration_number          VARCHAR(100),

    contact_person               VARCHAR(150),

    email_address                VARCHAR(255),

    mobile_number                VARCHAR(20),

    broker_status                VARCHAR(30) NOT NULL,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);