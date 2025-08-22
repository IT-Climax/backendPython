# src/controller/response_controller.py

from flask import Blueprint, request, jsonify
from services.db import get_db_connection

response_bp = Blueprint('responses', __name__)


@response_bp.route('/responses', methods=['POST'])
def create_response():
    """
    Create a new response.
    Expects JSON payload with: { "client_id": 1, "question_id": 1, "name": "Selected Answer" }
    """
    data = request.get_json()
    client_id = data.get('client_id')
    question_id = data.get('question_id')
    name = data.get('name')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO responses (client_id, question_id, name) VALUES (?, ?, ?)",
                   (client_id, question_id, name))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return jsonify({'message': 'Response created successfully', 'response_id': new_id}), 201


@response_bp.route('/responses', methods=['GET'])
def get_responses():
    """
    Retrieve all responses.
    """
    conn = get_db_connection()
    responses = conn.execute("SELECT * FROM responses").fetchall()
    conn.close()
    responses_list = [dict(response) for response in responses]
    return jsonify(responses_list)


@response_bp.route('/responses/<int:response_id>', methods=['GET'])
def get_response(response_id):
    """
    Retrieve a specific response by its ID.
    """
    conn = get_db_connection()
    response = conn.execute("SELECT * FROM responses WHERE id = ?", (response_id,)).fetchone()
    conn.close()
    if response is None:
        return jsonify({'error': 'Response not found'}), 404
    return jsonify(dict(response))


@response_bp.route('/responses/<int:response_id>', methods=['PUT'])
def update_response(response_id):
    """
    Update an existing response.
    Accepts JSON payload with any of the fields: client_id, question_id, name.
    """
    data = request.get_json()
    client_id = data.get('client_id')
    question_id = data.get('question_id')
    name = data.get('name')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE responses
        SET client_id = COALESCE(?, client_id),
            question_id = COALESCE(?, question_id),
            name = COALESCE(?, name)
        WHERE id = ?
    """, (client_id, question_id, name, response_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Response updated successfully'})


@response_bp.route('/responses/<int:response_id>', methods=['DELETE'])
def delete_response(response_id):
    """
    Delete a response by its ID.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM responses WHERE id = ?", (response_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Response deleted successfully'})
