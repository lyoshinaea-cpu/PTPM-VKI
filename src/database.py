
import sqlite3


class Database:
    def __init__(self, db_path="triangles.db"):
        self.connection = sqlite3.connect(db_path)

        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS triangles (
                side_a REAL NOT NULL,
                side_b REAL NOT NULL,
                side_c REAL NOT NULL,
                triangle_type TEXT,
                error_message TEXT,
                PRIMARY KEY (side_a, side_b, side_c)
            )
        """)
        self.connection.commit()

    def add_record(self, a, b, c, triangle_type, error_message):
        with self.connection:
            self.connection.execute("""
                INSERT INTO triangles
                (side_a, side_b, side_c, triangle_type, error_message)
                VALUES (?, ?, ?, ?, ?)
            """, (a, b, c, triangle_type, error_message))

    def get_record(self, a, b, c):
        cursor = self.connection.execute("""
            SELECT triangle_type, error_message
            FROM triangles
            WHERE side_a = ? AND side_b = ? AND side_c = ?
        """, (a, b, c))

        return cursor.fetchone()

    def delete_record(self, a, b, c):
        with self.connection:
            cursor = self.connection.execute("""
                DELETE FROM triangles
                WHERE side_a = ? AND side_b = ? AND side_c = ?
            """, (a, b, c))

        return cursor.rowcount > 0

    def close(self):
        self.connection.close()
