# Floating Point Numbers

Fixed point numbers have a severe limitation: the same multiplication factor must be used everywhere (that's what makes it *fixed*).
If different numbers were to use different factors, we'd have to store that which factor somewhere for each number.
The math would become more complicated: for each operation, we'd have to check if the numbers are using the same factor and if not, perform the necessary multiplications to make it so.
Therefore, having to deal with different factors would make fixed point math much less efficient.

However, it would actually be quite useful to be able to use different factors.
For example, very small numbers like 0.000000001 we would need a much higher factor, 10,000 is not sufficient.
But if we choose a large factor, what happens if we need to represent a large number such as 1,000,000,000?
Integers have a maximum size: what we win in precision, we lose in range.
Being able to pick the right factor for each number would be ideal.

This ability to have number-dependent factors is called *floating point*: the decimal point's position "floats around" depending on your needs.

Good news: this floating-point math is directly supported by CPUs, meaning we can have both flexibility *and* efficiency.

## Comparison Integers and Floating Points

Let's compare 64 bit integers and 64 floating point numbers.
These are two radically different ways of representing numbers: they require different circuitry on the CPU and mathematical operations must be done using different instructions.

64 bit integers can take on 2<sup>64</sup> numbers, so if we restrict ourselves to positive numbers,
we can represent numbers from 0 up to 18,446,744,073,709,551,616, or approximately 18&times;10<sup>18</sup>.
The precision is lacking a bit: the smallest increment between two numbers is 1, i.e., we cannot represent a number between 0 and 1.

A 64 bit floating point number, however, can get as large as 10<sup>308</sup>.
Very small numbers are also possible: the smallest nonzero number is 10<sup>-308</sup>.

## Why Not Always Floating Point?

Based on this comparison, it might seem that we should simply always be using floating points: far greater range and far greater precision, same efficiency thanks to hardware support.
To get a better feeling for the limitations of floating points, imagine you're working in decimal but only have room for a 3 digit integer and a unit, such as millimeter, micrometer, nanometer, kilometer, etc.
Now say you want to represent 1.243m.

* The rules say you must only work with integer values, meaning you either have to go with 1m or 2m.
* Decimeter is better: 12cm is rather close to our intended value, but we're needlessly imprecise: we have room for 3 digits and only use 2.
* Let's try centimeter: 124cm is very close, but we will have that last digit 3 that we miss.
* Millimeters should allow for that 3, but at what cost: 1243mm would be ideal, but having being restricted to three digits, we can only go as far as 999mm.

Floating point numbers are therefore not as precise as they may seem.
While they can represent very large numbers, the can only store a limited number of significant digits.
Whereas integers can represent all values between 0 and 2<sup>64</sup>, floating points have a larger range, but there are many gaps of unrepresentable values inside this range.

In a machine, floating point numbers are stored in binary, and the unit is actually just an exponent: meter would correspond to 0, kilometer to 3, millimeter to -3, etc.
The exponent itself has a certain range of values it can take (-1022 to 1023).

## Question

Say we use floating points using decimal notation and three digits.
The exponent itself can range from -9 to 9.

We start off with the value 0 then keep adding 1 to it: the number grows from 0 to 1 to 2 to 3 to ...
We add 1 a billion times.
What is the final result?
Write your answer as a regular decimal number, e.g., if you think the end result is one billion, write `1000000000` in `solution.txt`.
