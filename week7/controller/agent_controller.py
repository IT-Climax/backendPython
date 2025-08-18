from flask import Blueprint, request, jsonify
from services.db import get_db_connection

agent_bp = Blueprint("agents", __name__)



@agent_bp.route("/agents", methods=["GET"])
def get_agents():
    connection = get_db_connection()
    agents=connection.execute("SELECT * FROM agents").fetchall()
    connection.close()
    agents_list=[dict(row)for row in (agents)]
    return jsonify(agents_list)

@agent_bp.route('/agents/<int:agent_id>', methods=["GET"])
def get_one_agent(agent_id):
    connection=get_db_connection
    Agents = connection.execute('SELECT * FROM agents WHERE agent_id =?', (agent_id)).fetchone
    connection.close()
    if Agents is None:
        return jsonify("record does not exist"), 404
    return jsonify(dict(Agents))

@agent_bp.route("/agents", methods=["POST"])
def post_agents():
    data = request.get_json()
    name = data.get('name')
    sex = data.get ('sex')
    roll = data.get('roll')
    number = data.get('number')
    email = data.get ('email')

    connection= get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO agents (name, sex, roll,number,email) VALUES (?,?,?,?,?)",
                   (name, sex, roll, number, email))
    connection.commit()
    connection.close()
    return jsonify("Message: Record uploaded successfully")

@agent_bp.route ('/agents/<int:agent_id>', methods= ['PUT'])
def update_agent_info(agent_id):

    data = request.get_json()
    name = data.get('name')
    sex = data.get('sex')
    roll = data.get('roll')
    number = data.get('number')
    email = data.get('email')

    connection = get_db_connection()
    cursor=connection.cursor()

    cursor.execute("""
        UPDATE agents
        SET name = COALESCE(?, name),
            sex = COALESCE(?, sex),
            roll = COALESCE(?, roll),
            number = COALESCE(?, number),
            email = COALESCE(?, email )
        WHERE  agent_id = ?
    """, (name, sex, roll, number,email, agent_id))
    connection.commit()
    connection.close()
    return jsonify({'message': 'Successfully updated Project'})


@agent_bp.route('/agents/<int:agent_id>', methods=['DELETE'])
def delete_agent(agent_id):

    connection =get_db_connection()
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM agents WHERE agent_id = ?', (agent_id,))
    connection.commit()
    connection.close()
    
    return jsonify({"message":"successfuly deleted a record"})