#Boolean Values
#Booleans represent one of two values: True or False.
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

#Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
#Evaluate Values and Variables
#Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

#Evaluate two variables:
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.

#The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#You can create functions that returns a Boolean Value:
def myFunction() :
  return True

print(myFunction())

#You can execute code based on the Boolean answer of a function:
#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))