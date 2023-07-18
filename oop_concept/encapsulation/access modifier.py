"""
encapsulation
public
privet
protected
"""
#public
class vehicle:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour

#protecter
class bank:
    def __init__(self,name,trn):
        self.name=name
        self._trn=trn
bank=bank('sbi',123442435)
print(bank._trn)

#privet
class school:
    def __init__(self, name,fees):
        self.name = name
        self.__fees = fees

abc=school('anagha',25000)
# print(abc.__fees)#cannot access


# class conpany:
#     def __init__(self,ename,sal,):

#abstract
