import psycopg2

from .config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


class PostgresManager:
    def __init__(self, dbname, user, password, host, port) -> None:
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        self.conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )
        self.cur = self.conn.cursor()
        return self

    def get_cursor(self):
        return self.cur

    def get_connection(self):
        return self.conn

    def close_connection(self):
        self.cur.close()
        self.conn.close()


db = PostgresManager(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT).connect()
