import sqlite3
from config.configure import DATABASE

def get_connection():
    connect = sqlite3.connect(DATABASE)
    connect.row_factory = sqlite3.Row
    return connect

def init_db():
    try:
        connect = get_connection()
        cursor = connect.cursor()
        
        # Create clients table
        cursor.execute("""CREATE TABLE IF NOT EXISTS clients(
                       client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       age INTEGER,
                       gender TEXT,
                       marital_status TEXT,
                       location TEXT,
                       education TEXT,
                       highest_level_education TEXT
                    )""")
        print("[INFO] clients table created successfully")

        # Create questions_edu table
        cursor.execute("""CREATE TABLE IF NOT EXISTS questions_edu(
                        question_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        questions TEXT,
                        client_id INTEGER,
                        FOREIGN KEY (client_id) REFERENCES clients (client_id)
                    )""")
        print("[INFO] questions table created successfully")

        # Create question_empower table
        cursor.execute("""CREATE TABLE IF NOT EXISTS question_empower (
                       question_empo_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       questions TEXT,
                       client_id INTEGER,
                       FOREIGN KEY (client_id) REFERENCES clients (client_id)
                    )""")
        print("[INFO] empower table created successfully")

        # Create assistive_technology table
        cursor.execute("""CREATE TABLE IF NOT EXISTS assistive_technology (
                       question_tech_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       questions TEXT,
                       client_id INTEGER, 
                       FOREIGN KEY (client_id) REFERENCES clients (client_id)
                    )""")
        print("[INFO] Assistive table created successfully")

        # Create awareness table
        cursor.execute("""CREATE TABLE IF NOT EXISTS awareness(
                       awareness_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       awareness TEXT
                    )""")
        print("[INFO] awareness table created successfully")

        # Create digital_inclusion table
        cursor.execute("""CREATE TABLE IF NOT EXISTS digital_inclusion(
                       digital_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       inclusion_questions TEXT
                    )""")
        print("[INFO] digital table created successfully")

        # Create supports table
        cursor.execute("""CREATE TABLE IF NOT EXISTS supports(
                       support_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       support_questions TEXT
                    )""")
        print("[INFO] support table created successfully")

        # Create financial_inclusion table
        cursor.execute("""CREATE TABLE IF NOT EXISTS financial_inclusion(
                       financial_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       financial_questions TEXT
                    )""")
        print("[INFO] financial table created successfully")

        # Create mentorship table
        cursor.execute("""CREATE TABLE IF NOT EXISTS mentorship(
                       mentors_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       client_id INTEGER,
                       question_id INTEGER,
                       question_empo_id INTEGER,
                       question_tech_id INTEGER,
                       support_id INTEGER,
                       digital_id INTEGER,
                       financial_id INTEGER,
                       FOREIGN KEY (client_id) REFERENCES clients (client_id),
                       FOREIGN KEY (question_id) REFERENCES questions_edu (question_id),
                       FOREIGN KEY (question_empo_id) REFERENCES question_empower (question_empo_id),
                       FOREIGN KEY (question_tech_id) REFERENCES assistive_technology (question_tech_id),
                       FOREIGN KEY (support_id) REFERENCES supports (support_id),
                       FOREIGN KEY (digital_id) REFERENCES digital_inclusion (digital_id),
                       FOREIGN KEY (financial_id) REFERENCES financial_inclusion (financial_id)
                    )""")
        print("[INFO] Mentors table created successfully")

        # Commit changes
        connect.commit()
        connect.close()

        print("[INFO] Database Initialization completed successfully")

    except Exception as e:
        print(f"[ERROR] Database Initialization failed: {e}")
