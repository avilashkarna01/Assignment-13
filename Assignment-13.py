# Q.1- Name and handle the exception occured in the following program: 

# a=3
 # if a<4:
    # a=a/(a-3)
     # print(a)

#solution
#Name of error="ZeroDivisionError will occured and it will handle by exception".
try:
	a=3
	if a<4:
		a=a/(a-3)
		print(a)
except Exception:
		print("an exception occured")
print("\n")


#Q.2- Name and handle the exception occurred in the following program: 
# l=[1,2,3]
# print(l[3])
#solution

#Name:"IndexError"
try:
	l=[1,2,3]
	print(l[3])
except Exception:
	print("An exception occured")
print("\n")


#Q.3- What will be the output of the following code:

#Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    raise  # To determine whether the exception was raised or not
#following error will be :" raise NameError("Hi there")  # Raise Error
 NameError: Hi there"
print("\n")

#Q.4- What will be the output of the following code:

 # Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
#Output will be:
-5.0
a/b result in 0
 
#Q.5- Write a program to show and handle following exceptions: 
# 1. Import Error

#before handling
import book
print("hello world")
#after handling
try:
 import python
 print("hello world")
except Exception:
   print("exception occured")
("hello world")

#2 . Value error
#before handling
n=int(input("enter a number"))
print("enter a number",n)

#after handling
try:
 n=int(input("enter a number:"))
 print(n)
except Exception:
 print("value error")

#3 . index error
#before handling
l=[1,2,3]
print(l[4])

#after handling
l=[1,2,3]
try:
  print(l[4])
except Exception:
  print("index error")

#Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18. 
#The code must keep taking input till the user enters the appropriate age number(less than 18).
class AgeTooSmallError(Exception):
 pass
a=1
while True:
  
 print("you have to enter the age 18 or more than 18")
 try:
  a=int(input("enter the age:"))
  if a<18:
   raise  AgeTooSmallError()
  print("Correct")
  break
     
 except Exception:
   print("Incorrect Age")
 	
	
