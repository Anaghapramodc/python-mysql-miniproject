#4. Write a Python function that takes a number as a parameter and check  the number is prime or not
def check(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c=c+1
    if c==1:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
n=int(input("enter the number"))
check(n)