import sqlite3
from flask import Flask,request, jsonify

app = Flask(__name__)

storage = 'document.db'

def connect_db():
    connect=sqlite3.conn(storage)
    connect.row_factory = sqlite3.Row
    return jsonify(connect)

def init_db():
    connect=connect_db()
    cursor=connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXIST client(
                   client_id AUTO INCREMENT PRIMARY KEY,
                   name TEXT,
                   email  (20) VARCHAR,
                   number INT
                   )
                   """)
    connect.commit()
    connect.close()

@app.route('/')
def home():
    return jsonify({"key" : "value"})

@app.route('/agent', methods=['POST'])
def create_agent():
    data=request.get_json()
    name=data.get('name')
    email = data.get('email')
    number = data.get('number')
    
    connect=connect_db()
    cursor=connect.cursor()
    cursor.execute('INSERT INTO agent(name,email,number) VALUES(?,?,?)',
                   (name,email,number))
    connect.commit()
    connect.close()

    return jsonify({"message":"Agent created successfully"})

if __name__ == ('__main__'):
    init_db
    app.run(debug=True)