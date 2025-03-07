def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    return len(words)
    
with open('text.txt', 'w') as file:
    file.write("Hello, World! \nPython is cool.")
    
print(count_words('text.txt'))
