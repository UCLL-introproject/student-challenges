# XML

XML is another well-known format.
Our student data would look as follows:

```xml
<students>
  <student>
    <r-number>
      r0000001
    <r-number>
    <first-name>
      John
    <first-name>
    <last-name>
      Doe
    </last-name>
  </student>
  <student>
    <r-number>
      r0000002
    <r-number>
    <first-name>
      Jane
    <first-name>
    <last-name>
      Doe
    </last-name>
  </student>
  <student>
    <r-number>
      r0000003
    <r-number>
    <first-name>
      John
    <first-name>
    <last-name>
      Deere
    </last-name>
  </student>
</students>
```

XML structures its data as hierarchical elements.
An element starts with a start tag, for example, `<first-name>`, and ends with a corresponding end tag, `</first-name>`.
Elements can contain other elements, e.g., `students` contains three `student` elements, and each `student` element contain three elements named `r-number`, `first-name` and `last-name`.
An XML file should contain only one root element which contains all other elements as children. In our example the root is `students`.

## Question

Convert the country data into XML format.
Use `countries` as root element.
Each country must have a corresponding `country` element, which each contains a `name`, `capital` and `population` element.
