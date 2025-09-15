# Including Hidden Files

Files and directories can be hidden, which has a number of benefits:

* Hiding files/directories helps reduce cluttering.
* Hiding important files reduces the chances that the user accidentally modifies or removes them.

How hidden files are actually implemented depends on the OS.
Windows stores this information as metadata, where it also keeps other details like "is the file readonly?" and "who has access to this file?".
UNIX-like systems, however, store the "hidden-ness" of a file simply in its filename:
if you want to hide a file, its name must start with a dot.

Now, when using a UNIX-like shell on Windows, this same rule applies:
the Git Bash shell will *pretend* files starting with `.` are hidden,
but as far as Windows and all other programs are concerned, it's just a visible file with a weird name.
It's a bit confusing, but it's best to know about this weird discrepancy.

## Question

When listing the contents of a directory, hidden files and subdirectories are not shown, which is, of course, the whole point of hidden files.
However, it must be possible somehow insist on showing hidden items anyway, otherwise they might as well be lost.
Which shell command can be used to ask for the current directory's listing, including the hidden files and subdirectories?
