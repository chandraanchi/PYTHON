# function
'''
function is a block of code ,which only runs when it is called ,
you can pass data ,known as parameters into a function
a function can return data as a result:

in a pyhton a function is defined using the def keyword
to call a function ,use the function name followed by paranthesis

'''
# def function():  # function defination
#     print("function body")      #function body
# function()          # function calling


# def fun_1():
#     print("functions")
# fun_1()

# def func(x,y):
#     print("hello function",x,y)
# func(100,1000)

# def func2(x,y,z):
#     print("hello func2",x,y,z)
# func2(10,100,1000)

# def tuple(*x):
#     print("this is tuple",x)
# tuple(1,2,3,4,5,6)

# def dict(**x):
#     print("this is dict",x)
# dict(k="value",add=123,ph=999,vil="jkp")



# def add(x,y):
#     print(x+y)
# def sub(x,y):
#     print(x-y)
# def mul(x,y):
#     print(x*y)
# def div(x,y):
#     print(x/y)


'''
from python perspective, a function is a block of code ,which only runs when it is called,
you can pass the data know as parameters into a function
a function can return data as a result,,


information can be passed into functions as arguments,
arguments are specified after the function name inside the parenthesis ,you can add as many arguments as you want
just seperate them with comma,,

from python perspective 
argemnts or parametre are used for same thing,information can be that are passed into function

a parameter is the variable listed inside the parenthesis inthe function definantion
an argument is the value that is sent to function when it is called

'''
# def hellofunction():
#     print("hi")
# hellofunction()

# def function(x):
#     print("this is func body",x)
# function(100)
# function(1000)
# function(10)

'''if you dont know howmany arguments that will be  passed into your function add * to before the parameter name in the function definition,
this way the fuction will receive a tuple of arguments'''
# print("arbitary arguments *args")
# def tup(*x):
#     print(x)
# tup(1,2,1,3,4,5,6)



'''
if you donot know how many arguments that will be passed into your functon ,add** before the parameter name 
in the function defination,
this way the function will receive a dictinary type arguments


'''
# print("arbitary keyword arguments **kwargs")
# def dic(**x):
#     print(x)
# dic(key="value",ph=123,add="jkp",name="chandra")


'''default parameter values'''
# def fruits(apple="none",banana="none",mango="none"):
#     print("apple=",apple,"banana=",banana,"mango=",mango)
# fruits(10,100,100)
# fruits(10,100)
# fruits(10)
# fruits(10)

'''doc string'''

# def docs(x):
#     '''this is doc string'''
#     print(x)
# print(docs.__doc__)
# docs(100)

# def chandra():
#     '''this is doc string '''
#     print("docstring")
# print(chandra.__doc__)
# chandra()



# def csa(x):
#     '''this is doc string hello how are you'''
#     print("doc",x)
# print(csa.__doc__)
# csa(100)
# csa(1000)
# csa(10000)
# csa(100000)


# from practice import *
# add(10,10,10)
# sub(100,100,10)
# mul(10,3,200)
# div(100,100,10)
# modulo(100,10)

# def add(x,y):
#     return(x+y)
# def sub(x,y):
#     return(x-y)
# def mul(x,y):
#     return(x*y)