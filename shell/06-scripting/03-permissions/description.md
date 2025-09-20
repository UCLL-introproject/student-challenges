# Permissions

Once you have your shell script, you still need to make it executable.
In this challenge, we'll briefly discuss the UNIX file permission model, which is used in Linux and macOS,
but is also useful for Windows users to know about.

A user can have three types of permission when dealing with files:

* *Read* permission (`r`) allows the user to look at the contents of a file.
* *Write* permission (`w`) allows the user to update the contents of a file.
* *Execute* permission (`x`) allows the user to execute the contents of the file.

These permissions cannot be specified on a per-user basis, i.e., it is not possible to assign different permissions to each user individually.
Instead, there are three ownership levels:

* A file has an *owner*, which is the user who created the file.
* A file has an owning *group*. A group is simply a selection of users, and a user can belong to any number of groups.
  Each file has one group that owns it.
* The other users who are neither owner nor part of the owning group.

It is possible to specify which set of permissions each level has.
For example, I can create a shell script and give it the following permissions:

* To the owner (me), I give all permissions: `rwx`.
* To my coworkers, I give `r-x`: they can read the file and execute it, but I don't let them change it.
* To other people, I give `---`, i.e., no permissions whatsoever.

Changing permissions can be done using `chmod`.
Look up how you can use `chmod` to give yourself (i.e., the owner) execute access to a file named `my-script`, and leave all other permissions untouched.
