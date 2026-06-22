-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : master
-- Table   : customer_address
-- Purpose : Stores customer address information.
--
-- Author  : Vijay Rodrigues
-- ============================================================================

CREATE TABLE master.customer_address
(
    customer_address_id          BIGSERIAL PRIMARY KEY,

    customer_id                  BIGINT NOT NULL,

    address_type                 VARCHAR(30) NOT NULL,

    address_line_1               VARCHAR(255) NOT NULL,

    address_line_2               VARCHAR(255),

    landmark                     VARCHAR(255),

    city                         VARCHAR(100) NOT NULL,

    state                        VARCHAR(100) NOT NULL,

    postal_code                  VARCHAR(20) NOT NULL,

    country                      VARCHAR(100) NOT NULL,

    is_primary                   BOOLEAN NOT NULL DEFAULT FALSE,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);