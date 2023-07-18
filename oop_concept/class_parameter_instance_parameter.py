class person:
    #class parameter
    name="person"

    def __init__(self,name):
        #instance parameter
        self.name=name

obj=person("anagha")
print(person.name,"name is",obj.name)
obj1=person("anu")
print(person.name,"name is",obj1.name)



