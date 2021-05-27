
    
from dataHandling import *
import time
from analysisHelper import *
import numpy as np


def RunTimebatchDeletion():
    batchInsert()

    start = time.time()

    batchDeletion()

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


def PlotRowRunTime():
    xvalues = []
    yvalues = []
    for i in range(0, len(data), 500):
        xvalues.append(i)
        yvalues.append( RunTimerowInsertion(i) )

    plot(xvalues, yvalues)

    

def experiment():
    y = []  
    for i in range(10):
        y.append( RunTimebatchInsertion()  )

    bins = int( math.sqrt(len(y)) )
    binWidth = (max(y) - min(y) ) / bins
    plt.hist (y , bins = bins , weights = np.ones (len (y) ) /( len (y) * binWidth ),
    edgecolor='black' )
    plt.title("Time taken")
    plt.xlabel("")
    plt.ylabel("frequency")
    plt.show ()


PlotRowRunTime()

