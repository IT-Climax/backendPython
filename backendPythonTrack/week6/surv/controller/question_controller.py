# src/controller/question_controller.py

from flask import Blueprint, request, jsonify
from services.db import get_db_connection

question_bp = Blueprint('questions', __name__)


@question_bp.route('/questions', methods=['POST'])
def create_question():
    """
    Create a new survey question.
    Expects JSON payload with: { "name": "Question Text" }
    """
    data = request.get_json()
    name = data.get('name')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO questions (name) VALUES (?)", (name,))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return jsonify({'message': 'Question created successfully', 'question_id': new_id}), 201


@question_bp.route('/questions', methods=['GET'])
def get_questions():
    """
    Retrieve all survey questions.
    """
    conn = get_db_connection()
    questions = conn.execute("SELECT * FROM questions").fetchall()
    conn.close()
    questions_list = [dict(question) for question in questions]
    return jsonify(questions_list)


@question_bp.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    """
    Retrieve a specific survey question by its ID.
    """
    conn = get_db_connection()
    question = conn.execute("SELECT * FROM questions WHERE id = ?", (question_id,)).fetchone()
    conn.close()
    if question is None:
        return jsonify({'error': 'Question not found'}), 404
    return jsonify(dict(question))


@question_bp.route('/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    """
    Update an existing survey question.
    Accepts JSON payload with a new "name".
    """
    data = request.get_json()
    name = data.get('name')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE questions SET name = COALESCE(?, name) WHERE id = ?", (name, question_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Question updated successfully'})


@question_bp.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    """
    Delete a survey question by its ID.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM questions WHERE id = ?", (question_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Question deleted successfully'})
