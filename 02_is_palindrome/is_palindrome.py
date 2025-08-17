def is_palindrome(text):
    text = text.replace(" ", "").lower()
    if text == text[::-1]:
        return "This is a palindrome."
    else:
        return "This is not a palindrome."
input = input('Enter text: ')
result = is_palindrome(input)
print(result)


// version 2
import string
def is_palindrome(text):
    text = text.translate(str.maketrans("", "", string.punctuation)).lower().replace(" ", "")
    if text == text[::-1]:
        return "This is a palindrome."
    else:
        return "This is not a palindrome."
print(is_palindrome(input("Check if palindrome: ")))
