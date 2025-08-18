from flask import Blueprint, request, jsonify
from services.db import get_connection

technology_bp = Blueprint("assistive_technology ", __name__)



@technology_bp.route("/assistive_technology ", methods=["GET"])
def get_tech():
    connect = get_connection()
    technology=connect.execute("SELECT * FROM assistive_technology").fetchall()
    connect.close()
    technology_list=[dict(row)for row in (technology)]
    return jsonify(technology_list)

@technology_bp.route('/assistive_technology /<int:question_tech_id>', methods=["GET"])
def get_one_tech(question_tech_id):
    connect=get_connection()
    technology_list =connect.execute('SELECT * FROM assistive_technology WHERE question_tech_id =?', (question_tech_id)).fetchone()
    connect.close()
    if technology_list is None:
        return jsonify("record does not exist"), 404
    return jsonify(dict(technology_list))

@technology_bp.route('/assistive_technology', methods=["POST"])
def post_tech():
    data = request.get_json() 
    questions = data.get('question')
    client_id= data.get ('client_id')
  
    
    connect= get_connection()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO assistive_technology (questions,client_id) VALUES (?,?)",
                   (questions,client_id))
    connect.commit()
    connect.close()
    return jsonify("Message: Record uploaded successfully")

@technology_bp.route ('/assistive_technology/<int:question_tech_id>', methods= ['PUT'])
def update_tech_info(question_tech_id):

    data = request.get_json()
    questions = data.get('questions')
    client_id = data.get('client_id')
    

    connect = get_connection()
    cursor=connect.cursor()

    cursor.execute("""
        UPDATE assistive_technology
        SET questions = COALESCE(?, questions),
            client_id = COALESCE(?, client_id)
            
        WHERE  question_tech_id = ?
    """, (questions, client_id, question_tech_id))
    connect.commit()
    connect.close()
    return jsonify({'message': 'Successfully updated Project'})


@technology_bp.route('/qassistive_technology/<int:question_tech_id>', methods=['DELETE'])
def delete_tech_info(question_tech_id):

    connect =get_connection()
    cursor=connect.cursor()
    cursor.execute('SELECT * FROM assistive_technology WHERE question_tech_id = ?', (question_tech_id))
    connect.commit()
    connect.close()
    
    return jsonify({"message":"successfuly deleted a record"})