# TypeScript

JavaScript was originally not designed to be a language to write large programs in,
but merely to make some small rather unimportant additions to web pages.
JavaScript was meant to remain on the background:
if a browser did not support it, the web page should still be functional.
And if the script contained a bug, it should just be ignored: the ~~show~~ webpage simply must go on.
JavaScript had to enhance web pages without taking the risk to break them.

## Strong and Weak Typing

*Types* are an important concept in programming language.
Remember that ultimately, all data is just bits.
We as humans can bestow meaning on them: we can say 'these bits form actually a number' and 'those bits actually make up an image'.
This is the *type* of the data: it tells us how to interpret bits.
Examples of types are "number", "text", "color", "image", "audio", etc.

Programming consists of dealing with data of different types and performing operations on that data
(taking the square root of a number, searching for patterns in text, brightening colors, adding echo to sound, ...)
However, not all operations can be carried out on all types of data:
it makes no sense to add echo to numbers or take the square root of sound.

A *strongly typed* language will insist that operations are only applied to data with the right type.
If a nonsensical operation is performed, the language will loudly complain and interrupt the running program.

JavaScript, however, is *weakly typed*.
If an operation is performed with data of the wrong type, JavaScript will still try to make it work:
it will apply *type coercion*, implicitly converting the data from one type to another, often leading to nonsense.
A few examples:

* Adding text with a number `"5" + 1` gives `"51"`: the right operand is coerced from number to text.
* Subtracting a number from a string `"5" - 1` does the opposite: the text is coerced to a number, resulting in `4`.
* `{} + []` gives `0`, but `[] + {}` gives `'[object Object]'`.
* The number `0` is equal to the text `"0"`' (`0 == "0"`), as well as to empty text `""` (`0 == ""`), but `""` is not equal to `"0"` (`"0" != "0"`).

Even seemingly logical operations can lead to surprising results: adding to lists `[1, 2] + [3, 4]` gives `"1,23,4"`, i.e., text.

Most programming language offer strong typing, as it is by far the safest approach.
In cases type coercion "can make things work", it simply means a mistake was made and that the result of the operation is not trustworthy anymore, so best stop right there instead of pretending there is no error.

JavaScript can unfortunately not be fixed anymore: many programs have started using tricks relying type coercion, so removing type coercion would break those.

## Static Typing

The problem can actually be solved very easily: just invent another language with stricter rules, and write a compiler (often called *transpiler*) that translates this safe language into equivalent JavaScript.
However, what to do with existing JavaScript code?
Should we throw it all away?
Or keep using it, knowing it's a bit shaky?

TypeScript was developed as an answer to this problem.
You can imagine it was built as follows:

* First, it takes over everything from JavaScript, warts and all.
  Therefore, JavaScript code should still be correct and behave exactly the same.
* Next, the syntax is extended so as to allow for type annotations, which means that TypeScript allows you to indicate what type everything has.
  This extra information allows you to express your intent, and helps TypeScript examine your code and find potential bugs.
  Since browsers only understand JavaScript, a *transpiler* must translate TypeScript code back into equivalent JavaScript code.
  This is rather easy to do: simply remove all the type annotations.
* Extra language features were also added, such as classes, which had to be translated into equivalent JavaScript code.
  Many of these additions were later adopted by JavaScript, closing the gap again between both languages.

A short example of JavaScript vs TypeScript:

```typescript
// JavaScript
function max(a, b)
{
    if ( a >= b ) return a;
    else return b;
}

// TypeScript
function max(a: number, b: number): number
{
    if ( a >= b ) return a;
    else return b;
}
```

In the TypeScript version, the `: number` annotations makes clear that `max` is only valid on numbers, and that the result of taking a max of two numbers is again a number.
JavaScript would let you run `max("5", [100])` (which results in `"5"`), whereas TypeScript would gently point out your mistake.
To convert TypeScript back into JavaScript, one only needs to drop the `: number` parts.

When a programming language checks your code in this way, it is said to be [*statically typed*](https://en.wikipedia.org/wiki/Type_system#Static_type_checking).
Static typing is not new to JavaScript: many other languages use it too (see next section).
TypeScript's type system is, however, quite advanced compared to most other language's.
This is due to the fact that it had to deal with existing JavaScript code, which can be quite chaotic, so the typing system itself
had to be very flexible to be able to deal it.

## Static vs Dynamic Typing

As mentioned before, most languages are strongly typed.
However, they differ in how they check whether typing rules are followed.

*Statically typed languages* like TypeScript perform these checks at compile time, meaning they analyze your code without running it and tell you where they find errors.
This approach incurs no run time overhead: all type checking takes place ahead of time.

*Dynamically typed languages* will simply run your code, and perform type checks while it is running.
This causes programs to run slower.
This approach, however, is more flexible, as more information is available at runtime than when staring at the code, so more thorough checks can be performed.

| Statically Typed | Dynamically Typed |
| -----------------| ----------------- |
| TypeScript       | JavaScript        |
| C                | Python            |
| C++              | Lisp              |
| Java             |                   |
| C#               |                   |
| Fortran          |                   |
| Cobol            |                   |

## Question

TypeScript was developed at Microsoft by Anders Hejlsberg (who also designed C#).
Facebook also created a competing language but the same goal as TypeScript, namely adding static typing checking to JavaScript.
TypeScript won the battle, and Facebook's language is barely used anymore.

What is the name of this language?
