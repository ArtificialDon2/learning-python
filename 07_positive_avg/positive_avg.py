def positive_avg(num):
    positiveList = []
    for item in num:
        if item > 0:
            positiveList.append(item)
    if len(positiveList) == 0:
        return "No positive numbers."
    avg = sum(positiveList) / len(positiveList)
    return avg
input = list(map(int, input('Enter numbers separated by space: ').split()))
result = positive_avg(input)
print(result)