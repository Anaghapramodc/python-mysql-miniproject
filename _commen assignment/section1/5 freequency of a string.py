s1=str(input("enter the string"))
s2=set(s1)
if " " in s2:
    x=s2.remove(" ")
for i in s1:
    if i in s2:
       c=s1.count(i)
       print(f"{i}={c}")
       y=s2.remove(i)
