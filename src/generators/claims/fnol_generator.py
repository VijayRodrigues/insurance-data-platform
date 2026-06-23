import random

from generators.base_generator import BaseGenerator


class FNOLGenerator(BaseGenerator):

    LOSS_TYPES = [
        "COLLISION",
        "FIRE",
        "FLOOD",
        "THEFT",
        "WINDSHIELD",
        "LIABILITY"
    ]

    REPORT_CHANNELS = [
        "CUSTOMER_PORTAL",
        "CALL_CENTER",
        "AGENT",
        "BROKER"
    ]

    def generate(self, policy_df):

        fnols = []

        fnol_id = 1

        sample_policies = policy_df.sample(
            frac=0.30,
            random_state=42
        )

        for _, policy in sample_policies.iterrows():

            loss_date = self.fake.date_between(
                start_date=policy["policy_effective_date"],
                end_date=policy["policy_expiry_date"]
            )

            record = {

                "fnol_id": fnol_id,

                "fnol_number": f"FNOL-{fnol_id:08d}",

                "policy_id": policy["policy_id"],

                "reported_date": loss_date,

                "loss_date": loss_date,

                "loss_type": random.choice(
                    self.LOSS_TYPES
                ),

                "report_channel": random.choice(
                    self.REPORT_CHANNELS
                ),

                "loss_description": self.fake.sentence(),

                **self.audit_columns()

            }

            fnols.append(record)

            fnol_id += 1

        return self.dataframe(fnols)