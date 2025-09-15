# Octal

Binary uses 2 digit, ternary 3.
We now just straight to 8:

| Decimal | Octal |
| ------- | ----: |
| 0       |     0 |
| 1       |     1 |
| 2       |     2 |
| 3       |     3 |
| 4       |     4 |
| 5       |     5 |
| 6       |     6 |
| 7       |     7 |
| 8       |    10 |
| 9       |    11 |
| 10      |    12 |
| 11      |    13 |
| 12      |    14 |
| 13      |    15 |
| 14      |    16 |
| 15      |    17 |
| 16      |    20 |
| 17      |    21 |
| 18      |    22 |
| 19      |    23 |
| 20      |    24 |

Octal is admittedly not widely used, but it is typically a supported notation by programming languages.
An advantage is that it is easily convertible to binary and back, since one octal digit corresponds to three binary digits.

For example, let's say we have the binary data

```text
100111001010000011110000
```

We split it up in groups of 3:

```text
100 111 001 010 000 011 110 000
```

We can now translate each group separately:

```text
100 111 001 010 000 011 110 000
  4   7   1   2   0   3   6   0
```

Such a nice correspondence between digits does not exist between most notations.

Convert the octal number `51370041` to binary.
