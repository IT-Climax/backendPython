from flask import Blueprint, request, jsonify
from services.db import get_db_connection

question_bp = Blueprint("questions", __name__)



@question_bp.route("/questions", methods=["GET"])
def get_questions():
    connection = get_db_connection()
    questions=connection.execute("SELECT * FROM questions").fetchall()
    connection.close()
    questions_list=[dict(row)for row in (questions)]
    return jsonify(questions_list)

@question_bp.route('/questions/<int:question_id>', methods=["GET"])
def get_one_question(question_id):
    connection=get_db_connection()
    question =connection.execute('SELECT * FROM questions WHERE question_id =?', (question_id)).fetchone
    connection.close()
    if question is None:
        return jsonify("record does not exist"), 404
    return jsonify(dict(question))

@question_bp.route('/questions', methods=["POST"])
def post_question():
    data = request.get_json()
    name = data.get('name')
    question = data.get('question')

    connection= get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO questions (name, questions) VALUES (?,?)",
                   (name, question))
    connection.commit()
    connection.close()
    return jsonify("Message: Record uploaded successfully")

@question_bp.route ('/questions/<int:question_id>', methods= ['PUT'])
def update_question_info(question_id):

    data = request.get_json()
    name = data.get('name')
    question = data.get('question')

    connection = get_db_connection()
    cursor=connection.cursor()

    cursor.execute("""
        UPDATE questions
        SET name = COALESCE(?, name),
            question = COALESCE(?,question)
        WHERE  question_id = ?  """, (name, question, question_id))
    
    connection.commit()
    connection.close()
    return jsonify({'message': 'Successfully updated Project'})


@question_bp.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_question_info(question_id):

    connection =get_db_connection()
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM questions WHERE question_id = ?', (question_id,))
    connection.commit()
    connection.close()
    
    return jsonify({"message":"successfuly deleted a record"})