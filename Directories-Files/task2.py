import os
def check_access(path):
    if os.access(path, os.R_OK):
        print("Read: Yes")
    else:
        print("Read: No")
    if os.access(path, os.W_OK):
        print("Write: Yes")
    else:
        print("Write: No")
    if os.access(path, os.X_OK):
        print("Execute: Yes")
    else:
        print("Execute: No")
path = input("Enter path")
check_access(path)
