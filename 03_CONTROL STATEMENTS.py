#conditional statements
'''
1.if
2.if-else
3.if-elif-else
4.nested-if-elif-else
5.shorthand if else
'''

# x=int(input("enter number ?:"))
# y=int(input("enter number ?:"))

# if x<y:
#     print("x less than to y")
# else:
#     print("x is greater than to y")













# num=int(input("enter the num :"))

# if num%2==0:
#     print("this is even")
# else:
#     print("this is odd")











# marks=int(input("enter the marks :"))

# if marks>=90 and marks=<100:
#     print("a grade")
# elif marks>=80 and marks=<90:
#     print("b grade")
# elif marks>=60 and marks=<80:
#     print("c grade")
# elif marks>=35 and marks=<60:
#     print(" d grade")
# else:
#     print("fail")





# genearte username and password using bt if conditions

# username="codingrad"
# pass_word=1234

# user=input("enter your name :")
# pass_w=int(input("enter password :"))

# if username==user and pass_word==pass_w:
#     print("log in success")
# else:
#     print("log in fail,please try again")




# x=100; y=150; z=200

# if x<y and y<z:
#     print("true")
# elif x<y or y<z:
#     print("elif")
# else:
#     print("else")

# # short hand if else

# print("if") if x<y and y<z else print("else")



'''
loop conditions

while loop
for loop
'''

# x=1
# while x<10:
#     print("this is if while")
#     x=x+1
# else:
#     print("this is else while")

# i=6
# while i<20:
#     print(i)
#     i=i+1
# else:
#     print("this is closed else")
    
    
    
# i=100
# while i<121:    
#     print(i)
#     i +=1
# else:
#     print(" hello end")
    
    
    
    
'''applying jumping statements on while'''
#break
 
# i=1

# while i<11:
#     print(i) 
#     if i == 6:
#         break  #break the condition counting at 6
#     i=i+1
    
 
# x=20

# while x<30:
#     print(x) 
#     if x==27:
#         break  #condition breaked at 27
#     x=x+1
    
# else:
#     print("break")









# continue

# i=1

# while i<11:
#     i=i+1
#     if i==6:
#         continue  #stop continue and starts remianing numbers
#     print(i)
    
    
    
# x=20
# while x<30:
#     x=x+1
#     if x==25:
#         continue
#     print(x)   
    


#pass    
# x=1
# while x<10:
#     pass
    


# #break
# i=1
# while i<11:
#     print(i)
#     if i==5:
#         break
#     i=i+1  
    
    
# a=10

# while a<16:
#     print(a)   
#     if a == 12:
#         break
#     a=a+1
    
    
    
    
# x=1
# while x<11:
#     if x==3:
#         continue
#     x=x+1
#     print(x)    
    
 
 
 
 
 
 
 
 
 
   
# i=100

# while i <105:
#     if i == 103:
#         continue
#     i=i+1
#     print(i)    
    
    
    
# i=100
# while i <106:
#     print(i)  
#     if i==105:
#         break
#     i=i+1


#nested while loops

# i=1
# while i<11:
#     j=1
#     while j<11:
#         print(i,"*",j,"=",i*j)
    
#         j=j+1
#     i=i+1
#     print ("\n")



# i=1
# while i <3:
#     j=1
#     while j<5:
#         k=1
#         while k<5:
#             print(i,"+",j,"+",k,"=", i+j+k)
#             k=k+1
#         j=j+1
#     i=i+1 
#     print("\n")




#multiplication table

# i=1
# while i<=10:
#     j=1
#     while j<=10:
#         print (i*j)       
#         j=j+1
#     i=i+1
#     print("\n")




'''for loops'''

# for i in range(1,10,2):
#     print(i)

# for kiran in "string":
#     print(kiran)
    
    
# for i in "chandra":
#     print(i)


# for i in range(1,10):
#     for j in range(1,10):
#         print(i*j,end=" ")
#     print( )
        
        
        
# for i in range(1,11):
#     for j in range(1,i+1):
#         print(j,end="")
#     print( )