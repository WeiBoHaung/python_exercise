import  numpy as np
import random
def getData(d):
    for i in range(len(d)):
        d[i]=random.randint(0,99)
def printData(d):
    print(d)
def sort(d):
    for i in range(len(d)-1):
        for j in range(i+1,len(d)):
            if d[i]>d[j]:
                temp=d[i]
                d[i]=d[j]
                d[j]=temp

if __name__ == '__main__':
    n=10
    d=np.zeros([n])
    getData(d)
    printData(d)
    sort(d)
    printData(d)
