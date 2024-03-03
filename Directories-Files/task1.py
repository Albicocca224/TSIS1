import os
def list_direc(path):
    directories = []
    files = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            directories.append(item)
        else:
            files.append(item)
    all_items = os.listdir(path)
    return directories, files, all_items
path = "C:\Program Files (x86)"
directories, files, all_items = list_direc(path)
print("Directories:")
print(directories)
print("\nFiles:")
print(files)
print("\nAll:")
print(all_items)
