import os

from dotenv import load_dotenv

from pathlib import Path

# =============================================================================
# PROJECT
# =============================================================================

PROJECT_NAME = "Insurance Data Platform"

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

# =============================================================================
# DATASET SIZE
# =============================================================================

DATASET_SIZE = "SMALL"
# SMALL
# MEDIUM
# LARGE
# ENTERPRISE

# =============================================================================
# RANDOMNESS
# =============================================================================

RANDOM_SEED = 42

# =============================================================================
# DATABASE
# =============================================================================

DB_HOST = os.getenv(
    "DB_HOST",
    "localhost"
)

DB_PORT = int(
    os.getenv(
        "DB_PORT",
        "5432"
    )
)

DB_NAME = os.getenv(
    "DB_NAME",
    "insurance_platform"
)

DB_USER = os.getenv(
    "DB_USER",
    "postgres"
)

DB_PASSWORD = os.getenv(
    "DB_PASSWORD",
    "postgres"
)

# =============================================================================
# OUTPUT
# =============================================================================

WRITE_TO_POSTGRES = True

WRITE_PARQUET = False

PARQUET_OUTPUT_DIRECTORY = BASE_DIR / "output"

# =============================================================================
# BATCH
# =============================================================================

BATCH_SIZE = 10000