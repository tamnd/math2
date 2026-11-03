---
tag: FXBNZNG7X3
kind: concept
name: ElGamal encryption
msc: [94A60, 11T71]
specializes: [01E9MNJYEX]
sources:
  - url: https://en.wikipedia.org/wiki/ElGamal_encryption
same_as:
  wikidata: Q1162410
  wikipedia: ElGamal encryption
---

## Summary

ElGamal encryption is a public-key encryption scheme built on a [[cyclic group|0KVGH0J5B3]] in which the [[discrete logarithm|0HJHYMGN3C]] is hard.
It turns the [[Diffie–Hellman key exchange|01TKKESHSB]] into a cipher: a fresh shared group element masks the message by multiplication.
Taher ElGamal published it in 1985.
Encryption is randomized, so the same message gives different ciphertexts each time.

## Explanations

### L1 human

Bob publishes a group element $h = g^x$ and keeps the exponent $x$ secret.
To send a message $m$, Alice picks a random exponent $y$, sends $g^y$, and sends $m$ multiplied by $h^y$.
Bob can compute $h^y$ himself as $(g^y)^x$, divide it out, and read $m$.
An eavesdropper sees $g^x$ and $g^y$ but not $g^{xy}$, so the mask stays hidden as long as the Diffie–Hellman problem is hard.
