"""
file handing is the most important in python
open
read
write
append
read and write
write and read
"""

# f=open("demo.txt",mode="w")
# z=f.write("hi hello welcome to file handling")
# print(z)
# f=open("F:\demo.txt",mode="a")
# x=f.write("hello file handing")
# print(x)

f=open("demo.txt",mode="w")
result=f.write("hi welcome to file hadling in python")
print(result)

f=open("demo.txt",mode="a")
res=f.write("poiuytrs lkjhgfdsa MNBVCXZ LKJHFDSApoiuytrewq")
print(res)

f=open("demo.txt","r")
r=f.read()
s=f.readline(10)
print(s)
print(r)

f.close()


'''
import os
os.rename("file name path","rename the file")
os.remove("filename path)
os.mkdir("create folder name new")
os.chdir(""change folder name")
print(os.getcwd)
os.rmdir("remove directory name")


'''
import os
# os.rename("demo.txt","index.txt")
# # os.remove("demo.txt")