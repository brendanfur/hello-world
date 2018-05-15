import os
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.tododb

@app.route('/')
def todo():

    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('todo.html', items=items)

@app.route('/intake')
def intake():

    _items = db.intake.find()
    items = [item for item in _items]

    return render_template('intake.html', items=items)

@app.route('/new', methods=['POST'])
def new():

    item_doc = {
        'name_first': request.form['name_first'],
        'name_last': request.form['name_last'],
        'license': request.form['license'],
        'modalities': request.form['modalities']
    }
    db.tododb.insert_one(item_doc)

    return redirect(url_for('todo'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
