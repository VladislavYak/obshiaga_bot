from lib import PgConnect

class UsersTable:
    def __init__(self, pg):
        self.pg = pg

    def add_user(self, username):
        with self.pg.connection() as conn:
            with conn.cursor() as cur:
                sql_query = f"""
                INSERT INTO users (username) VALUES ('{username}')
                """
                print(sql_query)
                cur.execute(sql_query)


if __name__ == '__main__':
    pg = PgConnect('localhost', '5432', 'postgres', 'postgres', pw=None, sslmode='disable')
    UsersTable(pg).add_user('varvara')