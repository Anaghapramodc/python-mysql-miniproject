# with open(r"samplefile2.txt",'r+') as fp:
#     f3=open('samplefile1.txt','w')
#     for i in fp:
#         print(i)
#         f3.write(i)

# """write data in file"""
# file=open("artist_signup_details.txt",'w')
# file.write("sanjusanjay23@gmail.com""\n""sanju123@""\n"
# "shamendu12@gmail.com""\n" "shammu@172""\n"
# "rajrajan12@gmail.com""\n" "rajan@142""\n"
# "ganapathi34@gmail.com" "\n""ganapathi12@""\n"
# "punekae99@gmail.com""\n" "punness21@""\n"
# "sanjusanju@gmail.com""\n" "sanju09@""\n"
# "dipti66@gmail.com""\n" "dipti88@""\n"
# "ghanshyam44@gmail.com""\n" "ghan23@""\n"
# "nayakghana@gmail.com" "\n""ghan23@32""\n"
# "rajraj23@gmail.com""\n" "rajraj@12""\n"
# "paraspp23@gmail.com""\n" "paras@23""\n"
# "sureshsuresh12@gmail.com""\n" "susu@01""\n"
# "ganapathi45@gmail.com""\n" "ganahana@12""\n"
# "babu123@gmail.com""\n" "babu@123""\n"
# "govind123@gmail.com""\n""govi@123""\n")
# file.close()

# """ delete all datas in the file"""
# fp = open('artist_login_details.txt', 'r+')
# fp.truncate(0)
# fp.close()

x="govind1@gmail.com"
y="govi@123"
# print(x)
with open(r"artist_login_details.txt", 'r+') as fp:
     for i in fp:
         # print(i)
         if x in i or y in i:
             print("the file aldredy exist")
             break
     else:
         with open("artist_login_details.txt", "a") as f:
             f.write(x)
             f.write("\n")
             f.write(y)
             f.write("\n")
         print("recored")
# #
#
