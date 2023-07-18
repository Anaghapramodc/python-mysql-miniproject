# x=[2,3,4,5,6]
# sum=0
# for i in x:
#     sum=sum+i
#
# movies=[
# {"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
# {"language":"malayalam","name":"aadujeevitahm","rating":5,"year":2023,"genres":["fiction","drama"]},
# {"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
#  {"language":"malayalam","name":"sunny","rating":4,"year":2022,"genres":["drama","thriller"]},
#  {"language":"malayalam","name":"12th man","rating":3,"year":2022,"genres":["drama","thriller"]},
# {"language":"thamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
# {"language":"thamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
# {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
# {"language":"telungu","name":"kgf","rating":5,"year":2018,"genres":["action","romance","thriller"]}]
#
# for i in movies:
#     x = i.get("name")  # to access the the value of the key
#     print(x)
# print('\n')
# for i in movies:
#     y=i.get('rating')
#     if y==5:
#         print(i['name'])
# print('\n')
# for i in movies:
#     y=i.get('genres')
#     for g in y:
#         if g=='mystery':
#             print(i['name'])
# print('\n')
# for i in movies:
#     y=i.get('year')
#     if y==2023:
#         print(i['name'])
# print('\n')
# for i in movies:
#     y=i.get('rating')
#     if y==3:
#         print(i['name'])
# print('\n')
# for i in movies:
#     y=i.get('language')
#     if y=='malayalam':
#         print(i['name'])

# row=int(input("enter the rows"))
# for i in range(0,row,2):
#    for s in range(0,row-i):
#        print(" ",end="")
#    for j in range(1,i+2):
#        print("* ",end="")
#    print()




# import random
# x=[13,22,5,2,77,60,100,2,34,5,123,223,45]
# print(random.choice(x))
#
#
# a=0
# p="luminar"
# for i in range(1,len(p)+1):
#     for j in range(1,i+1):
#         print(p[a] ," ", end="")
#         a=a+1
#     print()
#     a=0

# n=8
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         y=i*j
#         print(y,end=' ')
#     print()



