# Find Pattern

In this series of challenges, we ask you to discover the pattern yourself:
you will need to find a regular expression that matches certain strings.
Since it would be trivial to simply use `.*` as a solution for every such challenge,
we also give you a number of strings that the regular expression should not match.

## Example

For example, we give you the following strings that should be accepted by the regex:

* `"abcd"`
* `"1234"`
* `"XXXX"`
* `"@1A="`

and the following strings should be rejected:

* `"123"`
* `"ABCDE"`

Based on this input, you should deduce we want the regex to match exactly 4 characters.
Note that in order to prevent you from hardcoding every string (`/abcd|1234|XXXX|@1A=/`) the verification script will check extra cases.

## Question

The following strings must be accepted:

* `"0"`
* `"01"`
* `"010"`
* `"0101"`
* `"01010"`

The following strings must be rejected:

* `""`
* `"1"`
* `"00"`
* `"11"`
* `"10102"`
* `"1001010101"`
