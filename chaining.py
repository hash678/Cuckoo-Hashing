# Implements the USet interface using hashing
# uses chaining for conflict/collision resolution
# We can make a two dimensional list
# A list In which every element is a chain
# Lets say table = [nill,nill,nill]
# (5,2) --> hash --> 2 --> [nill,nill,(5,2)]
# Now suppose (5,3) also wants to go to 2nd index; we have a collision
# To resolve this we just append (5,3) in the 2nd index
# And for that to happen every element of the table is a chain (another list)

class ChainedSet:
    def __init__(self, state=[]) -> None:
        # The table size will always be equal to 2^d
        self.d = 1
        # Initializing a 2d list
        # Every element of our table will be a list (a chain essentially)
        self.table = [[] for _ in range(len(self)) ]
        
        self.n = 0 # The number of daya elements in the table
        [ self.add(item) for item in state]
    
    # Returns the length of table
    # We make sure that length is always equal to 2^d
    def __len__(self):
        return (2**self.d)

    # Returns a hashed value
    # Modulus operator ensures that returned value 
    # is a valid index of the table
    def hashed(self, x):
        return hash(x) % len(self)

    # Does item exist in the table?
    def find(self, item):
        index = self.hashed(item) # Find the hashed index
        for element in self.table[index]: # Loop in that index
            if element == item: # yayy! Found item
                return True
        return False

    # Copy every element from temp to original table
    def resizeHelper(self, tempTable):
        for chain in self.table: # Each element of table is a chain
            for item in chain: # Each element of chain is of our interest
                index = self.hashed(item) # Get the hashed index
                tempTable[index].append(item) # append the element in that index

        #We copied all items from table to tempTable
        #TempTable is just a resized table
        self.table = tempTable

    # Resizes the table
    # i.e. length(table) should always be greater than 2*n 
    # Where n is the data elements
    # We can say that the size doubles or halves
    def resize(self) -> None:
        self.d = 1
        while len(self) < 2*self.n:
            # Incrementing d untill the length of table is greater than 2*n
            self.d += 1
        
        # Make a temp table of the new size  
        temp = [[] for _ in range(len(self)) ]

        # Copies values from table to temp Table
        # table is set equal to temp table
        self.resizeHelper(temp)

    # Adds the item to the table
    def add(self, item, ItemIsKeyVal = False):
        # If item is already in the table; Do nothing
        if self.find(item): 
            return 
        # If the table has more elements than the length
        # We resize the table
        if (self.n+1) > len(self):
            self.resize()

        # If item is a key-value tuple pair
        # We will hash the key which can be accessed with index = 0
        element = item
        if ItemIsKeyVal: element = item[0]

        index = self.hashed(element) # Get the hashed index
        self.table[index].append(item) # append in that chain       
        self.n += 1 #Increment data elements

    # Removes item from the table
    def discard(self, item):
        index = self.hashed(item) # Get the hashed index
        if item in self.table[index]: # If item exists 
            self.table[index].remove(item) # Remove item from chain
            # If number of daya elements *3 is less than length we resize 
            if 3 * self.n < len(self): 
                self.resize()
            self.n -= 1 # Decrement 

    # Allows us to perform iteration on class object
    # If we perform iteration through for loop on class
    # The following function will be used to yield each iteration
    def __iter__(self):
        for chain in self.table: # Loop in table (each element is chain)
            for item in chain: # Loop in chain
                yield item # Essentially yield every possible element from table


# Implements the USet interface as an associative container 
# uses chaining for conflict/collision resolution
# Since the operations are similar; ChainedDict can be a child class
# To chainedSet
    # Uses the same methods of parent class; But Only Slightly different
    # in this class we hash keys from the key-value pair
    # In the parent class we did not have a key-value pair but only one value element
class ChainedDict(ChainedSet):
    # Uses the parent class to initialize the chainedDict
    # kind of makes the table as a 2d list  
    def __init__(self): 
        super().__init__()

    # Get the value assosiated with the key
    # If key does not exist; return the arguement passed 'NotFound'
    def get(self, key, notFound):
        index = super().hashed(key) # Get the hashed index
        for item in self.table[index]: # Look in that index
            if item[0] == key: # yayyy! we found the key
                return item[1] # get the value
        return notFound # Oh nooo! key was not found :(        

    # Does key exist in the table?        
    def find(self, key):
        return self.get(key, False) is not False

    # Copy value from table to temp table
    # And then setting table equal to temp table
    def resizeHelper(self, tempTable):
        for chain in self.table: # Loop in table
            for item in chain: # Loop in chain
                index = self.hashed(item[0]) # add in the hashed index
                tempTable[index].append(item)
        # The temp table is now our new resized table
        self.table = tempTable


    # If key exists: update the value of that key
    # If key does not exist: add (key, value) pair to the table
    def __setitem__(self, key, value): 
        if self.find(key): # Find key
            index = super().hashed(key) # Get the hashed index
            i = 0 # A counter
            for item in self.table[index]: # Look in the hashed index
                if item[0] == key: # yayyy! found it
                    break # stop looking please
                i+=1 # Incrememnt the counter
                # update the key-value pair in the hashed index
                # and the counter
            self.table[index][i] = (key, value)
        else:
            # Uses parent class's method to add item to table
            # This time the item is a key-value pair so we use this arguement  
            super().add((key, value), ItemIsKeyVal=True) 

    # Re-initialize the table
    # Since Every value has to be set to default
    # We can use the init function
    def clear(self):
        super().__init__()

    # Get all possible items from table
    def items(self):
        lst = []
        for chain in self.table: # Loop in table
            for item in chain: # Loop in chain
                lst.append((item[0], item[1])) # key-value pair appended to lst
        return lst # A list containing all key-value pairs
