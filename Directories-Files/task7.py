def copy_file(source_file, clone_file):
    with open(source_file, 'r') as source:
        contents = source.read()
        with open(clone_file, 'w') as clone:
            clone.write(contents)
    print("File copied successfully!")
source = "sample.txt"
clone = "A.txt"
copy_file(source, clone)
