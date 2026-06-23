import random
from datetime import date
from generators.base_generator import BaseGenerator


class ClaimReserveGenerator(BaseGenerator):

    RESERVE_STATUS = [
        "OPEN",
        "REVIEW",
        "CLOSED"
    ]

    def generate(self, claim_df):

        reserves = []

        claim_reserve_id = 1

        for _, claim in claim_df.iterrows():

            reserve_amount = round(
                claim["claim_amount"] *
                random.uniform(0.80, 1.20),
                2
            )

            

            last_review_date = None

            if random.random() < 0.80:

                reported_date = claim["reported_date"]

                if reported_date <= date.today():

                    last_review_date = self.fake.date_between(
                        start_date=reported_date,
                        end_date="today"
                    )

            record = {

                "claim_reserve_id":
                    claim_reserve_id,

                "claim_id":
                    claim["claim_id"],

                "reserve_amount":
                    reserve_amount,

                "reserve_status":
                    random.choice(
                        self.RESERVE_STATUS
                    ),

                "last_review_date":
                    last_review_date,

                **self.audit_columns()

            }

            reserves.append(record)

            claim_reserve_id += 1

        return self.dataframe(reserves)