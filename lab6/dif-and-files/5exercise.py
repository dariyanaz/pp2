def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        file.writelines("\n".join(data))

data = ["Apple", "Banana", "Cherry"]
filename = "output.txt"
write_list_to_file(filename, data)
print("List written to", filename)
