import re
def toSnake(match):
    return '_' + match.group(0).lower()
text = input()
print(re.sub("[A-Z]", toSnake, text))
