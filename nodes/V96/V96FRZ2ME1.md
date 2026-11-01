---
tag: V96FRZ2ME1
kind: statement
role: theorem
name: van der Waerden's theorem
msc: [05D10, 11B25]
about: [G5TWXV565S]
sources:
  - url: https://en.wikipedia.org/wiki/Van_der_Waerden's_theorem
same_as:
  wikidata: Q764287
  wikipedia: Van der Waerden's theorem
---

## Statement

Let $r \ge 1$ and $k \ge 1$ be integers.
Then there is a positive integer $N$ with the following property.
Let $\set{1, \ldots, N}$ be coloured with $r$ colours.
Then there are integers $a \ge 1$ and $d \ge 1$ such that the $k$ numbers $a, a + d, \ldots, a + (k-1)d$ lie in $\set{1, \ldots, N}$ and all have the same colour.

## Remarks

The least such $N$ is the van der Waerden number $W(r, k)$.
For example $W(2, 3) = 9$: the colouring $1, 2, 5, 6$ red and $3, 4, 7, 8$ blue of $\set{1, \ldots, 8}$ has no monochromatic three-term progression, while every $2$-colouring of $\set{1, \ldots, 9}$ has one.
The classical proof is a double induction with "colour focusing" and gives bounds that grow like the Ackermann function.
The theorem also follows from the [[Hales–Jewett theorem|14SGZ5HA4Y]]: a combinatorial line in $\set{0, \ldots, k-1}^n$ is sent to an arithmetic progression by the map $w \mapsto w_1 + \cdots + w_n$.
Shelah gave primitive recursive bounds, and Gowers gave the bound $W(r, k) \le 2^{2^{r^{2^{2^{k + 9}}}}}$ through his proof of [[Szemerédi's theorem|B23B0QEMN5]].

## Explanations

### L1 human

However you colour the positive integers with finitely many colours, one colour contains arithmetic progressions of every length.
The theorem says more: for a given length and number of colours, a fixed finite stretch $1, \ldots, N$ already suffices.

### L2 human

Van der Waerden's theorem is a cornerstone of [[Ramsey theory|G5TWXV565S]] in the integers.
Its density form is [[Szemerédi's theorem|B23B0QEMN5]]: a set of integers of positive upper density contains arbitrarily long progressions.
The colour classes of a colouring cannot all have density zero, so the density form implies the colouring form.
The [[Green–Tao theorem|H8BAHWSEMC]] gives progressions in the primes, which have density zero.
Exact values of $W(r, k)$ are known only for a few small cases.
