import random

from generators.base_generator import BaseGenerator


class BusinessCustomerGenerator(BaseGenerator):

    INDUSTRIES = [
        "Information Technology",
        "Manufacturing",
        "Healthcare",
        "Banking",
        "Retail",
        "Construction",
        "Education",
        "Hospitality",
        "Logistics",
        "Telecommunications"
    ]

    COMPANY_SUFFIXES = [
        "Private Limited",
        "Limited",
        "LLP",
        "Technologies",
        "Industries",
        "Solutions",
        "Enterprises",
        "Corporation"
    ]

    def generate(self, customer_df, business_customer_percentage=0.15):

        business_customers = []

        business_customer_id = 1

        for _, customer in customer_df.iterrows():

            if random.random() > business_customer_percentage:
                continue

            company_name = (
                f"{self.fake.company()} "
                f"{random.choice(self.COMPANY_SUFFIXES)}"
            )

            annual_revenue = random.randint(
                5_000_000,
                2_000_000_000
            )

            employee_count = random.randint(
                10,
                5000
            )

            business_customer = {

                "business_customer_id": business_customer_id,

                "customer_id": customer["customer_id"],

                "business_name": company_name,

                "registration_number": (
                    f"CIN{random.randint(1000000000,9999999999)}"
                ),

                "tax_identifier": (
                    self.fake.bothify(
                        text="#####AAAAA"
                    ).upper()
                ),

                "industry": random.choice(
                    self.INDUSTRIES
                ),

                "annual_revenue": annual_revenue,

                "employee_count": employee_count,

                "established_date": self.fake.date_between(
                    start_date="-40y",
                    end_date="-1y"
                ),

                **self.audit_columns()

            }

            business_customers.append(
                business_customer
            )

            business_customer_id += 1

        return self.dataframe(
            business_customers
        )