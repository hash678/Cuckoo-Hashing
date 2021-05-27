import sys
sys.path.insert(1, './cuckoo')

from cuckoo import *
from chain  import *
import csv

isCuckoo = None
table = None



def definer(cuckoo):
    global table
    global isCuckoo
    isCuckoo = cuckoo
    
    batchList()

    if isCuckoo:
        table = Cuckoo()
    if not isCuckoo:
        table = Chain()


def batchList():
    global data
    with open('records.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    

def batchInsert():

    cols = data[0]
    del data[0]

    for entry in data:
        id = entry[0]
        curr_data = dict()
        for i in range(0, len(cols) ):
            curr_data[cols[i]] = entry[i]
        table[id] = curr_data



def rowsInsertion(rows):

    cols = data[0]
    del data[0]

    for entry in data[0:rows]:
        id = entry[0]
        curr_data = dict()
        for i in range(0, len(cols) ):
            curr_data[cols[i]] = entry[i]
        table[id] = curr_data


def batchDeletion():
    for key in table.keys():
        table.pop(key)
    


