-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : master
-- Table   : insurance_product
-- Purpose : Stores insurance products offered by the company.
-- ============================================================================

CREATE TABLE master.insurance_product
(
    insurance_product_id         BIGSERIAL PRIMARY KEY,

    product_code                 VARCHAR(30) NOT NULL UNIQUE,

    product_name                 VARCHAR(150) NOT NULL,

    product_category             VARCHAR(100) NOT NULL,

    description                  TEXT,

    minimum_sum_insured          NUMERIC(18,2),

    maximum_sum_insured          NUMERIC(18,2),

    minimum_premium              NUMERIC(18,2),

    maximum_premium              NUMERIC(18,2),

    product_status               VARCHAR(30) NOT NULL,

    effective_from               DATE NOT NULL,

    effective_to                 DATE,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);