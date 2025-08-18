import sqlite3
from flask import Flask,request, jsonify

agent = Flask(__name__)

store = 'Agent.db'


def connect_db():
    connect = sqlite3.connect(store)
    connect.row_factory =sqlite3.Row
    return connect

def init_db():
    connect= connect_db()
    cursor = connect.cursor()


    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS agents(
                   agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT (50),
                   sex TEXT (10),
                   roll TEXT (50),
                   number INT (11)
                   )
                   """)
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS client(
                   Client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Name TEXT(50),
                   Sex TEXT (10),
                   Number INT (11),
                   Email VARCHAR (30)
                    )
                   """)
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS question(
                   Question_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Name TEXT(50),
                   Sex TEXT (10),
                   Number INT (11),
                   Questions TEXT (500)
                    )
                    """)
    
    connect.commit()
    connect.close()

@agent.route('/')
def home():
    return jsonify({"key": "Value"})

@agent.route('/agents', methods=['GET'])
def get_agent_info():
    connect = connect_db()
    agents = connect.execute('SELECT * FROM agents').fetchall()
    connect.close()

    agent_list = [dict(row) for row in agents]
    return jsonify(agent_list)

@agent.route('/agents', methods=['POST'])
def create_agents():
   
    data = request.get_json()
    name = data.get('name')
    sex = data.get('sex')
    roll = data.get('roll')
    number = data.get('number')

    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO agents (name, sex, roll, number) VALUES (?, ?, ?, ? )",
                   (name, sex, roll, number))
    
    connect.commit()
    connect.close()
    return jsonify({'message': 'Hurray you have successfully create a record'}), 201


if __name__ == "__main__":
    init_db()
    agent.run(debug=True)