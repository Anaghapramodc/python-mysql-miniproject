#Write a Python function to check whether a number falls within a given range.
def check(x,y,n):
    if x<n<y:
        print(f"{n} is b/n {x} and {y}")
    else:
        print(f"{n} is not b/n {x} and {y}")
x=int(input("enter the min range:"))
y=int(input("enter the max range:"))
n=int(input("enter the number:"))
check(x,y,n)


