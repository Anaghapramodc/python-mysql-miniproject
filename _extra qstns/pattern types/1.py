"""
* *
*
*
*
* * * *
*
*
*
*
*
*
* * * * * *

"""
n=int(input("enter the row"))
for i in range(1,n+1):
    for s1 in range(0,2*i):
        print("* ",end="")
    print()
    for j in range(i):
        for s2 in range(0,3):
            if i==3:
                continue
            print("*")

