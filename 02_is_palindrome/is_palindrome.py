def is_palindrome(text):
    text = text.replace(" ", "").lower()
    if text == text[::-1]:
        return "This is a palindrome."
    else:
        return "This is not a palindrome."
input = input('Enter text: ')
result = is_palindrome(input)
print(result)