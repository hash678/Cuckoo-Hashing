from chaining import *
from cuckoo import *

cuckoo = False

if cuckoo:
    employees = Cuckoo()
else:
    employees = ChainedDict()


import csv

with open('records.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

cols = data[0]
del data[0]

for entry in data:
    id = entry[0]
    employee_data = {}
    for i in range(1, len(cols) ):
        employee_data[cols[i]] = entry[i]
    employees[id] = employee_data


# print("""Add new employeee: Press 'A' 
# Delete a employee: Enter 'D'
# Lookup for a employee: Enter 'S'""")

# x = input()







