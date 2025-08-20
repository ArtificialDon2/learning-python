import string
def unique_words(text):
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = ''.join(char for char in text if not char.isdigit())
    text = text.lower().split()
    unique = set(text)
    return unique
print (unique_words(input("Enter text: ")))