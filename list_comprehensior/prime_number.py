list=[1,2,3,4,5,6,7,8,11,23,22]
l=[]
for i in list:
    if i>1:
      for j in range(2, i):
        if i % j == 0:
            break
      else:
        l.append(i)
print(l)

#prime numbers
list=[1,2,3,4,5,6,7,8,11,23,22]
new_list1=[i for i in list    if all(i%j!=0 for j in range(2,i)) and i>1 ]
print(new_list1)