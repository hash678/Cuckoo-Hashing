from cuckoo import *
from chain import *

employees1 = Cuckoo()
employees2 = dict()

import csv
with open('records.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

cols = data[0]
del data[0]

lst = []

for entry in data:
    id = entry[0]
    employee_data = {}
    for i in range(0, len(cols) ):
        employee_data[cols[i]] = entry[i]

    employees1[id] = employee_data
    employees2[id] = employee_data

    lst.append(id)

lst1 = []
lst2 = []


#cuckoo
for id in employees1.keys():
    lst1.append(employees1[id]['ID'])

#chain
for id in employees2.keys():
    lst2.append(employees2[id]['ID'])


# lst = sorted(lst)    #original ids
lst1 = sorted(employees1.keys())  #cuckoo hashed
lst2 = sorted(employees2.keys())  #chain hashed

print(lst1==lst2)
#print(lst2)
