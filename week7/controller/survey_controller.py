from flask import Blueprint, request, jsonify
from services.db import get_db_connection

survey_bp = Blueprint("survey", __name__)



@survey_bp.route("/survey", methods=["GET"])
def get_survey():
    connection = get_db_connection()
    survey=connection.execute   ("SELECT * FROM survey").fetchall()
    connection.close()
    survey_list=[dict(row)for row in (survey)]
    return jsonify(survey_list)

@survey_bp.route('/survey/<int:survey_id>', methods=["GET"])
def get_one_survey(survey_id):
    connection=get_db_connection()
    survey =connection.execute('SELECT * FROM survey WHERE survey_id =?', (survey_id)).fetchone
    connection.close()
    if survey is None:
        return jsonify("record does not exist"), 404
    return jsonify(dict(survey))

@survey_bp.route('/survey', methods=["POST"])
def post_survey():
    data = request.get_json()
    description= data.get('discription')
    name = data.get('name')
    agent_id = data.get('agent_id')
    
    connection= get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO survey (description, name, agent_id) VALUES (?,?,?)",
                   (description,name, agent_id))
    connection.commit()
    connection.close()
    return jsonify("Message: Record uploaded successfully")

@survey_bp.route ('/survey/<int:survey_id>', methods= ['PUT'])
def update_survey_info(survey_id):

    data = request.get_json()
    description = data.get('description')
    name = data.get('name')
    agent_id = data.get('agent_id')
   
    connection = get_db_connection()
    cursor=connection.cursor()

    cursor.execute("""
        UPDATE survey
        SET description = COALESCE(?, description),
            name = COALESCE (?, name),
            agent_id = COALESCE (?, agent_id)
            
        WHERE  survey_id = ?
    """, (description,name,agent_id, survey_id))
    connection.commit()
    connection.close()
    return jsonify({'message': 'Successfully updated Project'})


@survey_bp.route('/survey/<int:survey_id>', methods=['DELETE'])
def delete_survey_info(survey_id):

    connection =get_db_connection()
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM csurvey WHERE survey_id = ?', (survey_id,))
    connection.commit()
    connection.close()
    
    return jsonify({"message":"successfuly deleted a record"})