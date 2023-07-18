c=str(input("enter the sentence"))
l=0
d=0
for i in c:

    if i.isalpha():
        l=l+1
    if i.isdigit():
        d=d+1
print("letters=",l)
print("digits=",d)