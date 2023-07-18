i=10
t=2
print("prime numbers are")
while i<=100:
    while t<i:
        if i%t==0:
            break
        t+=1
    else:
        print(i)
    t=2
    i+=1