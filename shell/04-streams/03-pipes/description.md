# Pipes

Imagine you are in a situation where you start off with a very large file and need to perform multiple consecutive operations on it:
After every step, you save the intermediate results in a file:

```bash
$ command1 big-file > intermediate1
$ command2 intermediate1 > intermediate2
$ command3 intermediate2 > final-results
```

A better way to achieve this is to use piping:

```bash
$ command1 big-file | command2 | command3 > final-results
```

## Streams

We quickly spend some time explaining technical details so as to ensure you have a good grasp of what goes on exactly.

When you run a program (such as Chrome, your favorite game, or a shell command, they're all the same in the eyes of the OS), the OS prepares a few things,
such as setting apart some memory for the program to run in.
We won't go into too many details here, as that could fill a whole course.

What matters for our purposes is that the program is also given three things:

* A list of parameters.
* An input stream (`STDIN`), which, put simply, is something your application can read data from.
* An output stream (`STDOUT`), which your application can write data to.

Say you run the program from the shell using `command param1 param2 param3`, the following happens:

* The list of parameters will be populated with the extra arguments you specified after the name of the command.
  In the case of our example, this list is `["param1", "param2", "param3"]`.
* The input stream is linked to the keyboard: while the program is active, the program will be able to read from the input stream
  to find out what you've typed.
* The output stream is linked to the terminal: everything the program writes to `STDOUT` will be shown on the terminal.

A command that require some data to operate on will often start by checking the parameters.
If you provided parameters, it will assume they're the names of files you want it to operate on.
If there are no parameters, the command will read its data from `STDIN` instead.

Take the `cat` command, for example.
It's actually a very simple program: it reads data and then outputs it out again to `STDOUT`.
Normally, you invoke it with one or more filenames (e.g., `cat a.txt`), in which case it will happily open each file in turn and print out their contents to `STDOUT`.
If you call it without parameters (just `cat`), it will start reading from `STDIN`, i.e., the keyboard.

We suggest you try it: simply enter `cat` in the shell.
Now type something and press enter.
You will see that it gets repeated: `cat` read a line from `STDIN`, and then immediately outputs it again.
To signal that the end of input has been reached, you can press `CTRL+D`.

## Piping

Let's examine what happens when you write

```bash
$ command1 file | command2 | command3 > final-results
```

* There are three programs involved: `command1`, `command2` and `command3`.
  The OS will launch all three of them.
* `command1` is told that there is one parameter, namely `file`.
  Its `STDIN` is linked to the keyboard.
* `command1` and `command2` are linked together: `command1`'s `STDOUT` is attached to `command2`'s `STDIN`.
* `command2` and `command3` are also linked together, in the same way.
* A file `final-results` is created and `command3`'s `STDOUT` is rerouted to that file.
  In other words, all output it sends to `STDOUT` will be written to `final-results`.

Given that `command1` received a parameter, it will probably choose to get its data from `file`.
`command2` did not receive a parameter, so it will read its data from `STDIN`.
The same goes for `command3`.

So, ultimately, we start off with the data stored in `file`, this gets processed by `command1`,
whose output then gets processed by `command2`,
whose output then gets processed by `command3`,
whose output gets written to `final-results`.

## Advantages

Creating a pipeline like this has multiple advantages compared to working with intermediate files:

* No extra storage is necessary for the intermediate files.
* The programs in the pipeline all work in parallel, speeding up processing.

## Task

You are given a file `data.txt`.
This file contains codes, one per line.
However, many codes appear multiple times.
We want you to count how many unique codes there are.

Hint: look up `sort`, `uniq` and `wc`.
