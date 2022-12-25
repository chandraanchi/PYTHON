#sets
'''
sets are used to stored multiple items in single variable,

set items are unordered, unchangeble,and un indexed,do not allow duplicated values,

set items are written with curley brackets{},items are seperated with commas,

set methods

set.add()
    .clear()
    .copy()
    .pop()
    .remove()
    .update()
    
    
    union()
    intersection()
    difference()
    symmertic-difference()
    issubset()
    issuperset()
    isdisjoint()

'''

# thisset={1,1,2,3,4,5.5,889}

# print(type(thisset))


'''add'''
# s={1,1,2,2,3,3,333,43,3534,(123)}
# s.add(999)
# print(s)

'''copy'''
# s={1,1,2,2,3,3,333,43,3534,(123)}
# thisset=s.copy()
# s.add("hello")
# print(thisset)
# print(s)

'''clear'''
# s={1,1,2,2,3,3,333,43,3534,(123)}
# print(s.clear())

'''pop'''
# s={1,1,2,2,3,3,333,43,3534,(123)}
# s.pop()
# print(s)

'''remove'''
# s={1,1,2,2,3,3,333,43,3534,(123)}
# s.remove(1)
# print(s)
'''update'''
# s={1,1,2,2,3,3,333,43,3534,(123)}
# s.update("chandranchi")
# print(s)


'''union'''
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# print(set1.union(set2))

'''intersection'''
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# print(set1.intersection(set2))

''''''
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# print(set1.difference(set2))


'''symmertic-difference'''
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# print(set1.symmetric_difference(set2))


'''issubset'''
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# print(set1.issubset(set2))


# set1={1,2,3,4,5}
# set2={1,2,3,4,5,6,7,8}
# print(set1.issubset(set2))

'''issuperset'''
# set1={1,2,3,4,5}
# set2={1,2,3,4,5,6,7,8}
# print(set2.issuperset(set1))

'''isdisjoint'''
# set1={1,2,3,4,5}
# set2={6,7,8}
# print(set1.isdisjoint(set2))

'''find lenth in list'''
# list=[1,2,3,4,5]
# temp=0
# for i in list:
#     temp+=1
# print(temp)
# print(len(list))


'''find lenth code
'''
l=[1,23,3,4,5,6]
temp=0
for i in l:
    temp=temp+1
print(temp)