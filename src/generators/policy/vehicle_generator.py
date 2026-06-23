import random

from generators.base_generator import BaseGenerator


class VehicleGenerator(BaseGenerator):

    MANUFACTURERS = {

        "Maruti Suzuki": [
            "Swift",
            "Baleno",
            "Brezza",
            "Grand Vitara"
        ],

        "Hyundai": [
            "i20",
            "Creta",
            "Venue",
            "Verna"
        ],

        "Tata": [
            "Nexon",
            "Harrier",
            "Punch",
            "Altroz"
        ],

        "Mahindra": [
            "XUV700",
            "Scorpio N",
            "Thar"
        ],

        "Toyota": [
            "Innova Hycross",
            "Fortuner",
            "Urban Cruiser"
        ]

    }

    VEHICLE_TYPES = [
        "HATCHBACK",
        "SEDAN",
        "SUV"
    ]

    FUEL_TYPES = [
        "PETROL",
        "DIESEL",
        "CNG",
        "HYBRID",
        "ELECTRIC"
    ]

    TRANSMISSIONS = [
        "MANUAL",
        "AUTOMATIC"
    ]

    COLORS = [
        "White",
        "Black",
        "Silver",
        "Grey",
        "Blue",
        "Red"
    ]

    def generate(self, policy_df):

        vehicles = []

        vehicle_id = 1

        motor_policies = policy_df[
            policy_df["insurance_product_id"] == 1
        ]

        for _, policy in motor_policies.iterrows():

            manufacturer = random.choice(
                list(self.MANUFACTURERS.keys())
            )

            model = random.choice(
                self.MANUFACTURERS[manufacturer]
            )

            record = {

                "vehicle_id": vehicle_id,

                "policy_id": policy["policy_id"],

                "vehicle_identification_number":
                    self.fake.unique.bothify(
                        "#################"
                    ),

                "registration_number":
                    f"KA{random.randint(1,99):02d}"
                    f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
                    f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
                    f"{random.randint(1000,9999)}",

                "manufacturer": manufacturer,

                "model": model,

                "model_year": random.randint(
                    2015,
                    2026
                ),

                "vehicle_type": random.choice(
                    self.VEHICLE_TYPES
                ),

                "engine_number":
                    self.fake.unique.bothify(
                        "ENG########"
                    ),

                "chassis_number":
                    self.fake.unique.bothify(
                        "CHS############"
                    ),

                "fuel_type": random.choice(
                    self.FUEL_TYPES
                ),

                "transmission_type": random.choice(
                    self.TRANSMISSIONS
                ),

                "color": random.choice(
                    self.COLORS
                ),

                "market_value": random.randint(
                    400000,
                    3500000
                ),

                **self.audit_columns()

            }

            vehicles.append(record)

            vehicle_id += 1

        return self.dataframe(vehicles)