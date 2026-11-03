---
tag: ZH3TM0EVWQ
kind: concept
name: Ciphertext indistinguishability
msc: [94A60, 68P25]
sources:
  - url: https://en.wikipedia.org/wiki/Ciphertext_indistinguishability
same_as:
  wikidata: Q840661
  wikipedia: Ciphertext indistinguishability
---

## Summary

Ciphertext indistinguishability is a security notion for encryption schemes, defined by a game.
An adversary chooses two messages, receives the encryption of one of them, and must guess which one it was.
The scheme is secure if no efficient adversary guesses correctly with probability noticeably better than $1/2$.
Variants allow the adversary to ask for decryptions (chosen-ciphertext attacks), and the notion is equivalent to semantic security.

## Explanations

### L1 human

Imagine a test: you pick two messages, say "attack" and "retreat", and someone encrypts one of them at random.
If you cannot tell which was encrypted better than by tossing a coin, the ciphertext hides everything that matters.
One consequence is that encryption must be randomized.
If the same message always gave the same ciphertext, you could encrypt both candidates yourself and compare.
