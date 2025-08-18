import sqlite3
from flask import Flask, jsonify 
app = Flask(__name__)

@app.route("/about")
def about():
    p= 34
    d= 4
    return jsonify("",p*d)
if __name__ =='__main__':
    app.run(debug=False)