# Fixed Point Numbers

In an earlier challenge we discussed how computers represent numbers, more specifically, integers.
But what if we need to work with real numbers, such as `3.1415`?

Think of measuring a length: you can express something as meters, but if you're working with small
distances, working with 0.002m or 0.0004m<sup>2</sup> quickly becomes tiring.
In these cases, you would simply switch units and work with cm or mm instead: 0.002m becomes 2mm, 0.0004m<sup>2</sup> becomes 4cm<sup>2</sup>.

In short, if you're dealing with small numbers, you simply consistently multiple them by the same factor.
When working with measuring units such as m, cm and mm, they help you remember what this factor is: centi corresponds to 100, milli to 1000.

The same trick can be applied in computers: if you need to represent `3.1415` while only having access to integers, you simply multiply it by 10000 giving `31415`.
To keep it simple, we always use the same multiplication factor, e.g., 10,000.
This is known as *fixed point math*: we have to imagine there's a decimal point in our integer numbers, which is at a fixed position for all such numbers.

An advantage of this approach as that a CPU does not need new instructions to deal with fixed point numbers:
for many operations we can pretend they are regular integers, and the results will be correct.

For example, `1.2 + 4.3` should equal `5.5`.
In fixed point math with factor 10,000, `1.2` would be represented by `12000` and `4.3` by `43000`.
Adding those values together as if they were regular integers gives `55000`, which corresponds to `5.5`, exactly what we need.
Same goes for comparisons: we can determine whether `1.2` is smaller than `4.3` by comparing `12000` and `43000`.
In other words, the factor does not interfere.

Fixed point math used to be quite popular in games, as they were a very efficient way of dealing with fractional numbers.
However, fixed point numbers have been supplanted by floating point numbers, which we'll discuss in the next challenge.

## Question

For some operations we cannot just pretend fixed point numbers can be handled in the same way as regular integers; a correction can be required.

Say we use fixed point numbers with factor 10000, how much is 12000 times 43000?
Give the *correct* result.
