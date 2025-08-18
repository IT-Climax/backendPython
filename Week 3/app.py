import sqlite
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/home/")
def home():
    p= 34
    d = 43
    return jsonify("key", p*d)

if __name__ == "__main__":
    app.run(debug=True)
