from cuckoo import Cuckoo

def test_data_insert_small():
    sample_data = [x**2 for x in range(100)]
    table = Cuckoo(sample_data)
    assert table.len() != len(sample_data) 