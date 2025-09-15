# Contains xyz

Visit [this website](https://regex101.com/): it allows you to interactively experiment with regexes.

In the regular expression input, enter `a`.
In the test string box, add some random text, which preferably contains a number of `a`s.
You will notice that all `a`s are highlighted: these are the parts that match the pattern.

In order to distinguish between a regular expression `a` and some text `a`, we will surround the former with slashes: `/a/` is a regex, `a` is just text.

The regex `/a/` is a very basic one: it simply means "I match the letter `a`", which is why all `a`'s in the test string are highlighted.
See what happens if you add more letters to the regex.

What regular expression can we use to determine if some text contains `xyz`?
