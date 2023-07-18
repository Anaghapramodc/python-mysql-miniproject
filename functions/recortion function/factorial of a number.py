def fact(n):
    print("n=",n,end=" ")
    if n==1:
        print("n=", n)
        print("x=",1)
        return 1
    else:
        x=n*fact(n-1)
        print("n=",n)
        print("x=",x)
    return x
print(fact(5))
"""
n=1
x=1#this is the value of fact(1)
fact(1)=1
n=2
x=2*fact(2-1)
x=2*fact(1)
x=2*1=2=fact(2)#this is the value of fact(2)
n=3
x=3*fact(3-1)
x=3*fact(2)
x=3*2=6=fact(3)#this is the value of fact(3)
n=4
x=4*fact(4-1)
x=4*fact(3)
x=4*6=24=fact(4)#this is the value of fact(4)
n=5
x=5*fact(5-1)
x=5*fact(4)
x=5*24=120=fact(5)#this is the value of fact(5)
return x






"""