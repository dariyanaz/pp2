#Python Operators
#Operators are used to perform operations on variables and values.
#In the example below, we use the + operator to add together two values:
print(10 + 5)

#Python divides the operators in the following groups:
#Arithmetic operators: +, -, *, /, %, **, //  (Arithmetic operators are used with numeric values to perform common mathematical operations)
#Assignment operators: =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=  (Assignment operators are used to assign values to variables)
#Comparison operators: ==, !=, >, <, >=, <=  (Comparison operators are used to compare two values)
#Logical operators: and, or, not  (Logical operators are used to combine conditional statements)
#Identity operators: is, is not  (Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location)
#Membership operators: in, not in  (Membership operators are used to test if a sequence is presented in an object)
#Bitwise operators: &, |, ^, ~, <<, >>  (Bitwise operators are used to compare (binary) numbers)


#Operator Precedence
#Operator precedence describes the order in which operations are performed.

#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3))

#Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:
print(100 + 5 * 3)

'''
The precedence order is described in the table below, starting with the highest precedence at the top:

Operator	Description	Try it
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR	

If two operators have the same precedence, the expression is evaluated from left to right.
'''

#Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:
print(5 + 4 - 7 + 3) #5