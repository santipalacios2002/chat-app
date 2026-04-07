from psycopg import connect


def check_database_connection(database_url: str) -> bool:
    with connect(database_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            return cursor.fetchone() == (1,)
