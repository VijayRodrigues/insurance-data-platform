import random

from generators.base_generator import BaseGenerator


class BrokerGenerator(BaseGenerator):

    BROKER_STATUS = [
        "ACTIVE",
        "INACTIVE"
    ]

    COMPANY_SUFFIXES = [
        "Insurance Brokers Pvt Ltd",
        "Risk Solutions Pvt Ltd",
        "Insurance Services LLP",
        "Risk Advisors LLP",
        "Insurance Consultants Pvt Ltd"
    ]

    def generate(self, number_of_brokers=25):

        brokers = []

        for broker_id in range(1, number_of_brokers + 1):

            company_name = (
                f"{self.fake.company()} "
                f"{random.choice(self.COMPANY_SUFFIXES)}"
            )

            record = {

                "broker_id": broker_id,

                "broker_number": f"BRK-{broker_id:06d}",

                "broker_name": company_name,

                "registration_number": f"IRDAI-BR-{500000 + broker_id}",

                "contact_person": (
                    f"{self.fake.first_name()} "
                    f"{self.fake.last_name()}"
                ),

                "email_address": self.fake.unique.company_email(),

                "mobile_number": self.fake.msisdn()[:10],

                "broker_status": random.choice(
                    self.BROKER_STATUS
                ),

                **self.audit_columns()

            }

            brokers.append(record)

        return self.dataframe(brokers)