# Mega and Mibi

Just like we have meters, millimeters and kilometers, the same metric prefixes apply to bytes.
A millibyte, which would be 0.001 bytes, is admittedly not a very often used unit.
However, a kilobyte (written KB) definitely is a commonly used unit (or at least it was back in the 90s, when you were happy to reach the glorious download speed of 3.2KB per second).

We can go further up: kilo, mega, giga, tera, etc. are all [metric prefixes](https://en.wikipedia.org/wiki/Metric_prefix) to express larges sizes of data.
But, how many bytes are there in a kilobyte?
This is where it can get a little bit tricky.

If we were to follow the SI system strictly, a kilo should be 1,000, a mega 1,000,000 and so on.
However, for bytes an exception was made: kilo corresponded to 2<sup>10</sup> = 1,024, mega to 2<sup>20</sup> = 1,048,576.

Drive manufacturers would abuse this confusion.
For example, they would claim a drive had a capacity of, say, 100MB, by which they actually meant 100,000,000 bytes, but they knew very well that everyone would think it meant 104,857,600 bytes.
When connecting it to a computer, it would then report the size of the drive as being a mere 95MB, and people would wonder where the missing 5MB went.

To rid us from this confusion, new metric prefixes were invented specially for bytes.
These days, we consider a kilobyte (KB) to be equal to 1,000 bytes, just like there are a 1,000 meters in a kilometer.
We also introduced the *kibibyte* (KiB) which is equal to 1,024 bytes.

Here's a table of the units and their actual sizes ([more complete table on Wikipedia](https://en.wikipedia.org/wiki/Byte#Multiple-byte_units)):

| Unit   | Abbreviation | Size in bytes |
| -------| ------------ | ------------- |
| Kilobyte | KB   | 10<sup>3</sup> = 1,000 |
| Megabyte | MB | 10<sup>6</sup> = 1,000,000 |
| Gigabyte | GB | 10<sup>9</sup> = 1,000,000,000 |
| Terabyte | TB | 10<sup>12</sup> |
| Petabyte | PB | 10<sup>15</sup> |
| Kibibyte | KiB  | 2<sup>10</sup> = 1,024 |
| Mebibyte | MiB  | 2<sup>20</sup> = 1,048,576 |
| Gibibyte | GiB  | 2<sup>30</sup> = 1,073,741,824 |
| Tebibyte | TiB  | 2<sup>40</sup> |
| Pebibyte | PiB  | 2<sup>40</sup> |

Lots of software (even Windows and MacOS) still uses the old style (1KB=1024B), however, so if you need to accurately know the size of something, be sure to double check.

## Question

Say I buy an SSD drive that says 4TB, but I erroneously think it means 4TiB.
How much percentage of the drive's storage will be "missing"?

For example, if I expect 1200 bytes, and in reality it is only 1000 bytes, I am missing 200 bytes, or 16.7% of my expected capacity.