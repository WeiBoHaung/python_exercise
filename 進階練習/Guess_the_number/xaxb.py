import random
min=int(input('input min number : '))
max=int(input('input min number : '))
ans=random.randint(min,max)
print(ans)
while 1:
    test=int(input("input you'r answer : "))
    if ans==test:
        print("bingo")
        break
    elif test>ans:
        print("answer < testNumber")
    elif test<ans:
        print("answer > testNumber")
