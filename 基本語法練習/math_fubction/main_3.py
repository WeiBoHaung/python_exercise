import  math
def point(r,angle=0):#可以在此給定初始值
    x=r*angle*math.cos(angle*math.pi/180)
    y=r*angle*math.sin(angle*math.pi/180)
    return x,y #如果回傳兩個以上會用tuple型態回傳
if __name__ == '__main__':
    print('pi=%f' % math.pi)
    print(point(2,60))
    x=point(10,45)
    print(x[0],x[1])