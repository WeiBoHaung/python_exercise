import random

import numpy as np

if __name__ == '__main__':
    c=np.zeros([3,5])
    for i in range(len(c)):
        for j in range(len(c[i])):
            c[i][j]=random.randint(0,100)
            print(i)
            print(j)
            print("%d" %c[i,j])