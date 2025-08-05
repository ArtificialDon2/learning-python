def count_vowels(text):
    vowels = "aeuoiAEUOI"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
input = input('Enter text: ')
result = count_vowels(input)
print(f"Number of vowels: {result}")