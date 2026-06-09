import json

from database.connection import get_connection


class OpportunityPersistenceService:

    def save_from_json(self, file_path: str) -> None:

        with open(file_path, "r", encoding="utf-8") as file:
            opportunities = json.load(file)

        connection = get_connection()
        cursor = connection.cursor()

        for opportunity in opportunities:

            cursor.execute(
                """
                INSERT INTO opportunity_analysis (
                    job_file,
                    score,
                    recommendation,
                    decision,
                    confidence,
                    reason,
                    matched_skills,
                    missing_skills,
                    strengths,
                    weaknesses
                )
                VALUES (
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s
                )
                """,
                (
                    opportunity["job_file"],
                    opportunity["score"],
                    opportunity["recommendation"],
                    opportunity["decision"],
                    opportunity["confidence"],
                    opportunity["reason"],
                    json.dumps(opportunity["matched_skills"]),
                    json.dumps(opportunity["missing_skills"]),
                    json.dumps(opportunity["strengths"]),
                    json.dumps(opportunity["weaknesses"])
                )
            )

        connection.commit()

        cursor.close()
        connection.close()

        print(
            f"{len(opportunities)} opportunities saved successfully!"
        )