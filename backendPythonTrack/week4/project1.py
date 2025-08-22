"""
A basic Flask project example.

This file sets up a simple Flask web server with two endpoints.
It demonstrates how to create a Flask application, define routes,
and return responses in JSON format.
"""

# Import the Flask class and jsonify function from the flask package.
from flask import Flask, jsonify


# Create an instance of the Flask class.
# This instance will be our WSGI application.
app = Flask(__name__)


# Define a route for the home page ("/").
@app.route("/api/")
def home():
    """
    The home function handles requests to the root URL.
    It returns a simple JSON response welcoming the user.
    """
    return jsonify({"message": "Welcome to the Flask project!"})


# Define another route for the about page ("/about").
@app.route("/api/about")
def about():
    """
    The about function handles requests to the '/about' URL.
    It returns a JSON response with a brief description.
    """
    d = 23
    b = 21
    return jsonify({"description": b*d})


# This block ensures that the Flask application runs only if this script is executed directly.
if __name__ == "__main__":
    # Run the Flask application in debug mode.
    # Debug mode provides helpful error messages and automatically reloads the server when code changes.
    app.run(debug=True)
