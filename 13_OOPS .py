'''
object oriented programming is a way of computer programming using the idea of objects to represent
data and methods,
it is also an approach used for creating neat and reussable code instead of reduandent one.

it is botton - up  approach,
program divided into a objects
makes use of access modifiers public private and protected
it is more secure 
and object can move freely with in member functions
it supports inheritance
ex--->  c++,python,java

oops features
1.class
2.object
3.inheritance
4.polymorphism
5.encapsulation
6.data abstarction


class:

we will define class by using class keyword
class is blue print to a objects
collection of objects is called class
ex--- fruits

object

object is a physical entity
memory is created when it declared
ex---apple ,mango,orange


object oriented programming is a way of computer programming using the idea of objects,
to represent data and methods ,it is also an approach used for creating neat and reusable code 
instead of reduandent one,

oop is s bottom -up approach,
it is more secura 
programme divided into objects
objeects can move freely with in functons
it is suppeorts inheritance
makes use of access modifers public private protectedd


c++,java,python




oops features
class
object
inheritance
polymorphism
encapsulation
data abstaraction
'''

# class Chandu():                 #class defination
#     '''hello this is oops'''    #docstring
#     attribute=100               #atribute
#     def Chandu_info(self):      #method function
#         print("hello oops=",self.attribute)
# o=Chandu()                      #object declaration
# o.Chandu_info()                 #object.function name
# print(Chandu.__doc__)

# class Home():
#     '''using items for house costruction'''
#     brick=5
#     wood=100
#     sandal=10
#     cement=100
#     def Home_info(self):
#         print(self.brick+self.wood+self.sandal+self.cement)
# print(Home.__doc__)
# h=Home()
# h.Home_info()


# class Python():
#     fee=50000
#     def Python_info(self):
#         print(self.fee)
# p=Python()
# p.Python_info()


# class Chandu():
#     x=100
#     def Chandu_info(self):
#         print("hello",self.x)
# c=Chandu()
# c.Chandu_info()


# class Chandu():
#     def __init__(self,a,b,c,d):
#         self.aa=a
#         self.bb=b
#         self.cc=c
#         self.dd=d
#     def Chandu_info(self):
#         print("hello",self.aa,self.bb,self.cc,self.dd)
# c=Chandu(1,2,3,4)
# c.Chandu_info()
        

# class Dhamaka():
#     def __init__(self,hero,heroin,director):
#         self.h=hero
#         self.hin=heroin
#         self.d=director
        
#     def Dhamaka_info(self):
#         print("movie hero =",self.h)
#         print("movie herin =",self.hin)
#         print("movie director =",self.d)
        
# h=input("movie hero =")
# hin=input("movie heroin =")
# d=input("movie director =")

# d=Dhamaka(h,hin,d)
# d.Dhamaka_info()
        
# class Movie():
#     '''
#     this is tollywood movie information
    
#     '''   
#     def __init__(self,moviename,hero,heroin,director,producer,musicdirector):
#         self.mn=moviename
#         self.h=hero
#         self.hn=heroin
#         self.d=director
#         self.p=producer
#         self.md=musicdirector
    
#     def Movie_info(self):
#         print("movie name =",self.mn)
#         print("hero =",self.h)
#         print("heroin =",self.hn)
#         print("director =",self.d)
#         print("producer =",self.p)
#         print("music director =",self.md)
# mn=input("movie name =")
# h=input("hero =")
# hn=input("heroin =")
# d=input("director =")
# p=input("producer =")
# md=input("music director =")

# print(Movie .__doc__)
# print("_"*5,"tollywood","_"*5)
# m=Movie(mn,h,hn,d,p,md)
# m.Movie_info()
        

'''inheritance
parent class=super class or base class or parentclass
child class=child or sub class or derived class


single inheritance
multilpe inheritance
multilevel inheritance
hirarical inheritance

'''
        
#single iheritance
# class Parent():
#     def Parent_info(self):
#         print("hello this is parent class")     
# class Child(Parent):
#     def Child_info(self):
#         print("this is child class")
# c=Child()
# c.Parent_info()
# c.Child_info()
        
        
# class India():
#     '''india and ap'''
#     def India_info(self):
#         print("india")
# class Ap(India):
#     def Ap_info(self):
#         print("ap")
# print(India .__doc__)        
# a=Ap()
# a.India_info()
# a.Ap_info()


        
'''multilevel inheritance'''       
# class World():
#     def World_info(self):
#         print("world")
# class India(World):
#     def Inida_info(self):
#         print("india")
# class Ap(India):
#     def Ap_info(self):
#         print("ap")
# a=Ap()
# a.World_info()
# a.Inida_info()
# a.Ap_info()

'''multiple inheritance'''

# class Father():
#     def Father_info(self):
#         print("father")
# class Mother():
#     def Mother_info(self):
#         print("mother")
# class Child(Father,Mother):
#     def Child_info(self):
#         print("child")
# c=Child()
# c.Father_info()
# c.Mother_info()
# c.Child_info()




