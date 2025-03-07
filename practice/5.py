
'''
import re
def is_valid_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9._]+\.[A-Za-z]{2,7}$'
    return bool(re.match(pattern, email))
print(is_valid_email('test@mail.com'))
print(is_valid_email("invalid@com"))
'''


import re
def number(nnn):
    pattern = r'^[A-Za-z0-9.%+-]+\@[A-Za-z0-9._]+\.[A-Za-z]{2,7}$'
    return bool(re.match(pattern,nnn))
print(number('gjkaskjasgjksd@hhjsfc.com'))