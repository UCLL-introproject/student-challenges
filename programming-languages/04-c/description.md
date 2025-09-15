# C

The C programming language dates from 1972 and is probably the most influential and widely used programming language in existence.

Every programming language has a set of design goals that influence each little choice made during the creation of the language.
C's original purpose was to (re)write the UNIX operating system, develop device drivers, etc. which lead to the following design goals:

* C had to be portable (lesson learned from FORTRAN).
* C had to give absolute control to the programmer, e.g., direct access to the computers hardware, which an OS desperately needs in order to function.
  This is, however, at odds with portability, so a good balance had to be found.
* C had to be efficient, *very* efficient. An OS can quickly turn into a bottleneck: if it is slow, then everything that runs on it will also be slow.

## Usage

C became a huge success and even up to this day is among the most popular languages:

* Windows' and macOS' kernels (the "brain" of the OS) are written in C.
* Most Linux components (kernel (brain), GNU tools (organs), ...) are written in C.
* Embedded systems (i.e., low power, little memory) are often programmed in C.
* There is probably a C compiler out there for every platform in existence.
* C acts as a lingua franca of some sorts: in simplified terms, whenever a program needs to interact with the OS
  (e.g., read/write files, display something on the screen, send data through the network, ...),
  it has to "speak C" because that's the only language the OS talks.
  If a program is not written in C, then some [translation](https://en.wikipedia.org/wiki/Language_binding) needs to take place.

Which again leads us to the question: why is C not used for everything?
Why the need for other programming languages.

Even though C is a rather small language, it is quite difficult to master.
Imagine you ask for a vehicle built for speed, and they present you with an [Avangard](https://en.wikipedia.org/wiki/Avangard_(hypersonic_glide_vehicle)) with a chair bolted on.
Sure, it can go 30 times the speed of sound, but actually getting to your destination in one piece will prove rather challenging.

## Question

What is the name of the C-function that allocates a block of memory?
