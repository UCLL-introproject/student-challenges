# CSV

## Graphics Formats

You probably are familiar with some of the following file types:

* JPG
* PNG
* GIF
* SVG
* PDF

They are all graphics formats, but differ in the way they actually encode the images.

* JPG views images as a grid of pixels (it is a *raster* format).
  It typically uses lossy compression, meaning that in order to achieve smaller files, it does sacrifice a bit of image quality.
* GIF also views images as a grid of pixels, i.e., it is a raster format.
  However, contrary to JPG, it applies *lossless* compression, meaning there is no loss of quality: each pixel's color will be faithfully stored in the file.
  GIF also supports simple animations.
* In the mid 90s, it was announced that people would have to start paying royalties when using GIFs.
  PNG was developed as a free alternative: it is a raster format and employs lossless compression, but it does not support animations.
  GIF has regained popularity since the relevant patents expired mid 2000s.
* SVG is a vector based graphics format: instead of describing an image as pixels, it uses geometric shapes.
  This makes it rather useless for pictures, but it is great for logos, charts, etc.
* PDF combines both raster and vector based.

These formats are all specialized in graphics.
Sometimes, however, we need to store other kinds of data.

## General Data Formats

Say, for example, we need to store data about students: their first name, their last name, their r-number, etc.

We could rely on a database to store this data: this would be very efficient and would allow us to easily perform complex data lookups using SQL.
Sometimes, however, a simpler format is necessary, e.g., when data needs to be communicated between two parties, such as you downloading something data from a server.

There are two main categories of data formats: binary and text formats.
Suffice it to say that a binary format is typically more compact but is not human-friendly: it's a bunch of bytes that depending on their position in the file mean different things.
Text formats are meant to be human readable and typically contain some extra metadata, i.e., extra annotations that explain what each part represents.

## CSV

One well known text format is CSV, short for "Comma Separated Values".
While it does lack a bit in flexibility, it has the advantage of being structured in a way that is very spreadsheet-friendly: CSV files can easily be imported into Excel/Google Sheets/...

A CSV file could look as follows:

```csv
rnumber,fname,lname
r0000001,John,Doe
r0000002,Jane,Doe
r0000003,John,Deere
```

CSV files must be read line by line, also called rows.
The first row is optional and can be seen as metadata and explains how each of the following rows will be structured.
In our example, it states that each row will contain three pieces of data, namely an r-number, a first name and a last name.
The next three rows each represent a student.

CSV only allows for one type of rows.
For example, it is not possible no also store course data in the same file, as that data does not follow the `rnumber,fname,lname` mold imposed by the first line.
You would need a separate CSV file for this.

Theoretically, a CSV file can contain all kinds of data, including image data:

```csv
x,y,r,g,b
0,0,0,0,0
1,0,255,0,0
...
```

However, this would be *absurdly* inefficient.

## Question

Say we want to keep a list of countries with their capital and population in millions.
Let's keep it simple:

* France with capital Paris: 69 million people.
* Belgium with capital Brussels: 12 million people.
* Netherlands with capital Amsterdam: 17 million people.

Fill `solution.txt` with CSV-formatted data.
There should be a header row with column names `country`, `capital` and `population`.
The `population` column should contain an integer number that expresses the number of millions inhabitants, for example, `12` for Belgium (and not `12000000`).
