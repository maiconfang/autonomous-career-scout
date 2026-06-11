# from src.database.connection import get_connection

# connection = get_connection()

# cursor = connection.cursor()

# cursor.execute(
#     """
#     INSERT INTO opportunities (
#         title,
#         company,
#         location,
#         match_score,
#         recommendation
#     )
#     VALUES (%s, %s, %s, %s, %s)
#     """,
#     (
#         "Senior SDET",
#         "StackAdapt",
#         "Remote",
#         95,
#         "STRONG_APPLY"
#     )
# )

# connection.commit()

# cursor.close()
# connection.close()