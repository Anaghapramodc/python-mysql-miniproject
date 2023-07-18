import random
list_item=[1,2,3,4,5,6]
print(dir(random))
print(random.choice(list_item))#choose a variable randomly in the list
print(random.random())
print(random.randint(5,15))
print(random.randrange(5,15,2 ))
random.shuffle(list_item)
print(list_item)
