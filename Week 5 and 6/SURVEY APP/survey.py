
import sqlite3
from flask import Flask, request, jsonify

# Instantiate flask project
major = Flask(__name__)

# Defining database storage file with sqlite
DataStore = 'survey_db.db'

# Defining class that create connection to the created database
def db_connections():
    """
        Create and return a connection to the SQLite database.
        The row_factory setting allows rows to be returned as dictionaries.
    """
    conn = sqlite3.connect(DataStore)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
            Initialize the database by creating the 'agents', 'clients', 'questions',
            'answers', and 'responses' tables if they do not already exist.
            """
    conn = db_connections()
    cursor = conn.cursor()

    # Create the agents table.
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS agents (
                    agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    email TEXT,
                    phone_number INTEGER,
                    NIN INTEGER,
                    LGA TEXT,
                    State TEXT
                )
            """)

    # Create the clients table with a foreign key reference to the agents table.
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    agent_id INTEGER,
                    full_name TEXT,
                    email TEXT,
                    phone_number INTEGER,
                    NIN INTEGER,
                    LGA TEXT,
                    State TEXT,
                    
                    FOREIGN KEY(agent_id) REFERENCES agents(agent_id)
                )
            """)

    # Create the questions table with a foreign key reference to the agents table.
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS question (
                        question_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        agent_id INTEGER
                    )
                """)

    # Create the answers table with a foreign key reference to the questions table.
    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS answers (
                            answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            question_id INTEGER
                            
                        )
                    """)

    # Create the responses table with foreign keys reference to the clients table and questions table .
    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS response (
                            response_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            client_id INTEGER,
                            question_id INTEGER,
                            response_date TEXT,
                            FOREIGN KEY(client_id) REFERENCES clients(client_id),
                            FOREIGN KEY(question_id) REFERENCES questions(question_id)
                        )
                    """)

    conn.commit()
    conn.close()

@major.route('/agents', methods=['GET'])
def get_agents():
    """
        To retrieve all agents.
    """
    conn = db_connections()
    agents = conn.execute("SELECT * FROM agents").fetchall()
    conn.close()

     # To convert rows to a list of dictionaries.

    agents_list = [dict(row) for row in agents]
    return jsonify(agents_list)

@major.route('/agents', methods=['POST'])
def create_agents():
    """
    Create a new agents record.
    Expected JSON payload: { "name": "full_name", "email": "email", "phone_number": 123456, "nin": 12334545, "LGA": "LGA", "STATE": "STATE" }
    """
    data = request.get_json()
    name = data.get('full_name')
    email = data.get('email')
    phone_number = data.get('phone_number')
    nin = data.get('nin')
    lga = data.get('lga')
    state = data.get('state')

    conn = db_connections()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO agents (name, email, phone_number, nin, lga, state) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, email, phone_number, nin, lga, state))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    # return the new agent id so the frontend will be able to set it in order to create clients
    return jsonify({'message': 'Hurray you have successfully create a record','agent_id': new_id}), 201

@major.route('/agents/<int:agent_id>', methods=['GET'])
def get_agent(agent_id):
    """
    Retrieve a specific agents by its ID.
    """
    conn = db_connections()
    agents = conn.execute("SELECT * FROM agents WHERE agent_id = ?", (agent_id,)).fetchone()
    conn.close()

    if agents is None:
        return jsonify({'error': 'No record of such agent with this ID number'}), 404

    return jsonify(dict(agents))

@major.route('/agents/<int:agent_id>', methods=['PUT'])
def update_agents(agent_id):
    """
    Update an existing agents.
    Expected JSON payload: { "name": "full_name", "email": "email", "phone_number": 123456, "nin": 12334545, "LGA": "LGA", "STATE": "STATE" }
    """
    data = request.get_json()
    name = data.get('full_name')
    email = data.get('email')
    phone_number = data.get('phone_number')
    nin = data.get('nin')
    lga = data.get('lga')
    state = data.get('state')

    conn = db_connections()
    cursor = conn.cursor()
    # Use COALESCE to update only fields that are provided.
    cursor.execute("""
        UPDATE agents
        SET name = COALESCE(?, full_name),
            email = COALESCE(?, email),
            phone_number = COALESCE(?, phone_number),
            nin = COALESCE(?, nin),
            lga = COALESCE(?, lga),
            state = COALESCE(?, state)
        WHERE agent_id = ?
    """, (name, email, phone_number, nin, lga, state, agent_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Successfully updated agent'})

@major.route('/agents/<int:agent_id>', methods=['DELETE'])
def delete_agents(agent_id):
    """
    Delete an agent by its ID.
    """
    conn = db_connections()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM agents WHERE agent_id = ?", (agent_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Successfully deleted a record from agents'})

if __name__== '__main__':
    init_db()
    major.run(debug=True)