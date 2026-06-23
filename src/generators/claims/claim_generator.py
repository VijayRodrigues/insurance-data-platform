import random

from generators.base_generator import BaseGenerator


class ClaimGenerator(BaseGenerator):

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

            estimated_loss = random.randint(
                10000,
                1500000
            )

            approved = round(
                estimated_loss *
                random.uniform(0.60, 1.00),
                2
            )

            record = {

                "claim_id": claim_id,

                "claim_number":
                    f"CLM-{claim_id:08d}",

                "fnol_id":
                    fnol["fnol_id"],

                "claim_status":
                    random.choice(
                        self.CLAIM_STATUS
                    ),

                "estimated_loss_amount":
                    estimated_loss,

                "approved_amount":
                    approved,

                "closed_date":
                    None,

                "remarks":
                    None,

                **self.audit_columns()

            }

            claims.append(record)

            claim_id += 1

        return self.dataframe(claims)