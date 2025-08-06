def count_each(text):
    count = {}
    text = text.split()
    for item in text:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count
input = input('Enter text: ')
result = count_each(input)
print(result)