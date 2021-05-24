from cuckoo import Cuckoo
import random


#Batch insert and retrieval tests 
def data_insert(size):
    sample_keys = ['key'+str(x**2) for x in range(size)]

    sample_data = dict()

    for key in sample_keys:
        sample_data[key] = key + str(random.randint(0,size))

    table = Cuckoo(sample_data)

    original_data = []
    hash_table_data = []

    test_keys = [sample_keys[random.randint(0,size-1)] for x in range(0,size)]

    for key in test_keys:
        original_data.append(sample_data[key])
        hash_table_data.append(table[key])


    return hash_table_data == original_data

#Random inserts and retrieval tests 
def random_inserts(size):
    
    sample_keys = ['key'+str(x**2) for x in range(size)]

    sample_data = dict()

    for key in sample_keys:
        sample_data[key] = key + str(random.randint(0,size))

    table = Cuckoo()

    original_data = []
    hash_table_data = []

    test_table = dict()
    test_keys = [sample_keys[random.randint(0,size-1)] for x in range(0,size)]
    

    for key in test_keys:
        table[key] = sample_data[key]
        test_table[key] = sample_data[key]


    for key in test_keys:
        if test_table[key] != table[key]:
            return False

    return True

from cuckoo import *
from chain import *
import csv

def checkCuckoo():
    employees1 = dict()
    employees2 = Chain()
    employees3 = Cuckoo()

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

    return (lst1 == lst2 == lst3)










def test_data_insert():
    assert data_insert(1000)


def test_data_insert_large():
    assert data_insert(100000)

def test_random_inserts():
    assert random_inserts(100)

def test_random_inserts_large():
    assert random_inserts(100000)

# def test_check_Cuckoo():
#     assert checkCuckoo()


#Daredevil tests - If you decide to go on a self destructive quest to prove that my code doesn't work
# def test_random_inserts_large():
#     assert random_inserts(1000000)


# def test_data_insert_large():
#     assert data_insert(1000000)
