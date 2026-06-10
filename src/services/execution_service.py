from database.connection import get_connection


class ExecutionService:

    def create_execution(self) -> int:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO executions
            DEFAULT VALUES
            RETURNING id
            """
        )

        execution_id = cursor.fetchone()[0]

        connection.commit()

        cursor.close()

        connection.close()

        print(
            f"Execution #{execution_id} created successfully!"
        )

        return execution_id