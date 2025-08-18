import sqlite3
from flask import Flask, request, jsonify

# Instantiate flask project
major = Flask(__name__)

# Defining database storage file with sqlite
DataStore = 'construction.db'


# Defining class that create connection to the created database
def db_connection():
    """
        Create and return a connection to the SQLite database.
        The row_factory setting allows rows to be returned as dictionaries.
    """
    conn = sqlite3.connect(DataStore)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
        Initialize the database by creating the 'projects' and 'materials' tables if they do not already exist.
        """
    conn = db_connection()
    cursor = conn.cursor()

    # Create the projects table.
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Survey (
                agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                email TEXT,
                budget REAL
            )
        """)

    # Create the materials table with a foreign key reference to the projects table.
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


@major.route('/survey', methods=['GET'])
def get_projects():
    """
    Retrieve all projects.
    """
    conn = db_connection()
    projects = conn.execute("SELECT * FROM projects").fetchall()
    conn.close()

    # Convert rows to a list of dictionaries.
    project_list = [dict(row) for row in projects]
    return jsonify(project_list)


@major.route('/projects', methods=['POST'])
def create_project():
    
    # Create a new project record.
    # Expected JSON payload: { "name": "Project Name", "location": "Location", "budget": 123456 }
    
    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    budget = data.get('budget')

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projects (name, location, budget) VALUES (?, ?, ?)",
                   (name, location, budget))
    conn.commit()
    # new_id = cursor.lastrowid
    # , 'project_id': new_id
    conn.close()

    return jsonify({'message': 'Hurray you have successfully create a record'}), 201


@major.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    
    # Retrieve a specific project by its ID.
    
    conn = db_connection()
    project = conn.execute("SELECT * FROM projects WHERE project_id = ?", (project_id,)).fetchone()
    conn.close()

    if project is None:
        return jsonify({'error': 'No record of such project with this ID number'}), 404

    return jsonify(dict(project))


@major.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    
    # Update an existing project.
    # Expected JSON payload: { "name": "New Name", "location": "New Location", "budget": 654321 }
    # Only provided fields will be updated.
    
    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    budget = data.get('budget')

    conn = db_connection()
    cursor = conn.cursor()

    # Use COALESCE to update only fields that are provided.
    cursor.execute("""
        UPDATE projects
        SET name = COALESCE(?, name),
            location = COALESCE(?, location),
            budget = COALESCE(?, budget)
        WHERE project_id = ?
    """, (name, location, budget, project_id))
    conn.commit()
    
    return jsonify({'message': 'Successfully updated Project'})

@major.route('/projects/<int:project_id>', methods=['DELETE'])
def project_delete(project_id):
    
    # Delete a project by its ID.
    
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE project_id = ?", (project_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Successfully deleted a record from Project'})
    







@major.route('/materials', methods=['GET'])
def get_materials():

    conn = db_connection()
    all_materials = conn.execute("SELECT * FROM materials").fetchall()
    conn.close()

    material_list = [dict(row) for row in all_materials]
    return jsonify(material_list)
    

@major.route('/materials', methods=['POST'])
def create_material():
    data = request.get_json()
    material_name = data.get('material_name')
    quantity = data.get('quantity')
    project_id = data.get('project_id')

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO materials (material_name, quantity, project_id) VALUES (?, ?, ?)",
                   (material_name, quantity, project_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'You have successfully create a record'}), 201


@major.route('/materials/<int:material_id>', methods=['GET'])
def get_material(material_id):

    conn = db_connection()
    material = conn.execute("SELECT * from materials WHERE material_id = ?", (material_id)).fetchone()
    conn.commit()
    conn.close()

    if material is None:
        return jsonify({'error': 'No record of material with this ID number'}), 404

    return jsonify(dict(material))


@major.route('/materials/<int:material_id>', methods=['PUT'])
def update_material(material_id):

    data = request.get_json()
    material_name = data.get('material_name')
    quantity = data.get('quantity')

    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE materials
        SET material_name = COALESCE(?, material_name), quantity = COALESCE(?, quantity)
        WHERE material_id = ?
    """, (material_name, quantity, material_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "successfully updated Materials"})



@major.route('/materials/<int:material_id>', methods=['DELETE'])
def delete_material(material_id):
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM materials WHERE material_id = ?", (material_id))

    conn.commit()
    conn.close()

    return jsonify({"message": "Material deleted successfully"})



if __name__ == '__main__':
    init_db()
    major.run(debug=True)