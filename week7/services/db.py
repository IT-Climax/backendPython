import sqlite3
from config.configure import DATABASE

def get_db_connection():
    connect=sqlite3.connect(DATABASE)
    connect.row_factory =sqlite3.Row
    return connect

def init_db():
    try:
        connect= get_db_connection()
        cursor = connect.cursor()
        #the agents table
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS agents(
                    agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT (50),
                    sex TEXT (10),
                    roll TEXT (50),
                    number INT (11),
                    email VARCHAR (30)
                    )
                    """)
        print("[INFO] Agents table created successfully")
    
        #the clients table
        cursor.execute("""CREATE TABLE IF NOT EXISTS clients(
                    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT(50),
                    sex TEXT (10),
                    number INT (11),
                    email VARCHAR (30),
                    state TEXT (20),
                    country TEXT (20)
                    )
                    """)
        print("[INFO] Clients table created successfully")
        
        # the questions table
        cursor.execute("""CREATE TABLE IF NOT EXISTS questions(
                    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT(50),
                    questions TEXT (225)
                    )
                    """)
        print("[INFO] Questions table created successfully")

     #the answer table  
        cursor.execute("""CREATE TABLE IF NOT EXISTS answers(
                    answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT(50),
                    question_id,
                    client_id,
                    FOREIGN KEY (question_id) REFERENCES quextions (question_id),
                    FOREIGN KEY (client_id) REFERENCES clients (client_id)
                    )
                    """)
        print("[INFO] Answers table created successfully)")

        #the response table 
        cursor.execute("""CREATE TABLE IF NOT EXISTS responds(
                    respond_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT(50),
                    question_id,
                    client_id,
                    FOREIGN KEY (question_id) REFERENCES quextions (question_id),
                    FOREIGN KEY (client_id) REFERENCES clients (client_id)
                    )
                    """)
        print("[INFO] Responds table created successfully")
        
        #the survey table
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS survey(
                    survey_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT (500),
                    name VARCHER (225) NOT NULL,
                    agent_id,
                    FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
                    )
                    """)
        print("[INFO] Survey table created successfully")
        
        connect.commit()
        connect.close()

        print("[INFO] Database Initialization completed successfully")

    except Exception as e:
        print(f"[ERROR] Database Initialization failed: {e}")
