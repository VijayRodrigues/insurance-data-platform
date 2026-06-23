import random

from generators.base_generator import BaseGenerator


class ClaimPaymentGenerator(BaseGenerator):

    PAYMENT_METHODS = [
        "NEFT",
        "RTGS",
        "CHEQUE",
        "IMPS"
    ]

    def generate(
            self,
            claim_df):

        payments = []

        claim_payment_id = 1

        settled_claims = claim_df[
            claim_df["claim_status"] == "SETTLED"
        ]

        for _, claim in settled_claims.iterrows():

            amount = round(
                claim["approved_amount"] *
                random.uniform(0.95, 1.00),
                2
            )

            payments.append({

                "claim_payment_id":
                    claim_payment_id,

                "claim_id":
                    claim["claim_id"],

                "payment_amount":
                    amount,

                "payment_method":
                    random.choice(
                        self.PAYMENT_METHODS
                    ),

                "payment_reference":
                    self.fake.unique.bothify(
                        "CLMPAY##########"
                    ),

                "payment_date":
                    self.fake.date_between(
                        start_date="-1y",
                        end_date="today"
                    ),

                **self.audit_columns()

            })

            claim_payment_id += 1

        return self.dataframe(
            payments
        )