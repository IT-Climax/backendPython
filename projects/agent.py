import sqlite3
from flask import Flask,request, jsonify

#representing flask with tthe word agent

agent = Flask(__name__)

#representing my database with the word store

store = 'Agent.db'


def connect_db():
    connect = sqlite3.connect(store)
    connect.row_factory = sqlite3.Row
    return connect



def init_db():
    connect= connect_db()
    cursor = connect.cursor()

    
    #the agents table
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS agents(
                   agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT (50),
                   sex TEXT (10),
                   roll TEXT (50),
                   number INT (11)
                   )
                   """)
    
    #the clients table
    cursor.execute("""CREATE TABLE IF NOT EXISTS client(
                   client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT(50),
                   sex TEXT (10),
                   number INT (11),
                   email VARCHAR (30)
                    )
                   """)
    
    # the questions table
    cursor.execute("""CREATE TABLE IF NOT EXISTS question(
                   question_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT(50),
                   sex TEXT (10),
                   number INT (11),
                   questions TEXT NOT NULL
                    )
                    """)
  #the answer table  
    cursor.execute("""CREATE TABLE IF NOT EXISTS answers(
                   answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT(50),
                   sex TEXT (10),
                   number INT (11),
                   answer TEXT (500),
                   email VARCHAR (30)
                    )
                    """)
    #the response table 
    cursor.execute("""CREATE TABLE IF NOT EXISTS responds(
                   respond_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT(50),
                   Sex TEXT (10),
                   Number INT (11),
                   responds TEXT (500)
                    )
                    """)
    
    #the survey table
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS survey(
                   survey_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   description TEXT (500),
                   title VARCHER (225) NOT NULL
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


@agent.route('/agents/<int:agent_id>', methods=['GET'])
def agent_info(agent_id):
    connect = connect_db()
    agents= connect.execute('SELECT * FROM agents WHERE agent_id = ?', (agent_id,)).fetchone()
    connect.close()
    if agent is None:
        return jsonify("Error: Client record does not exist"), 404
    return jsonify(dict(agents))


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


@agent.route('/agents/<int:agent_id>', methods=['DELETE'])
def delete_agent_info(agent_id):

    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM agents WHERE agent_id = ?', (agent_id,))
    connect.commit()
    connect.close()
    
    return jsonify({"message":"successfuly deleted a record"})

@agent.route ('/agents/<int:agent_id>', methods= ['PUT'])
def update_agent_info(agent_id):

    data = request.get_json()
    name = data.get('name')
    sex = data.get('sex')
    roll = data.get('roll')
    number = data.get('number')

    connect = connect_db()
    cursor=connect.cursor()

    cursor.execute("""
        UPDATE agents
        SET name = COALESCE(?, name),
            sex = COALESCE(?, sex),
            roll = COALESCE(?, roll),
            number = COALESCE(?, number)
            WHERE  agent_id = ?
    """, (name, sex, roll, number, agent_id))
    connect.commit()
    connect.close()
    return jsonify({'message': 'Successfully updated Project'})


@agent.route('/client', methods=['GET'])
def get__info():
    connect = connect_db()
    client = connect.execute('SELECT * FROM client').fetchall()
    connect.close()

    client_list = [dict(row) for row in client]
    return jsonify(client_list)


@agent.route('/client/<int:client_id>', methods=['GET'])
def get_client_info(client_id):
    connect = connect_db()
    clients = connect.execute('SELECT * FROM client WHERE client_id = ?', (client_id,)).fetchone()
    connect.close()
    if clients is None:
        return jsonify("Error: Client record does not exist"), 404
    return jsonify(dict(clients))

@agent.route('/client', methods= ['POST'])
def post_client_info():
    data = request.get_json()
    name = data.get('name')
    sex = data.get('sex')
    number = data.get('number')
    email = data.get('email')

    connect=connect_db()
    cursor=connect.cursor()
    cursor.execute('INSERT INTO client (Name, Sex, Number, Email) VALUES (?, ?, ?, ?)',
                   (name,sex,number,email))
    connect.commit()
    connect.close()
    return jsonify('Congratulations: You have sucessfully added a record.')


@agent.route('/client/<int:client_id>', methods=['DELETE'])
def delet_single_record(client_id):
    connect = connect_db()
    cursor=connect.cursor()
    cursor.execute("SELECT * FROM client WHERE Client_id = ?", (client_id,))
    connect.commit()
    connect.close()
    return jsonify({"message":"Deleted successfuly"})
    

@agent.route('/client/<int:client_id>', methods=['PUT'])
def update_client_info(client_id):
    data = request.get_json()
    name = data.get ('name')
    sex = data.get('sex')
    number = data.get('number')
    email = data.get('email')

    connect = connect_db()
    cursor = connect.cursor()

    cursor.execute("""
        UPDATE client
        SET name = COALESCE(?, name),
            sex = COALESCE(?, sex),
            number = COALESCE(?, number),
            email = COALESCE(?, email)
        WHERE Client_id = ?
    """, (name, sex, number, email, client_id))

    connect.commit()
    connect.close()
    return jsonify({'message': 'Successfully updated client'})

@agent.route('/question', methods=['POST'])
def post_question():
    data = request.get_json()
    name = data.get('name')
    sex = data.get('sex')
    number = data.get('number')
    questions = data.get('questions')

    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute('INSERT INTO question (name, sex, number, questions) VALUES (?, ?, ?, ?)',
    (name, sex, number, questions))
    connect.commit()
    connect.close()
    return jsonify('Congratulations: You have successfully added a record.')

# returning the whole information
@agent.route('/question', methods=['GET'])
def get_questions_info():
    connect = connect_db()
    questions = connect.execute('SELECT * FROM question').fetchall()
    connect.close()

    question_list = [dict(row) for row in questions]
    return jsonify(question_list)

# returning a single information
@agent.route('/question/<int:question_id>', methods=['GET'])
def get_question_info(question_id):
    connect = connect_db()
    question = connect.execute('SELECT * FROM question WHERE question_id = ?', (question_id,)).fetchone()
    connect.close()
    if question is None:
        return jsonify("Error: Question record does not exist"), 404
    return jsonify(dict(question))

@agent.route('/question/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    connect = connect_db()
    cursor=connect.cursor()
    cursor.execute('SELECT * FROM question WHERE question_id = ?', (question_id,))
    connect.commit()
    connect.close()
    return jsonify({"message":"successfully deleted a record"})
    

@agent.route('/question/<int:question_id>', methods=['PUT'])
def update_question(question_id):

    data = request.get_json()
    name = data.get('name') 
    sex = data.get('sex')
    number = data.get('number')
    questions = data.get('questions')

    connect = connect_db()
    cursor = connect.cursor()
    
    cursor.execute("""
        UPDATE question
        SET name = COALESCE(?, name),
            sex = COALESCE(?, sex),
            number = COALESCE(?, number),
            questions = COALESCE(?, questions)
        WHERE question_id = ?
        """, (name,sex,number,questions ,question_id))
    connect.commit()
    connect.close()
    return jsonify({'message': 'Successfully updated question'})



@agent.route('/answers', methods=['GET'])
def get_answer_info():
    connect = connect_db()
    answer = connect.execute('SELECT * FROM answers').fetchall()
    connect.close()

    answer_list = [dict(row) for row in answer]
    return jsonify(answer_list)


@agent.route('/answers', methods=['POST'])
def post_answers():
    data = request.get_json()
    name = data.get('name')
    sex = data.get('sex')
    number = data.get('number')
    answer = data.get('answer')
    email = data.get('email')   

    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute('INSERT INTO answers (name, sex, number, answers, email) VALUE(?,?,?,?,?)',
    (name,sex,number,answer,email))
    
    connect.commit
    connect.close
    return jsonify('Congratulations: You have successfully added a record.')


@agent.route('/answers/<int:answer_id>', methods=['GET'])
def get_answers_info(answer_id):
    connect = connect_db()
    answer = connect.execute('SELECT * FROM answers WHERE answer_id = ?', (answer_id,)).fetchone()
    connect.close()

    answer_list = [dict(row) for row in answer]
    return jsonify(answer_list)


@agent.route('/answers/<int:answer_id>', methods=['DELETE'])
def delete_answer(answer_id):
    connect = connect_db()
    cursor=connect.cursor()
    cursor.execute('SELECT * FROM answers WHERE Answer_id = ?', (answer_id,))
    connect.commit()
    connect.close()
    
    return jsonify({"Message":"Successfuly Deleted"})



@agent.route('/answers/<int:answer_id>', methods=['PUT'])
def update_answer(answer_id):
    data = request.get_json()
    name = data.get('name')
    sex = data.get('sex')
    number = data.get('number')
    answer = data.get('answer')
    email = data.get('email')

    connect = connect_db()
    cursor = connect.cursor()

    cursor.execute("""
        UPDATE answers
        SET name = COALESCE(?, name),
            sex = COALESCE(?, sex),
            number = COALESCE(?, number),
            answer = COALESCE(?, answer),
            email = COALESCE(?, email)
        WHERE Answer_id = ?
    """, (name, sex, number, answer, email, answer_id))

    connect.commit()
    connect.close()
    return jsonify({'message': 'Successfully updated answer'})



@agent.route('/responds', methods=['GET'])
def get_responds_info():
    connect = connect_db()
    respond = connect.execute('SELECT * FROM responds').fetchall()
    connect.close()

    respond_list = [dict(row) for row in respond]
    return jsonify(respond_list)


@agent.route('/responds', methods=['POST'])
def post_responds():
    data = request.get_json()
    name = data.get('name')
    sex = data.get('sex')
    number = data.get('number')
    responds = data.get('responds')

    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute('INSERT INTO responds (name, sex, number, responds) VALUES (?, ?, ?, ?)',
                   (name, sex, number, responds))

    connect.commit()
    connect.close()
    return jsonify('Congratulations: You have successfully added a record.')

@agent.route('/responds/<int:respond_id>', methods=['GET'])
def get_respond_info(respond_id):
    connect = connect_db()
    respond = connect.execute('SELECT * FROM responds WHERE Answer_id = ?', (respond_id,)).fetchone()
    connect.close()
    if respond is None:
        return jsonify("Error: Respond record does not exist"), 404
    return jsonify(dict(respond))

@agent.route('/responds/<int:respond_id>', methods=['DELETE'])
def delete_respond(respond_id):
    connect = connect_db()
    cursor=connect.cursor()
    cursor.execute('SELECT * FROM responds WHERE Answer_id = ?', (respond_id,))
    connect.commit()
    connect.close()
   
    return jsonify({"message": "Successfuly deleted"})

@agent.route('/responds/<int:respond_id>', methods=['PUT'])
def update_respond(respond_id):
    data = request.get_json()
    name = data.get('name')
    sex = data.get('sex')
    number = data.get('number')
    responds = data.get('responds')

    connect = connect_db()
    cursor = connect.cursor()

    cursor.execute("""
        UPDATE responds
        SET name = COALESCE(?, name),
            sex = COALESCE(?, sex),
            number = COALESCE(?, number),
            responds = COALESCE(?, responds)
        WHERE Answer_id = ?
    """, (name, sex, number, responds, respond_id))

    connect.commit()
    connect.close()
    return jsonify({'message': 'Successfully updated respond'})



# BEGINING OF SURVEY

@agent.route('/survey', methods=['GET'])
def get_surveys_info():
    connect = connect_db()
    survey = connect.execute('SELECT * FROM survey').fetchall()
    connect.close()

    survey_list = [dict(row) for row in survey]
    return jsonify(survey_list)


@agent.route('/survey', methods=['POST'])
def post_survey():
    data = request.get_json()
    description = data.get('description')
    title = data.get('title')

    connect = connect_db()
    cursor = connect.cursor()
    cursor.execute('INSERT INTO survey (description, title) VALUES (?, ?)',
                   (description, title))

    connect.commit()
    connect.close()
    return jsonify('Congratulations: You have successfully added a record.')

@agent.route('/survey/<int:survey_id>', methods=['GET'])
def get_survey_info(survey_id):
    connect = connect_db()
    survey = connect.execute('SELECT * FROM survey WHERE survey_id = ?', (survey_id,)).fetchone()
    connect.close()
    if survey is None:
        return jsonify({"Error": "Survey record does not exist}"}), 404
    return jsonify(dict(survey))


@agent.route('/survey/<int:survey_id>', methods=['DELETE'])
def delete_survey(survey_id):
    connect = connect_db()
    cursor=connect.cursor()
    cursor.execute('SELECT * FROM survey WHERE survey_id = ?', (survey_id,))
    connect.commit()
    connect.close()
    return jsonify({"message": "Deleted"})

@agent.route('/survey/<int:survey_id>', methods=['PUT'])
def update_survey(survey_id):
    data = request.get_json()
    description = data.get('description')
    title = data.get('title')

    connect = connect_db()
    cursor = connect.cursor()

    cursor.execute("""
        UPDATE survey
        SET description = COALESCE(?, description),
            title = COALESCE(?, title)
        WHERE survey_id = ?
    """, (description, title, survey_id))

    connect.commit()
    connect.close()
    return jsonify({'message': 'Successfully updated survey'})


if __name__ == "__main__":
    init_db()
    agent.run(debug=True)
