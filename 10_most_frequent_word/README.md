# Task 10 - Most Frequent Word

## Prompt
- Write a function that takes a string and returns the word that appears most frequently.
- Ignore punctuation.
- If two words have the same frequency, return the one that appears first in the text.

## Notes
- `import string` -> lets you use Python’s built-in `string` module, which contains handy constants like `string.punctuation` (a string containing all common punctuation marks: `!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`).
- `text.translate(str.maketrans("", "", string.punctuation))`:
    1. `str.maketrans("", "", string.punctuation)` creates a translation table tellin Python: "delete every character that's in `string.punctuation`."
    2. `.translate(...)` uses that table to go through `text` and remove those characters.
It's a cleaner, more scalable replacement for chaining `.replace(",", "").replace(".", "")...` over and over.