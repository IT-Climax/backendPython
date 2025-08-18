from flask import Flask
from config.configure import DEBUG
from services.db import init_db

app = Flask(__name__)


init_db()

if __name__ == "__main__":
    app.run(debug=DEBUG)