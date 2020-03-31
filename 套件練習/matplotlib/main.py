import pylab as plt
import numpy as np
import random

if __name__ == '__main__':
    x=np.linspace(0,10,10)
    y=2*x+3
    plt.figure(figsize=(6,6))
    plt.xlim(0,15)
    plt.xlim(0,20)
    plt.plot(x,y)
    plt.show()
