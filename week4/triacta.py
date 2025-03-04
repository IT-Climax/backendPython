import _sqlite3
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
            CREATE TABLE IF NOT EXISTS projects (
                project_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT,
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


@major.route('/projects', methods=['GET'])
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
    """
    Create a new project record.
    Expected JSON payload: { "name": "Project Name", "location": "Location", "budget": 123456 }
    """
    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    budget = data.get('budget')

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projects (name, location, budget) VALUES (?, ?, ?)",
                   (name, location, budget))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    # return the new project id so the frontend will be able to set it in order to create materials
    return jsonify({'message': 'Hurray you have successfully create a record','project_id': new_id}), 201


@major.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    Retrieve a specific project by its ID.
    """
    conn = db_connection()
    project = conn.execute("SELECT * FROM projects WHERE project_id = ?", (project_id,)).fetchone()
    conn.close()

    if project is None:
        return jsonify({'error': 'No record of such project with this ID number'}), 404

    return jsonify(dict(project))


@major.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """
    Update an existing project.
    Expected JSON payload: { "name": "New Name", "location": "New Location", "budget": 654321 }
    Only provided fields will be updated.
    """
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
    conn.close()

    return jsonify({'message': 'Successfully updated Project'})


@major.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    Delete a project by its ID.
    """
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE project_id = ?", (project_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Successfully deleted a record from Project'})


# Material methods

@major.route('/materials', methods=['GET'])
def get_materials():
    """
    Retrieve all projects.
    """
    conn = db_connection()
    materials = conn.execute("SELECT * FROM materials").fetchall()
    conn.close()

    # Convert rows to a list of dictionaries.
    materials_list = [dict(row) for row in materials]
    return jsonify(materials_list)


# Create a new material with associated project Id
@major.route('/materials', methods=['POST'])
def create_material():
    """
    Create a new project record.
    Expected JSON payload: { "name": "Project_id":1, "material_name": "quantity":20}
    """

    data = request.get_json()
    project_id = data.get('projId')
    material_name = data.get('name')
    quantity = data.get('quantity')

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO materials (project_id, material_name, quantity) VALUES (?, ?, ?)",
                   (project_id, material_name, quantity))
    conn.commit()
    # new_id = cursor.lastrowid
    # , 'project_id': new_id
    conn.close()

    return jsonify({'message': 'Hurray you have successfully create a record'}), 201


# get project with associated materials used
@major.route('/project_materials', methods=['GET'])
def get_project_materials():
    """
    Retrieve projects with their associated materials.
    Each project is returned as a JSON object that includes a "materials" field,
    which is a list of all related material records.
    """
    conn = db_connection()
    query = """
        SELECT 
            p.project_id, 
            p.name AS project_name, 
            p.location, 
            p.budget,
            m.material_id, 
            m.material_name, 
            m.quantity
        FROM projects p
        LEFT JOIN materials m ON p.project_id = m.project_id
    """
    results = conn.execute(query).fetchall()
    conn.close()

    # Group results by project_id
    projects_dict = {}
    for row in results:
        project_id = row["project_id"]

        # If project is not already added, add it and initialize an empty materials list
        if project_id not in projects_dict:
            projects_dict[project_id] = {
                "project_id": project_id,
                "project_name": row["project_name"],
                "location": row["location"],
                "budget": row["budget"],
                "materials": []
            }

        # If there's a material in this row, add it to the project's materials list
        if row["material_id"] is not None:
            material = {
                "material_id": row["material_id"],
                "material_name": row["material_name"],
                "quantity": row["quantity"]
            }
            projects_dict[project_id]["materials"].append(material)

    # Convert the projects dictionary into a list for JSON output
    projects_list = list(projects_dict.values())
    return jsonify(projects_list)


# Get single project with associate materials
@major.route('/project_material/<int:project_id>', methods=['GET'])
def get_project_material(project_id):
    """
    Retrieve a specific project by its ID along with its associated materials.
    The response is a JSON object with project details and a "materials" field
    that lists all material records related to that project.
    """
    conn = db_connection()
    query = """
        SELECT 
            p.project_id, 
            p.name AS project_name, 
            p.location, 
            p.budget,
            m.material_id, 
            m.material_name, 
            m.quantity
        FROM projects p
        LEFT JOIN materials m ON p.project_id = m.project_id
        WHERE p.project_id = ?
    """
    results = conn.execute(query, (project_id,)).fetchall()
    conn.close()

    # If no rows are returned, the project doesn't exist.
    if not results:
        return jsonify({'error': 'Project not found'}), 404

    # Build the project data with materials as a sub-list.
    project_data = {
        "project_id": results[0]["project_id"],
        "project_name": results[0]["project_name"],
        "location": results[0]["location"],
        "budget": results[0]["budget"],
        "materials": []
    }

    # Loop through results and add material records if they exist.
    for row in results:
        if row["material_id"] is not None:
            material = {
                "material_id": row["material_id"],
                "material_name": row["material_name"],
                "quantity": row["quantity"]
            }
            project_data["materials"].append(material)

    return jsonify(project_data)


if __name__ == '__main__':
    init_db()
    major.run(debug=True)
