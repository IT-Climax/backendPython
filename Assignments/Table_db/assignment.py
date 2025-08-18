import sqlite3
from flask import Flask, request, jsonify

major = Flask(__name__)
DataStore = 'construction.db'


def db_connection():
    """Create and return a connection to the SQLite database."""
    conn = sqlite3.connect(DataStore)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")  # Enforce foreign keys
    return conn


def init_db():
    conn = db_connection()
    cursor = conn.cursor()

    # AGENTS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS AGENTS (
            agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT,
            phone_no TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # CLIENTS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CLIENTS (
            client_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            email TEXT,
            phone_num TEXT
        )
    """)

    # QUESTIONS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS QUESTIONS (
            question_id INTEGER PRIMARY KEY AUTOINCREMENT,
            agent_id INTEGER NOT NULL,
            email TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(agent_id) REFERENCES AGENTS(agent_id)
        )
    """)

    # ANSWERS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ANSWERS (
            answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER,
            answer TEXT,
            FOREIGN KEY(question_id) REFERENCES QUESTIONS(question_id)
        )
    """)

    # RESPONSES
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS RESPONSES (
            response_id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER,
            question_id INTEGER,
            response_data DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(client_id) REFERENCES CLIENTS(client_id),
            FOREIGN KEY(question_id) REFERENCES QUESTIONS(question_id)
        )
    """)

    conn.commit()
    conn.close()


# --------------------
# CRUD for AGENTS
# --------------------
@major.route("/agents", methods=["GET", "POST"])
def agents():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        data = request.get_json()
        full_name = data.get("full_name")
        email = data.get("email")
        phone_no = data.get("phone_no")

        cursor.execute(
            "INSERT INTO AGENTS (full_name, email, phone_no) VALUES (?, ?, ?)",
            (full_name, email, phone_no)
        )
        conn.commit()
        return jsonify({"message": "Agent added successfully"}), 201

    elif request.method == "GET":
        cursor.execute("SELECT * FROM AGENTS")
        agents = [dict(row) for row in cursor.fetchall()]
        return jsonify(agents)


@major.route("/agents/<int:agent_id>", methods=["GET", "PUT", "DELETE"])
def agent_detail(agent_id):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM AGENTS WHERE agent_id=?", (agent_id,))
        row = cursor.fetchone()
        if row:
            return jsonify(dict(row))
        return jsonify({"error": "Agent not found"}), 404

    elif request.method == "PUT":
        data = request.get_json()
        cursor.execute("""
            UPDATE AGENTS SET full_name=?, email=?, phone_no=? WHERE agent_id=?
        """, (data.get("full_name"), data.get("email"), data.get("phone_no"), agent_id))
        conn.commit()
        return jsonify({"message": "Agent updated successfully"})

    elif request.method == "DELETE":
        cursor.execute("DELETE FROM AGENTS WHERE agent_id=?", (agent_id,))
        conn.commit()
        return jsonify({"message": "Agent deleted successfully"})





if __name__ == '__main__':
    init_db()
    major.run(debug=True)
