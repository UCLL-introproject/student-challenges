# Video Compression

Let's turn attention to video, and how much storage is actually required for it.
In order to determine how much storage video requires, we must first find out how video is represented digitally.

## What's a Video

A video is actually nothing more than a quick succession of images.
How many images per second are actually used varies a lot: for movies this tends to be 24, which is more or less the minimum
if we want to perceive it as a movie and not as a slideshow.
Higher frame rates make for a smoother experience: gamers have come to expect 60fps, but prefer 144fps, and professional esports players insist on going up to 240fps or even higher.

## Compression

Let's actually calculate how large a 2 hour movie would be.
We assume the following:

* Its frame rate is 24fps.
* The movie has a resolution of 1920x1080.
* Colors are represented using 24 bits.

Putting all of this together gives us a total of around 1000 GiB.
In other words, it would take 142 MiB per second (not considering audio).
Imagine if you would need that much bandwidth to watch a movie online.

Luckily, compression helps us out again and reduces the storage requirements dramatically.
We don't delve into this, as this would be a course of its own (and involves *lots* of complex maths).

## Question

Let's find out how much storage compression saves.
When using the Netflix app on PC, you can press CTRL+ALT+SHIFT+D to view some technical information.
We started watching a Sandman episode and got

```text
...
Playing bitrate (a/v): 128 / 3502 (1920x1080)
...
Framerate: 23.976
...
```

Using this information:

* Resolution 1920 x 1080
* 24 bits per pixel
* 23.976 fps
* 3502 kibibits per second for Netflix's video stream

How many times smaller does Netflix's compression make the video?
