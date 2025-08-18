from flask import Flask
from config.configure import DEBUG
from services.db import init_db
from controller.agent_controller import agent_bp
from controller.client_controller import client_bp
from controller.question_controller import question_bp
from controller.answer_controller import answer_bp
from controller.responds_controller import respond_bp
from controller.survey_controller import survey_bp


app = Flask(__name__)

app.register_blueprint(agent_bp)
app.register_blueprint(client_bp)
app.register_blueprint(question_bp)
app.register_blueprint(answer_bp)
app.register_blueprint(respond_bp)
app.register_blueprint(survey_bp)


init_db()

if __name__ == "__main__":
    app.run(debug=DEBUG)