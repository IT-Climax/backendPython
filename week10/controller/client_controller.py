from flask import Blueprint, request, jsonify
from services.db import get_connection

client_bp = Blueprint("clients", __name__)



@client_bp.route("/clients", methods=["GET"])
def get_clients():
    connect = get_connection()
    clients=connect.execute("SELECT * FROM clients").fetchall()
    connect.close()
    clients_list=[dict(row)for row in (clients)]
    return jsonify(clients_list)

@client_bp.route('/clients/<int:client_id>', methods=["GET"])
def get_one_client(client_id):
    connect=get_connection()
    client_list =connect.execute('SELECT * FROM clients WHERE client_id =?', (client_id)).fetchone()
    connect.close()
    if client_list is None:
        return jsonify("record does not exist"), 404
    return jsonify(dict(client_list))

@client_bp.route('/clients', methods=["POST"])
def post_clients():
    data = request.get_json() 
    name = data.get('name')
    age = data.get ('age')
    gender = data.get('gender')
    marital_status = data.get ('marital_status')
    location = data.get('location')
    education = data.get('education')
    highest_level_education=('highest_level_education')
    
    connect= get_connection()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO clients (name, sex,number,email, state, country) VALUES (?,?,?,?,?,?)",
                   (name, age, gender, marital_status,location, education, highest_level_education))
    connect.commit()
    connect.close()
    return jsonify("Message: Record uploaded successfully")

@client_bp.route ('/clients/<int:client_id>', methods= ['PUT'])
def update_client_info(client_id):

    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    marital_status = data.get('marital_status')
    location = data.get('location')
    education = data.get('education')
    highest_level_education =data.get('highest_level_education')

    connect = get_connection()
    cursor=connect.cursor()

    cursor.execute("""
        UPDATE clients
        SET name = COALESCE(?, name),
            age = COALESCE(?, age),
            gender = COALESCE(?, gender),
            marital_status = COALESCE(?, marital_status ),
            location = COALESCE(?, location),
            education = COALESCE(?, education),
            highest_level_education = COALESCE(?, highest_level_education)
        WHERE  client_id = ?
    """, (name, age, gender,marital_status, location,education, highest_level_education, client_id))
    connect.commit()
    connect.close()
    return jsonify({'message': 'Successfully updated Project'})


@client_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client_info(client_id):

    connect =get_connection()
    cursor=connect.cursor()
    cursor.execute('SELECT * FROM clients WHERE client_id = ?', (client_id,))
    connect.commit()
    connect.close()
    
    return jsonify({"message":"successfuly deleted a record"})