"""
set
used to print multiple data item
sequential
unorderd
no duplicats
immutable (we cant change values)
unordered
unintexed

"""
set1={1,2,3,4,5,"apple","baa"}
print(set1)
print(5 in set1)
#empty set= set()
for i in set1:
    print(i)



#methords in set
#add()
set1.add("banana")#add elements in a set
print(set1)
#update()
set1={1,2,3,4,5,"apple","baa"}
set2={1,11,22,33,44,"kewi"}
set1.update(set2)#update elements in a set
print(set1)
set1={1,2,3,4,5,"apple","baa"}
set1.update("grapes")
print(set1)
set1={1,2,3,4,5,"apple","baa"}
list1=["car","lorry","jeep"]
set1.update(list1)
print(set1)
print("\n")
#remove()
set1={1,2,3,4,5,"apple","baa","apple","orange","banana"}
set1.remove("apple")#to remove the element
print(set1)
print("\n")
#discard()
set1={1,2,3,4,5,"apple","baa","apple","orange","banana"}
set1.discard("python")#to remove the element also when the removeing element doent existing in the string then it cnt print error
print(set1)
set1.discard("baa")
print(set1)
print("\n")
#pop()
set1={1,2,3,4,5,"apple","baa","apple","orange","banana"}
print(set1)
x=set1.pop()#remove one element which is in the first possition
print(set1)
print("\n")
#clear()
set1={1,2,3,4,5,"apple","baa","apple","orange","banana"}
set1.clear()
print(set1)
#del
set1={1,2,3,4,5,"apple","baa","apple","orange","banana"}
del set1#delete set in the memmary
# print(set1)
print("\n")
#union()
set1={"a","b","c"}
set2={1,5,8}
set3=set1.union(set2)#to unite two set
print(set3)
print("\n")
#intersection()
set1={"a","b","c"}
set2={1,5,8}
z=set1.intersection(set2)#used to print commen elements in the sets
print(z)
set1={"a","b","c",1,2,5}
set2={1,5,8}
z=set1.intersection(set2)
print(z)
print("\n")
#difference()
set1={"a","b","c"}
set2={1,5,8}
z=set1.difference(set2)#print the elements which are in set1 but not in set2
print(z)
set1={"a","b","c",1,2,5}
set2={1,5,8}
z=set1.difference(set2)
print(z)
print("\n")
#symmetric_difference()#used to print unique elemet in two sets
set1={"a","b","c",1,2,5}
set2={1,5,8}
z=set1.symmetric_difference(set2)
print(z)
print("\n")
#intersection_update()
set1={"a","b","c",1,2,5}
set2={1,5,8}
z=set1.intersection(set2)
print(z)
set1.intersection_update(set2)
print(set1)
print("\n")
#difference_update()
set1={"a","b","c",1,2,5}
set2={1,5,8}
z=set1.difference(set2)
print(z)
set1.difference_update(set2)
print(set1)
print("\n")
#symmetric_difference_update()
set1={"a","b","c",1,2,5}
set2={1,5,8}
z=set1.symmetric_difference(set2)
print(z)
set1.symmetric_difference_update(set2)
print(set1)
print("\n")
#isdisjoint()
set1={"a","b","c",1,2,5}
set2={1,5,8}
z=set1.isdisjoint(set2)#when all elements in the sets are unique then print true else false
print(z)
set1={"a","b","c",1,2,5}
set2={4,3,8}
y=set1.isdisjoint(set2)
print(y)
print("\n")
#issubset()
set1={1,2,5}
set2={"a","b","c",1,2,5}
z=set1.issubset(set2)#when all elements in the first sets are present in the second set then print true
print(z)
set1={"a","b","c",1,2,5}
set2={4,3,8}
y=set1.issubset(set2)
print(y)
print("\n")
#issuperset()
set1={"a","b","c",1,2,5}
set2={1,2,5}
z=set1.issuperset(set2)#when all the selent of the second set is also in the first set then the firstset called super set
print(z)
set1={"a","b","c",1,2,5}
set2={4,3,8}
y=set1.issuperset(set2)
print(y)


set1={"a","b","c",1}
set2={1,5,8}
z=set1.difference(set2)#print the elements which are in set1 but not in set2
print(z)

