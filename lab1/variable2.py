#Variable Names

#A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

#Legal variable names:
myvar = "Dariya"
my_var = "Dariya"
_my_var = "Dariya"
myVar = "Dariya"
MYVAR = "Dariya"
myvar2 = "Dariya"

#Illegal variable names:
2myvar = "Dariya"
my-var = "Dariya"
my var = "Dariya"

#Multi Words Variable Names
#Variable names with more than one word can be difficult to read.
#There are several techniques you can use to make them more readable:
myVariableName = "Dariya"
MyVariableName = "Dariya"
my_variable_name = "Dariya"

#Many Values to Multiple Variables
#Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
#And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables
#The Python print() function is often used to output variables
x = "Python is awesome"
print(x)

#In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x = 5
y = "John"
print(x + y)

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)

#Global Variables

#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.

#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)