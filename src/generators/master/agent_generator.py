import random

from generators.base_generator import BaseGenerator


class AgentGenerator(BaseGenerator):

    AGENT_STATUS = [
        "ACTIVE",
        "INACTIVE",
        "ON_LEAVE"
    ]

    def generate(self, branch_df, number_of_agents=50):

        agents = []

        for agent_id in range(1, number_of_agents + 1):

            branch = branch_df.sample(1).iloc[0]

            hire_date = self.fake.date_between(
                start_date="-20y",
                end_date="-30d"
            )

            record = {

                "agent_id": agent_id,

                "agent_number": f"AGT-{agent_id:06d}",

                "first_name": self.fake.first_name(),

                "last_name": self.fake.last_name(),

                "email_address": self.fake.unique.email(),

                "mobile_number": self.fake.msisdn()[:10],

                "license_number": f"IRDAI-AG-{100000 + agent_id}",

                "hire_date": hire_date,

                "branch_id": branch["branch_id"],

                "agent_status": random.choice(
                    self.AGENT_STATUS
                ),

                **self.audit_columns()

            }

            agents.append(record)

        return self.dataframe(agents)