from flask import Blueprint, request, jsonify
from services.db import get_connection

empower_bp = Blueprint("question_empower", __name__)



@empower_bp.route("/question_empower", methods=["GET"])
def get_edu():
    connect = get_connection()
    question=connect.execute("SELECT * FROM question_empower").fetchall()
    connect.close()
    questions_list=[dict(row)for row in (question)]
    return jsonify(questions_list)

@empower_bp.route('/question_empower/<int:question_empo_id>', methods=["GET"])
def get_one_edu(question_empo_id):
    connect=get_connection()
    questions_list =connect.execute('SELECT * FROM question_empower WHERE question_empo_id =?', (question_empo_id)).fetchone()
    connect.close()
    if questions_list is None:
        return jsonify("record does not exist"), 404
    return jsonify(dict(questions_list))

@empower_bp.route('/question_empower', methods=["POST"])
def post_edu():
    data = request.get_json() 
    questions = data.get('question')
    client_id= data.get ('client_id')
  
    
    connect= get_connection()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO question_enpower (questions,client_id) VALUES (?,?)",
                   (questions,client_id))
    connect.commit()
    connect.close()
    return jsonify("Message: Record uploaded successfully")

@empower_bp.route ('/question_empower/<int:question_empo_id>', methods= ['PUT'])
def update_edu_info(question_empo_id):

    data = request.get_json()
    questions = data.get('questions')
    client_id = data.get('client_id')
    

    connect = get_connection()
    cursor=connect.cursor()

    cursor.execute("""
        UPDATE question_empower
        SET questions = COALESCE(?, questions),
            client_id = COALESCE(?, client_id)
            
        WHERE  question_empo_id = ?
    """, (questions, client_id, question_empo_id))
    connect.commit()
    connect.close()
    return jsonify({'message': 'Successfully updated Project'})


@empower_bp.route('/question_empower/<int:question_empo_id>', methods=['DELETE'])
def delete_client_info(question_empo_id):

    connect =get_connection()
    cursor=connect.cursor()
    cursor.execute('SELECT * FROM question_empower WHERE question_empo_id = ?', (question_empo_id))
    connect.commit()
    connect.close()
    
    return jsonify({"message":"successfuly deleted a record"})