import random
from datetime import date
from generators.base_generator import BaseGenerator


class ClaimGenerator(BaseGenerator):

    CLAIM_TYPES = [
        "OWN_DAMAGE",
        "THIRD_PARTY",
        "FIRE",
        "THEFT",
        "FLOOD",
        "LIABILITY"
    ]

    CLAIM_STATUS = [
        "OPEN",
        "UNDER_REVIEW",
        "SETTLED",
        "REJECTED"
    ]

    def generate(self, fnol_df):

        claims = []

        claim_id = 1

        for _, fnol in fnol_df.iterrows():

            claim_amount = random.randint(
                10000,
                1500000
            )

            approved_amount = round(
                claim_amount *
                random.uniform(0.60, 1.00),
                2
            )

            

            settlement_date = None

            if random.random() < 0.40:

                reported_date = fnol["reported_date"]

                if reported_date <= date.today():

                    settlement_date = self.fake.date_between(
                        start_date=reported_date,
                        end_date="today"
                    )

            record = {

                "claim_id": claim_id,

                "claim_reference":
                    f"CLM-{claim_id:08d}",

                "fnol_id":
                    fnol["fnol_id"],

                "policy_id":
                    fnol["policy_id"],

                "claim_type":
                    random.choice(
                        self.CLAIM_TYPES
                    ),

                "claim_status":
                    random.choice(
                        self.CLAIM_STATUS
                    ),

                "loss_date":
                    fnol["incident_date"],

                "reported_date":
                    fnol["reported_date"],

                "claim_amount":
                    claim_amount,

                "approved_amount":
                    approved_amount,

                "settlement_date":
                    settlement_date,

                **self.audit_columns()

            }

            claims.append(record)

            claim_id += 1

        return self.dataframe(claims)