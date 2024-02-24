import re
def upper_repl(match):
    return match.group(0)[1:].upper()
text = input()
print(re.sub("_[a-z]", upper_repl, text))
