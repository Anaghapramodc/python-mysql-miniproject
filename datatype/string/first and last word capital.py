s=str(input("enter the string"))
for char in s.split(" "):
    l=len(char)
    x1=char[0].upper()
    x2=char[1:l-1].lower()
    x3 = char[l - 1].upper()
    if l==1:
        print(x1,end=" ")
    else:
        x=x1+x2+x3
        print(x,end=" ")