import random

from generators.base_generator import BaseGenerator


class PolicyCoverageGenerator(BaseGenerator):

    def generate(
            self,
            policy_version_df,
            coverage_type_df):

        policy_coverages = []

        policy_coverage_id = 1

        for _, version in policy_version_df.iterrows():

            number_of_coverages = random.randint(1, 3)

            coverages = coverage_type_df.sample(
                n=min(
                    number_of_coverages,
                    len(coverage_type_df)
                ),
                replace=False
            )

            for _, coverage in coverages.iterrows():

                coverage_limit = float(
                    coverage["default_limit_amount"]
                )

                deductible = float(
                    coverage["default_deductible_amount"]
                )

                premium = round(
                    coverage_limit *
                    random.uniform(0.004, 0.015),
                    2
                )

                record = {

                    "policy_coverage_id": policy_coverage_id,

                    "policy_version_id": version[
                        "policy_version_id"
                    ],

                    "coverage_type_id": coverage[
                        "coverage_type_id"
                    ],

                    "coverage_limit_amount": coverage_limit,

                    "deductible_amount": deductible,

                    "premium_amount": premium,

                    "coverage_status": "ACTIVE",

                    **self.audit_columns()

                }

                policy_coverages.append(record)

                policy_coverage_id += 1

        return self.dataframe(policy_coverages)