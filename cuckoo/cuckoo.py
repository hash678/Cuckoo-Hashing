import enum
from copy import deepcopy
from helper import *
import pickle

import os
import sys
hashseed = os.getenv('PYTHONHASHSEED')
if not hashseed or hashseed is None:
    os.environ['PYTHONHASHSEED'] = '0'
    os.execv(sys.executable, [sys.executable] + sys.argv)


# class Table(enum.Enum):
#     Table_A = 1
#     Table_B = 2

class Cuckoo:
    max_size = 0
    current_size = 0
    selected_table = 0
    
    max_iterations = 6
    resize_multiplier = 12

    

    total_tables = 2
    tables = [[] for i in range(total_tables)]
    

    def __init__(self,data:dict = dict()):

        #initial data must only be dictionary. since python sucks does not have proper type safety. 
        if not type(data) == dict:
            raise Exception("Batch insert of dictionary allowed only. Please provide a valid dictionary")
                
        
        #Setting max length of each has table to 3 times the initial data's size.
        self.max_size = max(len(data.keys()) * self.resize_multiplier,50)

        #Side note: out occupied indexes actually follow a pattern. 
        #At the first index of the string we have the table. The other thing is the key   
       # self.occupied_indexes = []

        #Creating two hashtables

        self.tables = [[None for x in range(self.max_size)] for i in range(self.total_tables)]
        self.insert_all(data)

        # log("BATCH INSERTING: "+str(data))



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

        if self.tables[table][index] != None and self.tables[table][index][0] == key:
            return self.tables[table][index][1]

  
        

    def pop(self,key):
        index_data = self.get_item_index(key)

        if index_data == None:
            return False
        
        index, table = index_data


        if self.tables[table][index] != None and self.tables[table][index][0] == key:
            self.tables[table][index] = None
           # self.occupied_indexes.pop( self.occupied_indexes.index(str(table.value)+str(index)))
            return True
 


    def keys(self):
        
        keys = []


        for table in self.tables:
            for index in table:
                if index != None:
                    keys.append(index[0])


        return keys


    #batch insert data from a list
    def insert_all(self,data):
        for key in data.keys():
            self[key] = data[key]
    

    #replace value if already exists
    def replace_value(self,index:int,newValue,tableIndex:int):
        # log("REPLACING VALUE")

        self.tables[tableIndex][index] = (self.tables[tableIndex][index][0],newValue)
        # else:
        #     self.tableB[index] = (self.tableB[index][0],newValue)

        # self.occupied_indexes.pop(str(table.value)+str(index))



       
    def insert_into_table(self,item,index:int,tableIndex:int):


        carry_over_value = self.tables[tableIndex][index]
        self.tables[tableIndex][index] = item

        if carry_over_value != None:    
            if carry_over_value[0] == item[0]:
                self.replace_value(index,carry_over_value[1],tableIndex)
                carry_over_value = None



        return carry_over_value



    #get index 
    def get_item_index(self,key) -> tuple:

        indexes = []
        for i in range(self.total_tables):
            indexes.append(self.hash(key,i))

        for index in range(len(indexes)):
            tableIndex = indexes[index]

            if self.tables[index][tableIndex] != None and self.tables[index][tableIndex][0] == key:
                return(tableIndex,index)
    

        return None


    def push(self,item, count = 0) -> bool:
        # print("\nINSERTING ITEM: "+str(item))
   

        itemIndex = self.get_item_index(item[0])
        if itemIndex != None:
            self.replace_value(itemIndex[0],item[1],itemIndex[1])



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
        

        #insert into B if it is selected
        
        carry_over_value = self.insert_into_table(item,index,self.selected_table)
        
        #There was no egg in that position in the nest, so no birdy dies today :))
        if carry_over_value == None:
            return True


        #There was a birdy in that place. Time to move him some where else
        #We are also switching the selected table
        self.selected_table = ((self.selected_table + 1)) % self.total_tables
        self.push(carry_over_value,count + 1)


    def clear(self):
        #create new big tables to store our old data
        self.tables = [[None for x in range(self.max_size)] for i in range(self.total_tables)]

        self.current_size = 0
        self.selected_table = 0
       # self.occupied_indexes = []

    
    def re_hash(self):
        # print("\nREHASHING: ")

        #make a copy of our current data
        copy_self = pickle.loads(pickle.dumps(self))
        

        self.max_size = self.max_size * self.resize_multiplier
        self.clear()


        self.insert_all(copy_self)



    #bounding function. can be changed to optimize code.
    def bound_value(self,value,bound):
        return int(value % bound)


    #hashing function
    #returns a key depending on the hash table selected
    def hash(self,key,table:int):
        hash_value = int(key)        
        return self.bound_value(hash_value+table,self.max_size) 
        



    def dump_data(self):
        for table in self.tables:
            log("TABLE : "+str(table))
  


    

