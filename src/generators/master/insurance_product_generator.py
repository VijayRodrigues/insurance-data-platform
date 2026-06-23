from datetime import date

from generators.base_generator import BaseGenerator


class InsuranceProductGenerator(BaseGenerator):

    def generate(self):

        products = [

            {
                "insurance_product_id": 1,
                "product_code": "MOTOR_PRIVATE_CAR",
                "product_name": "Private Car Insurance",
                "product_category": "MOTOR",
                "description": "Comprehensive insurance for private passenger vehicles.",
                "minimum_sum_insured": 100000.00,
                "maximum_sum_insured": 5000000.00,
                "minimum_premium": 2500.00,
                "maximum_premium": 150000.00,
                "product_status": "ACTIVE",
                "effective_from": date(2024, 1, 1),
                "effective_to": None,
                **self.audit_columns()
            },

            {
                "insurance_product_id": 2,
                "product_code": "HOME_INSURANCE",
                "product_name": "Home Insurance",
                "product_category": "PROPERTY",
                "description": "Residential building and contents insurance.",
                "minimum_sum_insured": 500000.00,
                "maximum_sum_insured": 50000000.00,
                "minimum_premium": 5000.00,
                "maximum_premium": 250000.00,
                "product_status": "ACTIVE",
                "effective_from": date(2024, 1, 1),
                "effective_to": None,
                **self.audit_columns()
            },

            {
                "insurance_product_id": 3,
                "product_code": "COMMERCIAL_PROPERTY",
                "product_name": "Commercial Property Insurance",
                "product_category": "COMMERCIAL",
                "description": "Insurance for commercial buildings and business assets.",
                "minimum_sum_insured": 1000000.00,
                "maximum_sum_insured": 100000000.00,
                "minimum_premium": 10000.00,
                "maximum_premium": 1000000.00,
                "product_status": "ACTIVE",
                "effective_from": date(2024, 1, 1),
                "effective_to": None,
                **self.audit_columns()
            }

        ]

        return self.dataframe(products)