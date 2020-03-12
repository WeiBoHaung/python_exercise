def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
if __name__ == '__main__':
    x=f(5)
    print('x=%d' % x)
'''f(5)
n=5
return 5*f(4)
'''
'''f(4)
n=4
return 4*f(3)
'''
'''f(3)
n=3
return 3*f(2)
'''
'''f(2)
n=2
return 2*f(1)
'''
'''f(1)
n=1
return 1
'''
