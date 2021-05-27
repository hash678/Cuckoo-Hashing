import time
from dataHandling import *
from analysisHelper import *

def RunTimebatchDeletion(isCuckoo):
    definer(isCuckoo)
    batchInsert()

    start = time.time()

    batchDeletion()

    time.sleep(1)
    end = time.time()

    return (end - start) #time taken
 
def RunTimebatchInsertion(isCuckoo):
    definer(isCuckoo)

    start = time.time()

    batchInsert()

    time.sleep(1)
    end = time.time()

    return (end - start) #time taken


def RunTimerowInsertion(isCuckoo):
    definer(isCuckoo)
    data = batchList()

    xvalues = []
    yvalues = []
    for i in range(0, len(data), 1000):
        xvalues.append(i)
        yvalues.append( rowsInsertion(i) )

    plot(xvalues, yvalues)


    

def experiment():
    y = []  
    for i in range(100):
        y.append( batchInsert()  )

    bins = int( math.sqrt(len(y)) )
    binWidth = (max(y) - min(y) ) / bins
    plt.hist (y , bins = bins , weights = np.ones (len (y) ) /( len (y) * binWidth ),
    edgecolor='black' )
    plt.title("Number of times hypothesis is rejected")
    plt.xlabel("The proportion of rejection count")
    plt.ylabel("frequency")
    plt.show ()