from faker import Faker
import random
import pandas as pd

from config.settings import RANDOM_SEED

fake = Faker("en_IN")

Faker.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)


class MasterDataGenerator:

    def generate_branches(self):

        branches = [

            {
                "branch_code": "BLR001",
                "branch_name": "Bangalore Branch",
                "city": "Bangalore",
                "state": "Karnataka",
                "country": "India"
            },

            {
                "branch_code": "MUM001",
                "branch_name": "Mumbai Branch",
                "city": "Mumbai",
                "state": "Maharashtra",
                "country": "India"
            },

            {
                "branch_code": "DEL001",
                "branch_name": "Delhi Branch",
                "city": "New Delhi",
                "state": "Delhi",
                "country": "India"
            },

            {
                "branch_code": "CHE001",
                "branch_name": "Chennai Branch",
                "city": "Chennai",
                "state": "Tamil Nadu",
                "country": "India"
            },

            {
                "branch_code": "HYD001",
                "branch_name": "Hyderabad Branch",
                "city": "Hyderabad",
                "state": "Telangana",
                "country": "India"
            }

        ]

        return pd.DataFrame(branches)

    def generate_products(self):

        products = [

            {
                "product_code": "AUTO_STD",
                "product_name": "Private Car Insurance",
                "product_category": "Motor"
            },

            {
                "product_code": "HOME_STD",
                "product_name": "Home Insurance",
                "product_category": "Property"
            },

            {
                "product_code": "COMM_PROP",
                "product_name": "Commercial Property Insurance",
                "product_category": "Commercial"
            }

        ]

        return pd.DataFrame(products)

    def generate_coverages(self):

        coverages = [

            {
                "coverage_code": "COMP",
                "coverage_name": "Comprehensive"
            },

            {
                "coverage_code": "TP",
                "coverage_name": "Third Party"
            },

            {
                "coverage_code": "FIRE",
                "coverage_name": "Fire Damage"
            },

            {
                "coverage_code": "THEFT",
                "coverage_name": "Theft"
            },

            {
                "coverage_code": "FLOOD",
                "coverage_name": "Flood"
            }

        ]

        return pd.DataFrame(coverages)

    def generate_agents(self, count=50):

        data = []

        for i in range(count):

            data.append({

                "agent_number": f"AGT{i+1:05d}",

                "first_name": fake.first_name(),

                "last_name": fake.last_name(),

                "email": fake.email(),

                "mobile": fake.phone_number()

            })

        return pd.DataFrame(data)

    def generate_underwriters(self, count=20):

        data = []

        for i in range(count):

            data.append({

                "underwriter_number": f"UND{i+1:05d}",

                "first_name": fake.first_name(),

                "last_name": fake.last_name(),

                "email": fake.email()

            })

        return pd.DataFrame(data)

    def generate_brokers(self, count=25):

        data = []

        for i in range(count):

            data.append({

                "broker_number": f"BRK{i+1:05d}",

                "broker_name": fake.company(),

                "email": fake.company_email()

            })

        return pd.DataFrame(data)