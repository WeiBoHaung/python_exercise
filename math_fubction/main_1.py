from decimal import  Decimal
if __name__ == '__main__':
    g=pow(2,10)#次方
    print("g=%f" % g)
    h=round(1.115,2)#四捨五入
    print("h=%f" % h)
    #提高精準度
    a=Decimal("1.115")
    print(round(a,2))


