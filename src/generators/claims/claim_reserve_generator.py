import random

from generators.base_generator import BaseGenerator


class ClaimReserveGenerator(BaseGenerator):

    RESERVE_TYPES = [
        "INDEMNITY",
        "EXPENSE"
    ]

    def generate(self, claim_df):

        reserves = []

        claim_reserve_id = 1

        for _, claim in claim_df.iterrows():

            reserve_amount = round(
                claim["estimated_loss_amount"] *
                random.uniform(0.80, 1.20),
                2
            )

            reserves.append({

                "claim_reserve_id": claim_reserve_id,

                "claim_id": claim["claim_id"],

                "reserve_type": random.choice(
                    self.RESERVE_TYPES
                ),

                "reserve_amount": reserve_amount,

                "available_amount": reserve_amount,

                **self.audit_columns()

            })

            claim_reserve_id += 1

        return self.dataframe(reserves)