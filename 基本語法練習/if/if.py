import random

salay=random.randint(0,100000)

print("you're salay is " , salay)


if salay<=20000:
    print("you're tax is  6%")
elif  salay<=40000:
    print("you're tax is  7%")
elif salay<=60000:
    print("you're tax is  8%")
elif salay<=80000:
    print("you're tax is  9%")
elif salay>80000:
    print("you're tax is  10%")
    