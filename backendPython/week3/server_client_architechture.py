"""
Hi Class Am Olatunbosun Adeniyi Facilitating this class for this week
Topic: Client-Server Architecture
In client-server architecture, an application is divided into two main parts:
Client: The front end—the user interface (like a web browser or mobile app) that sends requests (HTTP requests) to the server.
Server:The back end—the part that processes incoming requests, interacts with databases, runs business logic, and sends back responses (like HTML pages or JSON data).

Considering the two main popular frameworks for web application development using python, Django and Flask
The server receives a request from a client, processes it (often by querying a database, processing data, and rendering a view), and then returns a response.
"""

from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


def init_db():
    """
    Initialize the SQLite database.
    This function creates a 'projects' table if it does not exist.
    """
    conn = sqlite3.connect("construction.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT,
            budget REAL
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/projects', methods=['GET'])
def get_projects():
    """
    Endpoint to fetch all construction projects.
    It reads from the SQLite database and returns the projects as JSON.
    """
    conn = sqlite3.connect("construction.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    rows = cursor.fetchall()
    conn.close()

    # Convert database rows to a list of dictionaries
    projects = [
        {"id": row[0], "name": row[1], "location": row[2], "budget": row[3]}
        for row in rows
    ]
    return jsonify(projects)


@app.route('/projects', methods=['POST'])
def add_project():
    """
    Endpoint to add a new construction project.
    It reads JSON data from the request, inserts it into the database,
    and returns a confirmation message.
    """
    new_project = request.get_json()
    name = new_project.get("name")
    location = new_project.get("location")
    budget = new_project.get("budget")

    conn = sqlite3.connect("construction.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO projects (name, location, budget) VALUES (?, ?, ?)",
        (name, location, budget)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Project added successfully!"}), 201


if __name__ == '__main__':
    init_db()  # Set up the database when the app starts
    app.run(debug=True)
