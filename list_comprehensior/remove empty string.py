list1=["john"," ","jack","emma"," ","jins","lina"]
while " " in list1:
    list1.remove(" ")
print(list1)





list1=["john"," ","jack","emma"," ","jins","lina"]
list2=[j for j in list1 if " "!=j ]
print(list2)