import json

from src.database.connection import (
    get_connection
)


class OpportunityReportRepository:

    def save(
        self,
        linkedin_job_id: str,
        title: str,
        company: str,
        score: int,
        decision: str,
        confidence: str,
        recommendation: str,
        strengths: list,
        weaknesses: list,
        matched_skills: list,
        missing_skills: list
    ):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO opportunity_reports (
                linkedin_job_id,
                title,
                company,
                score,
                decision,
                confidence,
                recommendation,
                strengths,
                weaknesses,
                matched_skills,
                missing_skills
            )
            VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
            ON CONFLICT (linkedin_job_id)
            DO NOTHING
            """,
            (
                linkedin_job_id,
                title,
                company,
                score,
                decision,
                confidence,
                recommendation,
                json.dumps(strengths),
                json.dumps(weaknesses),
                json.dumps(matched_skills),
                json.dumps(missing_skills)
            )
        )

        connection.commit()

        cursor.close()

        connection.close()

    def find_all(self):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM opportunity_reports
            ORDER BY id DESC
            """
        )

        rows = cursor.fetchall()

        cursor.close()

        connection.close()

        return rows