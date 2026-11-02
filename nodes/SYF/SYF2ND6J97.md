---
tag: SYF2ND6J97
kind: concept
name: Banach limit
msc: [40H05, 46B45]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_limit
same_as:
  wikidata: Q806060
  wikipedia: Banach limit
---

## Summary

A Banach limit is a positive, shift-invariant linear functional on the space $\ell^\infty$ of bounded real sequences.
It gives the value $1$ to the constant sequence $1$.
It extends the ordinary limit from convergent sequences to all bounded sequences.
Banach limits exist by the [[Hahn–Banach theorem|QB5AE3VYZZ]], but none can be written down explicitly, and there are many of them.
They define [[almost convergence|8HTHB1QPZY]] and are a basic example of an invariant mean.

## Explanations

### L1 human

The sequence $1, 0, 1, 0, \dots$ has no limit, but it is natural to say that its "average limit" is $1/2$.
A Banach limit is a rule that assigns such a value to every bounded sequence.
It must be linear, it must give a nonnegative value to a nonnegative sequence, and it must not change when you drop the first term.
These rules force the value $1/2$ for $1, 0, 1, 0, \dots$ and the usual limit for every convergent sequence.
