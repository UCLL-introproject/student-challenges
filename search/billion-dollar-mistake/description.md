# Billion Dollar Mistake

Many programming languages support the notion of "nothingness", the absence of a thing.
The concept has many names: `null`, `NULL`, `nullptr`, `nil`, `None`, `Nothing`, ...

For example, California's DMV (department of motor vehicles) uses `NULL` to indicate that a vehicle has no license plate.
Someone [tried to exploit this](https://www.forbes.com/sites/zakdoffman/2019/08/14/hacker-gets-12000-in-parking-tickets-after-null-license-plate-trick-backfires/)
by securing the vanity plate `NULL` (i.e., he paid extra to be able to choose his own plate instead of being assigned one by the DMV).
In so doing, he hoped that the system would get confused and that he would become invisible, as it were.
However, it backfired: he ended up receiving all parking tickets of people with missing plates.

While `null`/`nil`/... can be useful to represent missing values, ultimately it ends up being more a curse than a boon.
Every time the computer deals with data, it has to take into account the extra possibility that the value may actually be missing.
Forgetting somewhere to deal with that possibility leads (in the best case!) to a crash.
Fortunately, newer programming languages provide better support, making the issue disappear completely.

## Question

Who invented the null reference and considers it his billion dollar mistake?
