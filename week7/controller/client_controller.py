from flask import Blueprint, request, jsonify
from services.db import get_db_connection

client_bp = Blueprint("clients", __name__)



@client_bp.route("/clients", methods=["GET"])
def get_clients():
    connection = get_db_connection()
    clients=connection.execute("SELECT * FROM clients").fetchall()
    connection.close()
    clients_list=[dict(row)for row in (clients)]
    return jsonify(clients_list)

@client_bp.route('/clients/<int:client_id>', methods=["GET"])
def get_one_client(client_id):
    connection=get_db_connection()
    client_list =connection.execute('SELECT * FROM clients WHERE client_id =?', (client_id)).fetchone()
    connection.close()
    if client_list is None:
        return jsonify("record does not exist"), 404
    return jsonify(dict(client_list))

@client_bp.route('/clients', methods=["POST"])
def post_clients():
    data = request.get_json() 
    name = data.get('name')
    sex = data.get ('sex')
    number = data.get('number')
    email = data.get ('email')
    state = data.get('state')
    country = data.get('country')
    connection= get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO clients (name, sex,number,email, state, country) VALUES (?,?,?,?,?,?)",
                   (name, sex, number, email, state, country))
    connection.commit()
    connection.close()
    return jsonify("Message: Record uploaded successfully")

@client_bp.route ('/clients/<int:client_id>', methods= ['PUT'])
def update_client_info(client_id):

    data = request.get_json()
    name = data.get('name')
    sex = data.get('sex')
    number = data.get('number')
    email = data.get('email')
    state = data.get('state')
    country = data.get('country')

    connection = get_db_connection()
    cursor=connection.cursor()

    cursor.execute("""
        UPDATE clients
        SET name = COALESCE(?, name),
            sex = COALESCE(?, sex),
            number = COALESCE(?, number),
            email = COALESCE(?, email )
            state = COALESCE(?, state),
            country = COALESCE(?, country)
        WHERE  client_id = ?
    """, (name, sex, number,email, state,country, client_id))
    connection.commit()
    connection.close()
    return jsonify({'message': 'Successfully updated Project'})


@client_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client_info(client_id):

    connection =get_db_connection()
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM clients WHERE client_id = ?', (client_id,))
    connection.commit()
    connection.close()
    
    return jsonify({"message":"successfuly deleted a record"})