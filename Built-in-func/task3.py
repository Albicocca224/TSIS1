str=str(input())
str=str.lower()
str=str.replace(" ", "")
print(str)
if str==str[::-1]:
    print("palindrome")
else:
    print("not palindrome")