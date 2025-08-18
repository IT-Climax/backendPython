from flask import Flask
from flask_migrate import Migrate
from src.config import Config
from src.db.core import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate (app, db)

    with app.app_context():
        from src.db.model.sections import Section
        from src.db.model.user import User
        # from src.api.controllers.auth import Auth

        from src.api.resources.sections import sections_bp
        from src.api.resources.user import users_bp
        # from src.api.controllers.auth import auth_bp
        app.register_blueprint(sections_bp)
        app.register_blueprint(users_bp)
        # app.register_blueprint(auth_bp)


    @app.route('/')
    def home():
        return {'message': 'Survey API Running'}
    
    return app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)