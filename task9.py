import re
def whiteSp(match):
    if match.start() == 0:
        return match.group(0)
    else:
        return ' ' + match.group(0)
text = input()
print(re.sub("[A-Z]", whiteSp, text))
