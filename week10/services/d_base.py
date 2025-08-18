import sqlite3
from config.config import DATABASE

def get_d_base_connection():

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():

    try:

        conn = get_db_connection()
        cursor = conn.cursor()

        # Create the agents table.
        cursor.execute("""
                            CREATE TABLE IF NOT EXISTS client (
                                agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                email TEXT,
                                phone TEXT
                            )
                        """)
        print("[INFO] Agents table created successfully.")
