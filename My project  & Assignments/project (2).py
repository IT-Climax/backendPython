import sqlite3
from flask import Flask ,request,jsonify

project_app=Flask(__name__)
data_store="constructiom.db"
def db_connection():
    """
    create and return a connection to the sqlite database
    the row factory setting allows rows to be returned a dictionaries
    """
    conn=sqlite3.connect(database=)
    conn.row_factory=sqlite3.Row
    return conn