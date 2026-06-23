from pathlib import Path

import pandas as pd

from config.settings import PARQUET_OUTPUT_DIRECTORY

from loaders.base_loader import BaseLoader


class ParquetWriter(BaseLoader):

    def write_dataframe(

            self,

            dataframe: pd.DataFrame,

            schema: str,

            table: str):

        self.validate_dataframe(
            dataframe
        )

        output_directory = (

            Path(

                PARQUET_OUTPUT_DIRECTORY

            )

            / schema

        )

        self.create_output_directory(
            output_directory
        )

        output_file = (

            output_directory

            / f"{table}.parquet"

        )

        dataframe.to_parquet(

            output_file,

            index=False

        )

        self.logger.info(

            f"Parquet written : "

            f"{output_file}"

        )