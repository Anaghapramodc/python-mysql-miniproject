"""
2.check the size of the file
"""
import os
file_path=r'C:\Users\ANAGHA\PycharmProjects\pythoncourse\file handling\sample_file.txt'
s=os.path.getsize(file_path)
print(f"size= {s} bytes")