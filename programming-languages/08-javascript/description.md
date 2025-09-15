# JavaScript

First of all, let's be clear on one thing: Java and JavaScript are completely unrelated programming languages.
JavaScript was merely named as such mostly for marketing reasons: Java happened to be popular at the time.

Web pages these days can contain a lot of functionality:

* When viewing your emails, you can see them appear as they arrive.
  There is no need to continually refresh.
* Web applications can become an alternative to desktop applications: Microsoft has made online versions of Word, Excel, there are websites with graphics editors, and so on.
* Webpages can contain full fledged games.

JavaScript is what made this possible.

## Early Web

Originally, web pages were just static documents.
When you browsed to a website, the following exchange would take place:

* Your browser contacted the server on which the website was hosted.
* The website responded by sending back an HTML document.
  An HTML is a full description of what the web page contains.
  If you want to see what it looks like, right click on a webpage and choose "Show source".
* The browser received the HTML document and displayed it on the screen.

If you interacted with the website, say, adding an item to your shopping basket,
the browser had to tell the server about this action, and the server would generate a fresh HTML for the browser to display.
This was rather inefficient, because every little thing you did required contacting the server and asking it for an updated HTML.
In essence, all the work happened on the server side: your browser was merely an HTML viewer.

Netscape had the idea of moving part of this work to the client side, i.e., that your browser would be given a bit more autonomy.
It would lessen the workload of the servers, would reduce the amount of network traffic, and make web pages more reactive.
This could be achieved by telling the web browser how to react to certain inputs.
For example, a website could tell the browser "if the user presses this "Add Item" button, you should add that item to that list over there that represents the shopping basket. You should also add this value (the item price) to that number (the total cost) and display it down there."
This allowed the browser to update the HTML on its own without having to ask the server for an updated version each time.

To make this possible, a language was needed in which to describe this behavior.
Brendan Eich was hired by Netscape (the company behind the Netscape browser which had 90+% market share at the time) to develop this language.
Unfortunately, he only got 10 days to do so (most other languages are years in the making), and it must be said, it showed.
But that's okay, because it was only meant to do small things like animations and improving the user experience here and there.

Thus was born JavaScript.

## Evolution of JavaScript

Website developers, however, saw a lot of potential in such a client-side language, and started to leverage it to build increasingly elaborate websites.
JavaScript underwent quite some changes:

* The language itself grew significantly, being extended with new features that would aid in building more complex applications.
* JavaScript was not designed with speed in mind and as applications grew, performance suffered.
  A lot of resources were subsequently invested in improving JavaScript's performance: Google's [V8](https://en.wikipedia.org/wiki/V8_(JavaScript_engine))
  Mozilla's [SpiderMonkey](https://en.wikipedia.org/wiki/SpiderMonkey) and Apple's JavaScriptCore are the major JavaScript engines currently in use.
* The semantics (meaning) of JavaScript code were very loosely defined, causing different browsers to interpret the same code differently.
  This caused a lot of chaos and required JavaScript programmers to write browser specific code.
  It took quite a long time before a thorough standardized specification emerged and browsers actually adhered to it.

Originally JavaScript was meant as an exclusively client-side language, forever trapped within a browser.
However, JavaScript escaped its prison as it were and spread to the servers:
thanks to software like [Node.js](https://nodejs.org/en) it is possible to run JavaScript code without needing a browser.

## Alternatives

Applets were another attempt at making web pages more dynamic: these would be written in Java and would be embedded in HTML pages.
However, they could not fully interact with the HTML page they were part of, which restricted their usefulness.
Applets are nowhere to be found anymore: a series of critical security flaws in the Java browser plugin caused the major browsers to outright ban applets.
It didn't help that the Java updater often silently failed on Windows.
Ironically, this caused the released patches to cause more harm than good:
hackers would take their time to reverse engineer them and find out what vulnerability they fixed, which they could then exploit,
because few users had actually installed the patch.

Flash was very similar to Java applets, but was geared towards graphical content (i.e., games).
It suffered the same fate as Java applets, and for the same reasons: it was terribly insecure.

WebAssembly (Wasm) is, apart from JavaScript, the only other language in existence that can be run directly in browsers.
It is designed with speed and security in mind.
The idea is that when a web page needs to perform some intensive calculations,
JavaScript code can start up a Wasm program, which runs in an isolated sandbox with no connections to the rest of the world (no file access, no access to the HTML, ...).
Of course, it must be able to somehow send the result of its computations back to JavaScript, but this happens in a very restricted manner.

## Question

This is actual JavaScript code:

```javascript
[][(![]+[])[+!+[]]+(!![]+[])[+[]]][([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+!+[]]+(+[![]]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+!+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(+(!+[]+!+[]+!+[]+[+!+[]]))[(!![]+[])[+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([]+[])[([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]][([][[]]+[])[+!+[]]+(![]+[])[+!+[]]+((+[])[([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]+[])[+!+[]+[+!+[]]]+(!![]+[])[!+[]+!+[]+!+[]]]](!+[]+!+[]+!+[]+[!+[]+!+[]])+(![]+[])[+!+[]]+(![]+[])[!+[]+!+[]])()((![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]+(!![]+[])[+[]]+([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[+!+[]+[+!+[]]]+([]+[])[(![]+[])[+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(!![]+[])[+[]]+([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]()[+!+[]+[!+[]+!+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(+(+!+[]+[+[]]+[+!+[]]))[(!![]+[])[+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([]+[])[([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]][([][[]]+[])[+!+[]]+(![]+[])[+!+[]]+((+[])[([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]+[])[+!+[]+[+!+[]]]+(!![]+[])[!+[]+!+[]+!+[]]]](!+[]+!+[]+!+[]+[!+[]+!+[]+!+[]+!+[]])[+!+[]]+(+[![]]+[])[+[]]+(+[![]]+[][(!![]+[])[!+[]+!+[]+!+[]]+([][[]]+[])[+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]())[+!+[]+[+!+[]]]+([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+[!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+([]+[])[(![]+[])[+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(!![]+[])[+[]]+([][(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]()[+!+[]+[!+[]+!+[]]]+([]+[]+[][(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[!+[]+!+[]]])
```

Luckily, this code is not representative at all; it abuses some JavaScript quirks.
Find a way to execute this code, it will give you the key to success.
