# Rust

C and C++ are very powerful languages: they give the programmer a lot of freedom and control,
and in the right hands this can result in incredibly efficient code.
However, that freedom has a downside: it also allows you to make serious mistakes:

* [Buffer overflows](https://en.wikipedia.org/wiki/Buffer_overflow) can allow hackers to have your computer run arbitrary code.
* [Memory leaks](https://en.wikipedia.org/wiki/Memory_leak) will lead to [thrashing](https://en.wikipedia.org/wiki/Thrashing_(computer_science)), slowing down the entire machine, and/or
  a crash. Memory leaks can be exploited to perform [denial of service attacks](https://en.wikipedia.org/wiki/Denial-of-service_attack).
* [Out of bounds reads](https://en.wikipedia.org/wiki/Bounds_checking) (e.g., reading the 11th element of a list that only contains 10) are not caught and can allow hackers
  to access [sensitive information](https://en.wikipedia.org/wiki/Heartbleed).
* Uninitialized memory can lead to information leaks.
* [Undefined behavior](https://en.wikipedia.org/wiki/Undefined_behavior) is common in C and C++. Languages associate semantics with syntax, meaning
  that when you write code, it should have a well-defined meaning. However, C/C++ leave gaps: some things simply do not have any meaning (undefined behavior) and the compiler
  is free to translate such code to anything it wishes. This is meant to allow for more aggressive optimizations, but can lead to [critical bugs](https://lwn.net/Articles/342330/).

It is therefore essential that C/C++ programmers are very aware of these potential pitfalls and take care to avoid them.
For example, the [Cybersecurity and Infrastructure Security Agency](https://www.cisa.gov/resources-tools/resources/product-security-bad-practices) states

> The development of new product lines for use in service of critical infrastructure or NCFs in a memory-unsafe language (e.g., C or C++) where readily available alternative memory-safe languages could be used is dangerous and significantly elevates risk to national security, national economic security, and national public health and safety.

All kinds of measures of been taken to attempt to make C and C++ safer to program in:

* Library improvements that perform more checks.
* Compilers that become smarter and warn you of potential dangers.
* External tools that analyze C/C++ code and look for errors.

## Broken Elevators

In 2016, Graydon Hoare decided he had had enough: the elevator was out of order once again, making him have to climb 21 flights of stairs to reach his apartment.
Suspecting the elevator's software was very probably probably written in C, he decided it was time for a better alternative.
Thus started the development of [Rust](https://en.wikipedia.org/wiki/Rust_(programming_language)).

Rust is a language that like C and C++ prioritize speed and provide low level control, but not at the cost of correctness and safety.
This is achieved by very elaborate static analyses: Rust very thoroughly inspects your code for mistakes before translating it into machine code.
For this, the programmer needs to annotate their code with elaborate types and lifetimes, so as to enable the Rust compiler to prove that everything is memory safe, type safe and thread safe.
Rust is also free of undefined behavior.

Since there is no such thing as a free lunch, it is inevitable that Rust has a downside: it is quite hard to program in.

Rust has steadily grown in popularity and is slowly replacing C/C++ code: parts of the Linux kernel are being rewritten in Rust, as well as Firefox, Dropbox, Discord, etc.
Deno is an alternative to Node.js written in Rust, Rustls is an alternative to OpenSSL, and so on.

## Question

What is Rust package manager called?
