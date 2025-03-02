def copy_file(src, dest):
    with open(src, 'r') as source, open(dest, 'w') as destination:
        destination.write(source.read())

src = input("Enter source file: ")
dest = input("Enter destination file: ")
copy_file(src, dest)
print("File copied successfully.")
