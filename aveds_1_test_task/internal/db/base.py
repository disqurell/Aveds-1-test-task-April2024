from settings.db import db


class DbBaseController:
    def __init__(self):
        self.conn = None
        self.cur = None

    def establish_connection(self):
        db.connect()
        self.conn = db.get_connection()
        self.cur = self.conn.cursor()

    def select_from_table_with_condition(
        self, table_name: str, condition: str, value: str
    ):
        try:
            select = f"""SELECT * FROM {table_name} WHERE {condition}='{value}';"""
            self.cur.execute(select)
        except Exception:
            self.establish_connection()
            self.cur.execute(select)
        return self.cur.fetchall()

    def select_from_table(self, table_name: str):
        try:
            select = f"""SELECT * FROM {table_name};"""
            self.cur.execute(select)
        except Exception:
            self.establish_connection()
            self.cur.execute(select)
        return self.cur.fetchall()

    def add(self, table_name: str, fields: tuple, values: tuple):
        SINGLE_INSERT_QUERY = (
            "INSERT INTO {table_name} {fields_name} VALUES {values};".format(
                table_name=table_name, fields_name=fields, values=values
            )
        )
        try:
            self.cur.execute(SINGLE_INSERT_QUERY)
            self.conn.commit()
        except Exception:
            self.establish_connection()
            self.cur.execute(SINGLE_INSERT_QUERY)
            self.conn.commit()
        return True

    def update_table_with_condition(self, table_name: str, field: str, field_value: str, condition: str, value: str):
        update = f"""UPDATE {table_name} SET {field}='{field_value}' WHERE {condition}='{value}';"""
        try:
            self.cur.execute(update)
            self.conn.commit()
        except Exception:
            self.establish_connection()
            self.cur.execute(update)
            self.conn.commit()
        return True


DbController = DbBaseController()
