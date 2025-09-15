# Greediness

On [regex101](https://regex101.com/), enter `/<.+>/` as regex and `<abc> ... <def>`  as input string.
We would like two find two matches: `<abc>` and `<def>`.
However, the `.+` matches as much as it can (which is called *greedy matching*), and we end up with only a single, overlong match.

One way to solve this is to replace `.` by a pattern that does not match `>`.
Another way is to use a non-greedy version of `.+`, written `.+?`: instead of the longest match possible, it will look for the shortest match possible.

Write a regex that can detect matching HTML tags.
For example, `<a>...</a> xxxxx <tag>foo</tag>` should match both `<a>...</a>` and `<tag>foo</tag>`.
Do not worry about nested tags such as `<a><b></b></a>`: only matching the outer tags is sufficient.
