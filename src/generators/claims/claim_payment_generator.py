import random

from datetime import date

from generators.base_generator import BaseGenerator


class ClaimPaymentGenerator(BaseGenerator):

    PAYMENT_METHODS = [
        "BANK_TRANSFER",
        "NEFT",
        "RTGS",
        "CHEQUE",
        "UPI"
    ]

    PAYMENT_STATUS = [
        "INITIATED",
        "PROCESSING",
        "COMPLETED",
        "FAILED"
    ]

    def generate(self, claim_df):

        payments = []

        claim_payment_id = 1

        for _, claim in claim_df.iterrows():

            if claim["approved_amount"] is None:
                continue

            if claim["claim_status"] != "SETTLED":
                continue

            payment_amount = round(
                claim["approved_amount"],
                2
            )

            settlement_date = claim["settlement_date"]

            if settlement_date is not None:

                payment_date = settlement_date

            else:

                reported_date = claim["reported_date"]

                if reported_date <= date.today():

                    payment_date = self.fake.date_between(
                        start_date=reported_date,
                        end_date="today"
                    )

                else:

                    payment_date = reported_date

            record = {

                "claim_payment_id":
                    claim_payment_id,

                "payment_reference":
                    f"PAY-{claim_payment_id:08d}",

                "claim_id":
                    claim["claim_id"],

                "payment_date":
                    payment_date,

                "payment_amount":
                    payment_amount,

                "payment_method":
                    random.choice(
                        self.PAYMENT_METHODS
                    ),

                "payment_status":
                    random.choice(
                        self.PAYMENT_STATUS
                    ),

                "transaction_reference":
                    self.fake.uuid4(),

                "remarks":
                    self.fake.sentence(),

                **self.audit_columns()

            }

            payments.append(record)

            claim_payment_id += 1

        return self.dataframe(payments)