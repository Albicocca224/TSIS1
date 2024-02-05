def is_palindrome(s):
    cleaned_str = ''.join(s.lower().split())
    return cleaned_str == cleaned_str[::-1]
word = "madam"
result = is_palindrome(word)
if result:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
