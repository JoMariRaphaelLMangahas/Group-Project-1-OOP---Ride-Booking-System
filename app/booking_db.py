import sqlite3
from sqlite3 import Error

class BookingDB:
    def __init__(self, db_file):
        self.conn = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file) -> sqlite3.Connection:
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return None

    def create_table(self):
        sql_create_table = """CREATE TABLE IF NOT EXISTS bookings (
                booking_number INTEGER PRIMARY KEY,
                status TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                pick_up_address TEXT NOT NULL,
                destination TEXT NOT NULL,
                vehicle_type TEXT NOT NULL,
                distance REAL,
                cost REAL,
                driver TEXT
            );"""

        try:
            c = self.conn.cursor()
            c.execute(sql_create_table)
        except Error as e:
            print(e)

    def retrieve_records(self) -> list:
        c = self.conn.cursor()
        try:
            c.execute("SELECT * FROM bookings")
            return c.fetchall()
        except Error as e:
            print(e)
            return []

    def add_record(self, record: tuple) -> bool:
        try:
            sql = ''' INSERT INTO bookings (booking_number, status, date, time, pick_up_address, destination, vehicle_type, distance, cost, driver)
                    VALUES(?,?,?,?,?,?,?,?,?,?) '''
            cur = self.conn.cursor()
            cur.execute(sql, record)
            self.conn.commit()
            self.conn.close()
            return True
        except:
            print("Error adding record")
            self.conn.rollback()
            self.conn.close()
            return False

if __name__ == '__main__':
    db = BookingDB("booking_data.db")

