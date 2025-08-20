# Task 12 - Unique Words

## Prompt
- Write a function that takes a sentence and returns the number of unique words in it.
    - Ignore punctuation and numbers.
    - Treat words in different cases as the same

## Notes
- `set()` -> data structure that keeps only unique things. It's short and clean but you lose counts.
- So the magic here is:
      - You don’t need an if word not in unique check
      - You don’t need to manage appending yourself
      - You don’t care about order, only uniqueness
