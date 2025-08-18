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
    CREATE TABLE IF NOT EXISTS AGENTS(
    agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(25),
    email VARCHAR UNIQUE,
    phone INTEGER(11) UNIQUE )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CLIENTS(
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(150),
    email VARCHAR UNIQUE,
    phone VARCHAR UNIQUE)
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS QUESTIONS(
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    survey_id INTEGER,
    question_text TEXT NOT NULL
        )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ANSWERS(
    answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    response_id INTEGER,
    FOREIGN KEY (response_id) REFERENCES responses(response_id)
                   )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS RESPONSES(
    response_id INTEGER PRIMARY KEY AUTOINCREMENT,
    survey_id INTEGER,
    client_id INTEGER,
    question_id INTEGER,
    answer_text TEXT NOT NULL,
    FOREIGN KEY (survey_id) REFERENCES surveys(survey_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id), 
    FOREIGN KEY (question_id) REFERENCES questions(question_id)
                   )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SURVEY(
    survey_id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id INTEGER,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id) )
    """)


    connect.commit()
    connect.close()

@app.route("/")
def home_page():
    return jsonify({"keys":"values"})

# AGENTS CRUD

@app.route('/agents', methods=['GET'])
def get_agents():
    """
    Retrieve all agents.
    """
    connect = connection_of_database()
    agents = connect.execute("SELECT * FROM AGENTS").fetchall()
    connect.close()

    # Convert rows to a list of dictionaries.
    agent_list = [dict(row) for row in agents]
    return jsonify(agent_list)


@app.route('/agents', methods=['POST'])
def create_agent():
    """
    Create a new agent record.
    Expected JSON payload: { "name": "Agent Name", "email": "agent@example.com", "phone": 1234567890 }
    """
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    connect = connection_of_database()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO AGENTS (name, email, phone) VALUES (?, ?, ?)",
                   (name, email, phone))
    connect.commit()
    new_id = cursor.lastrowid
    connect.close()

    return jsonify({'message': 'Successfully created an agent record', 'agent_id':new_id}), 201


@app.route('/agents/<int:agent_id>', methods=['GET'])
def getting_of_agent(agent_id):
    """
    Retrieve a specific agent by its ID.
    """
    connect = connection_of_database()
    agent = connect.execute("SELECT * FROM AGENTS WHERE agent_id = ?", (agent_id,)).fetchone()
    connect.close()

    if agent is None:
        return jsonify({'error': 'No record of such agent with this ID number'}), 404

    return jsonify(dict(agent))


@app.route('/agents/<int:agent_id>', methods=['PUT'])
def update_agent(agent_id):
    """
    Update an existing agent.
    Expected JSON payload: { "name": "New Name", "email": "new@example.com", "phone": 9876543210 }
    Only provided fields will be updated.
    """
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    connect = connection_of_database()
    cursor = connect.cursor()
    # Use COALESCE to update only fields that are provided.
    cursor.execute("""
        UPDATE AGENTS
        SET name = COALESCE(?, name),
            email = COALESCE(?, email),
            phone = COALESCE(?, phone)
        WHERE agent_id = ?
    """, (name, email, phone, agent_id))
    connect.commit()
    connect.close()

    return jsonify({'message': 'Successfully updated agent'})


@app.route('/agents/<int:agent_id>', methods=['DELETE'])
def delete_agent(agent_id):
    """
    Delete an agent by its ID.
    """
    connect = connection_of_database()
    cursor = connect.cursor()
    cursor.execute("DELETE FROM AGENTS WHERE agent_id = ?", (agent_id,))
    connect.commit()
    connect.close()

    return jsonify({'message': 'Successfully deleted an agent record'})

# CLIENTS CRUD

@app.route('/clients', methods=['GET'])
def get_clients():
    """
    Retrieve all clients.
    """
    connect = connection_of_database()
    clients = connect.execute("SELECT * FROM CLIENTS").fetchall()
    connect.close()

    # Convert rows to a list of dictionaries.
    client_list = [dict(row) for row in clients]
    return jsonify(client_list)


@app.route('/clients', methods=['POST'])
def create_client():
    """
    Create a new client record.
    Expected JSON payload: { "name": "Client Name", "email": "client@example.com", "phone": "1234567890" }
    """
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    connect = connection_of_database()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO CLIENTS (name, email, phone) VALUES (?, ?, ?)",
                   (name, email, phone))
    connect.commit()
    new_id = cursor.lastrowid
    connect.close()

    return jsonify({'message': 'Successfully created a client record', 'client_id': new_id}), 201


@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    """
    Retrieve a specific client by its ID.
    """
    connect = connection_of_database()
    client = connect.execute("SELECT * FROM CLIENTS WHERE client_id = ?", (client_id,)).fetchone()
    connect.close()

    if client is None:
        return jsonify({'error': 'No record of such client with this ID number'}), 404

    return jsonify(dict(client))


@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    """
    Update an existing client.
    Expected JSON payload: { "name": "New Name", "email": "new@example.com", "phone": "9876543210" }
    Only provided fields will be updated.
    """
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    connect = connection_of_database()
    cursor = connect.cursor()
    # Use COALESCE to update only fields that are provided.
    cursor.execute("""
        UPDATE CLIENTS
        SET name = COALESCE(?, name),
            email = COALESCE(?, email),
            phone = COALESCE(?, phone)
        WHERE client_id = ?
    """, (name, email, phone, client_id))
    connect.commit()
    connect.close()

    return jsonify({'message': 'Successfully updated client'})


@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    """
    Delete a client by its ID.
    """
    connect = connection_of_database()
    cursor = connect.cursor()
    cursor.execute("DELETE FROM CLIENTS WHERE client_id = ?", (client_id,))
    connect.commit()
    connect.close()

    return jsonify({'message': 'Successfully deleted a client record'})

# QUESTIONS CRUD

@app.route('/questions', methods=['GET'])
def get_questions():
    """
    Retrieve all questions.
    """
    connect = connection_of_database()
    questions = connect.execute("SELECT * FROM QUESTIONS").fetchall()
    connect.close()

    # Convert rows to a list of dictionaries.
    question_list = [dict(row) for row in questions]
    return jsonify(question_list)


@app.route('/questions', methods=['POST'])
def create_question():
    """
    Create a new question record.
    Expected JSON payload: { "survey_id": 1, "question_text": "What is your favorite color?", "question_type": "text" }
    """
    data = request.get_json()
    survey_id = data.get('survey_id')
    question_text = data.get('question_text')
    question_type = data.get('question_type')

    connect = connection_of_database()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO QUESTIONS (survey_id, question_text, question_type) VALUES (?, ?, ?)",
                   (survey_id, question_text, question_type))
    connect.commit()
    new_id = cursor.lastrowid
    connect.close()

    return jsonify({'message': 'Successfully created a question record', 'question_id': new_id}), 201


@app.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    """
    Retrieve a specific question by its ID.
    """
    connect = connection_of_database()
    question = connect.execute("SELECT * FROM QUESTIONS WHERE question_id = ?", (question_id,)).fetchone()
    connect.close()

    if question is None:
        return jsonify({'error': 'No record of such question with this ID number'}), 404

    return jsonify(dict(question))


@app.route('/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    """
    Update an existing question.
    Expected JSON payload: { "survey_id": 1, "question_text": "New question text", "question_type": "text" }
    Only provided fields will be updated.
    """
    data = request.get_json()
    survey_id = data.get('survey_id')
    question_text = data.get('question_text')
    question_type = data.get('question_type')

    connect = connection_of_database()
    cursor = connect.cursor()
    # Use COALESCE to update only fields that are provided.
    cursor.execute("""
        UPDATE QUESTIONS
        SET survey_id = COALESCE(?, survey_id),
            question_text = COALESCE(?, question_text),
            question_type = COALESCE(?, question_type)
        WHERE question_id = ?
    """, (survey_id, question_text, question_type, question_id))
    connect.commit()
    connect.close()

    return jsonify({'message': 'Successfully updated question'})


@app.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    """
    Delete a question by its ID.
    """
    connect = connection_of_database()
    cursor = connect.cursor()
    cursor.execute("DELETE FROM QUESTIONS WHERE question_id = ?", (question_id,))
    connect.commit()
    connect.close()

    return jsonify({'message': 'Successfully deleted a question record'})

# ANSWERS CRUD

@app.route('/answers', methods=['GET'])
def get_answers():
    """
    Retrieve all answers.
    """
    connect = connection_of_database()
    answers = connect.execute("SELECT * FROM ANSWERS").fetchall()
    connect.close()

    # Convert rows to a list of dictionaries.
    answer_list = [dict(row) for row in answers]
    return jsonify(answer_list)


@app.route('/answers', methods=['POST'])
def create_answer():
    """
    Create a new answer record.
    Expected JSON payload: { "choice_id": 1, "response_id": 1 }
    """
    data = request.get_json()
    choice_id = data.get('choice_id')
    response_id = data.get('response_id')

    connect = connection_of_database()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO ANSWERS (choice_id, response_id) VALUES (?, ?)",
                   (choice_id, response_id))
    connect.commit()
    new_id = cursor.lastrowid
    connect.close()

    return jsonify({'message': 'Successfully created an answer record', 'answer_id': new_id}), 201


@app.route('/answers/<int:answer_id>', methods=['GET'])
def get_answer(answer_id):
    """
    Retrieve a specific answer by its ID.
    """
    connect = connection_of_database()
    answer = connect.execute("SELECT * FROM ANSWERS WHERE answer_id = ?", (answer_id,)).fetchone()
    connect.close()

    if answer is None:
        return jsonify({'error': 'No record of such answer with this ID number'}), 404

    return jsonify(dict(answer))


@app.route('/answers/<int:answer_id>', methods=['PUT'])
def update_answer(answer_id):
    """
    Update an existing answer.
    Expected JSON payload: { "choice_id": 1, "response_id": 1 }
    Only provided fields will be updated.
    """
    data = request.get_json()
    choice_id = data.get('choice_id')
    response_id = data.get('response_id')

    connect = connection_of_database()
    cursor = connect.cursor()
    # Use COALESCE to update only fields that are provided.
    cursor.execute("""
        UPDATE ANSWERS
        SET choice_id = COALESCE(?, choice_id),
            response_id = COALESCE(?, response_id)
        WHERE answer_id = ?
    """, (choice_id, response_id, answer_id))
    connect.commit()
    connect.close()

    return jsonify({'message': 'Successfully updated answer'})


@app.route('/answers/<int:answer_id>', methods=['DELETE'])
def delete_answer(answer_id):
    """
    Delete an answer by its ID.
    """
    connect = connection_of_database()
    cursor = connect.cursor()
    cursor.execute("DELETE FROM ANSWERS WHERE answer_id = ?", (answer_id,))
    connect.commit()
    connect.close()

    return jsonify({'message': 'Successfully deleted an answer record'})

# RESPONSES CRUD

@app.route('/responses', methods=['GET'])
def get_responses():
    """
    Retrieve all responses.
    """
    connect = connection_of_database()
    responses = connect.execute("SELECT * FROM RESPONSES").fetchall()
    connect.close()

    # Convert rows to a list of dictionaries.
    response_list = [dict(row) for row in responses]
    return jsonify(response_list)


@app.route('/responses', methods=['POST'])
def create_response():
    """
    Create a new response record.
    Expected JSON payload: { "survey_id": 1, "client_id": 1, "question_id": 1, "answer_text": "Sample answer" }
    """
    data = request.get_json()
    survey_id = data.get('survey_id')
    client_id = data.get('client_id')
    question_id = data.get('question_id')
    answer_text = data.get('answer_text')

    connect = connection_of_database()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO RESPONSES (survey_id, client_id, question_id, answer_text) VALUES (?, ?, ?, ?)",
                   (survey_id, client_id, question_id, answer_text))
    connect.commit()
    new_id = cursor.lastrowid
    connect.close()

    return jsonify({'message': 'Successfully created a response record', 'response_id': new_id}), 201


@app.route('/responses/<int:response_id>', methods=['GET'])
def get_response(response_id):
    """
    Retrieve a specific response by its ID.
    """
    connect = connection_of_database()
    response = connect.execute("SELECT * FROM RESPONSES WHERE response_id = ?", (response_id,)).fetchone()
    connect.close()

    if response is None:
        return jsonify({'error': 'No record of such response with this ID number'}), 404

    return jsonify(dict(response))


@app.route('/responses/<int:response_id>', methods=['PUT'])
def update_response(response_id):
    """
    Update an existing response.
    Expected JSON payload: { "survey_id": 1, "client_id": 1, "question_id": 1, "answer_text": "Updated answer" }
    Only provided fields will be updated.
    """
    data = request.get_json()
    survey_id = data.get('survey_id')
    client_id = data.get('client_id')
    question_id = data.get('question_id')
    answer_text = data.get('answer_text')

    connect = connection_of_database()
    cursor = connect.cursor()
    # Use COALESCE to update only fields that are provided.
    cursor.execute("""
        UPDATE RESPONSES
        SET survey_id = COALESCE(?, survey_id),
            client_id = COALESCE(?, client_id),
            question_id = COALESCE(?, question_id),
            answer_text = COALESCE(?, answer_text)
        WHERE response_id = ?
    """, (survey_id, client_id, question_id, answer_text, response_id))
    connect.commit()
    connect.close()

    return jsonify({'message': 'Successfully updated response'})


@app.route('/responses/<int:response_id>', methods=['DELETE'])
def delete_response(response_id):
    """
    Delete a response by its ID.
    """
    connect = connection_of_database()
    cursor = connect.cursor()
    cursor.execute("DELETE FROM RESPONSES WHERE response_id = ?", (response_id,))
    connect.commit()
    connect.close()

    return jsonify({'message': 'Successfully deleted a response record'})

# SURVEY CRUD

@app.route('/surveys', methods=['GET'])
def get_surveys():
    """
    Retrieve all surveys.
    """
    connect = connection_of_database()
    surveys = connect.execute("SELECT * FROM SURVEY").fetchall()
    connect.close()

    # Convert rows to a list of dictionaries.
    survey_list = [dict(row) for row in surveys]
    return jsonify(survey_list)


@app.route('/surveys', methods=['POST'])
def create_survey():
    """
    Create a new survey record.
    Expected JSON payload: { "agent_id": 1, "title": "Survey Title", "description": "Survey Description" }
    """
    data = request.get_json()
    agent_id = data.get('agent_id')
    title = data.get('title')
    description = data.get('description')

    connect = connection_of_database()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO SURVEY (agent_id, title, description) VALUES (?, ?, ?)",
                   (agent_id, title, description))
    connect.commit()
    new_id = cursor.lastrowid
    connect.close()

    return jsonify({'message': 'Successfully created a survey record', 'survey_id': new_id}), 201


@app.route('/surveys/<int:survey_id>', methods=['GET'])
def get_survey(survey_id):
    """
    Retrieve a specific survey by its ID.
    """
    connect = connection_of_database()
    survey = connect.execute("SELECT * FROM SURVEY WHERE survey_id = ?", (survey_id,)).fetchone()
    connect.close()

    if survey is None:
        return jsonify({'error': 'No record of such survey with this ID number'}), 404

    return jsonify(dict(survey))


@app.route('/surveys/<int:survey_id>', methods=['PUT'])
def update_survey(survey_id):
    """
    Update an existing survey.
    Expected JSON payload: { "agent_id": 1, "title": "New Survey Title", "description": "New Survey Description" }
    Only provided fields will be updated.
    """
    data = request.get_json()
    agent_id = data.get('agent_id')
    title = data.get('title')
    description = data.get('description')

    connect = connection_of_database()
    cursor = connect.cursor()
    # Use COALESCE to update only fields that are provided.
    cursor.execute("""
        UPDATE SURVEY
        SET agent_id = COALESCE(?, agent_id),
            title = COALESCE(?, title),
            description = COALESCE(?, description)
        WHERE survey_id = ?
    """, (agent_id, title, description, survey_id))
    connect.commit()
    connect.close()

    return jsonify({'message': 'Successfully updated survey'})


@app.route('/surveys/<int:survey_id>', methods=['DELETE'])
def delete_survey(survey_id):
    """
    Delete a survey by its ID.
    """
    connect = connection_of_database()
    cursor = connect.cursor()
    cursor.execute("DELETE FROM SURVEY WHERE survey_id = ?", (survey_id,))
    connect.commit()
    connect.close()

    return jsonify({'message': 'Successfully deleted a survey record'})


if __name__=="__main__":
    initialization_of_db()
    app.run(debug=True)