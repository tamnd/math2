---
tag: PAXCH4FFSV
kind: concept
name: Double series
msc: [40B05]
sources:
  - url: https://en.wikipedia.org/wiki/Series_(mathematics)
---

## Summary

A double series $\sum_{m,n} a_{m,n}$ adds the terms of a [[double sequence|B70G8FYPG0]].
Its partial sums are sums over rectangles $\set{0, \ldots, M} \times \set{0, \ldots, N}$, and it converges when these tend to a limit as $M$ and $N$ both grow.
Double series arise from products of series, from power series in two variables, and from sums over lattices.
When the terms are absolutely summable, the double sum equals each iterated sum, by [[Fubini's theorem for series|WW53KG71KH]].
The exact definition is in [[double series|CWP26Y1TCZ]].

## Explanations

### L1 human

A double series adds up all the numbers of an infinite table.
One adds the entries in a growing rectangle in the top-left corner and asks whether these sums settle down.
For example, the table with entries $1/(2^m 3^n)$ has rectangle sums that approach $2 \cdot \tfrac32 = 3$.
