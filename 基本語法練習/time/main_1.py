import  time
t1=time.time()
for i in range(1000000):
    print("i =%d"% i)

t2=time.time()
print("t2-t1=%f" % (t2-t1))
