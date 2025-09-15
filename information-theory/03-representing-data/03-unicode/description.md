# Unicode

A new character encoding standard was clearly necessary to resolve the issues caused by having multiple encodings.
This led to the development of Unicode.

Where ASCII was only capable of encoding 128 characters, Unicode has room for 1,114,112.
Unicode works with so-called *codepoints*, which is really just a fancier name for "a number that represents a character".
So there are 1,114,112, each of which can be associated with a character.

For compatibility reasons, the first 128 codepoints were chosen to coincide with ASCII: for example, codepoint 65 in Unicode represents the same character `A` as ASCII.
As of version 16.0, only 154,998 codepoints have actual characters assigned to them, so there's still plenty of space available for more characters.

Unicode has [support](https://www.unicode.org/charts/) for many writing systems and symbols:

* All modern writing systems are included, such as the Latin alphabet, Cyrillic, Arabic script, ideographs used in Chinese, Japanese, Korean and Vietnamese, ...
* Historic scripts such as hieroglyphics and Linear A.
* Emojis.
* Mathematical symbols.
* Characters to draw boxes.
* Game symbols for chess, dominos, mahjong, cards.
* And many more.

## UTF-8

If we do the math, we find out that in order to have 1,114,112 different codepoints, we need at least 21 bits to be able to represent them all.
This is a strange number of bits, since it's not a multiple of 8.
Why didn't they just go for 24 bits and have full 3 bytes worth?

Having 3 bytes per characters may be a bit too decadent, memory consumption wise.
Yet that's what's needed if we want our many codepoints.
Fortunately, a solution was found: variable length encoding.

Ideally, the most common characters should only consume less bytes than rarely used characters.
This is exactly how the [UTF-8](https://en.wikipedia.org/wiki/UTF-8) format operates:
for the first 128 codepoints, only one byte is needed, and as we reach into the higher codepoints, we can need up to 4 bytes.
This approach makes UTF-8 also fully compatible with ASCII: text encoded in ASCII can also be interpreted as if it were UTF-8.

There also exist [UTF-16](https://en.wikipedia.org/wiki/UTF-16) and [UTF-32](https://en.wikipedia.org/wiki/UTF-32)
which use different approaches to represent the different Unicode codepoints.
In practice, `UTF-8` is by far the most used.

## Question

Find out what the Unicode codepoint of `↭` is.
Give your answer as a number written in decimal notation.
