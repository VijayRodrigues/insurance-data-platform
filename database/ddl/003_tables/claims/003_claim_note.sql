-- ============================================================================
-- Project : Insurance Data Platform
-- Database: insurance_platform
-- Schema  : claims
-- Table   : claim_note
-- Purpose : Stores notes and activities related to claims.
-- ============================================================================

CREATE TABLE claims.claim_note
(
    claim_note_id                BIGSERIAL PRIMARY KEY,

    claim_id                     BIGINT NOT NULL,

    note_date                    TIMESTAMP NOT NULL,

    note_type                    VARCHAR(30) NOT NULL,

    note_text                    TEXT NOT NULL,

    created_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at                   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    created_by                   VARCHAR(100) NOT NULL,

    updated_by                   VARCHAR(100) NOT NULL,

    is_deleted                   BOOLEAN NOT NULL DEFAULT FALSE
);