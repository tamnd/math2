---
tag: SVR0RPWAGP
kind: concept
name: Cyclic redundancy check
msc: [94B15, 94B20]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_redundancy_check
same_as:
  wikidata: Q245471
  wikipedia: Cyclic redundancy check
---

## Summary

A cyclic redundancy check, or CRC, is an error-detecting code that appends to a block of data the remainder of a polynomial division over $\F_2$.
The data bits are read as a polynomial.
The check bits are chosen so that the whole sent word is divisible by a fixed generator polynomial.
The receiver divides again; a nonzero remainder shows that an error occurred.
CRCs are cheap to compute with shift registers and detect all short bursts of errors.
So they are used in network protocols, storage and file formats.

## Explanations

### L1 human

A CRC is like a check digit, but computed by a division of polynomials with bits as coefficients.
The sender attaches the remainder to the message, so that the result divides evenly by an agreed polynomial.
If noise flips some bits on the way, the division almost certainly stops being even, and the receiver notices.
It cannot fix the error; it only raises the alarm so that the data can be sent again.
