-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- File    : 002_create_schemas.sql
-- Purpose : Create logical schemas for the Insurance Platform
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS master;

CREATE SCHEMA IF NOT EXISTS sales;

CREATE SCHEMA IF NOT EXISTS policy;

CREATE SCHEMA IF NOT EXISTS finance;

CREATE SCHEMA IF NOT EXISTS claims;

CREATE SCHEMA IF NOT EXISTS reference;

CREATE SCHEMA IF NOT EXISTS audit;