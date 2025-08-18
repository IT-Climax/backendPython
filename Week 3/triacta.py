
import sqlite3
from flask import Flask, request, jsonify

major = Flask(__name__)

DataStore = 'construction.db'



def db_connection():
    conn = sqlite3.connect(DataStore)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():

    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute ("""CREATE TABLE IF NOT EXISTS projects 
    (project_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, location TEXT, budget REAL
        )
    """)

    cursor.execute("""
     CREATE TABLE IF NOT EXISTS materials (
            material_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            material_name TEXT,
            quantity INTEGER,
            FOREIGN KEY(project_id) REFERENCES projects(project_id)
            )
    """)

    conn.commit()
    conn.close()

@major.route('/')
def home():
    return jsonify("key", "values")


@major.route('/projects', methods=['GET'])
def get_projects():
    conn = db_connection()
    projects = conn.execute("SELECT *FROM projects").fetchall()
    conn.close()

    project_list = [dict(row) for row in projects]
    return jsonify(project_list)

@major.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    budget = data.get('budget')

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projects (name, location, budget) VALUES (?, ?, ?)",
    (name, location, budget))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Hurray you have successfully created a record'}), 201

@major.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    conn = db_connection()
    project = conn.execute("SELECT *FROM projects WHERE project_id = ?", (project_id,)).fetchone()
    conn.close()

    if project is None:
        return jsonify({'error': 'No record of such project with this ID number'}), 404

    return jsonify(dict(project))


@major.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    budget = data.get('budget')

    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("""UPDATE projects SET name = COALESCE(?, name), location = COALESCE(?, location),
    budget = COALESCE(?, budget) WHERE project_id = ?""", (name, location, budget, project_id))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Successfully updated Project'})

@major.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM projects WHERE project_id = ?",(project_id,))
    conn.commit()
    conn.close()

    return jsonify({'Message': 'Successfully deleted a record from the project'})

if __name__== '__main__':
    init_db()
    major.run(debug=True)
