'''
1. 產生10個元素陣列
2. 放入隨機亂數
3. 印出來觀看
4. 氣泡排序
'''
import random
import numpy as np

temp=""
n=100
'''numpy'''
x_numpy=np.zeros([n])
for i in range(n):
    x_numpy[i]=random.randint(-100,100)
    print('%d' % x_numpy[i],end=',')
print()
for i in range(n):
    for j in range(i,n):
        if x_numpy[i] > x_numpy[j]:
            temp=x_numpy[i]
            x_numpy[i]=x_numpy[j]
            x_numpy[j]=temp
for i in range(n):
    print('%d' % x_numpy[i],end=',')
print()

'''list'''
x=[]
for i in range(n):
    x.append(random.randint(-100,100))
print(x)
for i in range(n):
    for j in range(i,n):
        if x[i]>x[j]:
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
print(x)
