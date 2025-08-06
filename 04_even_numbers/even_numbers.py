def even_numbers(list):
    unique = []
    for item in list:
        if item % 2 == 0 and item not in unique:
            unique.append(item)
    return sorted(unique)
input = list(map(int, input('Enter numbers separated by space: ').split()))
result = even_numbers(input)
print(f"Even  numbers in ascending order: {result}")