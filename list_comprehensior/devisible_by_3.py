#devisible by3
list_item=[1,3,2,44,5,32,13,12,65,40,42]
new_list=[]
for i in list_item:
    if i%3==0:
        new_list.append(i)
print(new_list)

list_item=[1,3,2,44,5,32,13,12,65,40,42]
new_list=[i for i in list_item if i%3==0]
print(new_list)






