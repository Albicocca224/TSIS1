import re
def match(text):
    pattern = r'ab{2,3}'
    match = re.search(pattern, text)
    if match:
        print("String matches")
    else:
        print("String does not match")
text = input("")
match(text)
