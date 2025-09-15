# Lisp

Lisp is the second oldest high level programming language still in use today.
It follows a rather different philosophy than FORTRAN, though.

One could say that FORTRAN believes machines to be so valuable that it is our duty to get the most out of them.
For this, we humans need to adapt to the machine and write code that is relatively close to what the machine can natively understand.

Lisp, however, disagrees, or at least its designers do, as programming languages don't really tend to have that many opinions.
The Lisp school of thought states that we developed machines to make our lives easier, and that includes the programmers' lives.
In other words, humans should not try to accommodate the machine; the machine should accommodate to us.
We don't necessarily just need raw computing power, we can trade it in for other desirable qualities such as easy of use, robustness, and safety.

## Garbage Collection

An example of a "decadent inefficient luxury" that Lisp offered is [*garbage collection*](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)) (GC).

Computers have memory.
Some have worryingly little, others have ludicrously much.
But most importantly, they all have a *finite* amount of it.

Programs all need memory to store their data in.
As they run, the amount of memory required evolves.
Consider a word processor (e.g., MS Word): as the user types in more text, bam, we need a bit more memory.
User adds an image, double bam, we need an extra million bytes.
Oh, user made a mistake and removes the image, we don't need that million bytes anymore.

Whenever a program needs to store more data, it can *allocate* more memory, i.e., it can claim an extra part of the machine's memory as its own.
However, when the data's usefulness ends, the program ought to *free* the memory, so that it becomes available for other uses.
If a program fails to do that (known as a *memory leak*), memory usage will keep increasing until, inevitably, memory runs out.

This is where GC kicks in.
It is a mechanism that detects whether data is still useful to keep around, and if not, the memory it's stored in will automatically be freed.
The skeptics among you can rest easy: GC is perfectly safe, never will it mistakenly free memory with useful data in it.

GC makes it seem like you have an infinite amount of memory: you can keep allocating extra memory, but behind the scenes, the garbage collector will clean up after you.
Of course, it is still possible to run out of memory if you have more data to store at once than there is memory in the machine.
GC only keeps you from accidentally forgetting to free memory.

GC is a nice example of where we sacrifice a bit of efficiency in return for robustness: with GC, there's no need to worry about memory leaks anymore.
These days, almost all programming languages (Python, Java, C#, JavaScript, Ruby, Go, ...) include a garbage collector.
Only few languages in use today (C, C++, Rust) choose not to include a GC so as to be able to achieve higher performance.
Know, however, that the complexity of manual memory management (= no GC) should not be underestimated.

## Usage

Lisp and its variants (Common Lisp, Racket, Clojure, ...) are quite the powerful languages, but nonetheless they are not much in use.
Originally, Reddit was written in [Common Lisp](https://gigamonkeys.com/book/), but has since been rewritten in Python.
[Clojure](https://clojure.org/) is a modern dialect of Lisp, which targets the Java Virtual Machine (JVM), meaning it can easily interoperate with Java code.

Even for today's standards, Lisp is a very advanced language, providing features that not even recent languages match.
A joke Lisp fans like to make is known as [Greenspun's tenth rule](https://en.wikipedia.org/wiki/Greenspun%27s_tenth_rule):

> Any sufficiently complicated C or Fortran program contains an ad hoc, informally-specified, bug-ridden, slow implementation of half of Common Lisp.

The C and Fortran references are due to the quote's age: it is equally valid for Java, Python, etc.

If Lisp is so great, how come it's not more popular?
Many people have their [theories](https://news.ycombinator.com/item?id=39375788).
In this writer's opinion, it is probably due to the fact the Lisp is actually *too* powerful:
you can extend it any way you want, write code that generates code that generates code,
its built-ins can be overridden, Lisp even allows its syntax to be completely overhauled.
In other words, Lisp is infinitely flexible, but languages should be about *facilitating communication*, which is dependent on structure and convention.

For example, English associates clear meaning to words (a 'cat' is a meowy animal, a 'chair' is something you sit on, etc.) and provides
grammar rules so as to be able to build sentences out of words.
However, if you need to work with someone who has changed the meaning of words and invented new tenses (as Common Lisp would allow you to do),
communication becomes that much harder.
Lisp can work well for a single programmer, as that programmer can taylor the language to their own needs.
However, once teamwork is involved, it quickly becomes a digital version of the [tower of Babel](https://en.wikipedia.org/wiki/Tower_of_Babel).

These days, programming languages are characterized by what they *don't* allow you to do, about enforcing restrictions and imposing structure.
This allows large teams of software engineers to work together more fluently, as everything becomes more predictable.

## Question

Determine what the output of the following code is:

```lisp
(defun gen (n &optional (p #'(lambda (x) T)) (k 2))
  (when (<= 0 n)
    (if (funcall p k)
      (cons k
            (gen (1- n)
                 (lambda (x)
                   (and (funcall p x)
                        (not (= 0 (mod x k)))))
                 (1+ k)))
      (gen n p (1+ k)))))

(format T "~{~a~^, ~}" (gen 10))
```

There are many lisps, so you might have to first find out which dialect it is.
Don't worry, we picked a rather common one.
