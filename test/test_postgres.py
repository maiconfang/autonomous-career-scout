import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="career_scout",
        user="career_user",
        password="career_password"
    )

    print("Connected successfully!")

    cursor = connection.cursor()

    cursor.execute("SELECT version();")

    result = cursor.fetchone()

    print(result)

    cursor.close()
    connection.close()

except Exception as error:
    print(error)