# Exactly Same Five

What regular expression can we use to determine if a string contains exactly five the same characters in a row, but not more?
For example, `abc55555def` is valid, because there are exactly 5 consecutive `5`s.
However, `abc555555def` should be rejected: there's one five too many.
`5abc55555def` should be accepted, because the sixth `5` is separated from the series of 5s.
