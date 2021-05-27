import matplotlib.pyplot as plt
import math

def plot(x,y):
    plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
            marker='o', markerfacecolor='blue', markersize=12)
            
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    
   
    plt.title('Analysis')
    
    # function to show the plot
    plt.show()

