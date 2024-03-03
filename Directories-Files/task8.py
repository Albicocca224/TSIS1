import os
def delete_file(file_path):
    if not os.path.exists(file_path):
        print("The file doesnt exist")
        return
    if not os.access(file_path, os.W_OK):
        print("No access")
        return
    os.remove(file_path)
file_path = input("Enter path")
delete_file(file_path)
