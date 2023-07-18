def num(n):
    def fact():
       p=1
       for i in range(1,n+1):
          p=p*i
       return p
    return fact()
n=int(input("enter the number"))
print(f"{n}! ={num(n)}")
