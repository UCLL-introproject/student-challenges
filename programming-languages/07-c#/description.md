# C#

Discussing C# in an objective manner can be quite difficult, because it involves Microsoft,
which have a reputation of being a bully and deeply distrusted for that reason.
While not unfounded, the writer of this text would also like to point out that Microsoft
was merely the biggest bully in a classroom full of bullies, and that these days, Microsoft has
definitely been out-bullied by others.

Java's ambition to be cross platform was both a gift and a curse:
it was nice that the same program could run on all platforms (Windows, Linux, macOS, ...),
but they ran slowly, were quite ugly and did not integrate well with the OS on which it ran.
Fortunately, most of these issues have been resolved right now.

Microsoft probably didn't like the idea of cross platform applications, as it could mean the end of the dominance of Windows.
Microsoft made Java applications to run better on Windows, but did this by [extending Java with Windows-specific functionality](https://en.wikipedia.org/wiki/Microsoft_Java_Virtual_Machine).
Programs relying on these extensions would not be cross platform anymore, much to the dismay of Sun, which promptly sued Microsoft.
There was a settlement and Microsoft had to discontinue "Microsoft Java".

Microsoft went on developed the .NET Framework, which like Java has its own bytecode named Common Intermediate Language (CIL).
Whereas Sun envisioned to have Java as the one and only language, Microsoft wanted to have a more "inclusive" platform towards languages:
the idea was that any programming language could be compiled to CIL and programs could easily interoperate with each other (which is otherwise a rather arduous task).
They also developed C# as the flagship language of .NET: it's a language Microsoft would have full control over and could therefore update as they saw fit.

C# started off as a language very much like Java, which was very probably done to attract Java programmers,
but rapidly gained many new language features which made using the language much more pleasant.
Java, on the contrary, evolved very slowly, but has luckily increased the pace since to catch up:
it took 22 years to go from Java 1 to Java 10, but 7 years to go from v10 to v25.

For a long time C# and .NET were de facto limited to Windows
(there was a Linux/macOS implementation named [Mono](https://en.wikipedia.org/wiki/Mono_(software)), but to the best of our knowledge it never really took off).
In 2016, however, Microsoft released .NET Core (since rebranded .NET), which is open source and cross platform,
making C# also a viable choice for Linux and macOS development.

Nowadays C# is used for server software, games (using the [Unity game engine](https://en.wikipedia.org/wiki/Unity_(game_engine)), which runs also on PlayStation, XBox, Switch, ...) and desktop software.

## Question

C# was designed by Anders Hejlsberg.
Which other well known programming language did he design prior to C#?
