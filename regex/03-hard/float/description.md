# Float

Write a regular expression that checks if a string represents a valid number.
The rules are:

* There can be a sign, e.g., `-5`.
* There can be no redundant characters, e.g., `5x` should not be accepted.
* A decimal point should be allowed.
  If there is a decimal point, at least one digit should follow it.
  For example, `4.` is not correct, but `4.0` is.
* No redundant zeros are allowed on the left side: `05` should be rejected.
  They are allowed after the decimal point.
