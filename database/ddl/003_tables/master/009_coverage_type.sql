-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : master
-- Table   : coverage_type
-- Purpose : Stores standard insurance coverage definitions.
-- ============================================================================

CREATE TABLE master.coverage_type
(
    coverage_type_id             BIGSERIAL PRIMARY KEY,

    coverage_code                VARCHAR(30) NOT NULL UNIQUE,

    coverage_name                VARCHAR(150) NOT NULL,

    coverage_description         TEXT,

    insurance_product_id         BIGINT NOT NULL,

    default_limit_amount         NUMERIC(18,2),

    default_deductible_amount    NUMERIC(18,2),

    coverage_status              VARCHAR(30) NOT NULL,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);