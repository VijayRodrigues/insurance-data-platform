import random

from generators.base_generator import BaseGenerator


class ClaimReserveTransactionGenerator(BaseGenerator):

    TRANSACTION_TYPES = [
        "INITIAL",
        "INCREASE",
        "DECREASE"
    ]

    def generate(self, reserve_df):

        transactions = []

        claim_reserve_transaction_id = 1

        for _, reserve in reserve_df.iterrows():

            transaction_count = random.randint(
                1,
                3
            )

            balance = reserve["reserve_amount"]

            for _ in range(transaction_count):

                amount = round(
                    random.uniform(
                        1000,
                        balance * 0.30
                    ),
                    2
                )

                transactions.append({

                    "claim_reserve_transaction_id":
                        claim_reserve_transaction_id,

                    "claim_reserve_id":
                        reserve["claim_reserve_id"],

                    "transaction_type":
                        random.choice(
                            self.TRANSACTION_TYPES
                        ),

                    "transaction_amount":
                        amount,

                    **self.audit_columns()

                })

                claim_reserve_transaction_id += 1

        return self.dataframe(
            transactions
        )