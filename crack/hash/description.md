# Hash

Passwords are a very popular method of authentication: if you want access to your account on some website, you need to give your password.
The idea is that a user knows a secret, and they can establish their identity by proving they know that secret.

When you enter your password, the website of course needs to be able to verify that it is indeed the right password.
So, it would make sense for the website to store all their users' passwords, otherwise how could they check the passwords?
This is actually quite a dangerous situation: if the website gets hacked and attackers get access to the database containing all passwords,
all users are at risk.
It only gets worse if users reuse passwords: those other accounts would be endangered as well.

So, it is crucial that websites don't store their users' passwords.
This raises the question: how can they then still verify that users enter the correct password?

## One Way Functions

Imagine we live in a world where we can easily compute the double of a number (4 gives 8), but halving them is *really* hard, bordering on the impossible.
This would make the following authentication scheme possible:

* You pick your secret, e.g., `15`.
* You compute the double: `30`.
* When registering a new account on the website, you state "I am the only one in the world who knows what the half of `30` is".
  The website stores this information.
* When you want to log in, the website asks you "Please prove that you do know what half of `30` is".
* You know that it is `15`, and tell them that.
* The website can easily verify that you are right: they can compute the double of `15`, get `30`, and know it is you.

If hackers were to break in, they would only get access to 30, which doesn't help them in the least, as they need half of 30 to log in, and they are incapable of computing that.

However, we do actually live in a world where halving is not difficult to do at all (especially in binary...).
But maybe we can do find another operation that is easy to do, but hard to undo?

## Cryptographic Hash Functions

Such operations have been developed.

To avoid confusion in the future, we first need to explain what exactly a *hash function* is.
A [hash function](https://en.wikipedia.org/wiki/Hash_function) is an algorithm that we can feed data of arbitrary size, and it will "hash" it into a fixed number of bits.
A trivial (but rather useless) hash function would be one that always returns `00000000`.
Another example would be one that always returns the first 100 bits, and if the output has fewer than 100 bits, just adds `0`s.

Hash functions are a very powerful tool and can for instance be used to build [hash tables](https://en.wikipedia.org/wiki/Hash_table), a very efficient way data structure.
However, this is out of the scope of this challenge.

Let's focus on a hash functions with a very specific property:
given a hash code, it must be *computationally infeasable* (a word that pops up often in the world of cryptography) to find an input that would be hashed into that code.
In other words, hashing must be easy, unhashing must be practically impossible.
These hash functions are called [*cryptographic hash functions*](https://en.wikipedia.org/wiki/Cryptographic_hash_function).
(Technically there are some extra properties it must have, but let's keep it simple.)

Designing a reliable cryptographic hash function is very difficult: you do not just roll your own.
Instead, there are a small number of standardized cryptographic hash functions which have been thoroughly analyzed and are free for all to use.
An example is the [SHA-2 family](https://en.wikipedia.org/wiki/SHA-2): it consists of six hash functions, among which SHA-224, SHA-256 and SHA-384, each differing
in the size of the produced hash code (224 bits, 256 bits and 384 bits, respectively).
You can see Sha-256 in action [here](https://emn178.github.io/online-tools/sha256.html).

## Back to Passwords

When you register, you provide a password.
This password is hashed, and only the hash code is stored in the database.
Authentication then consists of proving that you know an input that produces this hash code.
Hackers getting access to these hash codes are not able to derive your password from it.

There is plenty more to tell on the subject (salting to counter rainbow tables, which hash function to use, implementations of hash functions),
but we'll leave that for another course.

## Question

We have picked a seven letter (all upper case) password and hashed it using SHA-1, which produced `10ceee87f8b145ab495c3bca73b94455970159c6` (using hexadecimal notation).
What was this password?

(There is no clever trickery involved, only brute force. Hopefully you have a power computer.)
