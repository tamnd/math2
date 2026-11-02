---
tag: EWFWTSVY0B
kind: concept
name: Symbolic dynamics
msc: [37B10]
sources:
  - url: https://en.wikipedia.org/wiki/Symbolic_dynamics
same_as:
  wikidata: Q1350838
  wikipedia: Symbolic dynamics
---

## Summary

Symbolic dynamics studies systems whose states are infinite sequences of symbols from a finite alphabet.
Their time evolution is the shift of a sequence by one place.
These systems are the [[shift spaces|A1XE59ZHNM]].
It is also a method: one codes an orbit of a general system by the pieces of a finite partition that it visits.
Through such codings, questions about smooth or hyperbolic systems become combinatorial questions about sequences, as for [[subshifts of finite type|624XDXX8FN]].

## Explanations

### L1 human

Divide the space of a system into a few labelled regions, say $0$ and $1$.
Instead of following a point exactly, write down the label of the region it visits at each time.
The orbit becomes an infinite word such as $0110100\ldots$, and moving forward in time just deletes the first letter.
For the doubling map $x \mapsto 2x \bmod 1$, with the regions $[0, 1/2)$ and $[1/2, 1)$, the word of $x$ is its binary expansion.
Symbolic dynamics studies the sets of words that arise this way.
