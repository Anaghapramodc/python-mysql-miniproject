s=set(input("enter the string"))
s1=s.remove(" ")
print(s)
v={"a","e","i","o","u","A","E","I","O","U"}
vavls=[]
cnst=[]
for i in s:
    if i in v:
        x=vavls.append(i)
    else:
       y=cnst.append(i)
print("vavels inside the string",vavls)
print("constand inside the string",cnst)
