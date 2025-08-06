def repeating_words(text):
    word_count = {}
    duplicates = []
    for word in text:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
            if word_count[word] == 2:
                duplicates.append(word)
        else:
            word_count[word] = 1
    return duplicates
input = input('Enter text: ').split()
result = repeating_words(input)
print(result)