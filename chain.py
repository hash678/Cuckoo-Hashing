
class Chain:
    def __init__(self) -> None:
        self.d = 1
        self.table = [[] for _ in range(len(self)) ]
        self.n = 0

    def __len__(self):
        return (2**self.d)

    def hashed(self, x):
        return int(x) % len(self)

    def find(self, key):
        index = self.hashed(key) # Find the hashed index
        for k,v in self.table[index]: # Loop in that index
            if k == key: # yayy! Found item
                return True
        return False

    def resizeHelper(self, tempTable):
        for chain in self.table: # Each element of table is a chain
            for (key,value) in chain: # Each element of chain is of our interest
                index = self.hashed(key) # Get the hashed index
                tempTable[index].append((key,value)) # append the element in that index

        self.table = tempTable

    def resize(self) -> None:
        self.d = 1
        while len(self) < 2*self.n:
            self.d += 1
        
        # Make a temp table of the new size  
        temp = [[] for _ in range(len(self)) ]

        # Copies values from table to temp Table
        self.resizeHelper(temp)

    def __setitem__(self, key, value):
        if self.find(key): 
            return 

        if (self.n+1) > len(self):
            self.resize()


        index = self.hashed(key) # Get the hashed index
        self.table[index].append((key,value)) # append in that chain       
        self.n += 1 #Increment data elements

    def __getitem__(self, key):
        index = self.hashed(key)
        for i in self.table[index]:
            if i[0] == key:
                return (i[1])

    def keys(self):
        lst = []
        for chain in self.table: # Loop in table (each element is chain)
            for item in chain: # Loop in chain
                lst.append (item[0]) # Essentially yield every possible element from table
        return lst

    # Removes item from the table
    def pop(self, key):
        index = self.hashed(key) # Get the hashed index
        for k,v in self.table[index]: # If item exists 
            if k == key:
                self.table[index].remove((k,v)) # Remove item from chain
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
