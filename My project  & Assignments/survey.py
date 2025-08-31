"""
survey
{agent info-(agent_id
             agent_name
             agent_phone_no
             agent_email
              )}

{client info -(client_id
               client_name
               client_phone_no
               client_email
               )}
{questions-(question_id
            survey_id
            question
            )}
{answers-(answer_id
          question_id
          client_id
          answer
         )}
 {survey (survey_id
          survey_name
          agent info
          client_info
          questions
          answers)}
          """
import _sqlite3
import sqlite3
from flask import Flask,jsonify,request
main=Flask(__name__)
survey_record='survey.db'
#creating a connection
def db_connection():
    con = sqlite3.connect(survey_record)
    con.row_factory = sqlite3.Row
    return con
def init_survey():
      con=db_connection()
    cursor=con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS agent
                     ( agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      agent_name TEXT,
                      agent_phone_no INTEGER,
                      agent_email TEXT,)
                       """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS client,
                      (client_id INTEGER AUTOINCREMENT PRIMARY KEY,
                      client_name TEXT,
                      client_phone_number INTEGER,
                      client_email TEXT,)
                      """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS question,
                     (question_id INTEGER PRIMARY KEY AUTO INCREMENT,
                     question TEXT)         
                      """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS answer
                   (answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   question_id,
                   client_id,
                   survey_name,
                   question,
                   answer,
                   FOREIGN KEY (survey_name) REFERENCES survey(survey_name),
                    FOREIGN KEY (question) REFERENCES question (question_id))""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS response
                   (response_id INTEGER AUTOINCREMENT PRIMARY KEY,
                   client_id INTEGER, 
                   question_id INTEGER,
                   answer_id INTEGER,
                   response TEXT ,
                   FOREIGN KEY (client_id) REFERENCES client_info(client_id),
                   FOREIGN KEY (question_id) REFERENCES question(question_id),
                   FOREIGN KEY (answer_id) REFERENCES answer(answer_id))
  
                     
                    """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS survey
                          (survey_id INTEGER AUTOINCREMENT PRIMARY KEY,
                          agent_id INTEGER,
                          client_id INTEGER,
                          questions_id INTEGER,
                          answer_id INTEGER,
                          response_id INTEGER,
                          FOREIGN KEY (agent_id) REFERENCES agent(agent_id),
                          FOREIGN KEY (client_id) REFERENCES client(client_id),
                          FOREIGN KEY (questions_id) REFERENCES questions(questions_id),
                          FOREIGN KEY (answer_id) REFERENCES answer(answer_id)
                          FOREIGN KEY (response_id_ REFERENCES response(response_id))
                          """)

    con.commit()
    con.close()
if __name__=="__main__":

    main.run(debug=True)
@main.route ("/")
def home():
    return jsonify("key","arguement")
@main.route("/agent",method=['POST'])
def survey_input():
    input=request.get_json()
    agent_name=input.get('agent_name')
    agent_phone_no=input.get('agent_phone_no')
    agent_email=input.get('agent_email')
    con=db_connection()
    cursor=con.cursor()
    cursor.execute("INSERT INTO project (agent_name,agent_phone_no,agent_email) VALUES(?,?,?)",(agent_name,agent_phone_no,agent_email))
    con.commit()
    con.close()
    return jsonify({'message':'congratulations you have successfully created a table for agent information'})

     n