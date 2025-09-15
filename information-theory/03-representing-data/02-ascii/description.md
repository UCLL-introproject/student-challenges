# ASCII

How is text, like this question, represented using `0`s and `1`s?
Do we perhaps draw the letters, like many little black and white images one after the other?
Or is there a better way?

Memory was scarce and every bit counted.
So people set out to find a rather minimal set of characters which they deemed would suffice.

* Letters are quite important, both upper (A-Z) and lower case (a-z).
* Digits might also come in handy (0-9).
* Punctuation (comma, dot, parentheses, question mark, exclamation point, etc.).
* Mathematical symbols (`+`, `-`, `*`, `/`, `=`, `<`, `>`).
* Space itself should definitely also be a character.
* Since we don't want all text to be on a single line, we also need a character symbolizing a line ending.
* Special control characters like backspace were also included.
  Originally, backspace was literally a "backwards space", a way of going back left,
  so that it became possible to print two characters in the same place, which is useful for ácçènts, or ~~crossing out text~~.

With all this, we have 70+ different characters we need to be able to represent.
We need to assign a *unique* binary code to each of these characters.
With 6 bits we can only make 64 different codes, so we need at least 7 bits, which allows for 128.

Now comes the job of deciding which 7 bit sequences correspond to which character.
Since it was essential that everyone agrees on this bits-character correspondence,
an official standard was developed, called [ASCII](https://en.wikipedia.org/wiki/ASCII#Control_characters).
Since every bit sequence also represents a number, we can also say that ASCII assigns a unique number between 0 and 127 to each character.

ASCII was carefully designed so as to make certain functionality easy to implement:

* All uppercase letters are given consecutive numbers: `A` is 65, `B` 66, etc.
  The same is true for lowercase letters: `a` is 97, `b` is 98, etc.
  This makes it easy to check if a character is a letter (`65 <= c <= 90 or 97 <= c <= 122`).
  Iterating over all letters also became easy.
* Converting from upper to lower case and vice versa is a matter of flipping a single bit.
* Characters are grouped in blocks, and the first three bits determine which block.
  For example, uppercase letters all fit in the `010` block.

EBCDIC, an alternative to ASCII, did not share these qualities, which helped bring its own demise.

## Extended ASCII

ASCII is a 7 bit encoding.
However, at some point, it was settled that bytes are 8 bits, not 7.
While it is possible to cram 8 ASCII characters into 7 bytes, it is quite the hassle.
Instead, it was decided that a character would simply get a free upgrade in the form of an extra bit: every character now got an 8 bit code.

If the eighth bit was zero, the numerical value does not change and the meaning of each bit sequence remains the same as in regular ASCII: 65 was still `A`, 66 still `B`, etc.
However, it the eighth bit was set to one, the range 129 to 255 opened up and 128 extra codes became available.
The question is: what characters should they represent.

If you take a closer look at the ASCII table, you'll notice that it is quite English-centric.
English does not have accented letters (é, è, á, à, etc.), umlauts (ë, ü), German ßs, Danish øs or Icelandic þs.
Those extra 128 spots would be ideal to represent those non-English letters.
However, it turned out that 128 extra letters is not sufficient to contain all the weird letters of even just the European languages, let alone Chinese, Thai, Arabic, etc.

Thus began the great mess: multiple versions of Extended ASCII began to be developed (called code pages), each specialized in certain languages.
The problem was that when given a some text, it was not mentioned which code page was used.

For example, é was represented by 130 in [Code page 437](https://en.wikipedia.org/wiki/Code_page_437),
by 233 in [Windows-1252](https://en.wikipedia.org/wiki/Windows-1252)
and by 142 in [Mac OS Roman](https://en.wikipedia.org/wiki/Mac_OS_Roman)
This is why Amélie and Björn saw their names mangled to AmΘlie and Bj÷rn all the time.
Those were sad times for people with accents in their names.

## Question

You are given a text file with the following contents, shown in binary:

```text
01000011011011110111001001110010011001010110001101110100
```

What text does this represent?
