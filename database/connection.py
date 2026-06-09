import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="career_scout",
        user="career_user",
        password="career_password"
    )