from flask import Flask,jsonify
app=Flask(__name__)
@app.route("/")
def home ():
    p=3
    d=4

    return jsonify({ "description":p*d})
def about ():
    return jsonify({"my name is princess"})


if __name__=="__main__":
    app.run(debug=False)
import _sqlite3
import sqlite3
from flask import Flask ,request,jsonify
respons