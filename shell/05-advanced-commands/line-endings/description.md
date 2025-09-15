# Line Endings

Documents are built out of characters such as letters, digits, interpunction, but we must not
forget about the invisible characters such as space, tab and line endings.

Speaking of line endings, ASCII (and by extension Unicode) offers both

* Line feed (codepoint 12), generally written `\n`.
* Carriage return (codepoint 15), generally written `\r`.

The distinction dates from typewriter days: when you reached the end of a line, you had to both move the page one line up and move the carriage (the "cursor") back to the left.
While typing a text document, if you press enter, which characters are actually added depends on the OS you're working on:

* In the Windows world, line endings are represented as a combination of carriage return and line feed.
  Text editors running on Windows will therefore add `\r\n` every time you press enter.
* Old macOS uses `\r`.
* Modern macs and Linux use `\n` (Unix-style).

These differences can lead to some trouble, but in general, software is aware of these differences and will automatically adapt, e.g., a Windows program will know how to deal with files only containing `\n`, etc.
In some cases, it does make a difference and you'll want a quick way to convert from one style of line endings to another.

What is the name of the shell tool that you can use to convert all `\r\n` to `\n` in a file?
