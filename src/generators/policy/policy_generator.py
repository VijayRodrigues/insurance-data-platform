import random
from datetime import timedelta

from generators.base_generator import BaseGenerator


class PolicyGenerator(BaseGenerator):

    POLICY_STATUS = [
        "ACTIVE",
        "EXPIRED",
        "CANCELLED"
    ]

    CURRENCY_CODE = "INR"

    def generate(
            self,
            quote_df,
            quote_version_df,
            underwriter_df):

        policies = []

        policy_id = 1

        approved_versions = quote_version_df[
            quote_version_df["underwriting_decision"] == "APPROVED"
        ]

        for _, version in approved_versions.iterrows():

            quote = quote_df[
                quote_df["quote_id"] == version["quote_id"]
            ].iloc[0]

            underwriter = underwriter_df.sample(1).iloc[0]

            effective_date = quote["quote_date"] + timedelta(days=1)

            expiry_date = effective_date + timedelta(days=365)

            record = {

                "policy_id": policy_id,

                "policy_number": f"POL-{policy_id:08d}",

                "customer_id": quote["customer_id"],

                "insurance_product_id": quote["insurance_product_id"],

                "quote_id": quote["quote_id"],

                "branch_id": quote["branch_id"],

                "agent_id": quote["agent_id"],

                "broker_id": quote["broker_id"],

                "underwriter_id": underwriter["underwriter_id"],

                "policy_effective_date": effective_date,

                "policy_expiry_date": expiry_date,

                "policy_issue_date": effective_date,

                "policy_status": random.choice(
                    self.POLICY_STATUS
                ),

                "total_sum_insured": version[
                    "quoted_sum_insured"
                ],

                "total_premium": version[
                    "quoted_premium"
                ],

                "currency_code": self.CURRENCY_CODE,

                **self.audit_columns()

            }

            policies.append(record)

            policy_id += 1

        return self.dataframe(policies)