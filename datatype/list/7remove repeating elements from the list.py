#Write a python program to remove repeated elements from a given list without using built-in methods
      #  list_to_remove = ["let's","google","the","pineapple","photo","google","photo",""]


list1=["let's","google","the","pineapple","photo","google","photo"]
l2=[]
for i in list1:
    if i in l2:
        break
    else:
        l2.append(i)

print(l2)