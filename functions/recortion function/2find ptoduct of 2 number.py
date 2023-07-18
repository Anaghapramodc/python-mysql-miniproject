def product(x,y):
    if y==0:
        return 0
    else:
        return x+product(x,y-1)
x=int(input("enter the number:"))
y=int(input("enter the number:"))
print(f"{x}*{y}={product(x,y)}")
