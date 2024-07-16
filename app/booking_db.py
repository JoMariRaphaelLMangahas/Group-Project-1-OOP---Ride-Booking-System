import sqlite3
from sqlite3 import Error
from .record_model import Record

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

    def retrieve_records(self) -> list[Record]:
        c = self.conn.cursor()
        try:
            c.execute("SELECT * FROM bookings")
            rows = c.fetchall()
            records = []
            for row in rows:
                record = Record()
                record.from_tuple(row)
                records.append(record)
            return records
        except Error as e:
            print(e)
            return []

    def add_record(self, record: tuple) -> int:
        try:
            sql = ''' INSERT INTO bookings (status, date, time, pick_up_address, destination, vehicle_type, distance, cost, driver)
                    VALUES(?,?,?,?,?,?,?,?,?) '''
            cur = self.conn.cursor()
            cur.execute(sql, record)
            self.conn.commit()
            inserted_id = cur.lastrowid
            return inserted_id
        except:
            print("Error adding record")
            self.conn.rollback()
            return -1
        finally:
            cur.close()

    def update_record(self, record: Record) -> bool:
        try:
            sql = ''' UPDATE bookings
                    SET status = ?,
                        date = ?,
                        time = ?,
                        pick_up_address = ?,
                        destination = ?,
                        vehicle_type = ?,
                        distance = ?,
                        cost = ?,
                        driver = ?
                    WHERE booking_number = ? '''
            cur = self.conn.cursor()
            cur.execute(sql, record.to_tuple())
            self.conn.commit()
            return True
        except:
            print("Error updating record")
            self.conn.rollback()
            return False
        finally:
            cur.close()

    def delete_record(self, booking_number: int) -> bool:
        try:
            sql = ''' DELETE FROM bookings WHERE booking_number = ? '''
            cur = self.conn.cursor()
            cur.execute(sql, (booking_number,))
            self.conn.commit()
            return True
        except:
            print("Error deleting record")
            self.conn.rollback()
            return False
        finally:
            cur.close()

    def close_connection(self):
        self.conn.close()

if __name__ == '__main__':
    db = BookingDB("booking_data.db")

