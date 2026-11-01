---
tag: K26WG8C6PV
kind: concept
name: Baire function
msc: [26A21]
sources:
  - url: https://en.wikipedia.org/wiki/Baire_function
same_as:
  wikidata: Q803935
  wikipedia: Baire function
---

## Summary

Baire functions are the functions obtained from [[continuous functions|0P27W9RW0G]] by taking [[pointwise limits|056FSKG32J]] of sequences, again and again.
They are sorted into Baire classes indexed by the countable ordinals.
Class $0$ is the continuous functions, and class $1$ is the pointwise limits of continuous functions.
On $\R$, the Baire functions are exactly the Borel measurable functions.
The classes give a fine measure of how far a function is from being continuous.

## Explanations

### L1 human

Pointwise limits of continuous functions need not be continuous.
For example, $x^n$ on $[0, 1]$ tends to a function that is $0$ before $1$ and $1$ at $1$.
Such limits form Baire class $1$.
Limits of those can be even rougher, and they form class $2$, and the process continues.
