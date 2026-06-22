-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : master
-- Table   : customer
-- Purpose : Stores customer information for individual policyholders.
--
-- Author  : Vijay Rodrigues
-- Created : YYYY-MM-DD
-- ============================================================================

CREATE TABLE master.customer
(
    customer_id                 BIGSERIAL PRIMARY KEY,

    customer_number             VARCHAR(20) NOT NULL UNIQUE,

    first_name                  VARCHAR(100) NOT NULL,

    middle_name                 VARCHAR(100),

    last_name                   VARCHAR(100) NOT NULL,

    date_of_birth               DATE NOT NULL,

    gender                      VARCHAR(20),

    email_address               VARCHAR(255),

    mobile_number               VARCHAR(20),

    national_id_number          VARCHAR(50),

    occupation                  VARCHAR(100),

    marital_status              VARCHAR(30),

    customer_status             VARCHAR(30) NOT NULL,

    created_at                  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                  VARCHAR(100) NOT NULL,

    updated_by                  VARCHAR(100) NOT NULL,

    is_deleted                  BOOLEAN NOT NULL DEFAULT FALSE
);