from chain import *

table = Chain()

table[3] = 'habib'
table[5] = 'hello'

table.discard(5)

for i in table:
    print(i)
