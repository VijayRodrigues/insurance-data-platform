import random

from generators.base_generator import BaseGenerator


class UnderwriterGenerator(BaseGenerator):

    UNDERWRITER_STATUS = [
        "ACTIVE",
        "INACTIVE"
    ]

    UNDERWRITING_AUTHORITIES = [
        "LEVEL_1",
        "LEVEL_2",
        "LEVEL_3",
        "SENIOR",
        "CHIEF"
    ]

    def generate(self, branch_df, number_of_underwriters=20):

        underwriters = []

        for underwriter_id in range(1, number_of_underwriters + 1):

            branch = branch_df.sample(1).iloc[0]

            record = {

                "underwriter_id": underwriter_id,

                "underwriter_number": f"UND-{underwriter_id:06d}",

                "first_name": self.fake.first_name(),

                "last_name": self.fake.last_name(),

                "email_address": self.fake.unique.email(),

                "mobile_number": self.fake.msisdn()[:10],

                "underwriting_authority": random.choice(
                    self.UNDERWRITING_AUTHORITIES
                ),

                "branch_id": branch["branch_id"],

                "underwriter_status": random.choice(
                    self.UNDERWRITER_STATUS
                ),

                **self.audit_columns()

            }

            underwriters.append(record)

        return self.dataframe(underwriters)