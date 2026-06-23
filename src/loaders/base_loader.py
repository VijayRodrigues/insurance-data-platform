from abc import ABC
from pathlib import Path

import pandas as pd

from utils.logger import logger


class BaseLoader(ABC):

    def __init__(self):

        self.logger = logger

    def validate_dataframe(
            self,
            dataframe: pd.DataFrame):

        if dataframe is None:

            raise ValueError(
                "DataFrame cannot be None."
            )

        if dataframe.empty:

            raise ValueError(
                "DataFrame is empty."
            )

    def log_start(
            self,
            schema: str,
            table: str,
            row_count: int):

        self.logger.info(
            f"Loading {row_count:,} rows into "
            f"{schema}.{table}"
        )

    def log_complete(
            self,
            schema: str,
            table: str):

        self.logger.info(
            f"Finished loading "
            f"{schema}.{table}"
        )

    def create_output_directory(
            self,
            output_directory: Path):

        output_directory.mkdir(
            parents=True,
            exist_ok=True
        )