def add(x,y):
    sum=0
    for i in range(x,y):
        sum+=i
    return sum
if __name__ == '__main__':
    a=add(1,101)
    print(a)