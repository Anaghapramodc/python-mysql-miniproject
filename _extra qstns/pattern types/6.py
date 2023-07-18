row=int(input("enter the range"))
for i in range(row):
    for s1 in range(2*i,2*row):
        print("* ",end="")
    print()
    for s2 in range(i+1):
        print("*")