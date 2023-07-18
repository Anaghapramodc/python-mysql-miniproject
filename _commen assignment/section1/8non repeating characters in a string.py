s1=list(input("enter the string"))
s1.remove(" ")
for i in s1:
    c=s1.count(i)
    if c==1:
        print(i)
