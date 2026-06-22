-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : policy
-- Table   : vehicle
-- Purpose : Stores insured vehicle information.
-- ============================================================================

CREATE TABLE policy.vehicle
(
    vehicle_id                   BIGSERIAL PRIMARY KEY,

    policy_id                    BIGINT NOT NULL,

    vehicle_identification_number VARCHAR(50) NOT NULL UNIQUE,

    registration_number          VARCHAR(30) NOT NULL UNIQUE,

    manufacturer                 VARCHAR(100) NOT NULL,

    model                        VARCHAR(100) NOT NULL,

    model_year                   INTEGER NOT NULL,

    vehicle_type                 VARCHAR(50),

    engine_number                VARCHAR(50),

    chassis_number               VARCHAR(50),

    fuel_type                    VARCHAR(30),

    transmission_type            VARCHAR(30),

    color                        VARCHAR(50),

    market_value                 NUMERIC(18,2),

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);