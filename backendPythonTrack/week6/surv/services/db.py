import sqlite3
from config.config import DATABASE


def db_connection():
    """
    Create and return a connection to the SQLite database.
    The row_factory setting allows query results to be accessed as dictionaries.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Initialize the database by creating tables for the survey system.
    This includes tables for agents, clients, questions, answers, and responses.
    Displays the status of database creation upon application launch.
    """
    try:

        conn = db_connection()
        cursor = conn.cursor()

        # Create the agents table (Enumerators)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS agents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT
            )
        """)
        print("[INFO] Agents table created successfully.")

        # Create the clients table (Respondents - Biodata)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id INTEGER,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT,
                NIN TEXT,
                drive_license TEXT,
                Lga TEXT,
                address TEXT,
                state TEXT,
                education TEXT,
                business TEXT,
                sex TEXT,
                FOREIGN KEY(agent_id) REFERENCES agents(id)
            )
        """)
        print("[INFO] Clients table created successfully.")

        # Create the questions table (Assessments)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        print("[INFO] Questions table created successfully.")

        # Create the answers table (Possible answers for each question)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS answers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_id INTEGER,
                name TEXT,
                FOREIGN KEY(question_id) REFERENCES questions(id)
            )
        """)
        print("[INFO] Answers table created successfully.")

        # Create the responses table (Respondents' answers)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS responses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER,
                question_id INTEGER,
                name TEXT,
                FOREIGN KEY(client_id) REFERENCES clients(id),
                FOREIGN KEY(question_id) REFERENCES questions(id)
            )
        """)
        print("[INFO] Responses table created successfully.")

        conn.commit()
        conn.close()
        print("[SUCCESS] Database initialization completed.")
    except Exception as e:
        print(f"[ERROR] Database initialization failed: {e}")