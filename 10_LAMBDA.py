# list=[1,2,3,4,5,6,7,8]
# list2=[]
# for i in list:
#     l=lambda a:a+a
#     list2.append(l(i))
# print(list2)
    
    
# i=[1,2,3,4,5,6,7]    
# k=[]
# for j in i:
#     lam=lambda a:a+1
#     k.append(lam(j))
# print(k)

# age=[15,16,17,18,19,20]
# def vote(x):
#     if x>=18:
#         return True
#     else:
#         return False
# f=filter (vote,age)
# print(list(f))

# marks=[28,65,34,15,35,77,99,76]
# def result(x):
#     if x>=35:
#         return True
#     else:
#         return False
# school=filter (result,marks)
# print((school))


# numbers=[1,2,3,4,5,6,7,8]
# def even_odd(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# even=filter(even_odd,numbers)
# print(list(even))



# numbers=[12,87,3797889,663,6786128937129,76,98]
# even=list(filter(lambda x:x%2==0,numbers))
# print(even)
# odd=list(filter(lambda x: x%2 !=0,numbers))
# print(odd)


# marks=[12,23,34,35,67,88,75,99]
# pas=list(filter(lambda x:x>=35,marks))
# print(pas)
# fail=list(filter(lambda x: x<35,marks))
# print(fail)


# marks =[12,35,23,76,87,99,11,22,33,34,100]
# pas=(list(filter(lambda x:x>=35,marks)))
# print(pas)
# fail=(list(filter(lambda x : x<35,marks)))
# print(fail)


# items=[("soap",25),("oil",120),("veg",40),("milk",35)]
# print(type(items))

# high=list(filter(lambda item: item[1]>=125,items))
# print(high)
# low=list(filter(lambda item:item[1]<=125,items))
# print(low)

'''lambda is a small anonymous function, a lambda function can take any number of arguments and can take only one expression'''

"""r=lambda argumnets:expression"""
'''
1.filter
2.map
3.reduce

'''

#lambda 
# li=[1,2,3,4,5,6]

# list=[]
# for i in li:
#     res=lambda a :a+1
    
#     list.append(res(i))
# print(list)


# tuple1=(1,899783,973682,2436,76)
# tuple2=[]
# for  i in tuple1:
#     res=lambda x:x%2==0
#     tuple2.append(res(i))
# print(tuple2)


'''filter'''
# marks=[12,13,35,45,67,99,22,33]
# pas=print(list(filter(lambda x:x>=35,marks)))
# print(pas)
# fail=print(list(filter(lambda x:x<35,marks)))
# print(fail)


# numbers=[1,2,3,4,5]
# print(list(filter(lambda x:x%2==0,numbers)))
# print(list(filter(lambda x:x%2!=0,numbers)))

'''map'''
# tup=(1,2,3,4,5)
# tup2=(1,2,3,4,5)

# addboth=map(lambda x,y:x+y, tup,tup2)
# print(tuple(addboth))




'''reduce'''
# from functools import reduce
# num={1,2,3,4,5}
# print(set(reduce(lambda x,y: x+y, num)))


'''map'''
# num1=[1,2,3,4,5,6,7,8]
# num2=[2,1,2,3,4,5,6,7]

# addtwo=map(lambda x,y: x+y,num1,num2)
# print(list(addtwo))

# num1=[1,2,3,4,5,6,7,8]
# r=map(lambda x:x*x,num1)
# print(list(r))

"reduce"
from functools import reduce





