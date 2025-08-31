
#import _sqlite3
import sqlite3
from dbm.sqlite3 import GET_SIZE

from flask import Flask ,request,jsonify

app=Flask(__name__)

DataStore='construction.db'

def db_connection():
    """
    create and return a connection to the sqlite database
    the row factory setting allows rows to be returned a dictionaries
    """
    conn=sqlite3.connect(DataStore)
    conn.row_factory=sqlite3.Row
    return conn

def init_db():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
            project_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, 
            location TEXT,
            budget REAL
            )
            """
            )

    conn.commit()
    conn.close()

@app.route('/')
def home():
    return jsonify("Key","Argument")


@app.route ('/project',methods=['POST'])
def create_project():
     """create a new project record.
     Exepected JSON payload : {name : "Project Name",location":Location" ,"budget": "Budget"}
     """
     data =request.get_json()
     name = data.get('name')
     location=data.get('location')
     budget=data.get ('budget')

     conn=db_connection()
     cursor=conn.cursor()
     cursor.execute("INSERT INTO project (name,location,budget) VALUES (?,?,?)",(name, location,budget))
     conn.commit()
     conn.close()
     return jsonify({'message': 'hurray you have sucessfully created a record'}),201

if __name__=="__main__":
    init_db()
    app.run(debug=True)

@app.route('/project/<int:project_id>',methods=['DELETE'])
def delete_project(project_id):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM project WHERE project_id=2",(project_id,))
    conn.commit()
    conn.close()
    return ({'message':'project has been deleted'})
app.route('/project/<int:project_id>',methods=['GET'])
def to_get_ne_record():
    conn = db_connection()
    project=cursor. execute("SELECT FROM project WHERE project_id=?",(project_id,)).fetchone()
    conn.close(

def new_db():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute( """CREATE TABLE IF NOT EXISTS materials (
    material_id INTEGER PRIMARY KEY AUTO INCREMENT 
    project_id INTEGER
    material_name TEXT
    quantity INTEGER
    FOREIGN KEY  project_id references project(project_id))""")
    conn.commit()
    conn.close()

@app.route('/materials', methods=['POST'])
def material_details():
    info=request.get_json()
    material_name=info.get_json('material_name')
    quantity=info.get_json('quantity')
    project_id=info.get_json('project_id')
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO materials (material_name,quantity,project_id)values(?,?,?)",(material_name,quantity,project_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "congratulations you have successfully created a materials data base"})
@ app.route('/materials', methods=['GET'])
def material_info():
    conn=db_connection()
    material=conn.execute("SELECT * FROM materials").fetchall()
    material_list=[dict(row)for row in material]








