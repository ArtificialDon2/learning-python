# Task 03 - Remove Duplicates

## Prompt
- Write a function remove_duplicates(numbers) that takes a list of integers and returns a new list with all duplicates removed, keeping only the first occurrence of each number.

## Notes
- `unique = []` -> new list where duplicates are stored.
- `.append()` -> appends an element to the end of the list.
- `.split()` -> splits input into a list of strings, like `["1", "2", "3"]`.
- `map(int, ...)` -> takes each string from that list and turns it into an int.
- `list()` -> converts the result of `map()` (which is an iterable) back into a list, so now you get `[1, 2, 3]`
- `map()` -> executes a specified function for each item in an iterable (iterable - an object that can be looped over)