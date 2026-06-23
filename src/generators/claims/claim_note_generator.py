from generators.base_generator import BaseGenerator


class ClaimNoteGenerator(BaseGenerator):

    def generate(self, claim_df):

        notes = []

        claim_note_id = 1

        for _, claim in claim_df.iterrows():

            note_count = self.fake.random_int(
                min=1,
                max=5
            )

            for _ in range(note_count):

                notes.append({

                    "claim_note_id": claim_note_id,

                    "claim_id": claim["claim_id"],

                    "note_text": self.fake.paragraph(),

                    **self.audit_columns()

                })

                claim_note_id += 1

        return self.dataframe(notes)