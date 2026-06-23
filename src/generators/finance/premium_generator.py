import random
from datetime import timedelta

from generators.base_generator import BaseGenerator


class PremiumGenerator(BaseGenerator):

    PREMIUM_FREQUENCIES = [
        "ANNUAL",
        "HALF_YEARLY",
        "QUARTERLY",
        "MONTHLY"
    ]

    PREMIUM_STATUS = [
        "PAID",
        "PENDING",
        "OVERDUE"
    ]

    def generate(
            self,
            policy_df,
            policy_version_df):

        premiums = []

        premium_id = 1

        latest_versions = (
            policy_version_df
            .sort_values("version_number")
            .groupby("policy_id")
            .tail(1)
        )

        for _, version in latest_versions.iterrows():

            policy = policy_df[
                policy_df["policy_id"] == version["policy_id"]
            ].iloc[0]

            frequency = random.choice(
                self.PREMIUM_FREQUENCIES
            )

            if frequency == "ANNUAL":
                installments = 1

            elif frequency == "HALF_YEARLY":
                installments = 2

            elif frequency == "QUARTERLY":
                installments = 4

            else:
                installments = 12

            installment_amount = round(
                policy["total_premium"] / installments,
                2
            )

            for installment in range(installments):

                due_date = (
                    policy["policy_effective_date"] +
                    timedelta(days=30 * installment)
                )

                record = {

                    "premium_id": premium_id,

                    "premium_number":
                        f"PRM-{premium_id:08d}",

                    "policy_id":
                        policy["policy_id"],

                    "policy_version_id":
                        version["policy_version_id"],

                    "premium_frequency":
                        frequency,

                    "premium_amount":
                        installment_amount,

                    "tax_amount":
                        round(
                            installment_amount * 0.18,
                            2
                        ),

                    "total_amount":
                        round(
                            installment_amount * 1.18,
                            2
                        ),

                    "due_date":
                        due_date,

                    "premium_status":
                        random.choice(
                            self.PREMIUM_STATUS
                        ),

                    **self.audit_columns()

                }

                premiums.append(record)

                premium_id += 1

        return self.dataframe(premiums)