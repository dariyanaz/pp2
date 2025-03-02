import os

def path_info(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print("Path does not exist.")

path = input("Enter the path: ")
path_info(path)
