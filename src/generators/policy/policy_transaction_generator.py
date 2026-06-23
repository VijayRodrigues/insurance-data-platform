import random
from datetime import timedelta

from generators.base_generator import BaseGenerator


class PolicyTransactionGenerator(BaseGenerator):

    TRANSACTION_TYPES = [
        "NEW_BUSINESS",
        "ENDORSEMENT",
        "RENEWAL",
        "CANCELLATION"
    ]

    TRANSACTION_STATUS = [
        "COMPLETED",
        "PENDING"
    ]

    def generate(
            self,
            policy_df,
            policy_version_df):

        transactions = []

        policy_transaction_id = 1

        for _, version in policy_version_df.iterrows():

            policy = policy_df[
                policy_df["policy_id"] == version["policy_id"]
            ].iloc[0]

            transaction_type = (
                "NEW_BUSINESS"
                if version["version_number"] == 1
                else random.choice([
                    "ENDORSEMENT",
                    "RENEWAL"
                ])
            )

            amount = round(
                policy["total_premium"] *
                random.uniform(0.90, 1.10),
                2
            )

            record = {

                "policy_transaction_id": policy_transaction_id,

                "policy_id": policy["policy_id"],

                "policy_version_id": version[
                    "policy_version_id"
                ],

                "transaction_type": transaction_type,

                "transaction_date": (
                    version["effective_from"] +
                    timedelta(days=random.randint(0, 5))
                ),

                "transaction_status": random.choice(
                    self.TRANSACTION_STATUS
                ),

                "transaction_amount": amount,

                "remarks": None,

                **self.audit_columns()

            }

            transactions.append(record)

            policy_transaction_id += 1

        return self.dataframe(transactions)