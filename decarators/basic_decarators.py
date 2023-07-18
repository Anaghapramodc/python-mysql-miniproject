"""
modify functionality  of function

"""
# def name(a):
#     def me():
#        print("i am anagha")
#     return me
# def greating():
#     print("hai dear")
# result=name(greating())
# result()

def name(a):
    def me():
       a()
       print("i am anagha")
    return me
@name
def greating():
    print("hai dear")
greating()