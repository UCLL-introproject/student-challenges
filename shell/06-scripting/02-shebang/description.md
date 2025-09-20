# Shebang

A shell script should always start with a special line that designates which language the script is written in.
More precisely, the first line should state which program to use as an interpreter for the script.
Which interpreter you choose will also determine the language.

For example,

```bash
#!/usr/bin/python3

print("hello world!")
```

The first line states that there is a program named `python3` in the `/usr/bin` directory that will know how to interpret the contents of the file.
The `#!` sequence is called *shebang* (pronounced shuh-bang).
When you run a script, the shell will look at this first line and call the program that's mentioned on it.
In our case that would be `python3`, which, as you might have guessed, is a program that runs Python code.
The result is that `hello world!` will be printed.

In order to be able to use the commands you've learned about in this series of challenges, you have to specify that the file is a Bash script.
What should the first line contain?
