def num(x,y):
    def sqr():
        s=x**y
        print(f"{x}^{y}={s}")
    return sqr()
x=int(input("enter the number"))
y=int(input("enter the sqr value"))
num(x,y)






# def num(x,y):
#     def sqr():
#         for i in range(1, y + 1):
#             s = x ** i
#             print(f"{x}^{i}= {s}")
#     return sqr()
# x=int(input("enter the number"))
# y=int(input("enter the sqr value"))
# num(x,y)
