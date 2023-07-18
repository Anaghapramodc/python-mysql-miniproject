s1=str(input("enter the 1st string"))
s2=str(input("enter the 1st string"))
l1=list(s1)
l2=list(s2)
c=0
if len(l1)==len(l2):
    for i in l1:
        for j in l2:
            if i==j:
                c=c+1
    if c==len(l1):
        print(f"{s1} and {s2} are anagram ")
else:
    print(f"{s1} and {s2} are not anagram ")
