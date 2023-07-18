#Write a Python program to get the Fibonacci series between 0 to 50.
n1=0
n2=1
n=0
print(n1)
print(n2)
for i in range(0,51):
    n=n1+n2
    if n<=50:
       print(n)
    n1 = n2
    n2=n
