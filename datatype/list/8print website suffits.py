#["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
#Write a python program to print website suffixes (com , org , net ,in) from this list.

list=["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
l=[]
l2=[]
s=""
for i in list:
    x=i[::-1]
    # print(x)
    for j in x:
        if j==".":
            break
        else:
            l.insert(0,j)
    b=s.join(l)
    b="."+b
    l=[]
    # print(b)
    l2.append(b)
print(l2)


# list=["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
# l3=[]
# for i in list:
#     x=i.find(".",4)
#     # print(i[x:])
#     b=i[x:]
#     l3.append(b)
# print(l3)
#
