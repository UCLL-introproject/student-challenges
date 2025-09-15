# Python

We ordered the languages chronologically, but with Python we made an exception.
It is actually older than Java (1990 vs 1995), but it became popular only much later (around 2010).
These days, it's typically ranks in the top 5 most popular languages, often even ranking first.
But what did Python do to deserve all this recent love?

## Productivity

Whereas some languages are obsessed with efficiency (we're looking at you, C++), Python is more of a laid back "What's your hurry, dude?" language.
It was designed with simplicity in mind, and didn't mind making sacrifices to achieve that.
As such, Python is not terribly efficient: it can be 100&times; slower than equivalent code written in C++.

It is important to distinguish between development speed (= programmer productivity) and execution speed.
An efficient language like C++ will allow programmers to write blazingly fast programs,
but there is a cost: it takes a long time to actually write the code and make sure it actually works correctly.
Python allows for faster development as it takes care of many mundane details for you, among which

* It features a garbage collector, so programmers are relieved from having to worry about memory leaks and dangling pointers.
* It is memory safe and type safe. In C++, a security vulnerability is only a distraction away, while Python comes with many built-in protections.

In other words, Python just wants to help you get the job done.

## Speed

As mentioned above, Python can be quite slow, but in reality, this doesn't really matter.
Most programming languages allow to make bindings, which means that you can "talk" to code that's written in a different language, typically C.
Python is no exception.
This allows you to focus on the "overall picture" in Python, and write the computationally intensive parts of your program in optimized C.

It may now seem as if we're saying you'll also need to learn C if you want something decent done.
This brings us to the third advantage.

## Rich Ecosystem

Another strength of Python is that there already exist a huge amounts of [premade packages](https://pypi.org/) (650,000+ officially published ones at the time of this writing).
Most of them will be written purely in Python, but the efficiency sensitive ones will be written in C, ready for you to use in your Python project.
For example, [NumPy](https://numpy.org/) is a package that specializes in number crunching and is highly optimized.
Whenever you need to deal with large amounts of data, you can just ask NumPy to do the heavy lifting.

So, in practice, you'll probably never have to implement your own package in C: someone else has probably already done it for you.

## Question

Which popular library can you use to make games in Python?
Multiple answers are correct.
