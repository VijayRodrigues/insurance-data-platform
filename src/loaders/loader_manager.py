from config.settings import *

from loaders.parquet_writer import ParquetWriter
from loaders.postgres_loader import PostgreSQLLoader


class LoaderManager:

    def __init__(self):

        self.postgres = PostgreSQLLoader()
        self.parquet = ParquetWriter()

    def load(self, dataframe, schema, table):

        if WRITE_TO_POSTGRES:
            self.postgres.load_dataframe(
                dataframe,
                schema,
                table
            )

        if WRITE_PARQUET:
            self.parquet.write_dataframe(
                dataframe,
                schema,
                table
            )

    def load_all(self, datasets):

        for schema, table, dataframe in datasets:

            self.load(
                dataframe=dataframe,
                schema=schema,
                table=table
            )