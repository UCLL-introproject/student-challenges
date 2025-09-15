# Wildcards

Oftentimes, you want commands to operate on multiple files at once.
While you're free to manually type each filename, it is more convenient to rely on [*wildcards*](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm).

## `*` Wildcard

The most common wildcard is `*` and means 'zero or more characters'.
Say you have a directory containing the following files:

```text
foo.png
foo.txt
foo.pdf
bar.png
bar.txt
bar.pdf
```

Instead of writing `foo.png`, `foo.txt` and `foo.png`

```bash
$ command foo.png foo.txt foo.png
```

you can simply write

```bash
$ command foo.*
```

Another example:

```bash
$ command foo.png bar.png

# can be written als

$ command *.png
```

Do be careful though that you don't accidentally include files you do not want to pass along.
With irreversible commands, it is safer to check what the wildcard would expand to using `echo`.
For example,

```bash
$ echo command *.png
command bar.png foo.png
```

## Question

I want a list of all `pdf` files in the current directory.
Which shell command should I use?
