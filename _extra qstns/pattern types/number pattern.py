#1/2 + 2/3 +3/4 + 4/5 +5/6......
n=int(input("enter the range"))
s=0
for i in range(1,n+1):
    for j in range(i+1,i,-1):
        s=s+(i/j)

x= "{:.2f}".format(s)
print(x)
