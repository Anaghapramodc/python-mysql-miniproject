#1.Multiply all the numbers in a list using function
def multiple(num):
    m=1
    for i in num:
        m=m*i
    return m
num=[1,2,3,4,5,6,7]
print(multiple(num))
