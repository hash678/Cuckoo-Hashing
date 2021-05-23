from cuckoo import Cuckoo
import random


def test_data_insert():
    
    sample_keys = ['key'+str(x**2) for x in range(100)]

    sample_data = dict()

    for key in sample_keys:
        sample_data[key] = key + "-value"

    table = Cuckoo(sample_data)

    original_data = []
    hash_table_data = []

    test_keys = [sample_keys[random.randint(0,99)] for x in range(0,100)]
    # print(test_keys)

    for key in test_keys:
        original_data.append(sample_data[key])
        hash_table_data.append(table[key])


    print("TABLE DATA ")
    table.dump_data()
           
    assert hash_table_data == original_data



# def test_data_insert_len():
#     sample_data = [x**2 for x in range(100)]
#     table = Cuckoo(sample_data)
#     assert len(table) == len(sample_data)
