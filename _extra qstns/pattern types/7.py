row=int(input("enter the range"))
for i in range(1,row+1):
    for s1 in range(5*i):
        print("* ",end="")
    print()
    for s2 in range(3*i):
        if i==3:
            break
        print("*")