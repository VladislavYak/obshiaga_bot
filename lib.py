from contextlib import contextmanager
from typing import Generator

import psycopg2

class PgConnect:
    def __init__(self, host: str, port: str, db_name: str, user: str, pw: str, sslmode: str = "require") -> None:
        self.host = host
        self.port = int(port)
        self.db_name = db_name
        self.user = user
        self.pw = pw
        self.sslmode = sslmode

    def url(self) -> str:
        return """
            host={host}
            port={port}
            dbname={db_name}
            user={user}
            password={pw}
            target_session_attrs=read-write
            sslmode={sslmode}
        """.format(
            host=self.host,
            port=self.port,
            db_name=self.db_name,
            user=self.user,
            pw=self.pw,
            sslmode=self.sslmode)

    def client(self):
        return psycopg2.connect(self.url())

    @contextmanager
    def connection(self):
    #  -> Generator[psycopg2.Connect, None, None]:
        conn = psycopg2.connect(self.url())
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()


if __name__ == '__main__':
    pg = PgConnect('localhost', '5432', 'postgres', 'postgres', pw=None, sslmode='disable')
    a = pg.connection()
    a.