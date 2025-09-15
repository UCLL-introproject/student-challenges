# BrainF*ck

BF is a well-known esoteric language, meaning it's not made to be actually used for real programs.
BF's goal was to design a minimalistic language that could still do the same as any other language (this is known as Turing Completeness).
Writing code in BF can be seen as a programming puzzle.
In this series of challenges, we ask you to implement some simple programs in BF.
In regular languages, it would be a trivial task, but in BF it can get quite tricky.

## Machine

In order the understand how to program in BF, you have to first know the imaginary machine it runs on.
For these challenges, we simplified this machine a bit, so this explanation diverges somewhat from what you can find online.

The machine is equipped with memory, which you can see as a long sequence of boxes, each containing a number, initially `0`.
One of these boxes is considered the "active box".
At startup, the first box is active, but a program can change this.

A program consists of a series of commands, which are executed in turn.
There are eight commands:

* `+` adds 1 to the number in the active box.
* `-` subtracts 1 from the number in the active box.
* `>` makes the next box in line the active box.
* `<` makes the previous box the active box.
* `[` and `]` must always come in pairs.
  When `[` is encountered, the value in the active box is checked.
  If it is `0`, we must continue with the instructions coming after the corresponding `]`, effectively skipping all instructions in between the brackets.
  If it is not `0`, we simply move on to the next instruction.
* `]` jumps back to its corresponding `[`.
* `.` prints out the value in the active box.
* `,` receives a number from the outside world (e.g., the keyboard) and stores it in the active box.

## Example 1

The initial state of the machine can be represented as follows:

```text
0 0 0 0 0 ...
^
```

This represents a machine where all memory boxes contain `0`, and the first box is active.

Now consider the program `+++.`.
Execution goes as follows:

* The first command (`+`) gets executed.
  It increments the active box.
  The new machine state becomes

  ```text
  1 0 0 0 0 ...
  ^
  ```

* The second command gets executed, again a `+`.

  ```text
  2 0 0 0 0 ...
  ^
  ```

* The third command gets executed.

  ```text
  3 0 0 0 0 ...
  ^
  ```

* The final command is `.`, which means "print out the number in the active box".
  Therefore, `3` is printed.
* We run out of commands, so the program ends.

## Example 2

Consider the program `+[>+]`

* The initial state is

  ```text
  0 0 0 0 0 ...
  ^
  ```

* `+` increments the active box.

  ```text
  1 0 0 0 0 ...
  ^
  ```

* `[` checks if the active box contains `0`.
  It does not, therefore we continue with the next command.
* `>` makes the next box active.

  ```text
  1 0 0 0 0 ...
    ^
  ```

* `+` increments the active box.

  ```text
  1 1 0 0 0 ...
    ^
  ```

* `]` causes us to jump back to the `[`.
* `[` checks the value of the active box.
  Since it is not `0`, we continue with the next command.
* `>` changes the active box.

  ```text
  1 1 0 0 0 ...
      ^
  ```

* This box gets incremented.

  ```text
  1 1 1 0 0 ...
      ^
  ```

* We jump back to `[`.

This program actually never ends and fills memory with `1`s.

## Example 3

We consider the program `,[->++<]>.`.

* The initial state is

  ```text
  0 0 0 0 0 ...
  ^
  ```

* `,` requests a number.
  Let's say we give `3`.
  This number is stored in the active box.

  ```text
  3 0 0 0 0 ...
  ^
  ```

* `[` sees a nonzero in the active box.
  We therefore continue with the next command.
* `-` decrements the current box.
  ```text
  2 0 0 0 0 ...
  ^
  ```
* `>` makes the next box active.

  ```text
  2 0 0 0 0 ...
    ^
  ```

* We increment twice.

  ```text
  2 2 0 0 0 ...
    ^
  ```

* We move back to the first box.

  ```text
  2 2 0 0 0 ...
  ^
  ```

* We jump back to `[`.
* `[` sees a nonzero; we go to the next instruction.
* We have to execute `->++<`, which gives

  ```text
  1 4 0 0 0 ...
  ^
  ```

* `]` makes us jump back.
* We see that we need to execute the whole `->++<` once more.

  ```text
  0 6 0 0 0 ...
  ^
  ```

* `]` makes us jump back.
* `[` now finally sees a `0`.
  We jump over `[->++<]` and end up on `>`.

  ```text
  0 6 0 0 0 ...
    ^
  ```

* The last instruction `.` prints out the value in the current box: `6`.
* The program ends.

In other words, this program takes a number and prints out double its value.
