import random
from datetime import timedelta

from generators.base_generator import BaseGenerator


class PremiumPaymentGenerator(BaseGenerator):

    PAYMENT_METHODS = [
        "UPI",
        "NET_BANKING",
        "CREDIT_CARD",
        "DEBIT_CARD",
        "NEFT"
    ]

    PAYMENT_STATUS = [
        "SUCCESS",
        "FAILED",
        "PENDING"
    ]

    def generate(self, premium_df):

        payments = []

        premium_payment_id = 1

        for _, premium in premium_df.iterrows():

            if premium["premium_status"] == "PENDING":
                continue

            payment_date = (
                premium["due_date"] -
                timedelta(days=random.randint(0, 5))
            )

            record = {

                "premium_payment_id": premium_payment_id,

                "payment_reference":
                    f"PAY-{premium_payment_id:08d}",

                "premium_id":
                    premium["premium_id"],

                "payment_date":
                    payment_date,

                "payment_amount":
                    premium["total_amount"],

                "payment_method":
                    random.choice(
                        self.PAYMENT_METHODS
                    ),

                "payment_status":
                    "SUCCESS",

                "transaction_reference":
                    self.fake.unique.bothify(
                        "TXN############"
                    ),

                "received_by":
                    random.choice([
                        "ONLINE_PORTAL",
                        "BANK",
                        "AGENT"
                    ]),

                "remarks":
                    None,

                **self.audit_columns()

            }

            payments.append(record)

            premium_payment_id += 1

        return self.dataframe(payments)