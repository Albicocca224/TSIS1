import re
text=input()
print(re.sub("[\s,.]", ";", text))