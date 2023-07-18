#[1,2,4,3]
#o/p=[1,2,3,4]
s= t=[2,4,1,3]
s1=""
for i in range(len(s)):
    print("i=",i)
    for j in s:
        if s[i]>j:
            s1=s1+str(j)
            print(s1)
            t.remove(j)
            break
