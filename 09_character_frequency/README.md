# Task 09 - Character Frequency

## Prompt
- Write a function that takes a string and returns the most frequent character (ignoring spaces).
- If there’s a tie, return any one of the most frequent characters.

## Notes
- `max()` -> returns the item with the highest value
- When you give `max()` just a collection like `max(charUsed)`, it compares the items directly (in this case, the keys of the dict) and returns the “largest” according to Python’s default ordering — for strings, that’s alphabetical order, which isn’t what we want.
- By adding `key=charUsed.get`, we tell `max()`:

“Don’t compare the keys themselves — instead, look at the value in charUsed for each key and compare those.”
- Mechanics:
1. `charUsed` is a dictionary like `{'a': 5, 'b': 3, 'c': 5}`.
2. When `max()` goes through the keys `('a', 'b', 'c')`, it calls `charUsed.get(key)` for each key.
3. That returns the value `(5, 3, 5)` which is what `max()` uses to decide which key to return.
4. The key whose value is largest gets returned.
