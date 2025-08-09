def most_frequent_char(text):
    charUsed = {}
    text = text.replace(" ", "")
    for char in text:
        if char in charUsed:
            charUsed[char] += 1
        else:
            charUsed[char] = 1
    mostFrequent = max(charUsed, key=charUsed.get)
    return mostFrequent
print(most_frequent_char(input('Enter text: ')))