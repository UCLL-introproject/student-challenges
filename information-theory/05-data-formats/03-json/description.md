# JSON

JSON (pronounced Jason) is probably the most used format in use today.

```json
[
  {
    "rNumber": "r0000001",
    "firstName": "John",
    "lastName": "Doe"
  },
  {
    "rNumber": "r0000002",
    "firstName": "Jane",
    "lastName": "Doe"
  },
  {
    "rNumber": "r0000003",
    "firstName": "John",
    "lastName": "Deere"
  }
]
```

As you can see, it is much less verbose than XML.
JSON adds more structure to data: whereas XML consists of elements which can contain other elements or just plain text, JSON distinguishes between different kinds of data.

* Text data must be quoted: `"this is text"`.
* Numbers are written as you would expect: `542`.
* Lists are written `[first, second, ..., last]`, so for example `[1, 2, 3, 4]` is a list of four numbers.
  The elements of a list can be any other kind of data: text, numbers, other lists, objects (see below), ...
  In the example above, we use a list to hold the three students.
* Objects are key/value pairs.
  In our example, we use them to represent the students.
  `{"rNumber": "r0000001", "firstName": "John", "lastName": "Doe"}` has three key/value pairs:
  the first pair associates `rNumber` with `r0000001`,
  the second pair `firstName` with `John` and the last `lastName` with `Doe`.
  The keys must always be text, but the corresponding values can be kind of data.

Note that the layout can be freely chosen: e.g., everything can be put on a single line, or everything can be flushed left, etc.
It does not change anything about how the data is interpreted.

## Question

Convert the country data into JSON.
Use `country`, `capital` and `population` as keys in the objects that represent the countries.
At the top level, there should be a list, same as in the students example above.
