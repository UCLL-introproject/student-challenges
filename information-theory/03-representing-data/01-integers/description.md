# Integers

We have all these bits at our disposition, but how do we actually represent useful information with them?
We first look at how we can represent numbers, as they will form the basis for everything else.

## Decimal Notation

There are many ways to represent numbers.
For example, there's the symbol 7 which stands for seven.
We can also simply represent it using `.......`: a very simple notation, but would become unwieldy for larger numbers.
There are also Roman numerals: `VII`.
There are however quite tricky when trying to multiply or divide.

As humans we settled on the "base 10 positional system", also known as the decimal system.
Base 10 means we have 10 digits: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` and `9`.
Positional means that the position of the digit in the number gives it a certain weight.

Let's simply start counting.
We start off with the 'smallest' digit, namely `0`.
To go one higher, we need to use the next digit in the series, which is `1`.
We can go on like this: `2`, `3`, `4`, `4`, `5`, `6`, `7`, `8`, `9`.
But now we ran out of digits...

We all know the solution to this conundrum: we need to use two digit numbers.
The number that comes after `9` then becomes `10`, and off we go: `11`, `12`, ..., `19`, `20`.
When we reach `99`, we need to add a third digit, giving us `100`.

## Binary Notation

This base 10 positional notation requires 10 digits.
But could we settle for 2? Like, just `0` and `1`?
Because that's really all we've got.

This is definitely possible and is called "base 2 positional notation" or just "binary" for short.
Zero is then represented as `0`, and one is `1`.
Now we've run out of digits, so we need to a second digit to the number: `10`, then `11`.
Already we've reached the point we need three digits: `100`, `101`, `110`, `111`.

So now you know how to increment a binary number.
But what if you need to find the binary notation for one thousand?
It wouldn't be very practical to apply the +1 rule a thousand times.

Luckily, there is a formula to quickly convert from decimal to binary and vice versa.
We won't go into the details here, you'll learn all about it in another course.

## Question

How much is `10110101011` plus two?
Give the answer in binary.
