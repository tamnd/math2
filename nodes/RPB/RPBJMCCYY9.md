---
tag: RPBJMCCYY9
kind: concept
name: Homomorphic encryption
msc: [94A60, 68P25]
sources:
  - url: https://en.wikipedia.org/wiki/Homomorphic_encryption
same_as:
  wikidata: Q2154943
  wikipedia: Homomorphic encryption
---

## Summary

Homomorphic encryption is encryption that allows computation on ciphertexts without decrypting them.
Applying an operation to ciphertexts gives a ciphertext of the result of the operation on the plaintexts.
Schemes such as [[ElGamal encryption|FXBNZNG7X3]] and RSA allow one operation; fully homomorphic schemes allow any computation.
Craig Gentry constructed the first fully homomorphic scheme in 2009, using lattices.

## Explanations

### L1 human

Think of a locked glovebox: a worker can put their hands in and assemble the parts inside, but cannot take anything out.
With homomorphic encryption, a cloud server can compute on your encrypted data and return an encrypted answer.
Only you can decrypt the answer, and the server never sees your data.
For example, multiplying two ElGamal ciphertexts gives a ciphertext of the product of the two messages.
