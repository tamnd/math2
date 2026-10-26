---
tag: 01E9MNJYEX
kind: concept
name: Public-key cryptography
aliases: [asymmetric-cryptography]
msc: ["94A60"]
sources:
  - url: https://en.wikipedia.org/wiki/Public-key_cryptography
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Public-key_cryptography
    locator: Description
same_as:
  wikidata: Q201339
  wikipedia: Public-key cryptography
---

## Summary

Public-key cryptography is a kind of cryptography in which each user has a pair of keys: a public key and a private key.
Anyone can use the public key to encrypt a message or to check a signature. Only the owner of the private key can decrypt the message or make the signature.
Its security depends on problems that are believed to be hard to solve, such as integer factorization or the [[discrete logarithm|09B4X51J09]].

## Remarks

Before the mid-1970s, all ciphers were symmetric: both parties used the same secret key, which they had to exchange in a secure way.
The [[RSA cryptosystem|0HM584C465]] and the [[Diffie–Hellman key exchange|01TKKESHSB]] are two early examples.
Whitfield Diffie and Martin Hellman published the idea in 1976.

## Explanations

### L1 human

Think of a mailbox with a slot: anyone can drop a letter in, but only the owner has the key to open it.
The public key is the slot, and the private key is the key of the mailbox.
