from generators.base_generator import BaseGenerator


class CoverageTypeGenerator(BaseGenerator):

    def generate(self):

        coverages = [

            {
                "coverage_type_id": 1,
                "coverage_code": "COMP",
                "coverage_name": "Comprehensive Cover",
                "coverage_description": "Comprehensive damage protection.",
                "insurance_product_id": 1,
                "default_limit_amount": 5000000.00,
                "default_deductible_amount": 1000.00,
                "coverage_status": "ACTIVE",
                **self.audit_columns()
            },

            {
                "coverage_type_id": 2,
                "coverage_code": "TP",
                "coverage_name": "Third Party Liability",
                "coverage_description": "Third party legal liability.",
                "insurance_product_id": 1,
                "default_limit_amount": 7500000.00,
                "default_deductible_amount": 0.00,
                "coverage_status": "ACTIVE",
                **self.audit_columns()
            },

            {
                "coverage_type_id": 3,
                "coverage_code": "FIRE",
                "coverage_name": "Fire Damage",
                "coverage_description": "Fire and explosion coverage.",
                "insurance_product_id": 2,
                "default_limit_amount": 50000000.00,
                "default_deductible_amount": 5000.00,
                "coverage_status": "ACTIVE",
                **self.audit_columns()
            },

            {
                "coverage_type_id": 4,
                "coverage_code": "THEFT",
                "coverage_name": "Theft Coverage",
                "coverage_description": "Loss due to burglary or theft.",
                "insurance_product_id": 2,
                "default_limit_amount": 10000000.00,
                "default_deductible_amount": 2000.00,
                "coverage_status": "ACTIVE",
                **self.audit_columns()
            },

            {
                "coverage_type_id": 5,
                "coverage_code": "COMM_PROP",
                "coverage_name": "Commercial Property Cover",
                "coverage_description": "Commercial property asset protection.",
                "insurance_product_id": 3,
                "default_limit_amount": 100000000.00,
                "default_deductible_amount": 10000.00,
                "coverage_status": "ACTIVE",
                **self.audit_columns()
            }

        ]

        return self.dataframe(coverages)