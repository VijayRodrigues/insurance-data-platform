from abc import ABC
from datetime import datetime
import random

import pandas as pd
from faker import Faker

from config.settings import RANDOM_SEED


class BaseGenerator(ABC):
    """
    Base class for all synthetic data generators.
    """

    def __init__(self):

        self.fake = Faker("en_IN")

        Faker.seed(RANDOM_SEED)
        random.seed(RANDOM_SEED)

    def current_timestamp(self):
        return datetime.now()

    def audit_columns(self):

        return {
            "created_at": self.current_timestamp(),
            "updated_at": self.current_timestamp(),
            "created_by": "SYSTEM",
            "updated_by": "SYSTEM",
            "is_deleted": False
        }

    def dataframe(self, records):

        return pd.DataFrame(records)