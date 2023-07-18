"""
1-create a class with instance attributes
"""
class student:
    def __init__(self,name,rollno,mark):
        self.name=name
        self.rollno=rollno
        self.mark=mark

    def __str__(self):  # print string model:-to print object
        return f"\n roll no:-{self.rollno} \n name:-{self.name} \n mark:-{self.mark}"

std1=student('anagha',1,98)
print(std1)