list=[1,2,4,5,7,8,44,51,11,2,4,5,16,5,32,224,5,14]
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even numbers=",even)
print("odd numbers=",odd)