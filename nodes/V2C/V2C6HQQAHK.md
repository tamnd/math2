---
tag: V2C6HQQAHK
kind: concept
name: Linear complexity of a sequence
msc: [94A55, 94A60, 11B37]
sources:
  - url: https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Massey_algorithm
---

## Summary

The linear complexity of a sequence over a field is the length of the shortest [[linear-feedback shift register|WHX90SGEJ5]] that generates it.
It measures how far the sequence is from being predictable by a linear rule.
In cryptography, a keystream with small linear complexity is weak.
The [[Berlekamp–Massey algorithm|TXR1WX1NTT]] recovers a generating register from about twice as many terms as the complexity.
See the [[definition|6X41CC3QWM]].

## Explanations

### L1 human

Some sequences follow a short linear rule, like $1, 1, 0, 1, 1, 0, \dots$, where each term is the sum mod $2$ of the two before it.
The linear complexity is the number of earlier terms such a rule needs to look back at, in the best case.
A constant zero sequence has complexity $0$, and the sequence $1, 1, 0, 1, 1, 0$ has complexity $2$.
A truly random sequence of length $N$ has complexity close to $N/2$.
A sequence used to hide messages should have high linear complexity, or an attacker can extend it from a short piece.
