
from flask import Flask, json
from flask import jsonify
from flask import request
import csv
import io

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

import sys
sys.path.insert(1, './cuckoo')

app.run(debug=True)

# import hash tables
from cuckoo import *
from chain import *


mode = 1

table_cuckoo = Cuckoo()
table_chain = Chain()


def delete_employee(key):
    print(table_cuckoo.pop(key))
    table_chain.discard(key)


def delete_employees_all():
    keys = [key for key in table_cuckoo.keys()]
    for key in keys:
        delete_employee(key)

#Insert data into cuckoo or chaining table
def insert_data(key,data):
    if mode == 1:
        table_cuckoo[key] = data
        return
    
    table_chain[key] = data

#Get data from cuckoo and chaining 
def get_data(key):
    if mode == 1:
        return table_cuckoo[key]
    return table_chain[key]


def get_all_data(max_value):
    keys =  table_cuckoo.keys()
    if max_value !=None:
        keys[:min(len(keys),max_value)]

    return [table_cuckoo[key] for key in keys]


@app.route('/set')
def set_mode():
    global mode
    mode_value = request.args.get('mode')
    mode = int(mode_value)
    return 'Table Change to: ' + ('Cuckoo' if mode == 1 else 'Chaining')


@app.route('/employees/<user_id>', methods = ['GET', 'POST', 'DELETE'])
@cross_origin()
def employees(user_id):
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        data = request.form # a multidict containing POST data
        
        userData = data.to_dict()
        userData['id'] = user_id
        insert_data(user_id,userData)
        return "<h1>"+user_id+"</h1>"

    if request.method == "DELETE":
        delete_employee(user_id)
        return "Delete successful"

    if request.method == "GET":
        if user_id == "all":
            return jsonify(get_all_data())

        return jsonify(get_data(user_id))


@app.route('/employees-all/', methods = [ 'GET', 'POST'])
@cross_origin()
def employees_all():
    if request.method == "GET":
        return jsonify(get_all_data(None))



@app.route('/employees-batch/', methods = [ 'GET', 'POST','DELETE'])
@cross_origin()
def employees_batch():

    if request.method == "DELETE":
        delete_employees_all()
        return 'Deleted All'


    f = request.files['data_file']
    if not f:
        return "No file"

    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    reader = csv.reader(stream)
    data = list(reader)

        
    cols = data[0] # column names of the csv file 
    del data[0] # delete column row

    for entry in data:    
        id = entry[0]
        print(id)
        some_data = {}
        for i in range(0, len(cols) ):
            some_data[cols[i]] = entry[i]
        insert_data(id,some_data)

    return "Insert Complete"






@app.route('/')
@cross_origin()
def hello_world():
    return "<h1>hello</h1>"




@app.route('/insert')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    id = request.args.get('id')
    user = request.args.get('user')
    insert_data(id,user)
    return "Successful"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)