import enum

class Table(enum.Enum):
    Table_A = 1
    Table_B = 2

class Cuckoo:
    max_size = 0
    current_size = 0

    def __init__(self,data):
        
        #Setting max length of each has table to 3 times the initial data's size.
        self.max_size = len(data) * 3


        #Creating two hashtables
        self.tableA = [None for x in range(self.max_size)]
        self.tableB = [None for x in range(self.max_size)]

        self.batch_insert(data)


    #batch insert data from a list
    def batch_insert(self,data):
        for i in data:
            self.push(i)
    

    #insert item to index. index is optional
    def push(self,item,index = -1):

        if index == -1:
            index == self.current_size

        self.current_size += 1


    #select table to insert into
    def select_table(self,item,index,iteration):
        pass


    #TODO: Change hashing functions

    #hashing function
    #returns a key depending on the hash table selected
    def hash(self,index,table):
        if (type == Table.Table_A):
            return index*2 % self.max_size
        
        return index % self.max_size 

    #Insert item
    def insert(self,item):
        pass


    #Get size of data
    def len(self):
        return self.current_size



    