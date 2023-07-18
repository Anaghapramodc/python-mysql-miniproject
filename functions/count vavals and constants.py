
def vavals_constant(s):
     s.remove(" ")
     v={"a","e","i","o","u","A","E","I","O","U"}
     c1=0
     c2=0
     for i in s:
         if i in v:
            c1=c1+1
         else:
             c2=c2+1
     print("vavels =", c1)
     print("consonant =", c2)
     return c1,c2
s=list(input("enter the string"))
vavals_constant(s)
