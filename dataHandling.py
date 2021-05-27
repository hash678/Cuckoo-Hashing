from cuckoo import *
from chain  import *
import csv


def definer(icCuckoo):
    global table
    if icCuckoo:
        table = Cuckoo()
    else:
        table = Chain()


def batchList():
    with open('records.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    return data

def batchInsert():
    data = batchList()

    cols = data[0]
    del data[0]

    for entry in data:
        id = entry[0]
        curr_data = dict()
        for i in range(0, len(cols) ):
            curr_data[cols[i]] = entry[i]
        table[id] = curr_data



def rowsInsertion(rows):
    data = batchList()

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
    


