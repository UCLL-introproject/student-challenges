# Anchors

By default, a regex will look for a match inside the string.
For example, `/a/` will find the `a` inside `xxxxxaxxxxxx`.
Sometimes, however, you want the regex to match the whole string.

Anchors are special patterns that don't actually match characters, but rather positions:

* `^` matches the beginning of the string.
* `$` matches the ending.

`/^a` therefore matches only `a`s at the very beginning of a string.

Write a regular expression that checks that a string is exactly five characters long.
