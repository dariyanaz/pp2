def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for _ in file)

filename = input("Enter the file path: ")
print("Number of lines:", count_lines(filename))
