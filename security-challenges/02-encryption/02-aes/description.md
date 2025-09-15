# AES

Encryption algorithms have become indispensable in our modern world.
Encryption is not just used for reliable authentication or performing payments: your Google searches, your Wikipedia visits, your video streaming, ... are all encrypted.

For example, when you browse to a website, the [TLS protocol](https://en.wikipedia.org/wiki/Transport_Layer_Security) is used to securely communicate with the server, which involves encrypting all data in both directions.
If you're connected to the internet using Wi-Fi, [WPA3](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access) will cause that TLS encrypted data to get encrypted a second time.
While repeatedly encrypting the same data does not make it "uncrackabler", it does have benefits in this case.
Using TLS, the communication between you and the server itself is encrypted, but not the recipients of the messages: without that information, internet routers would not know who to deliver the messages to.
When using wireless communication, malicious agents can easily "hear your conversations".
They might not understand *what* you're saying, but they know *who* you're saying it to, which in itself violates privacy.
WPA3's extra layer of encryption solves this issue by also concealing the recipients.

Given that the world relies on encryption so much, it is also crucial that the encryption algorithms be efficient and de facto unbreakable.
Creating such an algorithm is extremely hard and requires the involvement of the greatest minds in the field.
Even the largest companies such as Google, Microsoft or Amazon would not dare think of creating their own encryption methods.

So how then are encryption algorithms created?
Well, by having a contest, more or less.

## NIST

In 1997, [NIST](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology) announced
that they [wanted a new encryption algorithm](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard_process), because the old one (DES, dating from the 70s) was starting to show its age.

In a first step, they invited everyone to give their opinion on how DES's successor should be chosen.
Very excited about the open nature of this process, the cryptographic community immediately responded en masse.

After receiving all this feedback, it was decided that candidate algorithms could be submitted.
These would then be analyzed by cryptographers and discussed on conferences.
There were three rounds of voting and only the algorithms with the most votes would make it to the next round.
Ultimately, the algorithm known as Rijndael won and was chosen as the new standard way of encryption.

AES remains as of yet still unbroken, despite many attempts.
It is used in many places, including WPA3 (Wi-Fi), TLS (browsing the web), VPNs, password managers ([Lastpass](https://www.lastpass.com/security/zero-knowledge-security), [Bitwarden](https://bitwarden.com/help/what-encryption-is-used/), ...), cloud services (AWS, Azure, ...), governments, etc.
Basically, when you need encryption (symmetric key encryption, to be precise), AES is safe choice.
AES is so widely used it is even built into modern processors.

Later on, Europe would hold their [own contest](https://en.wikipedia.org/wiki/NESSIE), as well as [Japan](https://en.wikipedia.org/wiki/CRYPTREC).
Rijndael/AES was among the winners in both.

## Question

Rijndael, the winner of the AES contest, was developed by two KU Leuven researchers.
What are their names (= first name and surname)?
Write their names on separate lines in `solution.txt`.
