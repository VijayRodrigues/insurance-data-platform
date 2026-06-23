-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : policy
-- Table   : property
-- Purpose : Stores insured property information.
-- ============================================================================

CREATE TABLE policy.property
(
    property_id                  BIGSERIAL PRIMARY KEY,

    policy_id                    BIGINT NOT NULL,

    property_identifier          VARCHAR(50) NOT NULL UNIQUE,

    property_type                VARCHAR(50) NOT NULL,

    address_line_1               VARCHAR(255) NOT NULL,

    address_line_2               VARCHAR(255),

    city                         VARCHAR(100) NOT NULL,

    state                        VARCHAR(100) NOT NULL,

    postal_code                  VARCHAR(20) NOT NULL,

    country                      VARCHAR(100) NOT NULL,

    construction_type            VARCHAR(100),

    year_built                   INTEGER,

    number_of_floors             INTEGER,

    replacement_value            NUMERIC(18,2),

    market_value                 NUMERIC(18,2),

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);