import sqlite3 
from flask import Flask, app, request, jsonify

program = Flask(__name__)

dataStore="conncetion"
def conncetion_of_db():
    conn = sqlite3.connect(dataStore)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = conncetion_of_db()
    cursor = conn.cursor()

    cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS projects(
                   project_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   location TEXT,
                   budget REAL)"""
                  )
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS materials(
                   material_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   project_id INTEGER,
                   material_name TEXT,
                   quantity INTEGER,
                   FOREIGN KEY (project_id) REFERENCES project (project_id)
                   ) 
                   """)


    return jsonify("kkey", "value")

@program.route('/')
def home():
     return jsonify("key", "value")

@program.route('/project', methods=['POST'])
def create_project():

    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    budget = data.get('budget')

    conn = conncetion_of_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO project(name, location, budget) VALUES (?,?,?)"
                   (name, location, budget))
    conn.commit()

    conn.close()

    return jsonify({'message': 'Hurray you have successfully create a record'}),



if __name__ == '__main__':
    init_db()
    app.app()
    program.run(debug=True)