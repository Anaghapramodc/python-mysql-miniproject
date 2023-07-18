"""
*
*
* * *
* *
* *
* * * * * *
* * *
* * *
* * *
* * * * * * * * *
"""

n=int(input("enter the row"))
print("*")
for i in range(1,n+1):
    for c in range(i):
        for s1 in range(i):
           print("* ",end="")
        print()
    for s2 in range(3*i):
        print("* ",end="")
    print()




