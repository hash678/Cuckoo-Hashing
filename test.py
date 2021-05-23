from cuckoo import Cuckoo
import random


def test_data_insert():
    
    sample_keys = ['key'+str(x**2) for x in range(100)]

    sample_data = dict()

    for key in sample_keys:
        sample_data[key] = key + str(random.randint(0,100))

    table = Cuckoo(sample_data)

    original_data = []
    hash_table_data = []

    test_keys = [sample_keys[random.randint(0,99)] for x in range(0,100)]

    for key in test_keys:
        original_data.append(sample_data[key])
        hash_table_data.append(table[key])


           
    assert hash_table_data == original_data


def test_data_insert_large():
    size = 100000

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


    assert hash_table_data == original_data


##VERY LARGE DATA SET. RUN AT YOUR OWN EXPENSE.
# def test_data_insert_very_large():
#     size = 1000000

#     sample_keys = ['key'+str(x**2) for x in range(size)]

#     sample_data = dict()

#     for key in sample_keys:
#         sample_data[key] = key + "-value"

#     table = Cuckoo(sample_data)

#     original_data = []
#     hash_table_data = []

#     test_keys = [sample_keys[random.randint(0,size-1)] for x in range(0,size)]

#     for key in test_keys:
#         original_data.append(sample_data[key])
#         hash_table_data.append(table[key])


#     assert hash_table_data == original_data

