import string
def generateFiles():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, "w") as file:
            file.write("hello world")
generateFiles()
