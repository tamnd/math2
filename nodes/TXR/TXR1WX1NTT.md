---
tag: TXR1WX1NTT
kind: concept
name: Berlekamp–Massey algorithm
msc: [94A55, 94B35, 68W30]
sources:
  - url: https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Massey_algorithm
same_as:
  wikidata: Q821007
  wikipedia: Berlekamp–Massey algorithm
---

## Summary

The Berlekamp–Massey algorithm finds the shortest [[linear-feedback shift register|WHX90SGEJ5]] that generates a given finite sequence over a field.
It runs in $O(N^2)$ field operations for a sequence of length $N$, and so computes the [[linear complexity|V2C6HQQAHK]] of the sequence.
Berlekamp found it for decoding [[BCH codes|YY5ZM93GBY]], and Massey recast it as a shift-register synthesis algorithm.
It is used in decoding BCH and [[Reed–Solomon codes|5VBWJ7EFTX]], in cryptanalysis of stream ciphers, and in computer algebra to find linear recurrences.
See the [[definition|PPKMDQAPRP]].

## Explanations

### L1 human

Suppose you see the first terms of a sequence and suspect that each term is a fixed linear combination of a few earlier ones.
The Berlekamp–Massey algorithm finds the shortest such rule.
It reads the terms one at a time and keeps a current best rule.
When a new term disagrees with the prediction, it repairs the rule using an older rule that failed at an earlier step, lengthening the rule only when it must.
For example, from $1, 1, 0, 1, 1, 0$ over $\F_2$ it finds the rule "each term is the sum of the previous two".
