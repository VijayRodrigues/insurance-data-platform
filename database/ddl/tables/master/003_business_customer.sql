-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : master
-- Table   : business_customer
-- Purpose : Stores business customer information.
--
-- Author  : Vijay Rodrigues
-- ============================================================================

CREATE TABLE master.business_customer
(
    business_customer_id         BIGSERIAL PRIMARY KEY,

    customer_id                  BIGINT NOT NULL,

    business_name                VARCHAR(255) NOT NULL,

    registration_number          VARCHAR(100) NOT NULL UNIQUE,

    tax_identifier               VARCHAR(100),

    industry                     VARCHAR(100),

    annual_revenue               NUMERIC(18,2),

    employee_count               INTEGER,

    established_date             DATE,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);