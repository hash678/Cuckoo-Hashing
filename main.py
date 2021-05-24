from cuckoo import *
from chain import *

employees1 = dict()
employees2 = Chain()
employees3 = Cuckoo()


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
    employees3[id] = employee_data
    lst.append(id)


lst1 = [] #dict
lst2 = [] #chain
lst3 = [] #cuckoo


for id in employees1.keys():
    lst1.append(employees1[id]['ID'])


for id in employees2.keys():
    lst2.append(employees2[id]['ID'])

for id in employees2.keys():
    lst3.append(employees2[id]['ID'])


lst = sorted(lst)                 
lst1 = sorted(employees1.keys())  
lst2 = sorted(employees2.keys())  
lst3 = sorted(employees2.keys()) 

print(lst1 == lst2 == lst3)



