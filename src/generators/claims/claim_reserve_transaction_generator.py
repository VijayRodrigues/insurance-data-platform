import random

from generators.base_generator import BaseGenerator


class ClaimReserveTransactionGenerator(BaseGenerator):

    ADJUSTMENT_REASONS = [
        "INITIAL_RESERVE",
        "SURVEYOR_UPDATE",
        "CLAIM_REASSESSMENT",
        "LEGAL_REVIEW",
        "FINAL_SETTLEMENT"
    ]

    def generate(self, reserve_df):

        transactions = []

        claim_reserve_transaction_id = 1

        for _, reserve in reserve_df.iterrows():

            previous_amount = round(
                reserve["reserve_amount"] *
                random.uniform(0.70, 0.95),
                2
            )

            new_amount = reserve["reserve_amount"]

            record = {

                "claim_reserve_transaction_id":
                    claim_reserve_transaction_id,

                "claim_reserve_id":
                    reserve["claim_reserve_id"],

                "transaction_date":
                    self.fake.date_time_between(
                        start_date="-180d",
                        end_date="now"
                    ),

                "previous_amount":
                    previous_amount,

                "new_amount":
                    new_amount,

                "adjustment_reason":
                    random.choice(
                        self.ADJUSTMENT_REASONS
                    ),

                **self.audit_columns()

            }

            transactions.append(record)

            claim_reserve_transaction_id += 1

        return self.dataframe(transactions)