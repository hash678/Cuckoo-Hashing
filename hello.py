
from flask import Flask, json
from flask import jsonify
from flask import request
import csv
import io
import time

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


def delete_employee_attendance(key):
    if mode == 1:
        table_cuckoo[key]['Attendance'] = None
    if mode == 0:
        table_chain[key]['Attendance'] = None


def delete_employee(key):
    if mode == 1:
        table_cuckoo.pop(key)
    if mode == 0:
        table_chain.pop(key)


def delete_employees_all():
    keys = [key for key in table_cuckoo.keys()]
    for key in keys:
        delete_employee(key)

#Insert data into cuckoo or chaining table
def insert_data(key,data):
    if mode == 1:
        table_cuckoo[key] = data
        return 
    else:   
        # print("USING CHAINING")
        table_chain[key] = data

#Get data from cuckoo and chaining 
def get_data(key):
    if mode == 1:
        return table_cuckoo[key]
    return table_chain[key]


def get_all_data(max_value):
    
    if mode == 1:
        keys =  table_cuckoo.keys()
    else:
        keys  = table_chain.keys()
        
    # if max_value !=None:
    #     keys[:min(len(keys),max_value)]

    if mode == 1:
        return [table_cuckoo[key] for key in keys]
    else:
        return [table_chain[key] for key in keys]

def delete_attendance_user(user_ID):
    keys = [key for key in table_cuckoo.keys()]
    for key in keys:
        delete_employee_attendance(key)




def mark_user_attendance(user_ID,data):
    if mode == 1:

        if not 'Attendance' in table_cuckoo[user_ID]:
             table_cuckoo[user_ID]['Attendance'] = [data]
        else:
            table_cuckoo[user_ID]['Attendance'] = ([data] + table_cuckoo[user_ID]['Attendance'])
        return 

    else:
        if not 'Attendance' in table_chain[user_ID]:
             table_chain[user_ID]['Attendance'] = [data]
        else:
            table_chain[user_ID]['Attendance'] = ([data] + table_chain[user_ID]['Attendance'])
        return 
           
        # print("USING CHAINING")
   


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
        start_time = time.time()
        insert_data(user_id,userData)
        return jsonify({'timeTaken':(time.time()-start_time)})

    if request.method == "DELETE":
        start_time = time.time()
        delete_employee(user_id)
        return "Delete successful"

    if request.method == "GET":
        start_time = time.time()
        gotData = get_data(user_id)
        return jsonify({'timeTaken':(time.time()-start_time),'data':gotData})



@app.route('/employees-all/', methods = [ 'GET', 'POST'])
@cross_origin()
def employees_all():
    if request.method == "GET":
        start_time = time.time()
        gotData = get_all_data(None)
        return jsonify({'timeTaken':(time.time()-start_time),'data':gotData})



@app.route('/employees-batch/', methods = [ 'GET', 'POST','DELETE'])
@cross_origin()
def employees_batch():

    #Batch Delete Data
    if request.method == "DELETE":
        start_time = time.time()
        delete_employees_all()
        
        return jsonify({'timeTaken':(time.time()-start_time)})


    #Insert Data in Batch
    start_time = time.time()
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
        some_data = {}
        for i in range(0, len(cols) ):
            some_data[cols[i]] = entry[i]
        insert_data(id,some_data)

    timeTaken = (time.time()-start_time)
    print(timeTaken)
    return jsonify({'timeTaken':timeTaken})


@app.route('/attendance/<user_id>', methods = [ 'GET', 'POST','DELETE'])
@cross_origin()
def employee_attendance(user_id):

    #Batch Delete Data
    if request.method == "DELETE":
        start_time = time.time()
        delete_attendance_user(user_id)
        return jsonify({'timeTaken':(time.time()-start_time)})

    if request.method == "POST":
        data = request.form
        userData = data.to_dict()
        start_time = time.time()
        mark_user_attendance(user_id,userData)

        timeTaken = (time.time()-start_time)
        print(timeTaken)

        return jsonify({'timeTaken':timeTaken})

    if request.method == "GET":
        data = request.form
        userData = data.to_dict()
        start_time = time.time()
        attendance = get_data(user_id)['Attendance']

        timeTaken = (time.time()-start_time)
        print(timeTaken)

        return jsonify({'timeTaken':timeTaken,'data':attendance})


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