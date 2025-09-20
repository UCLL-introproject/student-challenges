# `xargs`

Piping works when one command prints its output to `STDOUT` and the next one takes its input from `STDIN`.
However, there are cases where the arguments are taken from the parameter list.
`rm` is such a command.

Using `xargs` you can use the `STDOUT` output from one command as parameters for another:

```bash
$ cat to-be-deleted.txt | xargs rm
```

Say `to-be-deleted.txt` contains lines `a`, `b` and `c`:

* `cat` reads the file and outputs these three lines to `STDOUT`.
* `xargs` reads its `STDIN`, thereby receiving `a`, `b` and `c`.
  It then calls `rm` with these three values as parameters: `rm a b c`.

The subdirectory `text-files` contains a number of text files.
Determine the total number of lines of text in these files.
