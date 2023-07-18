"""
*
* * * *
*
*
* * * * * * * *
*
*
*
* * * * * * * * * * * *
"""
row=int(input("enter the range"))
for i in range(1,row+1):
    for s1 in range(i):
        print("*")
    for s2 in range(4*i):
        print("* ",end="")
    print()
