set1={"apple","orange","pineapple","MANGO","KEWI"}
set2={"a","e","i","o","u","A","E","I","O","U"}
c=0
for i in set1:
    for j in i:
        if j in set2:
            c=c+1

print("number of vavales present in the string=",c)