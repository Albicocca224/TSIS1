import re
def match(text):
    pattern = r'\Aa.+b\Z'
    match = re.search(pattern, text)
    if match:
        print("String matches")
    else:
        print("String does not match")
text = input("")
match(text)
