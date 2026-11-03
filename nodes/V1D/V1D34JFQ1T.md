---
tag: V1D34JFQ1T
kind: concept
name: Locally testable code
msc: [94B60, 68W20]
specializes: [TAE6K8NQ46]
sources:
  - url: https://en.wikipedia.org/wiki/Locally_testable_code
same_as:
  wikidata: Q6664705
  wikipedia: Locally testable code
---

## Summary

A locally testable code is an [[error-correcting code|TAE6K8NQ46]] that comes with a randomized test.
The test reads only a few symbols of a word and tells whether the word is a codeword or far from every codeword.
Codewords always pass, and words far from the code fail with a probability that grows with their distance from the code.
Locally testable codes are closely tied to probabilistically checkable proofs and the [[PCP theorem|WJXX7H6B6V]].

## Explanations

### L1 human

Imagine checking a long file for damage while you may look at only three of its symbols.
For a general code this is hopeless, but some codes have so much internal structure that local checks reveal global damage.
The [[Hadamard code|HSXZD57ABX]] is the standard example.
Its codewords are the linear functions $f \colon \F_2^k \to \F_2$, and the test picks random $a, b$ and checks $f(a) + f(b) = f(a + b)$.
A linear function always passes, and a function that is far from every linear function fails often.
