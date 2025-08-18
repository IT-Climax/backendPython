# """
# Survey System
# agent - Enumerators (id, name, phone, email)
# client - Respondents (id, agent_id, name, phone, email, NIN, Drive license, Lga, address, state, education, business, sex) - Biodata
# question - assessments (id, name)
# answers - (id, question_id, name)
# responses - (id, client_id, question_id, name)
# input field
# options (yes/no/female/male)
# selection

# sex (famale and male)
# how are your  am fine thank
# side join of the database
# id              name
# 1               what is the name of your country?
# 2               what is your gender?
# 3               Please tell me about your self
# 4               are available for meeting tomorrow by 4pm?

# leave it open for frontend
# option2 configure your country

# Answers
# id              question_id         name
# 1               1                   Nigeria
# 2               1                   Cameroon
# 3               1                   Gambia
# 4               1                   Niger
# 5               2                   Female
# 6               2                   Male
# 7               4                   Yes
# 8               4                   No


# Grade (id name)
# """

import sqlite3
from flask import Flask, request,jsonify
app = Flask(__name__)

store= "document.db"

def connect_db():
    connect=sqlite3.connect(store)
    connect.row_factory=sqlite3.Row
    return connect

def init_db():
    connect=connect_db()
    cursor=connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS agents(
    agent_id INTEGER,
    agent_name TEXT,
    phone INT,
    email VARCHAR)
    """)
    
    
    
    connect.commit()
    connect.close()



    
if __name__=='__main__':
    init_db()
    app.run(debug=True)