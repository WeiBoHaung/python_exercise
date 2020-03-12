
    
class forTemplate():
    def __init__(self):
        # 1
        # 2
        # 3
        # 4
        # 5
        # ---------------------------
        for i in [1,2,3,4,5]:
            print(i)
        print("---------------------------")
        # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7
        # 8
        # 9
        # 10
        # ---------------------------
        for i in range(1,11):
            print(i)
        print("---------------------------")
        # 1
        # 3
        # 5
        # 7
        # 9
        # ---------------------------
        for i in range(1,11,2):
            print(i)
        print("---------------------------")
        # 1 2 3 4 5 6 7 8 9 10
        # ---------------------------
        for i in range(1,11):
            print("%d"%i,end=" ")
        print()
        print("---------------------------")
    def printTriangel():
        # * * * * *
        # * * * *
        # * * *
        # * *
        # *
        # ---------------------------
        for i in range(1,6):
            for j in range(i,6):
                print("*",end=" ")
            print()
        print("---------------------------")
        # *
        # * *
        # * * *
        # * * * *
        # * * * * *
        # ---------------------------
        for i in range(1,6):
            for j in range(1,i+1):
                print("*",end=" ")
            print()
        print("---------------------------")
        # *
        # * *
        # * * *
        # * * * *
        # * * * * *
        # * * * *
        # * * *
        # * *
        # *
        # ---------------------------
        for i in range(1,5):
            for j in range(1,i+1):
                print("*",end=" ")
            print()
        for i in range(1,6):
            for j in range(i,6):
                print("*",end=" ")
            print()
        print("---------------------------")
    def printDiamond():
        #      *
        #     * *
        #    * * *
        #   * * * *
        #  * * * * *
        #   * * * *
        #    * * *
        #     * *
        #      *
        # ---------------------------

        for i in range(1,6):
            for k in range(6,i,-1):
                print(" ",end='')
            for j in range(1,i+1):
                print("*",end=" ")
            print()
        for i in range(5,1,-1):
            for k in range(6,i,-1):
                print("",end=' ')
            for j in range(i,1,-1):
                print(" *",end='')
            print()
        print()
        print("---------------------------")

        for i in range(1,6):
            for j in range(i,6):
                print("*",end=" ")
            for j in range(i,1,-1):
                print("  ",end="  ")
            for j in range(i,6):
                print("*",end=" ")
            print()
        for i in range(2,6):
            for j in range(1,i+1):
                print("*",end=" ")
            for j in range(i,5):
                print("  ",end="  ")
            for j in range(1,i+1):
                print("*",end=" ")
            print()
        print("---------------------------")
ans=int(input('keyin 1 or 2 or 3 : '))
if ans==1:
    forTemplate()
elif ans==2:
    forTemplate.printTriangel()
elif ans==3:
    forTemplate.printDiamond()
else:
    print('error')