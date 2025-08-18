import string
def is_strict_palindrome(text):
    text = text.lower().replace(" ", "")
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = ''.join(char for char in text if not char.isdigit())
    if text == text[::-1]:
        return "This is a palindrome."
    else:
        return "This is not a palindrome."
print(is_strict_palindrome(input('Check if palindrome: ')))