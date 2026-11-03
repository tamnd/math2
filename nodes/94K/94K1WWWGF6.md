---
tag: 94K1WWWGF6
kind: concept
name: Perfect code
msc: [94B25, 94B65]
specializes: [TAE6K8NQ46]
sources:
  - url: https://en.wikipedia.org/wiki/Hamming_bound
---

## Summary

A perfect code is an [[error-correcting code|TAE6K8NQ46]] whose Hamming balls of some radius $t$ around the codewords cover the whole space without overlap.
Equivalently, it meets the [[Hamming bound|RZEGDKR7C7]] with equality.
Perfect codes are as efficient as possible for correcting $t$ errors.
They are rare.
Over prime power alphabets they are classified.
If $t \ge 1$ and there are two or more codewords, the parameters are those of a Hamming, Golay or odd binary repetition code.

## Explanations

### L1 human

Picture each codeword with a bubble around it containing the words with at most $t$ errors.
In a perfect code the bubbles do not overlap and leave no gap: every possible word lies in exactly one bubble.
So every received word is decoded without doubt to the codeword of its bubble.
The $[7, 4, 3]$ Hamming code is perfect: its $16$ bubbles of $8$ words each fill all $128$ words of length $7$.
