#get the key of a minimum value from  a dictionary
dict1={"num1":1,"num2":20,"num3":12,"num4":0.5}
list1=[]
for i in dict1:
    t=dict1.get(i)
    list1.append(t)
m=min(list1)
for i in dict1:
    if m==dict1.get(i):
        print(f"minimum value= {m} \n key={i}")

