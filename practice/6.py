'''import re

def extract_phones(text):
    pattern = r"\+?\d[-()\d\s]+"
    return re.findall(pattern, text)

# Тестируем
text = "Мои контакты: 8-900-123-4567, +7(495)555-55-55, 77777777777."
print(extract_phones(text))  # ['8-900-123-4567', '+7(495)555-55-55', '77777777777']
'''

import re
def isnumber(number):
    pattern = r'\+?\d[-()\d\s]*\d'
    return re.findall(pattern, number)
text = "guiguic we58979697 87779798979 +8 "
print(isnumber(text))