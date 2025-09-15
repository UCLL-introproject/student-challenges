# Jeopardy

Jeopardy is a well known TV quiz show, more than 9000 episodes having been aired.
It distinguished itself from other shows by providing the answer and expecting the candidates to give a corresponding question.

IBM decided they also wanted to participate and developed a "question answering computing system" for the occasion.
For human beings, the most difficult aspect of getting the answer right is recall, i.e., *knowing* the relevant facts.
This is a rather trivial task for a machine: simply dump all of Wikipedia on a drive.
However, understanding the question and being able to correctly look it up in the stored Wikipedia pages, while easy for humans, can prove quite challenging for a machine.

In 2011, "Jeopardy: The IBM Challenge" was broadcast in which IBM's machine played against the two (human) champions Ken Jennings and Brad Rutter.
The game ended with $77,147 for the AI, $24,000 for Jennings and $21,600 for Rutter.
IBM won the $1,000,000 prize, which they donated to charity.

Today we have ChatGPT, Gemini, Claude, etc. who would be able to perform the same task as IBM's machine.
Note that these LLMs work in a fundamentally different way.
IBM's AI is, in a way, a lot more handcrafted:

* Algorithms to dissect sentences need to be implemented, i.e., recognizing the subject and verb, etc.
* Words in sentences refer to previously introduced entities.
  For example, in the sentence `Sarah saw her mother`, `her` refers back to `Sarah`.
  Internally, such sentences may need to be simplified to `Sarah saw Sarah's mother`.
  If Sarah's mother has a name, this information also needs to be linked somehow, etc.
* Ways to efficiently look up information in a large database had to be developed.

An LLM more or less programs itself: human programmers created an artificial neural network, which they then feed it massive amounts of data so that it can "learn".
In other words, LLMs are a sort of brute force approach to AI: human programmers only need to build the foundations, after which they rely on raw computing power to do the rest.

## Question

What was the name of IBM's machine?
