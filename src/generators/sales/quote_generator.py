import random
from datetime import timedelta

from generators.base_generator import BaseGenerator


class QuoteGenerator(BaseGenerator):

    QUOTE_STATUS = [
        "DRAFT",
        "SUBMITTED",
        "APPROVED",
        "REJECTED",
        "EXPIRED"
    ]

    CURRENCY_CODE = "INR"

    def generate(
            self,
            customer_df,
            product_df,
            agent_df,
            broker_df,
            branch_df):

        quotes = []

        quote_id = 1

        for _, customer in customer_df.iterrows():

            number_of_quotes = random.randint(1, 3)

            for _ in range(number_of_quotes):

                product = product_df.sample(1).iloc[0]
                agent = agent_df.sample(1).iloc[0]
                broker = broker_df.sample(1).iloc[0]
                branch = branch_df.sample(1).iloc[0]

                quote_date = self.fake.date_between(
                    start_date="-3y",
                    end_date="today"
                )

                premium = round(
                    random.uniform(2500, 150000),
                    2
                )

                quote = {

                    "quote_id": quote_id,

                    "quote_number": f"QT-{quote_id:08d}",

                    "customer_id": customer["customer_id"],

                    "insurance_product_id": product["insurance_product_id"],

                    "agent_id": agent["agent_id"],

                    "broker_id": broker["broker_id"],

                    "branch_id": branch["branch_id"],

                    "quote_date": quote_date,

                    "quote_expiry_date": quote_date + timedelta(days=30),

                    "quote_status": random.choice(self.QUOTE_STATUS),

                    "total_premium": premium,

                    "currency_code": self.CURRENCY_CODE,

                    "remarks": None,

                    **self.audit_columns()

                }

                quotes.append(quote)

                quote_id += 1

        return self.dataframe(quotes)