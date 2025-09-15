# FORTRAN

What makes computers so useful is the fact that they are *programmable*.
Many chips have a single purpose and have their software "baked in" as it were: they can only perform one kind of task, meaning they are not programmable.
They are cheap, and they are fast, but they're one trick ponies.
The development of chips that could take *instructions* as input opened up a whole new world of possibilities: the same machine could be used to perform *any* kind of computation.

## ISA

The *CPU* (Central Processing Unit) or *processor* is the chip in your computer that execute instructions, also called *machine code*.
Processors expect these instructions to take a very specific form, which is called the [ISA](https://en.wikipedia.org/wiki/Instruction_set_architecture).
You can think of an ISA as the language spoken by a CPU, and machine code as a story written in that language.

For example, say we want to add to numbers.
To tell an Intel x86 processor (which powers your Windows/Linux laptop) to do this, one should use `0000 0001 1101 0000`.
However, a RISC-V processor represents the same operation using `1001 1101 0010 1101`, and the ARMv9 processor (which powers Macs) has yet another bit sequence for it.

This means that

* Programming by speaking the processor's language directly is *hard*: we would have to carefully get every `0` and `1` right.
  Getting a single bit wrong would ruin the entire program.
* Lack of portability: code written for one machine could not run on another that used a processor with a different ISA.
  If you wanted the same program to run on both machines, you had to write it twice in two different ISAs.

## Assemblers

A first step into making programming easier was the development of [assembly](https://en.wikipedia.org/wiki/Assembly_language).
Each CPU instruction is given a more human-readable name, such as `ADD` for adding, `MUL` for multiplying, etc.
An assembler is a program that translates these into their corresponding bit representation, relieving humans from having to deal with endless `0`s and `1`s.

One might think that this solves the issue of portability, i.e., that `ADD` should simply be translated into the bits for the right CPU.
However, processors differ in much more fundamental ways than just which bits represent what operation, so programs still had to be rewritten from scratch when targeting a different ISA.

## High Level Language

FORTRAN is generally considered the first *high level programming language*.
One of its novelties was its syntax: it allowed users to write formulas using a standard mathematical notation.
For example, originally, an expression like "result = a + b &times; c" had to be split up in single operations so that the machine could understand them:

```text
MUL B, C, TEMP
ADD A, TEMP, RESULT
```

FORTRAN instead allowed programmers to write

```fortran
RESULT = A + B * C
```

FORTRAN would translate the human-friendly latter into the machine-friendly former, which then was further translated into actual machine code.
These translation steps were performed by what is called a *compiler*.

FORTRAN was also the first portable language, as it abstracted away the difference between processors: you could not write FORTRAN code that would use specific features of a particular processor.
This allowed compilers to be written that could translate FORTRAN code to machine code for any processor.
There would be no need to rewrite the same FORTRAN program to run on different processors:
if a new processor were created, you would only need to write a specialized compiler once, and all FORTRAN code in existence would be able to run on your new processor.

## Usage

Despite its age (admittedly, it has received some face lifts during the decades), FORTRAN is still used today for scientific computing where performance is crucial due to the huge amount of calculations involved.
Examples are astronomy, climate modeling, computational physics, etc.

Its portability is of course also essential to its lasting success: since the 50's, many processor architectures have been come and gone, but none of the FORTRAN code was lost.
It should come as no surprise that subsequent programming language would prioritize portability.

## Question

What does FORTRAN stand for?
