# Task 11 - Is Strict Palindrome

## Prompt
- Write a function is_strict_palindrome(text) that:
    - ignores spaces, punctuation, numbers, and symbols
    - only checks the letters (case-insensitive)

## Notes
- `(char for char in text if not char.isdigit())`:
    - `for char in text` - loop throuhg each character in text
    - `if not char.isdigit()` - only keep characters that are not digits. `char.isdigit()` returns True if the character is a number. `not` flips it, so we keep only those characters that are not digits
    - `char` at the front - this is what we're outputting for each valid iteration
- `join()` - takes all items in an iterable and joins them into one string