#5. Generate a Python list of all the even numbers between 4 to 30
def even(a,b):
    list=[]
    for i in range(a,b+1,2):
        list.append(i)
    return list
print(f"even numbers = {even(4,30)}")