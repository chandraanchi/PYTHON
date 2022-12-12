'''print functon'''
# print("hello world!")
# print("welcome to python")

''' comments'''
# single line commnets
'''multi line comments'''

# print function
# print("hello world ,hello python")
# print("welcome")

'''sep=" " '''

print ("hello","welcome",sep="*")
print("pyhton","html","css","bootstrap","git",sep="  ")
print("pyhton","html","css","bootstrap","git",sep=" - ")

'''variables
variables are containers for storing data values
'''
x=20;
y=30;
print(x+y)
'''above the example x,y is variables and values are 20,30'''











'''
can you see the memory location use under this link '''

x=20;
print(id(x)) # id 
y=100
print(id(y))  # id









'''
built in functions

I-numeric data types
1.int
2.float
3.bool
4.complex
5.string

'''
a=100;b=2.5;c=True;d=False;e="string"
print(type(a))  #int
print(type(b))  #float
print(type(c))  #bool
print(type(d))  #bool
print(type(e))  #complex


'''
type convertion--type convertion is the converson from one data type to onother data type..

2 type of type convertion

1.implicit convertion--the python interpretter automatically coneverts one data type to onther datatype..
eg:small data to big data

2.explicit convertion--the python interpretter forcefully converts one data type to onther data type
eg: big data to small data

'''
x=10;
print(float(x))  #converts small to big data

y=2.567;
print(int(y))   # converts big data to small

import sys
a=20;
print(sys.getsizeof(a))


# input 

p=int(input("enter amount :"))
t=int(input("enter time :"))
r=float(input("enter rate of interest :"))
si=(p*t*r)/100

print(si)




















