import random

from generators.base_generator import BaseGenerator


class ClaimNoteGenerator(BaseGenerator):

    NOTE_TYPES = [
        "SYSTEM",
        "ASSESSOR",
        "CUSTOMER",
        "UNDERWRITER",
        "SURVEYOR"
    ]

    def generate(self, claim_df):

        notes = []

        claim_note_id = 1

        for _, claim in claim_df.iterrows():

            note_count = random.randint(1, 5)

            for _ in range(note_count):

                note_date = self.fake.date_time_between(
                    start_date=claim["reported_date"],
                    end_date="now"
                )

                record = {

                    "claim_note_id":
                        claim_note_id,

                    "claim_id":
                        claim["claim_id"],

                    "note_date":
                        note_date,

                    "note_type":
                        random.choice(
                            self.NOTE_TYPES
                        ),

                    "note_text":
                        self.fake.paragraph(),

                    **self.audit_columns()

                }

                notes.append(record)

                claim_note_id += 1

        return self.dataframe(notes)