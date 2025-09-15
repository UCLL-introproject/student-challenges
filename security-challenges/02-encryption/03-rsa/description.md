# RSA

## Symmetric Encryption

The goal of encryption is to allow two distant parties to communicate securely.
This requires both parties have to agree on shared secret, commonly called the key.
Only people with this key can encrypt and decrypt messages.

A popular analogy is of imagining an unbreakable chest with an unpickable lock on it.
Therefore, only those that have the key to this lock can open the chest.
To communicate, one party unlocks the chest, puts a message in it, and locks the chest.
The chest can then safely travel to the other party, who, with their own copy of the key, can open the chest and read the message.

But what happens if the chest is intercepted by a third party?
Well, nothing really, that's the whole point of encryption.
Without key, the third party cannot open the chest, so no secrets are revealed.
The worst they can do is keep the message from arriving.
It is also impossible for them to create a fake message, as it would require them to create a fake chest with the same lock as the real chest.

This encryption is called *symmetric* the same key is used for both encryption and decryption.
Of course, in reality, we do not work with actual chests, locks and keys, but with mathematics.
The most well known symmetric encryption algorithm is AES, which we discussed in the previous challenge.

## Downsides of Symmetric Encryption

Symmetric encryption has a major flaw.
Perhaps you want to take some time thinking about what this flaw could be?

In order to be able to use symmetric encryption, both parties need to have agreed on a key.
One party could choose a key and then needs to send it to the other party, but how does this key make it there safely?
With the chest analogy, we could imagine both parties coming together to create a key, but when sending data over the internet,
we cannot be expected to first have to physically go somewhere to receive our encryption key.

The situation only gets worse if we need more people involved in the same conversation.

## Rivest, Shamir, Adleman

Fortunately, in 1997, three men named Ron Rivest, Adi Shamir and Leonard Adleman put their heads together and found a way around this problem.
Let's go back to our chest analogy.
Alice and Bob are two friends who live far away from each other.
Alice wants to send a secret message to Bob.
They proceed as follows:

* Bob builds padlocks that all open with the same key.
  He keeps this key to himself, but freely distributes the padlocks: anyone get have as many as they wish.
* Alice gets one of Bob's padlocks.
  She puts her secret message in a chest, and locks it using Bob's padlock.
* The chest gets transported to Bob.
* Bob can open the chest, since he has the key to his padlock.

If Bob needs to send an answer to Alice, she needs to create her own padlocks and key.

Rivest, Shamir and Adleman found a mathematical equivalent of this approach.
The resulting algorithm was named RSA.
Notice how there is no key to be shared: thanks to this approach, two people who never met can actually communicate securely.

In encryption terms, the freely distributed padlock is called the *public key*, whereas the key that opens the padlock is known as the *private key*.
Whenever someone wants to be able to be contacted, they create a public/private key pair and publish the public key.
This is called asymmetric encryption, due to the fact that two different keys are involved with different purposes.

## Signature

A now have to deal with a new downside: if Bob receives a message, how can he be sure it comes from Alice?
Everyone has access to his public key, so the message could come from anyone.

Let's consider an interesting twist: what if we reverse the role of the public and private key?
In our previous scenario, Alice used Bob's *public* key to encrypt her message, and then Bob used his *private* key to decrypt.
The opposite is also possible: the private key can be used to encrypt, and the public key would then decrypt.

This allows Alice to "sign her messages" and prove authorship.
Consider the following scenario: Alice wants to send a message to Bob, but bob needs to be convinced it does indeed come from Alice.
Alice encrypts her message with her own private key, sends it to Bob, and he can decrypt it with her public key.
Note that the message can now be decrypted by everyone: since everyone has access to the public key, everyone can read the message.
However, the fact that the message can be decrypted using Alice's public key is proof that she is its author.

(In reality, proving authorship is done in a slightly different, more efficient way, but the above approach works just as well.)

## Confidentiality and Authenticity

Confidentiality (keeping the message secret) can be achieved by encrypting using the public key.
Authenticity (proving authorship) is obtained by encrypting using the private key.
We can combine both as follows:

* Alice encrypts her message with her own private key.
* Alice then encrypts the result with Bob's public key.
* Bob receives this doubly encrypted message.
* Bob first decrypts it using his private key.
* Next, he decrypts it using Alice's public key.
* Bob can now read the message, and he can be certain that
  * it comes from Alice, and
  * no one else has read it.

## Efficiency

While asymmetric encryption is very flexible, it sadly also tends to be computationally expensive, especially compared to symmetric encryption.
Luckily, it is possible to combine the strengths of both approaches:

* Alice decides she wants to talk to Bob.
* Alice creates a key for a *symmetric* encryption.
* Alice encrypts this key with Bob's public key.
* Bob decrypts it using his private key.
* All further communication takes place using symmetric encryption, relying on the key that Alice sent to Bob using asymmetric encryption.

This is also what happens in the real world, such as HTTPS (which is used to browse the web).

As you can see, we have these building blocks, also called cryptographic primitives, that can be used in different ways to achieve all kinds of desirable properties (confidentiality, authenticity, efficiency, ...)
In the world of cybersecurity, it is important to be aware of possible attacks, and to find ways to thwart them by combining the right primitives.

## Question

RSA is still very much in use today, but for newer systems, a different, more efficient approach is preferred.
What is this alternative called?
