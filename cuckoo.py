import enum

class Table(enum.Enum):
    Table_A = 1
    Table_B = 2

class Cuckoo:
    max_size = 0
    current_size = 0
    # selected_table:Table = Table.Table_A

    def __init__(self,data:dict = dict()):

        #initial data must only be dictionary. since python sucks does not have proper type safety. 
        if not type(data) == dict:
            raise Exception("Batch insert of dictionary allowed only. Please provide a valid dictionary")
                
        
        #Setting max length of each has table to 3 times the initial data's size.
        self.max_size = len(data.keys()) * 3


        #Creating two hashtables
        self.tableA = [None for x in range(self.max_size)]
        self.tableB = [None for x in range(self.max_size)]

        self.insert_all(data)



    #Get size of data
    def __len__(self):
        return self.current_size


    def __setitem__(self,key,value):
        key_value_pair = (key,value)
        self.push(key_value_pair)



    #get value at index
    def __getitem__(self,index:int,table):
        assert index < self.max_size
        return self.tableA[index] if table == Table.Table_A else self.tableB[index]



    #batch insert data from a list
    def insert_all(self,data):
        for key in data.keys():
            self[key] = data[key]
    

    def push(self,item) -> bool:
        index_a = self.hash(1,Table.Table_A)
        index_b = self.hash(1,Table.Table_B)

        if self.tableA[index_a] == None:








    #TODO: Change hashing functions

    #hashing function
    #returns a key depending on the hash table selected
    def hash(self,item,table:Table):
        if (type == Table.Table_A):
            return item*2 % self.max_size
        
        return item % self.max_size 

    # #Insert item
    # def insert(self,item):
    #     pass




    