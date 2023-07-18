# with open(r"sample_file.txt",'r+') as fp:
#
#     for i in fp:
#         if i.find('good ')==False:
#             print("the string is not exist in the file")
#             break
#     else:
#          print("the string is exist in the file")


with open(r"sample_file.txt",'r+') as fp:
    w=input("enter the string")
    for i in fp:
        if w in i:
            print(w,"is present")
            break
    else:
        print(w,"is not present")

