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

    FNOL_STATUS = [
        "OPEN",
        "UNDER_REVIEW",
        "CLOSED"
    ]

    def generate(self, policy_df):

        fnols = []

        fnol_id = 1

        sample_policies = policy_df.sample(
            frac=0.30,
            random_state=42
        )

        for _, policy in sample_policies.iterrows():

            incident_date = self.fake.date_between(
                start_date=policy["policy_effective_date"],
                end_date=policy["policy_expiry_date"]
            )

            reported_date = self.fake.date_between(
                start_date=incident_date,
                end_date=policy["policy_expiry_date"]
            )

            record = {

                "fnol_id": fnol_id,

                "fnol_reference":
                    f"FNOL-{fnol_id:08d}",

                "policy_id":
                    policy["policy_id"],

                "reported_by":
                    random.choice(self.REPORT_CHANNELS),

                "reported_date":
                    reported_date,

                "incident_date":
                    incident_date,

                "incident_location":
                    self.fake.address(),

                "incident_description":
                    self.fake.paragraph(),

                "loss_type":
                    random.choice(self.LOSS_TYPES),

                "fnol_status":
                    random.choice(self.FNOL_STATUS),

                **self.audit_columns()

            }

            fnols.append(record)

            fnol_id += 1

        return self.dataframe(fnols)