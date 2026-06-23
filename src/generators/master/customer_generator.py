import random
from datetime import date, timedelta

from generators.base_generator import BaseGenerator


class CustomerGenerator(BaseGenerator):

    CUSTOMER_STATUS = [
        "ACTIVE",
        "INACTIVE",
        "SUSPENDED"
    ]

    MARITAL_STATUS = [
        "SINGLE",
        "MARRIED",
        "DIVORCED",
        "WIDOWED"
    ]

    GENDER = [
        "MALE",
        "FEMALE"
    ]

    OCCUPATIONS = [
        "Software Engineer",
        "Doctor",
        "Teacher",
        "Accountant",
        "Business Owner",
        "Lawyer",
        "Sales Executive",
        "Civil Engineer",
        "Mechanical Engineer",
        "Government Employee"
    ]

    def generate(self, number_of_customers):

        customers = []

        for customer_id in range(1, number_of_customers + 1):

            dob = self.fake.date_of_birth(
                minimum_age=18,
                maximum_age=80
            )

            customer = {

                "customer_id": customer_id,

                "customer_number": f"CUST-{date.today().year}-{customer_id:08d}",

                "first_name": self.fake.first_name(),

                "middle_name": self.fake.first_name() if random.random() < 0.40 else None,

                "last_name": self.fake.last_name(),

                "date_of_birth": dob,

                "gender": random.choice(self.GENDER),

                "email_address": self.fake.unique.email(),

                "mobile_number": self.fake.unique.msisdn()[:10],

                "national_id_number": self.fake.unique.bothify("##########"),

                "occupation": random.choice(self.OCCUPATIONS),

                "marital_status": random.choice(self.MARITAL_STATUS),

                "customer_status": random.choice(self.CUSTOMER_STATUS),

                **self.audit_columns()

            }

            customers.append(customer)

        return self.dataframe(customers)