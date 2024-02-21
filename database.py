# database.py

import sqlite3

class DatabaseManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()

    def create_table(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def execute_query(self, query, params=None):
        if params:
            self.cur.execute(query, params)
        else:
            self.cur.execute(query)
        self.conn.commit()

    def fetch_data(self, query, params=None):
        if params:
            self.cur.execute(query, params)
        else:
            self.cur.execute(query)
        return self.cur.fetchall()

    def close_connection(self):
        self.conn.close()
