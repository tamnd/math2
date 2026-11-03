---
tag: 7YNRCX56CM
kind: concept
name: Cryptography
msc: [94A60, 68P25]
sources:
  - url: https://en.wikipedia.org/wiki/Cryptography
same_as:
  wikidata: Q8789
  wikipedia: Cryptography
---

## Summary

Cryptography is the mathematical study of methods that protect information against adversaries.
Its basic tasks are secrecy, integrity and authenticity.
Secrecy means that only the intended reader understands a message; integrity, that changes are noticed; authenticity, that the sender can be identified.
Modern cryptography states each task as a precise security definition and proves that a scheme meets it, often assuming that some computational problem is hard.
It draws on number theory, algebra, probability and complexity theory, and it secures most digital communication today.

## Explanations

### L1 human

Two people want to talk while an eavesdropper listens to everything they send.
Cryptography gives them ways to scramble a message with a secret key, so that it looks like noise to anyone without the key.
A classic toy example is the Caesar cipher: shift each letter three places, so that "ABC" becomes "DEF".
This cipher is easy to break, since there are only $26$ shifts to try.
Modern ciphers have so many keys that trying them all would take longer than the age of the universe, and their designs resist cleverer attacks too.
