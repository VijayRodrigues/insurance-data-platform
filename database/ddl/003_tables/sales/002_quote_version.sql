-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : sales
-- Table   : quote_version
-- Purpose : Stores version history of insurance quotations.
-- ============================================================================

CREATE TABLE sales.quote_version
(
    quote_version_id             BIGSERIAL PRIMARY KEY,

    quote_id                     BIGINT NOT NULL,

    version_number               INTEGER NOT NULL,

    effective_from               DATE NOT NULL,

    effective_to                 DATE,

    quoted_premium               NUMERIC(18,2),

    quoted_sum_insured           NUMERIC(18,2),

    deductible_amount            NUMERIC(18,2),

    underwriting_decision        VARCHAR(30),

    remarks                      TEXT,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);