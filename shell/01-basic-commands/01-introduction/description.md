# Introduction

Up until now, you probably only have been exposed to *graphical* user interfaces (GUIs).
Moving files is just a matter of dragging and dropping them,
printing a document consists of pressing an icon,
blurring an image is just a matter of picking the right filter in a menu.

There also exists the "old-style" approach, where arcane commands are entered into a minimalistic text terminal, often referred to as a *shell*.
But why would anyone prefer that?
Surely a GUI is so much nicer to work with.

While we definitely won't try to convince you to turn your back on GUIs, we will try to make a case for using the shell.

## Command Line Interface

The shell allows you to run programs using text commands:
For example:

```bash
$ shutdown
```

The `$` in front is not part of the command: it is customary to add it as a way of indicating that what follows is a shell command.
So, if you find instructions using the shell somewhere, you should never write the `$`.
In this example, what you would have to actually type is `shutdown`.

`shutdown` is a small program that, unsurprisingly, causes your system to shut down.
(Note that it might not work on your machine: whether it exists depends on your OS.)

The shell also allows you to pass extra information to the program:

```bash
$ shutdown 18:00
```

`shutdown` can see this extra piece of information (called *command line arguments*) and will interpret it as 'the user wants me to shut down the machine at 18:00'.

*Any* program (written in any programming language) can be called from the shell (Chrome, your favorite game, Excel, ...) but in order for it to be useful,
it should at the very least not ignore the command line arguments you give it.
For example, it would be perfectly possible for the Netflix application to allow you to give in commands on the shell:

```bash
$ netflix download Pantheon S1 E2
```

This could download the second episode of the first episode of Pantheon.
Sadly, Netflix did not actually implement such functionality.

## Advantage 1: Automation

Say you have an image you would like to resize so as to save some space.
This can easily be done using your favorite graphics editor.
However, what if you have a thousand images you need to resize?
Perhaps your favorite graphics editor provides an easy way to do this, but perhaps not.
What if you only want images starting with a certain prefix, or also want to change the image format from PNG to JPEG, and want them all watermarked?

What if you have a large number of zip files, which you'd rather recompress into 7z files because they would be smaller?

What if you have a long list of URLs of files you want to download?

While GUIs allow you easy access to an abundance of functionality, it can still require a lot of work to actually perform all tasks you need done.
There is no easy way to *automate* tasks with a GUI, unless the designers of the GUI anticipated your specific needs and took time to develop extra GUI components for that specific purpose.

A command line interface, however, can easily be called from scripts.
Scripts offer you a lot of freedom: you can specify any kind of logic in them.
If Photoshop were to provide a command line interface (it doesn't, but there are alternatives that do), we could theoretically write

```bash
$ photoshop -resize 640x480 *.png
```

You can also schedule certain actions to take place at a certain time, or to be repeated every hour, every time you log in, etc.

## Advantage 2: Development Time

If there is a task you need to be performed regularly, it can be worthwhile to write a small program that does it for you.
However, writing a full fledged graphical user interface takes a lot of effort.
In those cases you might want to consider just developing a command line interface, i.e., make your program usable from the shell.
This often takes only a fraction of the time needed to create a GUI.

## Your Task

Find out how to open a terminal on your OS.
There are many different terminals available and they differ in which commands are available to them, so it is important you get the right one.
These challenges require you to use Bash, or a compatible terminal.

Windows users should therefore stay away from `cmd.exe` and PowerShell, and rely instead on Git Bash, which comes with Git.
Linux and MacOS users should be able to use their default terminal.

To familiarize yourself with the shell, we suggest you take a look at this [webpage](https://linuxjourney.com/lesson/the-shell).
Another useful website is [explainshell.com](https://explainshell.com/): given a command, it can tell you what it does.

As you go through the challenges, we strongly suggest you actually run the commands on your machine (as long as you feel it's safe to do so; maybe you want to be ultra careful when it involves deleting files).
