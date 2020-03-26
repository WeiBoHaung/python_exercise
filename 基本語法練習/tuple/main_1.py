#跟list類似
#裡面的值不可變
t=("test","john","kevin")
print(t)
print(t[0])
#error   t[0]='error'

#須注意可重新指定新tuple
t=("tracy","john","kevin")
print(t[0])
#當只新建一個內容
y=()#空
z=(1)#給予1的意思
w=[10,]#一格內容的意思
print(y)
print(z)
print(w)