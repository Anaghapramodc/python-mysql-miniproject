"""
list
list is mutable
indexed
orderd allow duolicates
"""
str="anagha"
lst=list(str)
print(lst)
print(" ".join(lst))#to join a list
lst.remove("g")#to remove characters in list
print(lst)
print("".join(lst))
item=["apple",123,"orange",9.0]
print(item[1])
print(item[0:3])
print(item[3])
print(item[:1])
print(item[1:])
print(item[-1])
print(item[:-1])
print(item[::-1])
print("\n")
#list methords
item=["apple",123,"orange",9.0]
item1=[12,"cherry","banana","xyz"]
item.append("anagha")#to concatinate two list
print(item)
item=["apple",123,"orange",9.0]
item1=[12,"cherry","banana","xyz"]
item.extend(item1)#to extent the element of the string
print(item)
item=["apple",123,"orange",9.0]
item.insert(2,"anagha")#to insert an element to a possition in a list
print(item)
item=["apple",123,"orange",9.0]
item.pop(2)#to remove elements from the list using intex possition
print(item)
item=["apple",123,"orange",9.0]
item.pop()
print(item)
item=["apple",123,"orange",9.0]
item.reverse()#to reverse the list element
print(item)
item=["apple",123,"orange",9.0]
item.clear()#to clear all elements in the list
print(item)
item=["apple",123,"orange",9.0]
i=item.copy()#to copy a list to enother variable
print(i)
item=["apple",123,"orange",9.0]
i=item.count("apple")#to count how many times the element repeated
print(i)
item=["apple",123,"orange",9.0]
i=item.index("apple")#to find the index possition of the element
print(i)
item=["apple",123,"orange",9.0]
item.remove("orange")#to remove the element from the list
print(item)
item=["apple","mango","orange","kewie"]
item.sort()#to sort elements from the list
print(item)
item2=[1,2,4,6,2,11,4,6,3]
item2.sort()
print(item2)
item2.sort(reverse=True)
print(item2)
item.sort(reverse=True)
print(item)