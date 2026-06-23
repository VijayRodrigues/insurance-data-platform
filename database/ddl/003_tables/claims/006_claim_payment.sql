-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : claims
-- Table   : claim_payment
-- Purpose : Stores payments made against approved claims.
-- ============================================================================

CREATE TABLE claims.claim_payment
(
    claim_payment_id             BIGSERIAL PRIMARY KEY,

    payment_reference            VARCHAR(40) NOT NULL UNIQUE,

    claim_id                     BIGINT NOT NULL,

    payment_date                 DATE NOT NULL,

    payment_amount               NUMERIC(18,2) NOT NULL,

    payment_method               VARCHAR(30) NOT NULL,

    payment_status               VARCHAR(30) NOT NULL,

    transaction_reference        VARCHAR(100),

    remarks                      TEXT,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);