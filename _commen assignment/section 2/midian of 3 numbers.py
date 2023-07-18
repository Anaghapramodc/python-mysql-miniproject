n1=[]
for i in range(3):
    n=int(input("enter the number"))
    n1.append(n)
print(n1)
n1.sort(reverse=False)
print(n1)
print("midean of the number",n1[1])