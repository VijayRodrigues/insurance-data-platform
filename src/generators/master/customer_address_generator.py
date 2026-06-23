import random

from generators.base_generator import BaseGenerator


class CustomerAddressGenerator(BaseGenerator):

    ADDRESS_TYPES = [
        "HOME",
        "MAILING",
        "OFFICE"
    ]

    APARTMENT_NAMES = [
        "Prestige Shantiniketan",
        "Brigade Gateway",
        "Sobha Dream Acres",
        "Embassy Lake Terraces",
        "Purva Skywood",
        "Godrej Air",
        "Assetz Marq",
        "Salarpuria Sattva",
        "Mantri Serenity",
        "Brigade Cornerstone"
    ]

    def generate(self, customer_df):

        addresses = []

        customer_address_id = 1

        for _, customer in customer_df.iterrows():

            number_of_addresses = random.randint(1, 3)

            for address_number in range(number_of_addresses):

                city = self.fake.city()
                state = self.fake.state()
                postal_code = self.fake.postcode()

                address = {

                    "customer_address_id": customer_address_id,

                    "customer_id": customer["customer_id"],

                    "address_type": self.ADDRESS_TYPES[
                        min(address_number, len(self.ADDRESS_TYPES) - 1)
                    ],

                    "address_line_1": (
                        f"{random.randint(1,999)}, "
                        f"{self.fake.street_name()}"
                    ),

                    "address_line_2": (
                        random.choice(self.APARTMENT_NAMES)
                        if random.random() < 0.60
                        else None
                    ),

                    "landmark": None,

                    "city": city,

                    "state": state,

                    "postal_code": postal_code,

                    "country": "India",

                    "is_primary": address_number == 0,

                    **self.audit_columns()

                }

                addresses.append(address)

                customer_address_id += 1

        return self.dataframe(addresses)