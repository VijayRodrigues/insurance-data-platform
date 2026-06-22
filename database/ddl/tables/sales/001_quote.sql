-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : sales
-- Table   : quote
-- Purpose : Stores insurance quotations generated for customers.
-- ============================================================================

CREATE TABLE sales.quote
(
    quote_id                     BIGSERIAL PRIMARY KEY,

    quote_number                 VARCHAR(30) NOT NULL UNIQUE,

    customer_id                  BIGINT NOT NULL,

    insurance_product_id         BIGINT NOT NULL,

    agent_id                     BIGINT,

    broker_id                    BIGINT,

    branch_id                    BIGINT NOT NULL,

    quote_date                   DATE NOT NULL,

    quote_expiry_date            DATE NOT NULL,

    quote_status                 VARCHAR(30) NOT NULL,

    total_premium                NUMERIC(18,2),

    currency_code                VARCHAR(10) NOT NULL,

    remarks                      TEXT,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);