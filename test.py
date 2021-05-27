import sys
import random


import sys
sys.path.insert(1, './cuckoo')


# import hash tables
from cuckoo import *

#Batch insert and retrieval tests 
def data_insert(size):
    sample_keys = [str(x**2) for x in range(size)]

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
    
    sample_keys = [str(x**2) for x in range(size)]

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


def test_data_insert():
    assert data_insert(1000)


def test_data_insert_large():
    assert data_insert(10000)



def test_random_inserts():
    assert random_inserts(100)

def test_random_inserts_large():
    assert random_inserts(10000)



#Daredevil tests - If you decide to go on a self destructive quest to prove that my code doesn't work
# def test_random_inserts_large():
#     assert random_inserts(1000000)


# def test_data_insert_large():
#     assert data_insert(1000000)

