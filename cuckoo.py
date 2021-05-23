import enum

class Table(enum.Enum):
    Table_A = 1
    Table_B = 2

class Cuckoo:
    max_size = 0
    current_size = 0
    selected_table:Table = Table.Table_A
    
    max_iterations = 10
    resize_multiplier = 3

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
    



    def push(self,item, count = 0) -> bool:


        #We have reached maximum number of iterations of insert.
        #At this point too many birds have died in our endless desire of inserting things
        #Time to rehash and evaluate if it is really worth killing cute little birds
        if count == max_iterations:
            self.re_hash()

            #We'll still try to insert it tho. 
            return self.push(item)
            #comment above line and uncomment below one if we go into an infinite loop
            return False


        index = self.hash(1,self.selected_table)

        carry_over_value = None
        
        #insert into A if it is selected
        if self.selected_table == Table.Table_A:
            carry_over_value = self.tableA[index]
            self.tableA[index] = item
            
        
        #insert into B if it is selected
        if self.selected_table == Table.Table_B:
            carry_over_value = self.tableB[index]
            self.tableB[index] = item
        
        #There was no egg in that position in the nest, so no birdy dies today :))
        if carry_over_value == None:
            return True


        #There was a birdy in that place. Time to move him some where else
        #We are also switching the selected table
        self.selected_table = Table.Table_A if self.selected_table == Table.Table_A else Table.Table_B
        self.push(self,carry_over_value,count + 1)


    
    def re_hash(self):
        new_size = self.max_size * resize_multiplier
        
        #create new big tables to store our old data
        new_table_a = [None for x in range(new_size)]
        new_table_b = [None for x in range(new_size)]


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




    