# Tower of Abstraction

Abstraction is a very powerful tool: it allows us to build anything we want by combining simpler building stones, the smallest of which are `0`s and `1`s.
An operating system such as Windows or Linux is a nice example of what abstraction can achieve.

## CPU

Your computer very probably contains a CPU with multiple cores.
Let's ignore this for a moment and pretend there is only one core.
What difference would it make?
Would this mean you would not be able to run multiple programs at once?

Let's briefly delve into some technical details.
A CPU's job is to run instructions.
A series of instructions is called a *thread*.
A program (or, in OS jargon, *process*) must have at least one thread, otherwise there would be no instructions to execute.
A process can also be *multithreaded*, meaning it performs multiple tasks concurrently.

For example, a game often has many things going on at once:

* An AI needs to make decisions.
* Graphics needed to be rendered.
* Physics need to be simulated.
* Sounds, textures, meshes, ... needs to be loaded into memory.
* Data needs to be sent and received over a network for multiplayer games.

Each of these *can* be put in separate threads.
(Note that this is actually quite difficult to do correctly, causing many games to be not as multithreaded as they could be.)
Distributing the game logic over multiple threads allows them to be run in parallel: every thread can run on a separate core.

However, even with a single core CPU, running multiple threads is possible.
This is achieved by having the OS quickly switch between threads:
one thread is allowed to run for a short time slice, typically around 20ms, after which the OS interrupts it and gives control over the CPU to another thread.
Quickly switching between threads gives the impression that they are running in parallel.

On a single core CPU this does not make games run more quickly, but being able to run multiple threads still had the advantage of allowing running multiple programs at once:
you can have some music play and have a browser open, while you're doing very important school work in VSCode.

This technique of constantly switching threads is still very much relevant today, even with multiple cores, as there are many more threads that run than there are cores on your CPU.
In summary, thread switching allows the OS to pretend that there are many more cores available than there are physically present in your machine: if you start having more threads than cores, the OS will simply start

## Screens

Your computer has a graphics card, which is responsible for sending data to the screen.
Put very simply, the graphics card can be told the colors of each pixel on the screen.

If every program running on your OS would have direct access to the graphics card, things would become messy very quickly, as they would
start drawing over each other.

An OS will therefore claim the graphics card solely for itself and present each running application with a "virtual screen", on which it can draw all pixels it wants.
It will then be the OS's responsibility to determine which virtual screen's pixel data to send to the actual graphics card.

This is what a windowing GUI does: every window is in fact a virtual screen given to a program.
The OS allows the user to rearrange and resize these virtual screens on the physical screen.
This idea can be further generalized: one application can ask for as many virtual screens as it wants, and the user can install multiple monitors.
So, a windowing system can turn a single screen machine into a as-many-as-you-want-screens machine.

## Memory

Your machine has a certain amount of RAM, which, at the time of this writing, is probably between 16GiB and 32GiB.
This RAM has to hold all data your OS and programs need to operate.
It is also important that each program is well-behaved: it should not read and certainly not write to other programs' memory.

Just as with CPUs and screens, the OS will turn this limited amount of RAM into a seemingly infinite amount of RAM.
Whenever you start a program, a new *virtual memory space* is created, which on 64 bit machines is 17,179,869,184 GiB (or 18 exabytes) large, i.e., quite a bit more than you actually have.
Every program receives its own virtual memory space and therefore has the impression they're the sole program running.
This separation is paramount for stability and security: a buggy or malicious application cannot tamper with other programs running on your machine.

You can imagine this virtual memory as an infinitely large canvas you can paint on.
Initially, there is no canvas, it's just a lie the OS tells you.
But as you start moving your brush towards the nonexistent canvas, the OS quickly but a small square of real canvas, so that your paint has something to adhere to.
As you progress, you reach the bounds of the small square, and just as you are about to cross the borders of the canvas, the OS adds another piece of canvas.
As far as you are concerned, the canvas is indeed infinitely large: it's the OS's job to actually add new physical pieces of canvas as you go.

A similar story is true for RAM: RAM is divided into pages (typically 4KiB in size), and initially, none of the pages actually "exists".
Only when your program actually starts accessing memory will the OS start allocating physical RAM to fill in gaps where needed.
In other words, even though a program thinks it has 18 exabytes at its disposal, only the parts it actually stores data in are backed by real memory.

What happens if a program uses more memory than there is physical RAM installed?
This is when paging will take place: the OS will identify those pages of RAM that are least used (e.g., a program that you are running in the background but haven't interacted with for a while)
and write their contents to disk, thereby freeing some RAM.
If that program were to wake up again, the OS hurries to read those pages back in (which perhaps needs other parts of memory to be written to disk),
thereby giving the sleepy program the impression that it never lost its RAM pages.

## Other Examples

* The sound card is virtualized, meaning that the OS claims it for itself and provides "virtual sound cards" to each program.
  Sounds played by the different programs are then mixed together by the OS.
  Without such virtualization, only one program at a time would be able to play audio.
* The file system turns the drive (which is basically one large file) into files organized in a directory structure.

## Question

For networks, there is a standardized tower of abstraction which consists of seven layers.
What is the full name of this model?
