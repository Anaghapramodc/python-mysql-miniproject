"""
delete lines from a file
"""

file1=open("samplefile2.txt",'w')
file1.write("hair dears""\n"
            "welcome to python world""\n"
            "good moring dear....""\n"
            "good morning")
file1.close()
with open(r"samplefile2.txt",'r+') as fp:
     lines=fp.readlines()
     fp.seek(3)
     fp.truncate(3)
     fp.writelines(lines[1:])