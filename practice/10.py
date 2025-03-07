'''
import json

def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def load_from_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

# Тестируем
students = [{"name": "Алиса", "age": 21}, {"name": "Боб", "age": 22}]
save_to_json(students, "students.json")
print(load_from_json("students.json"))  # [{'name': 'Алиса', 'age': 21}, {'name': 'Боб', 'age': 22}]
'''
import json
def stj(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)
    
def ltj(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    
students = [{"name": "Алиса", "age": 21}, {"name": "Боб", "age": 22}]
stj(students, 'students.json')
print(ltj('students.json'))