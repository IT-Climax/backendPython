import sqlite3
from flask import Flask,request,jsonify

app = Flask(__name__)

connect_db = "construction.db"
def connection_of_database():
    connect = sqlite3.connect(connect_db)
    connect.row_factory = sqlite3.Row
    return connect

def initialization_of_db():
    connect = connection_of_database()
    cursor = connect.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXIST agents(
                   agent_id INTEGER,
                   name VARCHER,
                   phone INTEGER,
                   email TEXT)

""")
    cursor.execute("""
                    CREATE A TABLE IF NOT EXIST clinet(
                   client_id INTEGER,
                   agent_id INTEGER,
                   phone INTEGER,
                   name TEXT,
                   email TEXT,
                   NIN INTEGER,
                   driver_licens INTEGER,
                   LGA TEXT,
                   address TEXT,
                   state TEXT, 
                   educational_qualification  TEXT, 
                   business TEXT,
                   sex TEXT,
                

                   )
""")
    
    cursor.execute(""" CREATE TABLE IF NOT EXIST questions (
                   question_id INTEGER,
                   name TEXT
                   )
""")
    cursor.execute("""CREATE A TABLE IF NOT EXITS anwers(
                   answer_id TEXT,
                   question_id INTEGER,
                   name TEXT
                )   
""")
    cursor.execute("""
                    CREATE A TABLE IF NOT EXIST responses
                   (response_id INTEGER,
                    client_id INTEGER,
                    question_id INTERGER, 
                   name TEXT)
                   """)
    
    connect.commit()
    connect.close()