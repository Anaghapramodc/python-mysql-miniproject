"""
tuple
to store multiple items in a single variable
sequantial data type
immutable
ordered
indexed
allow duplicates


"""
tuple1=("car","jeep","lorry",1,6,9.0,3)
print(tuple1)
tuple2=("car","jeep","lorry",1,6,9.0,3,[1,2,4,6,7],(4,5,1,2,4))
print(tuple2)
print(tuple1[0:4])
print(len(tuple1))
print(tuple1[-1])
print(tuple2[-1])
print(tuple1[:-1])
print(tuple2[:-1])
print(tuple1[1:])
print(tuple2[1:])
print(tuple1[:-1])
print(tuple2[7][0])
print(tuple2[7][1:])
print(tuple2[7][:1])
print(tuple2[7][1:4])
print("\n")
#to remove an element
tuple1=("car","jeep","lorry",1,6,9.0,3)
t=list(tuple1)
print(t)
t.remove("jeep")
print(t)
tuple1=tuple(t)
print(tuple1)
#to replace an element
tuple1=("car","jeep","lorry",1,6,9.0,3)
t=list(tuple1)
print(t)
t.insert(2,"jeep")
print(t)
tuple1=tuple(t)
print(tuple1)
#to update an element
tuple1=("car","jeep","lorry",1,6,9.0,3)
t=list(tuple1)
print(t)
t[1]="anagha"
print(t)
tuple1=tuple(t)
print(tuple1)
#to reverse a tuple
tuple1=("car","jeep","lorry",1,6,9.0,3)
print(tuple1[::-1])
t=list(tuple1)
print(t)
t.reverse()
print(t)
tuple1=tuple(t)
print(tuple1)

#unpacking tuple
tuple1=("apple",[10,20,30],(5,12,25),2,3,4)
(x,*y)=tuple1
print(x)
print(*y)
(*x,y)=tuple1
print(*x)
print(y)
"""
zip
map
filter
reduce
"""
#tuple methords
#enumerate()
tuple1=("s","t","r","i","n","g")
y=enumerate(tuple1)#to print the index possition and values of a tuple
print(tuple(y))
#all()
tuple1=("s","t","r","i","n","g")
x=all(tuple1)#check whether the tuple contains the bbolian variables like 0,True,False
print(x)
tuple1=("s","t","r","i","n","g",1,2,4)
x=all(tuple1)
print(x)
tuple1=("s","t","r","i","n","g",1,2,4,0,)
x=all(tuple1)
print(x)
tuple1=("s","t","r","i","n","g",1,2,4,False,)
x=all(tuple1)
print(x)
tuple1=("s","t","r","i","n","g",1,2,4,True,)
x=all(tuple1)
print(x)
print("\n")
#any()
tuple1=("s","t","r","i","n","g")
x=any(tuple1)#whether the tuple have any value it print true
print(x)
tuple1=("s","t","r","i","n","g",1,2,4)
x=any(tuple1)
print(x)
tuple1=("s","t","r","i","n","g",1,2,4,0,)
x=any(tuple1)
print(x)
tuple1=("s","t","r","i","n","g",1,2,4,False,)
x=any(tuple1)
print(x)
tuple1=("s","t","r","i","n","g",1,2,4,True,)
x=any(tuple1)
print(x)
print("\n")
#max()
tuple2=(1,2,3,4,5)
x=max(tuple2)#to print maximum value in the tuple
print(x)
tuple2=("apple","orange")
x=max(tuple2)
print(x)
print("\n")
#min()
tuple2=(1,2,3,4,5)
x=min(tuple2)#to print minimum value in the tuple
print(x)
tuple2=("apple","orange")
x=min(tuple2)
print(x)
print(x)
print("\n")
#sorted()
tuple2=(11,3,21,1,2,3,4,5)
x=sorted(tuple2)#to sort the values in the tuple
print(x)
tuple2=("kewi","apple","orange")
x=sorted(tuple2)
print(x)
print("\n")
#sum()
tuple2=(1,2,3,4,5)
x=sum(tuple2)#to add the values in the string
print(x)
#tuple()
tuple2=[1,2,3,4,5]
x=tuple(tuple2)
print(x)
#len()
tuple2=(1,2,3,4,5)
x=len(tuple2)#to find the length of the string
print(x)




