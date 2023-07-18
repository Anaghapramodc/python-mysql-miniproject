"""
0 b
1 a
2 n
3 a
4 n
5 a
"""
fruite="banana"
for i in range(len(fruite)):
    print(i,fruite[i])
print("\n")
fruite = "banana"
i=0
while i<len(fruite):
    n=fruite[i]
    print(i,n)
    i+=1
print("\n")
for i in enumerate(fruite):#enumerate() is used to print the index
    print(i)                        #value and string value
