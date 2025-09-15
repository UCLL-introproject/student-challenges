# SQL

When dealing with large amounts of data, it is essential that it can be accessed and modified efficiently and safely:

* We need to be able to look up specific information very quickly.
* Many people/machines might want to update the data at the same time.
  In order to safeguard the integrity of the data, these accesses need to be coordinated very carefully.
* If there is some kind of problem (a crash, a power outage, ...) the data must not be corrupted.

Database management systems (such as PostgreSQL, MySql, MariaDB, MS SQL Server, MongoDB, ...) are highly advanced pieces of software that provide this exact functionality.

There are different styles of database systems (relational, NoSQL, ...) which organize the data differently.
Which is best depends on the usage patterns, but in practice, relational databases are still the most commonly used.

A language specialized in communicating with relational databases was designed: SQL (Structured Query Language, often pronounced sequel).
Becoming proficient in SQL will be important aspect of your education, which is why it is the focus of multiple courses.

## Hacking

If something is widely used, it automatically becomes a popular target of hackers: they try to find weaknesses or misuses that they can exploit.
One very common attack (there's even an [xckd](https://xkcd.com/327/) about it) goes as follows.

Say you're implementing the login page of a website: the user enters their name and password.
You want to ask the database, where their credentials are stored, if the provided name and password are indeed correct.
Your code contains a template SQL question for the database (actual SQL does not look like this, we simplified for the sake of clarity):

```text
Does user XXX have password YYY?
```

What you do is replace `XXX` by the username and `YYY` by the password, and send the question to the database.
If the database answers yes, you know you can safely let the user in.

Say a hacker enters `John` as username, and `azer1234, or is 1 + 1 equal to 2`.
The question that gets send to the database thus becomes

```text
Does user John have password azer1234, or is 1 + 1 equal to 2?
```

While the first part of the question is (hopefully) false, the second part is true, and the database will respond with "yes".
Now the hacker has successfully logged in as John.

## Question

What is this attack technique called?
