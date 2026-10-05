import sqlite3

DATABASE_NAME = "ahenk.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS coffee_products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            country TEXT NOT NULL,
            description TEXT,
            price REAL
        )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_tables()
    print("Ahenk veritabanı hazır!")