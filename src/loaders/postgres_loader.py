import pandas as pd

from sqlalchemy import create_engine

from config.settings import *

from loaders.base_loader import BaseLoader


class PostgreSQLLoader(BaseLoader):

    DATE_COLUMNS = {
        "effective_from",
        "effective_to",
        "quote_date",
        "quote_expiry_date",
        "policy_effective_date",
        "policy_expiry_date",
        "policy_issue_date",
        "payment_date",
        "reported_date",
        "loss_date",
        "closed_date",
        "due_date",
        "hire_date",
        "established_date",
        "created_at",
        "updated_at"
    }

    def __init__(self):

        super().__init__()

        connection_string = (

            f"postgresql+psycopg://"

            f"{DB_USER}:{DB_PASSWORD}"

            f"@{DB_HOST}:{DB_PORT}"

            f"/{DB_NAME}"

        )

        self.engine = create_engine(
            connection_string
        )

    def load_dataframe(
            self,
            dataframe: pd.DataFrame,
            schema: str,
            table: str):

        self.validate_dataframe(
            dataframe
        )

        self.log_start(
            schema,
            table,
            len(dataframe)
        )

        dataframe = dataframe.copy()

        for column in dataframe.columns:

            if column in self.DATE_COLUMNS:

                dataframe[column] = pd.to_datetime(
                    dataframe[column],
                    errors="coerce"
                )

        dataframe.to_sql(

            name=table,

            schema=schema,

            con=self.engine,

            if_exists="append",

            index=False,

            method="multi",

            chunksize=BATCH_SIZE

        )

        self.log_complete(
            schema,
            table
        )