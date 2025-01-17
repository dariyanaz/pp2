#In programming, data type is an important concept.
#Variables can store data of different types, and different types can do different things.
#Python has the following data types built-in by default, in these categories:
#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType

#You can get the data type of any object by using the type() function:
#Print the data type of the variable x:
x = 5
print(type(x))

#In Python, the data type is set when you assign a value to a variable:
x = "Hello World" #str
#display x:
print(x)
#display the data type of x:
print(type(x)) 

y = ["apple", "banana", "cherry"] #list
#display x:
print(y)
#display the data type of x:
print(type(y)) 


#If you want to specify the data type, you can use the following constructor functions:
z = str("Hello World")
#display x:
print(z)
#display the data type of x:
print(type(z)) 
