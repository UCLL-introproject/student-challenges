# Shell scripting

When you have complex command you want to use repeatedly, or multiple commands that always need to be run together, you should put them in a new file.
For example,

```bash
$ find -name "*.class" | xargs rm
```

removes all class files and deletes them.
If you put this line in a file named `clean`, then you can simple call `clean` as if it were a command as any other.
These files are called *shell scripts* and are a quick way to define your own commands that you can invoke from the shell.

If you try it out, though, you will see it does not work.
There are some details to get right first.
We'll discuss them in the coming challenges.
