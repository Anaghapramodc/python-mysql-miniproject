s="let's google the pineapple"
x1=""
x2=""
for i in s.split(" "):
    # print(i)
    for j in i:
        # print(j)
        if x1.find(j) == -1:
                x1=x1+j
        else:
                continue
    x2=x2+x1+" "
    x1=""
print(x2)

# s="let's google the pineapple"
# str1=s.split(" ")
# str2=[]
# for i in str1:
#     l=""
#     for j in i:
#         if j in l:
#             continue
#         else:
#             l=l+j
#     str2.append(l)
# print(" ".join(str2))
#
#
#
#
#
#
#
#
#
#
#
#
#
#





# for i in s.split(" "):
#        print(i)
#      for j in i:
#           print("j=",j)
# #         if x1.find(j)==-1:
#             x1=x1+j
#         else:
#             continue
# print(x1,end=" ")







#  if x1.find(j)==-1:
# #             x1=x1+j
# #         else:
# #             continue