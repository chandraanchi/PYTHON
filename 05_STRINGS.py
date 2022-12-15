'''
in python ,strings is the collection to the characters surounded by single quotes,double quotes,qnd triple quotes

string items are indexed and slicing

string metods are 
1.string.upper()
2       .lower()
3.      .count()
4.      .startswith()
5.      .endswith()
6.      .find ()
7.      .format()
8.      .index()
9.      .isalnum()
10.     .isdigit()
11.     .split()
12.     .join()
13.     .strip()
14.     .lstrip()
15.     .rstrip()
16.     .removeprefix()
17.     .removesuffix()
18.     .replace()
19.     .title()

string items are seperated with commas,and enclosed with rounded brackets()



'''


str=("hi how are you , is what you doing , this is your strength")

# print(type(str))

# '''upper'''
# print(str.upper())

# '''lower'''
# print(str.lower())

# '''count'''
# print(str.count("is"))
# print(str.count(" is"))

'''starts with'''
# print(str.startswith("hi"))
# '''endswith'''
# print(str.endswith("strength"))

'''real time starts with'''

# websites=["ap.gov","ts.gov","ap.in","ts.in","ap.com","ts.com"]
# ap=[]
# for i in websites:
#     if i.startswith("ap"):
#         ap.append(i)
# print(ap)

# com=[]
# for i in websites:
#     if i.endswith("com"):
#         com.append(i)
# print(com)


# str=("hello how are you ,i ll give you 30 percent discount for you")    
'''find ,index'''
# print(str.find("you"))
# print(str.index("you"))

# print(str.find("chandra"))  #find iste -1 vastadi
# print(str.index("chandra"))  #leni value iste error vastondi

'''format'''
# str="{}hello how are you ,i ll give you 30 percent discount for you".format("chandra")
# print(str)



# names=["apple","cherry","mango","banana","orange"]
# for i in names:
#     x="{i}hi how are thease fruits".format(i=i)
#     print(x)
    
    
# students=["chandra","soori","sunny","bunny","laddu","veeru"]

# for i in students:
#     x="{i} hi all of come to this monday".format(i=i)
#     print(x)




# names=["chandra","gani","pavan","soori"]

# for i in names:
#     x="{i}   hi this message only for you".format(i=i)
#     print(x)

# str=("abc123")
# x=str.isdigit()
# print(x)


# str=("abcdef12346")
# x=str.isalnum()
# print(x)


# str=("hello master welcome to python")
# title=str.title()
# print(title)


# str=("hello master welcome to python")
# x=str.replace("master","students")
# print(x)




# str=("           hello master         welcome to python           ")
# print(len(str))

# s=str.strip()
# print(s)
# print(len(s))

# ls=str.lstrip()
# print(ls)
# print(len(ls))


# rs=str.rstrip()
# print(rs)
# print(len(rs))


# str=("hi hello how are you")
# rp=str.removeprefix("hi")
# print(rp)

# str=("hi hello how are you")
# rs=str.removesuffix("you")
# print(rs)




# str=("hi hello how are you")
# sp=str.split()
# print(sp)
# d=" ".join(str)
# print(str)



'''
in python  strings is the collection of the characeters surounded by single ,double and tripe quotations

list methoda
upper
lower
count
starswith
endswith
find
format
index
insert
isalnum
isdigit
tile
strip
lstrip
rstrip
split
join
removeprefix
removesuffix
replace

'''

# str=("hi how are you whatyou are you doing ,are going there?")
# print(type(str))
# print(str.upper())
# print(str.lower())
# print(str.title())
# print(str.count(" you"))

# print(str.startswith("hi"))
# print(str.endswith("?"))

# web=["ap.gov","ts.gov","ap.com","ts.com","ap.in","ts.in"]

# ap=[]
# for i in web:
#     if i.startswith("ap"):
#         ap.append(i)
# print(ap)

# gov=[]
# for i in web:
#     if i.endswith("gov"):
#         gov.append(i)
# print(gov)

# str=("hi how are you whatyou are you doing ,are going there?")
# print(str.find("how"))
# print(str.index("how"))

# print(str.find("chandra"))
# print(str.index("chandra"))


# str="{}  hi how are you whatyou are you doing ,are going there?".format("chandra")
# print(str)


# names=["ramu","lakshmu","anju","jamba","valmiki","sugreeva"]

# for i in names:
#     x="{i}  hello  all ,how are you , where are you going".format(i=i)
#     print(x)

# str=("        hi how are you whatyou       are you doing ,are  going there  ?      ")


# st=str.strip()
# print(st)
# print(len(str))



# ls=str.lstrip()
# print(ls)
# print(len(ls))


# rs=str.rstrip()
# print(rs)
# print(len(rs))


# str=("hi how are you whatyou are you doing ,are going there?")
# sp=str.split()  #str convert to string 
# print(sp)

# j=" ".join(sp)  # re convert to list
# print(j)









