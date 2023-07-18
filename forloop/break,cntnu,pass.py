"""
break--->to break the contition

continue--->to continue the statement


pass--->used to print blank o/p




"""




# for i in range(1,11):
#     print(i)
#     if i==5:
#         print(i)
#         break
#     print(i)
#
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)
#
# for i in range(1,11):
#     if i==5:
#         pass

# fruits=["apple","orange","banana","kiwi"]
# for x in fruits:
#     print(x)
#     if x=="banana":
#         break

# fruits=["apple","orange","banana","kiwi"]
# for x in fruits:
#     if x=="banana":
#         break
# print(x)

fruits=["apple","orange","banana","kiwi","strawberry",1,2,3,4,5,6,7,8]
for x in fruits:
    if x=="orange":
       continue
    if x=="kiwi":
       continue
    if x==1:
       continue
    if x==3:
       continue
    if x==5:
       continue
    if x==7:
        continue
    else:
        pass
    print(x)