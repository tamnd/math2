---
tag: F51ANJH2XM
kind: concept
name: Semantic security
msc: [94A60, 68P25]
sources:
  - url: https://en.wikipedia.org/wiki/Semantic_security
same_as:
  wikidata: Q2333581
  wikipedia: Semantic security
---

## Summary

An encryption scheme is semantically secure if whatever an efficient adversary can compute about a message from its ciphertext, it could compute without the ciphertext.
It is the computational analogue of Shannon's perfect secrecy.
Shafi Goldwasser and Silvio Micali introduced it in 1982 with probabilistic encryption.
For encryption against eavesdroppers it is equivalent to [[ciphertext indistinguishability|ZH3TM0EVWQ]], which is easier to check.

## Explanations

### L1 human

A ciphertext should not help an eavesdropper learn anything about the message: not the message itself, not its first letter, not whether it is longer than another.
The eavesdropper may already know something, say that the message is a date.
Semantic security says that the ciphertext adds nothing to this knowledge, for any adversary that runs in reasonable time.
The ElGamal scheme in a suitable group is an example, under a standard assumption.
