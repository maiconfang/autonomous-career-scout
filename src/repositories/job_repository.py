import json

from src.database.connection import (
    get_connection
)


class JobRepository:

    def save(
        self,
        linkedin_job_id: str,
        title: str,
        company: str,
        location: str,
        job_url: str,
        description: str,
        skills: dict,
        score: int,
        recommendation: str
    ):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO opportunities (
                linkedin_job_id,
                title,
                company,
                location,
                job_url,
                description,
                skills,
                match_score,
                recommendation
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
                %s
            )
            """,
            (
                linkedin_job_id,
                title,
                company,
                location,
                job_url,
                description,
                json.dumps(
                    skills
                ),
                score,
                recommendation
            )
        )

        connection.commit()

        cursor.close()

        connection.close()

    def job_exists(
        self,
        linkedin_job_id: str
    ):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id
            FROM opportunities
            WHERE linkedin_job_id = %s
            LIMIT 1
            """,
            (
                linkedin_job_id,
            )
        )

        row = cursor.fetchone()

        cursor.close()

        connection.close()

        return row is not None

    def find_all(self):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM opportunities
            ORDER BY id DESC
            """
        )

        rows = cursor.fetchall()

        cursor.close()

        connection.close()

        return rows

    def find_top_matches(
        self,
        minimum_score: int = 80
    ):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM opportunities
            WHERE match_score >= %s
            ORDER BY match_score DESC
            """,
            (
                minimum_score,
            )
        )

        rows = cursor.fetchall()

        cursor.close()

        connection.close()

        return rows

    def find_top_5_jobs(self):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM opportunities
            ORDER BY match_score DESC
            LIMIT 5
            """
        )

        rows = cursor.fetchall()

        cursor.close()

        connection.close()

        return rows