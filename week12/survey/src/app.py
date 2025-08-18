from flask import Flask
from flask_migrate import Migrate
from src.config import Config
from src.db.core import db

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    # initialise database
    db.init_app(app)
    migrate = Migrate(app, db)
    

    with app.app_context():
        # import models FIRST
        from src.db.models.sections import Section
        from src.db.models.user import User
        # from src.db.core import db

        from src.api.resources.sections import sections_bp
        from src.api.resources.user import users_bp
        from src.api.controllers.auth import auth_bp
    
        # from src.api.resources. import users_bp
        # from src.api.resources.user import users_bp
        # from src.api.resources.auth import auth_bp

        app.register_blueprint(sections_bp)
        app.register_blueprint(users_bp)
        app.register_blueprint(auth_bp)

        # app.register_blueprint(users_bp)
        # app.register_blueprint(users_bp)
        # app.register_blueprint(auth_bp)

    
    @app.route("/")
    def home():
        return {"message":"Survey API Running"}
    
    return app
app = create_app()

if __name__== "__main__":
    app.run(debug = True)