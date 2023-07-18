list1=["fed","vento","volvo","audi",["cars","bus","lorry"],"bmw"]
print(list1[0])
print(list1[5])
print(list1[4])
print(list1[4][0])
print(list1[4][2])
print(list1[4][1:])
print(list1[4][::-1])
print(list1[::-1])
# print(list1[::-1])
print("\n")

#methords in nested list
#insert()
list1=["fed","vento","volvo","audi",["cars","bus","lorry"],"bmw"]
list1.insert(1,"anagha")
print(list1)
# list1=["fed","vento","volvo","audi",["cars","bus","lorry"],"bmw"]
list1[5].insert(1,"anagha")
print(list1)

#pop()
list1=["fed","vento","volvo","audi",["cars","bus","lorry"],"bmw"]
list1.pop(3)
print(list1)
list1=["fed","vento","volvo","audi",["cars","bus","lorry"],"bmw"]
list1[4].pop(2)
print(list1)

#remove()
list1=["fed","vento","volvo","audi",["cars","bus","lorry"],"bmw"]
list1.remove("audi")
print(list1)
list1=["fed","vento","volvo","audi",["cars","bus","lorry"],"bmw"]
list1[4].remove("cars")
print(list1)

# reverse()
list1=["fed","vento","volvo","audi",["cars","bus","lorry"],"bmw"]
list1.reverse()
print(list1)
list1[1].reverse()
print(list1)