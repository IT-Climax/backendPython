from flask import Blueprint, request, jsonify
from services.db import get_connection

education_bp = Blueprint("questions_edu", __name__)



@education_bp.route("/questions_edu", methods=["GET"])
def get_edu():
    connect = get_connection()
    question=connect.execute("SELECT * FROM questions_edu").fetchall()
    connect.close()
    questions_list=[dict(row)for row in (question)]
    return jsonify(questions_list)

@education_bp.route('/questions_edu/<int:question_id>', methods=["GET"])
def get_one_edu(question_id):
    connect=get_connection()
    questions_list =connect.execute('SELECT * FROM questions_edu WHERE question_id =?', (question_id)).fetchone()
    connect.close()
    if questions_list is None:
        return jsonify("record does not exist"), 404
    return jsonify(dict(questions_list))

@education_bp.route('/questions_edu', methods=["POST"])
def post_edu():
    data = request.get_json() 
    questions = data.get('question')
    client_id= data.get ('client_id')
  
    
    connect= get_connection()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO questions_edu (questions,client_id) VALUES (?,?)",
                   (questions,client_id))
    connect.commit()
    connect.close()
    return jsonify("Message: Record uploaded successfully")

@education_bp.route ('/questions_edu/<int:question_id>', methods= ['PUT'])
def update_edu_info(question_id):

    data = request.get_json()
    questions = data.get('questions')
    client_id = data.get('client_id')
    

    connect = get_connection()
    cursor=connect.cursor()

    cursor.execute("""
        UPDATE questions_edu
        SET questions = COALESCE(?, questions),
            client_id = COALESCE(?, client_id)
            
        WHERE  question_id = ?
    """, (questions, client_id, question_id))
    connect.commit()
    connect.close()
    return jsonify({'message': 'Successfully updated Project'})


@education_bp.route('/questions_edu/<int:question_id>', methods=['DELETE'])
def delete_client_info(question_id):

    connect =get_connection()
    cursor=connect.cursor()
    cursor.execute('SELECT * FROM questions_edu WHERE question_id = ?', (question_id))
    connect.commit()
    connect.close()
    
    return jsonify({"message":"successfuly deleted a record"})