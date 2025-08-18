# from flask import Flask
# from config.config import DEBUG
# from services.db import db_connection
# from controller.agent_controller import agent_bp
# #from controller.questions_controller import questions_bp
# #from controller.answer_controller import answer_bp
# #from controller.respones import responses_bp
# #from controller.client_controller import clients_bp


# app = Flask(__name__)
# app.register_blueprint(agent_bp)

# if __name__ == '__main__':
#     app.run(debug=True)


# src/app.py

"""
app.py - Main entry point for the Survey System API.

This file initializes the Flask application, registers the blueprints
for each resource, initializes the database, and runs the server.
"""

from flask import Flask
from config.config import DEBUG
from services.db import init_db
#from controller.agent_controller import agent_bp
from controller.client_controller import client_bp
# from controller.question_controller import question_bp
# from controller.answer_controller import answer_bp
# from controller.response_controller import response_bp

app = Flask(__name__)

# Register blueprints from the controllers
#app.register_blueprint(agent_bp)
app.register_blueprint(client_bp)
# app.register_blueprint(question_bp)
# app.register_blueprint(answer_bp)
# app.register_blueprint(response_bp)

# Initialize the database and create tables if they do not exist.
init_db()

if __name__ == '__main__':
    app.run(debug=DEBUG)