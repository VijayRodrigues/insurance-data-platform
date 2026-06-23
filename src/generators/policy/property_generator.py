import random

from generators.base_generator import BaseGenerator


class PropertyGenerator(BaseGenerator):

    PROPERTY_TYPES = [
        "RESIDENTIAL",
        "COMMERCIAL"
    ]

    CONSTRUCTION_TYPES = [
        "RCC",
        "STEEL",
        "BRICK",
        "MIXED"
    ]

    APARTMENT_NAMES = [
        "Prestige Shantiniketan",
        "Brigade Gateway",
        "Sobha Dream Acres",
        "Embassy Lake Terraces",
        "Purva Skywood",
        "Godrej Air",
        "Assetz Marq",
        "Salarpuria Sattva"
    ]

    def generate(self, policy_df):

        properties = []

        property_id = 1

        property_policies = policy_df[
            policy_df["insurance_product_id"].isin([2, 3])
        ]

        for _, policy in property_policies.iterrows():

            property_type = (
                "COMMERCIAL"
                if policy["insurance_product_id"] == 3
                else "RESIDENTIAL"
            )

            record = {

                "property_id": property_id,

                "policy_id": policy["policy_id"],

                "property_identifier":
                    f"PROP-{property_id:08d}",

                "property_type": property_type,

                "address_line_1":
                    f"{random.randint(1,999)}, "
                    f"{self.fake.street_name()}",

                "address_line_2":
                    random.choice(self.APARTMENT_NAMES),

                "city":
                    self.fake.city(),

                "state":
                    self.fake.state(),

                "postal_code":
                    self.fake.postcode(),

                "country":
                    "India",

                "construction_type":
                    random.choice(
                        self.CONSTRUCTION_TYPES
                    ),

                "year_built":
                    random.randint(1980, 2025),

                "number_of_floors":
                    random.randint(1, 25),

                "replacement_value":
                    random.randint(
                        1000000,
                        100000000
                    ),

                "market_value":
                    random.randint(
                        1000000,
                        120000000
                    ),

                **self.audit_columns()

            }

            properties.append(record)

            property_id += 1

        return self.dataframe(properties)