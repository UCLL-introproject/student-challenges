# Alternatives

This time, enter the following regex on [regex101](https://regex101.com/): `/a|b/`.
Experiment a bit to get an idea of how it works.

Now try `/abc|xyz/`.
There is some potential for ambiguity here: will it match `abc` and `xyz`, or
will it match `abcyz` and `abxyz` (i.e., the `|` only applies on the characters directly around it)?
Experiment to find out.

You can use parentheses as you would in mathematical formulae:
`/(abc)|(xyz)/` will match both `abc` and `xyz`,
while `/ab(c|x)yz/` will match `abcyz` and `abxyz`.

Write a regex that matches vowels.
