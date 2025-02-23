import re

#1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
pattern = r'a*b*'
string = "ab aabb aaabbbb abbb a"
print(re.findall(pattern, string))


#2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
pattern = r'ab{2,3}'
string = "abb abbb abbbb a ab"
print(re.findall(pattern, string))

#3. Write a Python program to find sequences of lowercase letters joined with a underscore.
pattern = r'[a-z]+_[a-z]+'
string = "hello_world regex_test python_code"
print(re.findall(pattern, string))

#4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
pattern = r'[A-Z][a-z]+'
string = "Hello World Regex Python JAVA"
print(re.findall(pattern, string))

#5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
pattern = r'^a.*b$'
string = ["abc", "a123b", "ab", "acb", "aXb", "aB"]
for s in string:
    print(f"{s}: {bool(re.match(pattern, s))}")

#6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
pattern = r'[ ,.]'
string = "Hello, world. Python is great!"
print(re.sub(pattern, ":", string))

#7. Write a python program to convert snake case string to camel case string.
def snake_to_camel(s):
    return ''.join(word.capitalize() for word in s.split('_'))

print(snake_to_camel("hello_world_example"))

#8. Write a Python program to split a string at uppercase letters.
pattern = r'[A-Z][a-z]*'
string = "HelloWorldRegexTest"
print(re.findall(pattern, string))

#9. Write a Python program to insert spaces between words starting with capital letters.
pattern = r'([A-Z])'
string = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
print(re.sub(pattern, r' \1', string).strip())

#10. Write a Python program to convert a given camel case string to snake case.
pattern = r'([a-z])([A-Z])'
string = "ConvertThisCamelCaseToSnakeCase"
print(re.sub(pattern, r'\1_\2', string).lower())
