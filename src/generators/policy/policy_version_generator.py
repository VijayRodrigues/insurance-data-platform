import random
from datetime import timedelta

from generators.base_generator import BaseGenerator


class PolicyVersionGenerator(BaseGenerator):

    VERSION_STATUS = [
        "ACTIVE",
        "SUPERSEDED"
    ]

    ENDORSEMENT_REASONS = [
        None,
        "Address Change",
        "Vehicle Change",
        "Coverage Increase",
        "Coverage Reduction",
        "Nominee Update",
        "Correction"
    ]

    def generate(self, policy_df):

        policy_versions = []

        policy_version_id = 1

        for _, policy in policy_df.iterrows():

            version_count = random.choices(
                population=[1, 2, 3],
                weights=[75, 20, 5],
                k=1
            )[0]

            effective_from = policy["policy_effective_date"]

            for version in range(1, version_count + 1):

                record = {

                    "policy_version_id": policy_version_id,

                    "policy_id": policy["policy_id"],

                    "version_number": version,

                    "effective_from": effective_from,

                    "effective_to": None,

                    "endorsement_reason": random.choice(
                        self.ENDORSEMENT_REASONS
                    ),

                    "version_status": (
                        "ACTIVE"
                        if version == version_count
                        else "SUPERSEDED"
                    ),

                    "remarks": None,

                    **self.audit_columns()

                }

                policy_versions.append(record)

                policy_version_id += 1

                effective_from = (
                    effective_from +
                    timedelta(days=random.randint(30, 180))
                )

        return self.dataframe(policy_versions)