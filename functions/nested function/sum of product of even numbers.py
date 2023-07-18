def even(x,y):
    l=[]
    for i in range(x,y+1,2):
        l.append(i)
    def sum():
        c=0
        for i in l:
            c=c+i
        return c
    return sum()
x=int(input("enter the number:"))
y=int(input("enter the number:"))
print(f"sum of even numbers b/n {x} and {y} = {even(x,y)}")



