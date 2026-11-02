---
tag: 8HTHB1QPZY
kind: concept
name: Almost convergence
msc: [40H05, 46A45]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_limit
---

## Summary

A bounded real sequence is almost convergent to $L$ when every [[Banach limit|SYF2ND6J97]] gives it the value $L$.
Every convergent sequence is almost convergent to its limit, but some divergent sequences, such as $1, 0, 1, 0, \dots$, are almost convergent too.
[[Lorentz's characterization|P8TMYNPSYD]] describes almost convergence by averages over long blocks of consecutive terms.

## Explanations

### L1 human

Banach limits are ways to assign a "limit" to every bounded sequence, and there are many of them.
For most divergent sequences they disagree with each other.
A sequence is almost convergent when all of them agree on one value.
For $1, 0, 1, 0, \dots$ they all give $1/2$, which is the average value the sequence takes in the long run, uniformly along the sequence.
