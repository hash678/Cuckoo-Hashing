
    
from dataHandling import *
import time
from analysisHelper import *
import numpy as np


def RunTimebatchDeletion():
    table = batchInsert()

    start = time.time()

    batchDeletion(table)

    time.sleep(1)
    end = time.time()

    return (end - start) #time taken
 
def RunTimebatchInsertion():

    start = time.time()

    batchInsert()

    time.sleep(1)
    end = time.time()

    return (end - start) #time taken


def RunTimerowInsertion(n):
    start = time.time()

    rowsInsertion(n)

    time.sleep(1)
    end = time.time()

    return (end - start) #time taken    


def PlotRowRunTime1():
    xvalues = []
    yvalues = []
    for i in range(0, len(data), 500):
        xvalues.append(i)
        yvalues.append( RunTimerowInsertion(i) )

    plot(xvalues, yvalues)


def PlotRowRunTime2():
    xvalues = []
    yvalues = []
    for i in range(0, len(data), 32000):
        xvalues.append(i)
        yvalues.append( RunTimerowInsertion(i) )

    plot(xvalues, yvalues)
    

def experiment1():
    y = []  
    for i in range(10):
        y.append( RunTimebatchInsertion()  )

    bins = int( math.sqrt(len(y)) )
    binWidth = (max(y) - min(y) ) / bins
    plt.hist (y , bins = bins , weights = np.ones (len (y) ) /( len (y) * binWidth ),
    edgecolor='black' )
    plt.title("Time taken")
    plt.xlabel("time")
    plt.ylabel("frequency")
    plt.show ()



def experiment2():
    y = []  
    for i in range(10):
        y.append( RunTimebatchDeletion()  )

    bins = int( math.sqrt(len(y)) )
    binWidth = (max(y) - min(y) ) / bins
    plt.hist (y , bins = bins , weights = np.ones (len (y) ) /( len (y) * binWidth ),
    edgecolor='black' )
    plt.title("Time taken")
    plt.xlabel("time")
    plt.ylabel("frequency")
    plt.show ()




## Test Batch insertion
# experiment1()


## Test Batch deletion
experiment2()


## Test CSV with 2500 rows (graph of every 500 rows)
# PlotRowRunTime1()


## Test CSV file with 160,000 rows (graph of every 32000 rows)
#PlotRowRunTime2()
