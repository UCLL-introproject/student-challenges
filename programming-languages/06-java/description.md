# Java

## Security

Operating systems provide all kinds of security features.
One of these is file access control: whenever you create a new file, the OS considers you the *owner* of it.
As an owner, you get to decide who else can read it, write to it, delete it, etc.
In general, whenever a user perform a task (handle a file, run a program, ...) the OS will check if that user has the necessary permissions to do so.

Now, what happens if the user runs a program that tries to read a file?
How does the OS decide whether it is permitted?

If a user runs a program, that program "inherits" the privileges of that user.
If you can read a file, the program can read the file.
If you can send data to some website, so can the program.
Which means that any program that you run can secretly send all your data to some malicious hacker.

Sure, you can install a firewall that blocks outgoing network traffic.
But if the program pretends to be an innocent game with online features, it *will* need access to the internet,
and then all bets are off.
There is no way to detect whether it's sending game-related data or your-private-files data.
In other words, this is why you shouldn't just download any program and run it.
You need to really know you can trust it.

## Rise of the Internet

You might now wonder how it's possible that computers were designed in such an insecure way.
You have to remember that back then, the internet wasn't really a thing and people were all offline.
If people were at all connected to a network, it would typically be a trusted network with trusted users, quite unlike the internet.

But computer systems were indeed still vulnerable and viruses did indeed exist to exploit said vulnerabilities.
They spread when users shared infected files using physical media.
Some viruses were merely [playful](https://en.wikipedia.org/wiki/Ping-Pong_virus),
while others could be very [destructive](https://en.wikipedia.org/wiki/Casino_(computer_virus)).

With the advent of the internet in the 90s, it became more important to find a way to download software and be able to safely run it.
Java gave a solution to this problem.

## Java

As explained before, programs written in C++ must be compiled into machine code (resulting in an executable file, `.exe` for Windows users) so that the processor understands what to do.
However, given just machine code, it is quite difficult to find out what it does exactly without actually running it.
There is no easy way to know if it can be trusted or not.

Java programs, however, do not get compiled to machine code.
Instead, they get compiled to Java bytecode, which can be seen as machine code, but for an imaginary processor.
Therefore, in order to be able to run it, a special piece of software is needed to interpret this Java bytecode.
This software is called the *Java Virtual Machine* (JVM).

When asking the JVM to run a Java program, it will check every bytecode instruction to ensure that it follows very strict rules before actually executing it.
Such an analysis is possible because Java bytecode has been designed specifically for that purpose.
If during the Java program's execution access to a file is requested, the JVM will ensure it has the necessary permissions.
Contrary to regular executables, Java programs do not necessarily inherit all of the user's permissions.
The JVM allows you to set fine grained security policies: you can specify which of your files are accessible, how much memory it program is allowed to use, which network connections it can listen to, etc.
In short, you can think of the JVM as a sandboxed mini-OS: it provides a very controlled environment for untrusted code to run in.

## Important Note

Please do not think that Java applications are safe no matter what.
Java applets, i.e., small applications that ran inside your web browser, were safe to run because the JVM was told to give them minimal permissions.
However, running a Java program as desktop application will by default give it all your permissions, making them not much safer than programs written in order languages.
But Java *does* allow you to easily impose restrictions, so it's only safe if you know what you're doing.

## Usage

Java originally had the ambition of being the new universally used language.
However, as time went by, competing languages would get the upper hand in specific areas:

* Applets were supplanted by HTML5 and JavaScript.
* Android development still uses Java, but Kotlin is preferred.
* Cross platform desktop applications are being developed using Electron (JavaScript) and Flutter (Dart).

Java is still very much alive though, but it has shifted towards the enterprise world, where a large part of server-side software is written in Java.
In other words, Java runs on the "internal" machines of many companies, while software that reaches your machines (desktop software, web applications, mobile apps, ...) are most often written in other languages.

## Question

A Java IDE is software that assists you in writing Java programs.
Give the name of a well known IDE.
There are multiple correct answers.
