# src/controller/client_controller.py

from flask import Blueprint, request, jsonify
from services.db import get_db_connection

client_bp = Blueprint('clients', __name__)


@client_bp.route('/clients', methods=['POST'])
def create_client():
    """
    Create a new client (respondent).
    Expects JSON payload with biodata fields and agent_id.
    """
    data = request.get_json()
    agent_id = data.get('agent_id')
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')
    NIN = data.get('NIN')
    drive_license = data.get('drive_license')
    Lga = data.get('Lga')
    address = data.get('address')
    state = data.get('state')
    education = data.get('education')
    business = data.get('business')
    sex = data.get('sex')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO clients (agent_id, name, phone, email, NIN, drive_license, Lga, address, state, education, business, sex)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (agent_id, name, phone, email, NIN, drive_license, Lga, address, state, education, business, sex))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return jsonify({'message': 'Client created successfully', 'client_id': new_id}), 201


@client_bp.route('/clients', methods=['GET'])
def get_clients():
    """
    Retrieve all clients.
    """
    conn = get_db_connection()
    clients = conn.execute("SELECT * FROM clients").fetchall()
    conn.close()
    clients_list = [dict(client) for client in clients]
    return jsonify(clients_list)


@client_bp.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    """
    Retrieve a single client by its ID.
    """
    conn = get_db_connection()
    client = conn.execute("SELECT * FROM clients WHERE id = ?", (client_id,)).fetchone()
    conn.close()
    if client is None:
        return jsonify({'error': 'Client not found'}), 404
    return jsonify(dict(client))


@client_bp.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    """
    Update an existing client.
    Accepts a JSON payload with any of the biodata fields.
    """
    data = request.get_json()
    agent_id = data.get('agent_id')
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')
    NIN = data.get('NIN')
    drive_license = data.get('drive_license')
    Lga = data.get('Lga')
    address = data.get('address')
    state = data.get('state')
    education = data.get('education')
    business = data.get('business')
    sex = data.get('sex')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE clients
        SET agent_id = COALESCE(?, agent_id),
            name = COALESCE(?, name),
            phone = COALESCE(?, phone),
            email = COALESCE(?, email),
            NIN = COALESCE(?, NIN),
            drive_license = COALESCE(?, drive_license),
            Lga = COALESCE(?, Lga),
            address = COALESCE(?, address),
            state = COALESCE(?, state),
            education = COALESCE(?, education),
            business = COALESCE(?, business),
            sex = COALESCE(?, sex)
        WHERE id = ?
    """, (agent_id, name, phone, email, NIN, drive_license, Lga, address, state, education, business, sex, client_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Client updated successfully'})


@client_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    """
    Delete a client by its ID.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Client deleted successfully'})
