file1=open("sample_file.txt",'w')
file1.write("hair dears""\n"
            "welcome to python world")
file1.close()
file1=open("sample_file.txt",'r')
# print(file1.read())
# lines=file1.readline()
# print(lines[1])

lines=file1.readlines()
print(lines[1])




file2=open("sample_file2.txt",'w')
file2=open("sample_file2.txt",'r')


