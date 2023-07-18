"""
string
string is set of characters.
eg:-str="Hello"
indexed
ordered
immutable
cnt allow duplicats
"""
str1="Hello"
print(type(str1))
print(str1[0])#--->o/p H
print(str1[1])#--->o/p e
print(str1[2])#--->o/p l
print(str1[3])#--->o/p e
print(str1[4])#--->o/p e
print("\n")
print(str1[-1])#--->o/p H
print(str1[-2])#--->o/p e
print(str1[-3])#--->o/p l
print(str1[-4])#--->o/p e
print(str1[-5])#--->o/p e
print("\n")
#string slicing
print(str1[0:3])
print(str1[1:4])
print(str1[1:5])
print(str1[1:])
print(str1[2:])
print(str1[2:5])
print(str1[2:4])
print("\n")
print(str1[::-1])
print(str1[-1:-6:-1])
print(str1[-2:-6:-1])
print(str1[-2:-5:-1])
print(str1[::-2])
print("\n")
str2="Hello world"
print(str2[0:5])
print(str2[0:7])
print(str2[0:])
print(str2[6:])
print("\n")
print(str2[-1:])
print(str2[-2:])
print(str2[::-1])
print(str2[-1:-6:-1])
print(str2[-7:-12:-1])
print("\n")

#string operations
str1="Hello world"
print(str1.upper())#o/p HELLOW WORLD
print(str1.lower())#hello world
#strip() to remove white space
print(str1.capitalize())#first letter capital
print(str1.count("hello"))#count how many times the word repeated
print("\n")
print("\n")
x=str1.find("world")#to find the word
print(x)
print(str1.isalpha())#check whether the string contines only alfabets
print(str1.index("w"))#to find the possition vales of the letter
print(str1.isalnum())#to check the string contains only alphabets or numbers not contains spacial charectors
print(str1.isdigit())#check whether the string is a digit
print(str1.islower())#check whether all alfabets are lower
print(str1.isupper())#check whether all alfebets are higher

"""
python f string
python f string is the newest python syntax to do string formatting.
it is available since python 3.6.python f-string provide a faster,morereadable
more concise and less error print way of formatting string in python.

the f string have the f perfix and use{} brackets to evaluate values.
"""
#format()
#it is used to print the o/p
name="anagha pramod c"
age=22
print("%s is %d years old"%(name,age))#string format
print("{} is {} years old".format(name,age))#format method
print(f"{name} is {age} year old")#f string methord

bag=3
applesinbag=12
print(f"there are tottel of {bag*applesinbag} apples")

#string concatination
#only strings are concatinate together
#strins and numbers cant concatinate together
str3="Hello"
str4="world"
print(str3+"",str4)


#replace()
 #used to replace the value of the string

t="hello anagha"
n=t.replace("anagha","ponnu")
print(n)
n1=t.replace("a","x",1)
print(n1)
n2=t.replace("a","x",2)
print(n2)
n3=t.replace("a","x",3)
print(n3)

#join()
list=["anagha","ammu","ponnu"]
x=" ".join(list)
print(x)

#split()
str1="hello world haiii 2 3 4 5"
str2=str1.split(" ")
print(str2)

s='anaghaPRamod'
x=s.isalpha
print(s.isspace())
