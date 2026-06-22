-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : finance
-- Table   : premium_payment
-- Purpose : Stores premium payment transactions.
-- ============================================================================

CREATE TABLE finance.premium_payment
(
    premium_payment_id           BIGSERIAL PRIMARY KEY,

    payment_reference            VARCHAR(40) NOT NULL UNIQUE,

    premium_id                   BIGINT NOT NULL,

    payment_date                 DATE NOT NULL,

    payment_amount               NUMERIC(18,2) NOT NULL,

    payment_method               VARCHAR(30) NOT NULL,

    payment_status               VARCHAR(30) NOT NULL,

    transaction_reference        VARCHAR(100),

    received_by                  VARCHAR(100),

    remarks                      TEXT,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);