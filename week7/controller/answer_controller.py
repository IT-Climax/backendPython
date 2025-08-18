from flask import Blueprint, request, jsonify
from services.db import get_db_connection

answer_bp = Blueprint("answers", __name__)



@answer_bp.route("/answers", methods=["GET"])
def get_answers():
    connection = get_db_connection()
    answers=connection.execute("SELECT * FROM answers").fetchall()
    connection.close()
    answers_list=[dict(row)for row in (answers)]
    return jsonify(answers_list)

@answer_bp.route('/answers/<int:answer_id>', methods=["GET"])
def get_one_answer(answer_id):
    connection=get_db_connection()
    answers =connection.execute('SELECT * FROM answers WHERE answer_id =?', (answer_id)).fetchone
    connection.close()
    if answers is None:
        return jsonify("record does not exist"), 404
    return jsonify(dict(answers))

@answer_bp.route('/answers', methods=["POST"])
def post_answer():
    data = request.get_json()
    name = data.get('name')
    question_id = data.get('question_id')
    client_id = data.get('client_id')
    
    connection= get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO answers (name,question_id,client_id) VALUES (?,?,?)",
                   (name,question_id,client_id))
    connection.commit()
    connection.close()
    return jsonify("Message: Record uploaded successfully")

@answer_bp.route ('/answers/<int:answer_id>', methods= ['PUT'])
def update_answer_info(answer_id):

    data = request.get_json()
    name = data.get('name')
    question_id = data.get('question_id')
    client_id = data.get('client_id')

    connection = get_db_connection()
    cursor=connection.cursor()

    cursor.execute("""
        UPDATE answers
        SET name = COALESCE(?, name),
            question_id = COALESCE(?, question_id),
            client_id = COALESCE (?, client_id)
        WHERE  answer_id = ?
    """, (name,question_id,client_id (answer_id)))
    connection.commit()
    connection.close()
    return jsonify({'message': 'Successfully updated Project'})


@answer_bp.route('/answers/<int:answer_id>', methods=['DELETE'])
def delete_answer_info(answer_id):

    connection =get_db_connection()
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM answers WHERE answer_id = ?', (answer_id,))
    connection.commit()
    connection.close()
    
    return jsonify({"message":"successfuly deleted a record"})