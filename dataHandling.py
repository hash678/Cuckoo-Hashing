from cuckoo import *
from chain  import *
import csv

isCuckoo = True
table = None

if isCuckoo:
    table = Cuckoo()
else:
    table = Chain()    


with open('records.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

cols = data[0]
del data[0]


def batchInsert():
    for entry in data:
        id = entry[0]
        curr_data = dict()
        for i in range(0, len(cols) ):
            curr_data[cols[i]] = entry[i]
        table[id] = curr_data

    return table


def rowsInsertion(rowNum):
    for entry in data [0:rowNum]:
        id = entry[0]
        curr_data = dict()
        for i in range(0, len(cols) ):
            curr_data[cols[i]] = entry[i]
        table[id] = curr_data


def batchDeletion():
    for key in table.keys():
        table.pop(key)