import random
import numpy as np

if __name__ == '__main__':
    b=np.zeros([10])
    sum=0
    for  i in range(len(b)):
        b[i]=random.randint(0,100)
        sum=sum+b[i]
        print("%d" % b[i])
    print("共 %d" % sum)
    print(" 平均= %f" %(sum/len(b)))