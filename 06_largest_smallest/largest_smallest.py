def largest_smallest(num):
    largest = max(num)
    smallest = min(num)
    return f"Largest: {largest}, smallest: {smallest}"
input = list(map(int, input('Enter a list of numbers separated by space: ').split()))
result = largest_smallest(input)
print(result)