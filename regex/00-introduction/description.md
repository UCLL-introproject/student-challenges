# Regular Expressions

Whether you are a software engineer, a system administrator, a cybersecurity expert or a data scientist, you will have to deal with textual data.
A very common operation is to find patterns:

* Websites need to validate input, such as email addresses or date.
  Checking if a date is correct consists of checking if a piece of text has the pattern dd-mm-yyyy, extracting the values for day, month and year, and verifying that they indeed form an existing date.
* When the system goes down for some reason, the logs have to be analyzed.
  These logs can grow quite large, and being able to filter out log entries that don't contain specific patterns (e.g., `ERROR` or specific dates) reduces the amount of data an administrator has to sift through.
* Suspicious activity can be detected by looking for certain patterns in logs, e.g., many failed login attempts.
* Data scientists have to deal with lots of data that often need to be cleaned up first, e.g. `3,14 vs 3.14`.

Regular expressions are supported in many places: programming languages provide regex-libraries, shell tools such as `grep` relies on them, even text editors (such as VSCode) offers them.
Note that there can be differences in different implementations of regexes: sometimes the syntax is slightly different, and some offer features that others don't.
For this series of exercises, we'll be relying on the Python implementation.

Note: in programming language jargon, the word `string` means text.
We will be using both terms interchangeably.
String comes from "a string of characters".