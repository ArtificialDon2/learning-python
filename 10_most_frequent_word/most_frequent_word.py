import string
def most_frequent_word(text):
    wordUsed = {}
    text = text.translate(str.maketrans("", "", string.punctuation))
    for word in text.split():
        if word in wordUsed:
            wordUsed[word] += 1
        else:
            wordUsed[word] = 1
    mostFrequent = max(wordUsed, key=wordUsed.get)
    return mostFrequent
print(most_frequent_word(input('Enter text: ')))