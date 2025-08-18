import sqlite3
from flask import Flask,request,jsonify

app = Flask(__name__)

store = 'shoping.db';

def connect_db():
    connect=sqlite3.connect(store)
    connect.row_factory=sqlite3.Row
    return connect

def init_db():
    connect=connect_db()
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS customers(
                   customers_id AUTO INCREMENT PRIMARY KEY,
                   name (20)TEXT,
                   country(15)TEXT,
                   state (20)TEXT,
                   email (30)VARCHAR,
                   number (11)INT 
                   )
                   """)
    connect.commit()
    connect.close()


app.route('/')
def home():
    return jsonify({"key":"Value"})  


app.route('/customers', methods=['POST'])
def post_customers():
    data = request.get_json()
    name = data.get('name')
    country = data.get('country')
    state = data.get('state')
    email = data.get('email')
    number = data.get('number')

    connect=connect_db()
    cursor = connect.cursor()
    cursor.execute('INSERT INTO customers (name,country,state,email,number) VALUES(?,?,?,?,?)',
                   (name, country, state, email, number))
    
    connect.commit()
    connect.close()
    return jsonify({'Message: you have successfully added a record'}), 404


app.route('/customers', methods=['GET'])
def get_all_info():
    connect=connect_db
    customer= connect.execute('SELECT * FROM customers').fetchall()
    connect.close()

    customer_list=[dict(row) for row in customer]
    return jsonify(customer_list)

  
if __name__=='__main__':
    init_db
    app.run(debug=True)