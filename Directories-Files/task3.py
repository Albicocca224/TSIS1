import os
def check_path(path):
    if os.path.exists(path):
        print("Path exists")
        dirname, filename = os.path.split(path)
        print("Directory:", dirname)
        print("Filename:", filename)
    else:
        print("Path doesnt exist")
given_path = input("Enter path: ")
check_path(given_path)
