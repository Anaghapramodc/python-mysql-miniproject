def myfunc(n):
    return lambda a:a*n
x=myfunc(5)
print(x(6))


def fun(n):
    return n
x=lambda a:a*fun(n)
n=int(input("enter the vaalue"))
print(x(2))

def myfunc(n):
    return lambda a:a*n
x=myfunc(5)
print(x(6))
