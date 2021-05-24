class Chain:
    def __init__(self, state=[]) -> None:
        # The table size will always be equal to 2^d
        self.d = 1
        # Initializing a 2d list
        # Every element of our table will be a list (a chain essentially)
        self.table = [[] for _ in range(len(self)) ]
        self.n = 0 #The number of data elements in the table

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
    def find(self, key):
        index = self.hashed(key) # Find the hashed index
        for element in self.table[index]: # Loop in that index
            if element == key: # yayy! Found item
                return True
        return False

    # Copy every element from temp to original table
    def resizeHelper(self, tempTable):
        for chain in self.table: # Each element of table is a chain
            for (key,value) in chain: # Each element of chain is of our interest
                index = self.hashed(key) # Get the hashed index
                tempTable[index].append((key,value)) # append the element in that index

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
    def __setitem__(self, key,value, ItemIsKeyVal = False):
        # If item is already in the table; Do nothing
        if self.find(key): 
            return 
        # If the table has more elements than the length
        # We resize the table
        if (self.n+1) > len(self):
            self.resize()

        # If item is a key-value tuple pair
        # We will hash the key which can be accessed with index = 0
        element = key

        index = self.hashed(element) # Get the hashed index
        self.table[index].append((key,value)) # append in that chain       
        self.n += 1 #Increment data elements

    def __getitem__(self, key):
        index = self.hashed(key)
        for i in self.table[index]:
            if i[0] == key:
                return (i[1])

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
            for key,value in chain: # Loop in chain
                yield (key,value) # Essentially yield every possible element from table

