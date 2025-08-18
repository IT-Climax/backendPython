from flask import Blueprint, request, jsonify
from services.db import get_db_connection

respond_bp = Blueprint("responds", __name__)



@respond_bp.route("/responds", methods=["GET"])
def get_responds():
    connection = get_db_connection()
    responds=("SELECT * FROM responds").fetchall()
    connection.close()
    responds_list=[dict(row)for row in (responds)]
    return jsonify(responds_list)

@respond_bp.route('/responds/<int:respond_id>', methods=["GET"])
def get_one_respond(respond_id):
    connection=get_db_connection
    responds =connection.execute('SELECT * FROM responds WHERE respond_id =?', (respond_id)).fetchone
    connection.close()
    if responds is None:
        return jsonify("record does not exist"), 404
    return jsonify(dict(responds))

@respond_bp.route('/responds', methods=["POST"])
def post_respond():
    data = request.get_json()
    name = data.get('name')
    question_id = data.get('question_id')
    client_id = data.get('client_id')
    
    connection= get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO responds (name,question_id,client_id) VALUES (?,?,?)",
                   (name,question_id,client_id))
    connection.commit()
    connection.close()
    return jsonify("Message: Record uploaded successfully")

@respond_bp.route ('/responds/<int:respond_id>', methods= ['PUT'])
def update_respond_info(respond_id):

    data = request.get_json()
    name = data.get('name')
    question_id = data.get('question_id')
    client_id = data.get('client_id')

    connection = get_db_connection()
    cursor=connection.cursor()

    cursor.execute("""
        UPDATE responds
        SET name = COALESCE(?, name),
            question_id = COALESCE(?, question_id),
            client_id = COALESCE (?, client_id)
        WHERE  respond_id = ?
    """, (name, question_id, client_id, respond_id))
    connection.commit()
    connection.close()
    return jsonify({'message': 'Successfully updated Project'})


@respond_bp.route('/responds/<int:respond_id>', methods=['DELETE'])
def delete_respond_info(respond_id):

    connection =get_db_connection()
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM responds WHERE respond_id = ?', (respond_id,))
    connection.commit()
    connection.close()
    
    return jsonify({"message":"successfuly deleted a record"})