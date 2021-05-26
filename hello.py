
from flask import Flask
from flask import jsonify
from flask import request

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


@app.route('/set')
def set_mode():
    global mode
    mode_value = request.args.get('mode')
    mode = int(mode_value)
    return 'Table Change to: ' + ('Cuckoo' if mode == 1 else 'Chaining')

@app.route('/')

def hello_world():

    id = request.args.get('id')
    return jsonify(get_data(id))

@app.route('/insert')
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    id = request.args.get('id')
    user = request.args.get('user')
    insert_data(id,user)
    return "Successful"


# if __name__ == '__main__':
#     # Threaded option to enable multiple instances for multiple user access support
#     app.run(threaded=True, port=5000)