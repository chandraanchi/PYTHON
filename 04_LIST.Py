'''
list can be defined as a collection of values or items of different data types,
[int,float,bool,comp,"string",tuple,set,dict,list],

the items in the list are seperated with commas,and enclosed with square brakets[items,items,items,item]

list elaments can access by index

the list items are ordered
                    changeble
                    allow dupilcated values
                    slicing
                    indexing
                    
            indexing has two types postive index and negative index
            the indexing start[0],end is[n-1]
            

list methods:
            1.append()
            2.extend()
            3.copy()
            4.count()
            5.clear()
            6.index()
            7.insert()
            8.pop()
            9.remove()
            10.reverse()
            11.sort()
                 sort has two type assending --->var.sort()
                                    descending --->var.sort(reverse=True)


'''

# var=[1,22,3.55,True,False,0,"string",(1,2,3,4),{123},[0,1,2,3,4],1,1,0]
# print(type(var))  # type
# print(len(var))     # length

#indexing
# print(var[0])  #index call 0
# print(var[5])  #index call 5
# print(var[-1]) #index call -1
# print(var[7])
# print(var[9])
# print(var[6])


#slicing
# var=[1,22,3.55,True,False,0,"string",(1,2,3,4),{123},[0,1,2,3,4],1,1,0]

# print(var[0:]) #show the after index number 0

# print(var[:-1]) #show the negative index left side

# print(var[::]) #show the asties list

# print(var[::-1])    # show the reverse


# print(var[0:10:3])      # [start : stop: skip betweem] 0:10 index

# print(var[10:0:-3]) #reverse range index [stop:start:skip]


# var=[1,22,3.55,True,False,0,"string",(1,2,3,4),{123},[0,1,2,3,4],1,1,0]

# print(var[0:])
# print(var[:-1])
# print(var[::])
# print(var[:])
# print(var[::-1])
# print(var[0:-1:2])
# print(var[10:0:3])
# print(var[0:5])


'''list methods'''

'''append'''
# list=[0,1,2.677,True,False,0,1]

# list.append(999)   #add items in the list
# print(list)

# list.append([9898,978,986776])
# print(list)



'''extend'''
# list=[0,1,2.677,True,False,0,1]

# list.extend([9999])      #manam data ni datatype brackets lone send cheyali
# print(list)


'''clear'''

# list=[0,1,2.677,True,False,0,1]

# sunny=list.copy()
# list.append("apple")
# print(sunny)
# print(list)


'''count'''

# list=[0,1,2.677,True,False,0,1]

# d=list.count(1)   # count
# print(d)

'''index'''
# list=[0,123,2.677,True,False,0,1]

# d=list.index(1)  #element iste index place choopistudi
# print(d)

# c=list.index(123) #element iste index place choopistundi
# print(c)

'''insert'''
# list=[0,123,2.677,True,False,0,1]

# list.insert(0,"cherry")  #insert anedi ye index lo value kavalo iste chestadi
# print(list)








'''pop'''
# list=[0,123,2.677,True,False,0,1]

# list.pop(1)  #pop will take index and then remove element
# print(list)

# list.pop(3)
# print(list)

'''remove'''

# list=[0,123,2.677,True,False,0,1]

# list.remove(0)  #will take element then also removed elemnt

# print(list)



'''reverse'''
# list=[0,123,2.677,True,False,0,1]
# list.reverse()
# print(list)

'''sort'''
# list=[0,123,2.677,True,False,0,1]
#assending

# list.sort()
# print(list)

#descending
# list.sort(reverse=True)
# print(list)


'''list comprehensions'''
#synatx
# lc=[expression ifcond for i in sequence]

#find even and odd numbers
# x=["even" if i%2==0 else "odd"  for i in range(50)]
# print(x)





# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new=[]
# for x in fruits:
#         if "a" in x:
#                 new.append(x)
# print(new)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[]
# for x in fruits:
#         if "a" not in x:
#                 newlist.append(x)
# print(newlist)

#list comprehension

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[x for x in fruits if "a" in x]
# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# new=[i for  i in fruits if "a" not in i]
# print(new)



'''find more index places'''
# index=[0,1,3,2,1,2,3,2,True,False,1,1,1,1,1]

# for i in range (len(index)):
#         if index[i]==0:
#                 print(i)

# for i in range (len(index)):
#         if index[i]==2:
#                 print(i)

# d=index.index(1)
# print(d)


# for x in range (len(index)):
#         if index[x]==1:
#                 print(x)



# list=[1,2,3,4,11,1,1,1,True,False]

# print(list[0:9])
# print(list[0:])
# print(list[:-1])
# print(list[::])
# print(list[::-1])

# list.append(123)
# print(list)
        
        
# list.extend([123])        
# print(list)
# list=[1,2,3,4,11,1,1,1,True,False]
# sunny=list.copy()
# list.append(123)
# print(sunny)
# print(list)


# print(list.clear())

# d=list.count(1)
# print(d)

# d=list.index(1)
# print(d)

# for i in range (len(list)):
#         if list[i]==1:
#                 print(i)






# list=[1,2,3,4,11,1,1,1,True,False]

# list.insert(0,"apple")

# print(list)

# list.pop(0)
# print(list)

# list.remove(1)
# print(list)

# list=[1,2,3,4,11,1,1,1,True,False]
# list.reverse()
# print(list)

# list.sort()
# print(list)

# list.sort(reverse=True)
# print(list)


# new=["even" if i%2==0 else "odd" for i in range(10)]
# print(new)


'''remove dupicate values'''

list=[1,1,1,2,3,4,3,2,4,5,554,3,3,323232,334]

# remove=[]
# for i in list:
#         if i not in remove:
#                 remove.append(i)
# print(remove)

'''find more index places'''
# list=[1,1,1,77,39,387,743,1,4,3]

# for i in range(len(list)):
#         if list[i]==1:
#                 print(i)

# remove duplicates

# rd=[]
# for i in list:
#         if i not in rd:
#                 rd.append(i)
# print(rd)