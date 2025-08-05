# Task 01 - Count Vowels

## Prompt
- Write a function `count_vowels(text)` that takes a string and returns the number of vowels (`a, e, i, o, u`) in it.
- Make sure it works for both lowercase and uppercase letters.

## Notes
- `def count_vowels(text):` → We’re saying: “I’m defining a function that takes a parameter called `text` — the user will give me a string.”
- Use `.lower()` to simplify matching — avoids checking both `A` and `a`.
- Loop through the string, check if each character is in `'aeiou'`, and count it.