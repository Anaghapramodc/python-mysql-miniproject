def revers(s):
    for i in range(len(s)-1,-1,-1):
        y= ""+s[i]
        print(y,end="")
        return  revers(s[:-1])
y=""
s=str(input("enter the string:"))
revers(s)

