---
tag: RF9TDRQ2P4
kind: concept
name: McEliece cryptosystem
msc: [94A60, 94B05, 11T71]
specializes: [01E9MNJYEX]
sources:
  - url: https://en.wikipedia.org/wiki/McEliece_cryptosystem
same_as:
  wikidata: Q1042583
  wikipedia: McEliece cryptosystem
---

## Summary

The McEliece cryptosystem is a public-key encryption scheme built from an error-correcting [[linear code|E85KREWV60]].
The public key is a scrambled generator matrix of a code with a fast decoder.
A ciphertext is a codeword plus a random error of small weight.
Robert McEliece proposed it in 1978, using binary [[Goppa codes|KJCJSAPV1P]].
No efficient quantum attack on it is known, so it is a candidate for post-quantum cryptography; its drawback is a very large public key.

## Explanations

### L1 human

The private key is a code that the owner knows how to decode quickly.
The owner hides it by scrambling its generator matrix, and publishes the result.
To encrypt, one encodes the message with the public matrix and deliberately adds a few random errors.
The owner unscrambles and uses the fast decoder to remove the errors.
An attacker sees only what looks like a random code, and decoding a random linear code is believed to be hard.
