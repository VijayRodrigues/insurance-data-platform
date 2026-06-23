import random
from datetime import timedelta

from generators.base_generator import BaseGenerator


class QuoteVersionGenerator(BaseGenerator):

    UNDERWRITING_DECISIONS = [
        "APPROVED",
        "REFERRED",
        "DECLINED"
    ]

    def generate(self, quote_df):

        quote_versions = []

        quote_version_id = 1

        for _, quote in quote_df.iterrows():

            version_count = random.choices(
                population=[1, 2, 3],
                weights=[70, 20, 10],
                k=1
            )[0]

            effective_from = quote["quote_date"]

            premium = quote["total_premium"]

            for version in range(1, version_count + 1):

                if version > 1:

                    premium = round(
                        premium * random.uniform(0.95, 1.10),
                        2
                    )

                    effective_from = effective_from + timedelta(days=3)

                record = {

                    "quote_version_id": quote_version_id,

                    "quote_id": quote["quote_id"],

                    "version_number": version,

                    "effective_from": effective_from,

                    "effective_to": None,

                    "quoted_premium": premium,

                    "quoted_sum_insured": random.randint(
                        100000,
                        10000000
                    ),

                    "deductible_amount": random.choice(
                        [0, 1000, 2500, 5000]
                    ),

                    "underwriting_decision": random.choice(
                        self.UNDERWRITING_DECISIONS
                    ),

                    "remarks": None,

                    **self.audit_columns()

                }

                quote_versions.append(record)

                quote_version_id += 1

        return self.dataframe(quote_versions)