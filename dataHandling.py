import sys
sys.path.insert(1, './cuckoo')
from cuckoo import *
from chain  import *
import csv

isCuckoo = False


with open('records2.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

cols = data[0]
del data[0]


def batchInsert():
    if isCuckoo:
        table = Cuckoo()
    else:
        table = Chain()    

    for entry in data:
        id = entry[0]
        curr_data = dict()
        for i in range(0, len(cols) ):
            curr_data[cols[i]] = entry[i]
        table[id] = curr_data

    return table

def rowsInsertion(rowNum):
    if isCuckoo:
        dataTable = Cuckoo()
    else:
        dataTable = Chain()
    for entry in data [0:rowNum]:
        id = entry[0]
        curr_data = dict()
        for i in range(0, len(cols) ):
            curr_data[cols[i]] = entry[i]
        dataTable[id] = curr_data


def batchDeletion(table):
    for key in table.keys():
        table.pop(key)