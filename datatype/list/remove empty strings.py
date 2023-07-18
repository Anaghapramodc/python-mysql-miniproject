list1=["john"," ","jack","emma"," ","jins","lina"]
list2=[]
for i in list1:
    if i==" ":
        continue
    else:
        list2.append(i)
print(list2)


list1=["john"," ","jack","emma"," ","jins","lina"]
while " " in list1:
    list1.remove(" ")
print(list1)


list1=["john"," ","jack","emma"," ","jins","lina"]
for i in list1:
    if i.isspace():
        list1.remove(" ")
print(list1)