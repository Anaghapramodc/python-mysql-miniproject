i=100
c=0
while i<=400:
    s=str(i)
    for j in s:
        if int(j)%2==0:
            c=c+1
    if c==3:
        print(",",i,end="")
    c=0
    i+=1