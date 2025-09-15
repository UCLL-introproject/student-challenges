# 32 vs 64 bit

Processors are characterized by their "bitness": the first Intel CPUs were 16 bit, which then evolved to 32 bit.
These days our CPUs are 64 bit.
But what does this number mean?
And when will we make the jump to 128 bit?

Quick disclaimer: the explanation below is a simplified take on reality.
We try to keep these assignment texts short, so it is inevitable that we ignore certain technical details.

## Word Size

A 32 bit CPU can deal with 32 bit numbers directly: it contains the circuitry to perform operations on them with a single instruction.
This means that a 32 bit CPU can deal directly with numbers of up to 2<sup>32</sup> ~= 4 billion (we ignore floating points here which can go much higher but at the cost of precision).
If we need the CPU to work with larger numbers, then we need to cut these large numbers up in smaller parts that fit in 32 bits and have the CPU perform multiple instructions on them.
Any processor can therefore perform calculations on arbitrarily large numbers, but it will take more instructions and therefore be slower.

So, one could say that one advantage of a 64 bit CPU over a 32 bit system is that it can deal with larger numbers more efficiently.
However, this was not the main reason the switch from 32 to 64 bit was made.

## Memory Addressing

Your computer needs memory to store data in.
This memory consists of bytes, a lot of them: if you have 16 GiB RAM, you have more than 16 billion bytes of memory to work with, each of which can store a number between 0 and 255.

Each byte has an address, i.e., a number that uniquely identifies it.
The first byte has address `0`, the next one `1`, etc.
A 32 bit CPU uses 32 bit addresses, meaning there are 4 billion unique addresses.
Therefore, a 32 bit CPU can only make use of 4 GiB of memory.
This was getting quite restrictive, causing a shift to 64 bit.

## Question

Up to how many GiB of RAM could a 64 bit system have, assuming each bytes is addressable?
Once you know this, you can ask yourself the question how long it will take before this will become a limiting factor and a move to 128 bit will be necessary.
