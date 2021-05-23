import enum
from copy import deepcopy
from helper import *

class Table(enum.Enum):
    Table_A = 1
    Table_B = 2

class Cuckoo:
    max_size = 0
    current_size = 0
    selected_table:Table = Table.Table_A
    
    max_iterations = 10
    resize_multiplier = 2


    

    def __init__(self,data:dict = dict()):

        #initial data must only be dictionary. since python sucks does not have proper type safety. 
        if not type(data) == dict:
            raise Exception("Batch insert of dictionary allowed only. Please provide a valid dictionary")
                
        
        #Setting max length of each has table to 3 times the initial data's size.
        self.max_size = max(len(data.keys()) * 3,100)

        #Side note: out occupied indexes actually follow a pattern. 
        #At the first index of the string we have the table. The other thing is the key   
        self.occupied_indexes = []

        #Creating two hashtables
        self.tableA = [None for x in range(self.max_size)]
        self.tableB = [None for x in range(self.max_size)]

        self.insert_all(data)

        log("BATCH INSERTING: "+str(data))



    #Get size of data
    def __len__(self):
        return self.current_size


    def __setitem__(self,key,value):
        key_value_pair = (key,value)
        self.push(key_value_pair)


    def __contains__(self,key):
        index_data = self.get_item_index(key)
        return index_data != None


    def __getitem__(self,key):
        index_data = self.get_item_index(key)

        if index_data == None:
            return None
        
        index, table = index_data


        if self.tableA[index] != None and self.tableA[index][0] == key:
            return self.tableA[index][1]
        
        if self.tableB[index] != None and self.tableB[index][0] == key:
            return self.tableB[index][1]
        

    def pop(self,key):
        index_data = self.get_item_index(key)

        if index_data == None:
            return False
        
        index, table = index_data


        if self.tableA[index] != None and self.tableA[index][0] == key:
            self.tableA[index] = None
            return True
        
        if self.tableB[index] != None and self.tableB[index][0] == key:
            self.tableB[index] = None
            return True


    def keys(self):
        
        keys = []

        for index in self.occupied_indexes:
            if index[0] == str(Table.Table_A.value):
                index_table = int(index[1:]) 
                keys.append(self.tableA[index_table][0])

            if index[0] == str(Table.Table_B.value):
                index_table = int(index[1:]) 
                keys.append(self.tableB[index_table][0])

        return keys


    #batch insert data from a list
    def insert_all(self,data):
        for key in data.keys():
            self[key] = data[key]
    

    #replace value if already exists
    def replace_value(self,index:int,newValue,table:Table):
        log("REPLACING VALUE")

        if table == Table.Table_A:
            self.tableA[index] = (self.tableA[index][0],newValue)
        else:
            self.tableB[index] = (self.tableB[index][0],newValue)



       
    def insert_into_table(self,item,index:int,table:Table):

        carry_over_value = None

        if self.selected_table == Table.Table_A:
            carry_over_value = self.tableA[index]
            self.tableA[index] = item

            log("INSERTING KEY INTO :" +str(table.value)+ " "+str(item))

            self.occupied_indexes.append(str(table.value)+str(index))


        if self.selected_table == Table.Table_B:
            carry_over_value = self.tableB[index]
            self.tableB[index] = item

            log("INSERTING KEY INTO :" +str(table.value)+ " "+str(item))

            self.occupied_indexes.append(str(table.value)+str(index))


        if carry_over_value != None:    
            log("CARRY OVER VALUE: "+str(carry_over_value))
            log("REMOVED FROM NEST: "+str(table.value))

            if carry_over_value[0] == item[0]:
                self.replace_value(index,carry_over_value[1],table)
                carry_over_value = None



        return carry_over_value



    #get index 
    def get_item_index(self,key) -> (int,Table):
        index_a = self.hash(key,Table.Table_A) 
        index_b = self.hash(key,Table.Table_B) 


        if self.tableA[index_a] != None and self.tableA[index_a][0] == key:
            return(index_a,Table.Table_A)
        
        if self.tableB[index_b] != None and self.tableB[index_b][0] == key:
            return(index_b,Table.Table_B)
        
        log("NOT FOUND: "+str(key))
        return None


    def push(self,item, count = 0) -> bool:
        log("\nINSERTING ITEM: "+str(item))
        log("SELECTED TABLE "+str(self.selected_table.value))
        log("-----------------------------")


        #We have reached maximum number of iterations of insert.
        #At this point too many birds have died in our endless desire of inserting things
        #Time to rehash and evaluate if it is really worth killing cute little birds
        if count == self.max_iterations:
            self.re_hash()

            #We'll still try to insert it tho. 
            return self.push(item)
            #comment above line and uncomment below one if we go into an infinite loop
            #return False

        item_key = item[0]
        index = self.hash(item_key,self.selected_table)

        carry_over_value = None
        
        #insert into A if it is selected
        if self.selected_table == Table.Table_A:
            carry_over_value = self.insert_into_table(item,index,Table.Table_A)
            
        
        #insert into B if it is selected
        if self.selected_table == Table.Table_B:
            carry_over_value = self.insert_into_table(item,index,Table.Table_B)
        
        #There was no egg in that position in the nest, so no birdy dies today :))
        if carry_over_value == None:
            return True


        #There was a birdy in that place. Time to move him some where else
        #We are also switching the selected table
        self.selected_table = Table.Table_B if self.selected_table == Table.Table_A else Table.Table_A
        self.push(carry_over_value,count + 1)


    def clear(self):
        #create new big tables to store our old data
        self.tableA = [None for x in range(self.max_size)]
        self.tableB = [None for x in range(self.max_size)]

        self.current_size = 0
        self.selected_table = Table.Table_A
        self.occupied_indexes = []

    
    def re_hash(self):
        
        #make a copy of our current data
        copy_self = deepcopy(self)

        self.max_size = self.max_size * self.resize_multiplier
        self.clear()


        self.insert_all(copy_self)



    #bounding function. can be changed to optimize code.
    def bound_value(self,value,bound):
        return int(value % bound)



    #hashing function
    #returns a key depending on the hash table selected
    def hash(self,key,table:Table):
        
        hash_value = hash(key)


        if (table == Table.Table_A):
            return self.bound_value(hash_value/11,self.max_size) 
        
        return self.bound_value(hash_value,self.max_size)



    def dump_data(self):
        log("TABLE A: "+str(self.tableA))
        log("TABLE B: "+str(self.tableB))

