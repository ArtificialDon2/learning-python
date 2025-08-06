def remove_duplicates(numbers):
    unique = []
    for item in numbers:
        if item not in unique:
            unique.append(item)
    return unique
input = list(map(int, input("Enter text: ").split()))
result = remove_duplicates(input)
print(result)