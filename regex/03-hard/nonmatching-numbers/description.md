# Non-matching Numbers

Write a regex that detects whether a string contains two instances of `#nnn` where `n` stands for a single digit.
It is also important that both instances are different.

For example, the regex should match

* `#123 #456`
* `#123 #124`
* `..... #491 ..... #102 ......`
* `#123 #123 #456`

but it should reject

* `#123 #123`: numbers are not different
* `#123 #xyz`: `xyz` is different but does not consist of digits.
