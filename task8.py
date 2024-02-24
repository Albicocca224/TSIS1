import re
def splitUpper(text):
    return re.findall('[A-Z][^A-Z]*', text)
text = input()
print(splitUpper(text))
