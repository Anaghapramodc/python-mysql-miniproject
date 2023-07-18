"""
1.check whether the file is exist or not
"""
import os
file_path=r'C:\Users\ANAGHA\PycharmProjects\pythoncourse\file handling\sample_file.txt'
f=os.path.exists(file_path)
if f:
    print(f'the file{file_path} exists')
else:
    print(f'the file{file_path} does not exist')