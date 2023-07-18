#sum of n natural number
def sum(r):
    sum=0
    for i in range(1,r+1):
        sum=sum+i
    print(f"sum of {r} natural numbers={sum}")
    return sum
r = int(input("enter the range"))
sum(r)


def sum(r):
    sum=0
    for i in range(1,r+1):
        sum=sum+i
    return sum
r = int(input("enter the range"))
print(sum(r))