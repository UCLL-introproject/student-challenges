# Hexadecimal

Hexadecimal notation uses 16 digits: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `A`, `B`, `C`, `D`, `E` and `F`.
As you see, we had to borrow some characters from the alphabet since we ran out of decimal digits, and we didn't want to bother
inventing six new symbols.

Counting again follows the same rules:

| Decimal | Hexadecimal |
| ------- | ----------: |
| 0       |           0 |
| 1       |           1 |
| 2       |           2 |
| 3       |           3 |
| 4       |           4 |
| 5       |           5 |
| 6       |           6 |
| 7       |           7 |
| 8       |           8 |
| 9       |           9 |
| 10      |           A |
| 11      |           B |
| 12      |           C |
| 13      |           D |
| 14      |           E |
| 15      |           F |
| 16      |          10 |
| 17      |          11 |
| 18      |          12 |
| 19      |          13 |
| 20      |          14 |

Whereas one octal digit corresponds to three bits, one hexadecimal digit corresponds to four bits.
This is quite nice, because a byte consists of eight bits, meaning that we can write bytes as two hexadecimal digits.
For this reason, hexadecimal is quite often used to represent binary data: it is much more compact than binary and can easily be converted.

Below is a series of bytes in hexadecimal notation.
Which byte is the largest?

```text
05 79 5C 98 7A 41 00 67 F4 9F 31
```