'''hirarchical inheritance'''


# class Parent():
#     def Parent_info(self):
#         print("parent assets")
        
# class Child1(Parent):
#     def Child1_info(self):
#         print("child1")
# class Child2(Parent):
#     def Child2_info(self):
#         print("child 2")
        
        
        
# c1=Child1()
# c2=Child2()

# c1.Parent_info()
# c1.Child1_info()

# c2.Parent_info()
# c2.Child2_info()

# class Chandu():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print(a,b)
        
# class Chandu_info(Chandu):
#     def __init__(self,a,b):
#         print(a,b)
#         super().__init__(a,b)
# class Chandu_one(Chandu_info):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#         print(a,b)

# c=Chandu_one(10,100)


'''polymorphism'''

'''method over loading'''

# class India():
#     def India_info(self,a=None,b=None,c=None,d=None):
#         print(a,b,c,d)
        


# c=India()
# c.India_info(10,100,1000,10000)
# c.India_info(10,100,1000)
# c.India_info(10,100)
# c.India_info(10)
# c.India_info()

    
    
# class Chandu():
#     def __init__(self,a,b):
#         print(a,b)
#         self.a=a
#         self.b=b
# class Chandra(Chandu):
#     def __init__(self, a, b):
#         print(a,b)
#         super().__init__(a,b)
        
         
       
# c=Chandra(100,100)


'''object oriented programming is a way of computer programming using the idea of the objects 
to represents data and methods,
it is also ,an approach using the code clean neat and reusable code instead of reduandent one,

oop is bottom up approach
it is more securable
programme diveded into objects,
objects can move freely with in functions,
oop  makes use of access modifiers 
public private protected
it suports inheritance


oops features are 
class
object
inheritance
polymorphism
encapsulation
data abstarction

'''


# class Movies():
#     def __init__(self,movie,hero,heroin):
#         self.m=movie
#         self.h=hero
#         self.hn=heroin
        
#     def Movie_info(self):
#         print("movie =",self.m)
#         print("hero =",self.h)
#         print("heroin =",self.hn)
# m=input("movie =")
# h=input("hero =")
# hn=input("heroin =")

# m=Movies(m,h,hn)
# m.Movie_info()


'''
inheritance and it types
single inheritance
multilevel inheritance
multiple inheritance
hirarichal inheritance
'''

# class Parent():
#     def Parent_info(self):
#         print("this is parent info")
# class Child(Parent):
#     def Child_info(self):
#         print("child info ")
# c=Child()
# c.Parent_info()
# c.Child_info()

"""multlevel inheritance"""

# class Grand_father():
#     def Grandfather_info(self):
#         print("grandfather")
# class Father(Grand_father):
#     def Father_info(self):
#         print("father")
# class Child(Father):
#     def Child_info(self):
#         print("child")
        
# c=Child()
# c.Grandfather_info()
# c.Father_info()
# c.Child_info()


'''multple inheritance'''
# # class Father():
# #     def Father_info(self):
# #         print("father")
# # class Mother():
# #     def Mother_info(self):
# #         print("mother")
# # class Child(Father,Mother):
# #     def Child_info(self):
# #         print("child")
# # c=Child()
# # c.Father_info()
# # c.Mother_info()
# # c.Child_info()

'''hirarchical inheritance'''
# class Parent():
#     def Parent_info(self):
#         print("parent assests")
# class Child1(Parent):
#     def Child1_info(self):
#         print("child1")
# class Child2(Parent):
#     def Child2__info(self):
#         print("child 2")
        
# c=Child1()
# c.Parent_info()
# c.Child1_info()

# c2=Child2()
# c2.Parent_info()
# c2.Child2__info()


# class Chandra_base():
#     def __init__(self,a,b,c,d):
#         print(a,b,c,d)
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
        
# class Chandra_sub(Chandra_base):
#     def __init__(self, a, b, c, d):
#         super().__init__(a, b, c, d)
#         print(a,b,c,d,)
        
# c=Chandra_sub(10,100,1000,10000)


'''POLYMORPHISM'''
#method over loading

# class Fruits():
#     def Fruits_info(slef,apple=None,banana=None,cherry=None):
#         print(apple,banana,cherry)
# f=Fruits()
# f.Fruits_info(10,100,1000)
# f.Fruits_info(10,100)
# f.Fruits_info(10)
# f.Fruits_info()


# method over riding
# class India():
#     def Inida_info(self):
#         print("india")
# class Ap(India):
#     def Inida_info(self):
#         print("ap")
#         super().Inida_info()
# class Atp(Ap):
#     def Inida_info(self):
#         print("atp")
#         super().Inida_info()
# a=Atp()
# a.Inida_info()

'''encapsulation

public 
private __
ptotected _


BVB
'''