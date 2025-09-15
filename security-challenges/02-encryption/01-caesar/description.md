# Caesar

Encrypting information - making it unreadable - is the domain of cryptography.
Many encryption techniques exist, let's start with a simple (and familiar?) one.

One of the oldest encryption systems is attributed to Julius Caesar and is called the [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher).
The idea is very simple, we encrypt a message by replacing each letter with a different letter that comes later in the alphabet:

```text
Plain      A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Encrypted  X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
```

The distance between the original and the encrypted letter is the *key* necessary for decrypting the message.
In the example above the key is 23.

Encrypting a message with the Caesar Cipher is as easy as replacing every letter in the message.
`I am a secret` becomes `F xj x pbzobq` with key 23.

Decrypting a message is easy if you know the key.
Unfortunately, in the case of the Caesar cipher, it is also not that difficult without knowing the key.
Since there are only 26 keys, trying them all will surely give you the answer.

Another help for decrypting is frequency analysis.
Some letters occur more in text than others.
By counting letters in encrypted text it is possible to guess which encrypted letter corresponds to an `e` for example, making it easier to guess the key used for encrypting.

## Challenge

Encode this string using a Caesar Cipher with key 5: `Caesar Cipher is a very easy encryption technique`.
Upper case characters are encrypted to upper case characters and lower case characters to lower case characters.
