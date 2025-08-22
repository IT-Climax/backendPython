# src/controller/agent_controller.py

from flask import Blueprint, request, jsonify
from services.db import get_db_connection

agent_bp = Blueprint('agents', __name__)

# @agent_bp.route('/agents', methods=['POST'])
# def create_agent():
#     """
#     Create a new agent (enumerator).
#     Expects JSON payload with: { "name": "Agent Name", "phone": "123456789", "email": "agent@example.com" }
#     """
#     data = request.get_json()
#     name = data.get('name')
#     phone = data.get('phone')
#     email = data.get('email')
#
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO agents (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
#     conn.commit()
#     new_id = cursor.lastrowid
#     conn.close()
#
#     return jsonify({'message': 'Agent created successfully', 'agent_id': new_id}), 201


@agent_bp.route('/agents', methods=['GET'])
def get_agents():
    """
    Retrieve all agents.
    """
    conn = get_db_connection()
    agents = conn.execute("SELECT * FROM agents").fetchall()
    conn.close()
    agents_list = [dict(agent) for agent in agents]
    return jsonify(agents_list)


@agent_bp.route('/agents/<int:agent_id>', methods=['GET'])
def get_agent(agent_id):
    """
    Retrieve a single agent by its ID.
    """
    conn = get_db_connection()
    agent = conn.execute("SELECT * FROM agents WHERE id = ?", (agent_id,)).fetchone()
    conn.close()
    if agent is None:
        return jsonify({'error': 'Agent not found'}), 404
    return jsonify(dict(agent))


@agent_bp.route('/agents/<int:agent_id>', methods=['PUT'])
def update_agent(agent_id):
    """
    Update an existing agent.
    Accepts JSON payload with any of the fields: name, phone, email.
    """
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE agents
        SET name = COALESCE(?, name),
            phone = COALESCE(?, phone),
            email = COALESCE(?, email)
        WHERE id = ?
    """, (name, phone, email, agent_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Agent updated successfully'})


@agent_bp.route('/agents/<int:agent_id>', methods=['DELETE'])
def delete_agent(agent_id):
    """
    Delete an agent by its ID.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM agents WHERE id = ?", (agent_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Agent deleted successfully'})
