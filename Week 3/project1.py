from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/home/")
def home():
    p= 2
    d = 4
    return jsonify("key", p*d)

if __name__ == "__main__":
    app.run(debug=True)

