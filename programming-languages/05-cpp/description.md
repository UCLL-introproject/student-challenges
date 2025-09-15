# C++

## Abstraction

Programming mainly consists of defining *abstractions*.
But what do we mean by "abstractions"?

Imagine you are an excellent engineer and someone asks you to build a device for them, such as a television, a car, an MRI scanner, ...
You, being the excellent engineer that you are, have no trouble creating the device.
However, your client is not as excellent as you (otherwise they would've build it themselves), but they still need to be able to operate the device.
So it is your job to also make it easy to use by hiding all the complexity behind a user-friendly interface.

For example, you wouldn't know how to build a television, but you can definitely operate it by simply using the remote control.
Same for the car: you know it has a steering wheel, a clutch and pedals, and off you go.
And the MRI scanner... uhm... probably involves some buttons.
So, in short: simple interfaces for complex machinery.
That is what abstraction is about: hiding complexity.

And exactly because software development is such a complex undertaking, it is important that we follow a disciplined approach and take the time to build robust abstractions.
Put simply: on one extreme, in a perfectly designed system, you only need to know the part you are working on.
On the other extreme, in a horribly designed system, making a change requires intimate knowledge of the entire codebase.

## Large Scale Software

C is a rather small language which lacks many features to assist programmers with building large scale software, such as a way to build robust abstractions.
In 1979, Bjarne Stroustrup decided to extend C with a programming concept known as *classes*, which you'll learn all about the coming years.
He gave his brainchild the very creative name "C With Classes".
Stroustrup then proceeded to add more features, giving rise to C++.
The idea behind C++ is to preserve the strengths of C (raw efficiency, direct access to hardware), while also give programmers the ability to build abstractions, enabling them to write large scale software more easily.

## Usage

C++ has become a very successful language.
Most of the software you use is probably written in C++:

* Browsers like Chrome and Firefox are mostly written in C++.
* Many performance-sensitive games are written in C++.
  The engines they run on ([Unreal Engine](https://www.unrealengine.com/en-US), [Decima](https://en.wikipedia.org/wiki/Decima_(game_engine)), [Unity](https://unity.com/), [Godot](https://godotengine.org/)) are also typically using C++.
* Many parts of Windows are written in C++.
* Java programs require a Java Virtual Machine to run, which is itself written in C++.

Unfortunately, C++ is a *very* complex language, partly due to the fact that new features keep being added so as to keep up with other languages.

## Question

C++ is a programming language.
In order to be able to actually run C++ code, it needs to be translated first into machine code using a compiler.
Which are the three most widely used compilers?
Write each on a separate line in `solution.txt`.
