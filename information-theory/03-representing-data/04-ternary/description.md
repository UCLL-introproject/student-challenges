# Ternary

We previously discussed binary (also known as base 2 positional notation).

| Decimal | Binary |
| ------- | -----: |
| 0       |      0 |
| 1       |      1 |
| 2       |     10 |
| 3       |     11 |
| 4       |    100 |
| 5       |    101 |
| 6       |    110 |
| 7       |    111 |
| 8       |   1000 |
| 9       |   1001 |
| 10      |   1010 |

Make sure to understand the pattern of how binary numbers are generated:
we start at the very right, and increment the digit.
If it's `0`, it becomes `1`.
If it's `1`, we are out of digits, so we make in `0` and move one digit to the left, where we apply the same logic.

Let's try the same, but now with three digits:

| Decimal | Ternary |
| ------- | ------: |
| 0       |       0 |
| 1       |       1 |
| 2       |       2 |
| 3       |      10 |
| 4       |      11 |
| 5       |      12 |
| 6       |      20 |
| 7       |      21 |
| 8       |      22 |
| 9       |     100 |
| 10      |     101 |

Ternary is not really used anywhere, but since it was a good step up from binary on our way to octal.

What would be 15 in ternary?
