# Base64

This explanation might get a little bit confusing, but we'll do our best to keep things as clear as possible.
Do read this text with the necessary focus, though.

## Notation Size

We have some data and wish to write it down in human readable form.
One possibility is to write it in binary: `01100110`.
As you can see, the data is just 8 bits, or 1 byte, long.
However, writing it down like this actually requires eight characters, so using binary representation takes 8 times more storage.

We can also write it down in decimal instead, this gives us `102`.
We needed three characters: `1`, `0` and `2`, so 3 &times; 8 = 24 bits = 3 bytes of storage.

We can go further and use hexadecimal: that would be `66`.
Only two characters necessary, way more efficient than the binary notation.

Technically, we could also just write `f`, because the ASCII table associates our value with this letter.
However, there are ASCII characters that are invisible (e.g., 0-31).
Had our data been equal to `0`, ASCII would have been of no use.
We need a representation that can be used for *any* data.

So, hexadecimal seems most efficient: if we have `N` bytes of actual data, its textual form will take `2N` bytes.
However, if we need to transfer a lot of data, having our storage needs double might be too much.

One could just say that we should simply transfer large amounts of data in its original form, no need to turn it into a textual format first.
If we need to be able to read it, there is plenty software do help us with that.
That would be a very reasonable thing to do, and is also what happens in practice.
Most of the time anyway.

Some technologies, such as SMTP (email), insist that data be actual readable text.
For example, if you attach an image to your email, that image's data is not text, and it will be rejected.
So, converting data into hexadecimal would be a solution, as it uses only `0`-`9`, `A`-`F`, which is all text.
But, as noticed before, it sacrifices storage.

As we went from binary to hexadecimal, you probably noticed that the number of digits necessary to encode a number went down.
What if we add more digits to hexadecimal?
We only use 6 letters, what if we also used the rest of the alphabet as digits? A base 36 notation?

That's exactly what we will do, but we can also make the distinction between lower case and upper case,
so we get a 10 + 26 + 26 = 62 base notation.
But 62 is a weird number, it'd be nicer if it'd be 64, so we also add `+` and `/` as digits.
Now a single base 64 digit corresponds to 6 bits, which is a nice property to have:
it is easier to convert between notations, and we can more easily end up with a whole number of bytes.

The digits are then `A` to `Z`, `a` to `z`, `0` to `9` and finally `+`, `/`.

## Using Base64

The goal is for us to be able to rewrite raw data of any size into Base64.
Say we have 3 bytes:

```text
10010110 11001010 01001110
```

To convert to Base64, we have to rearrange them into groups of 6 bits:

```text
100101 101100 101001 001110
```
Each group of 6 bits corresponds to a Base64 digit:

```text
100101 101100 101001 001110
l      s      p      O
```

If the data's size is a multiple of 3 bytes, we can always rearrange the bits in groups of 6
and 3 bytes of data will be converted to 4 bytes of Base64 notation.

But what if there are, say, 4 bytes of data?

```text
Four bytes of data, bits grouped by 8
10010110 11001010 01001110 10000110

Grouped by 6
100101 101100 101001 001110 100001 10????
```

Same with 5 bytes of data:

```text
Five bytes of data, bits grouped by 8
10010110 11001010 01001110 10000110 11001111

Grouped by 6
100101 101100 101001 001110 100001 101100 1111??
```

In these cases, we will encode to Base64 as if the missing bits (indicated by `?`) are actually `0`.
When converting back from Base64, we need to be aware of these added `0`s so that we don't think they are actually part of the data.
The solution to this is padding the Base64 string with `=` until there is a multiple of 4 Base64 digits.

This gives in case of 5 bytes:

```text
Four bytes of data, bits grouped by 8
10010110 11001010 01001110 10000110

Grouped by 6
100101 101100 101001 001110 100001 100000
l      s      p      O      h      g      = =
```

and 6 bytes:

```text
Five bytes of data, bits grouped by 8
10010110 11001010 01001110 10000110 11001111

Grouped by 6
100101 101100 101001 001110 100001 101100 111100
l      s      p      O      h      g      8      =
```

When decoding, the number of `=` indicates how many pairs of `0`s have been added as padding and should be ignored.

## Question

Decode the given file and find out where it's from.
