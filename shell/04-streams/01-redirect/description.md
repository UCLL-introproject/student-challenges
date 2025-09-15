# Redirecting

When invoking a command line tool, it can generate output that is shown on the terminal.
For example, when asking for the contents of the current directory, the names of each file and subdirectory are printed out.
You can redirect this output into a file:

```bash
$ command > file
```

Note that `file` will be overwritten.
If you want to output to be *appended*, you can use

```bash
$ command >> file
```

## Question

This challenge comes with a directory `root`.
From inside this directory, use a shell command to list all files.
Write these results into `solution.txt`.

Notes:

* Every line should contain one file.
* The order does not matter.
* Every line should start with `./`.
