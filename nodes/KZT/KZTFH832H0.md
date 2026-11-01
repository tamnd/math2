---
tag: KZTFH832H0
kind: statement
role: theorem
name: Stark–Heegner theorem
msc: [11R29, 11R11]
uses: [7SV4WA92SM, KTKK9B1X41, WQ46BD3ARY, KTGAS9DGRX, 0W4X9G6263, D3HEJTVY7G, SBDSYA037Q]
about: [7SV4WA92SM, KTKK9B1X41]
sources:
  - url: https://en.wikipedia.org/wiki/Stark%E2%80%93Heegner_theorem
same_as:
  wikidata: Q2793600
  wikipedia: Stark–Heegner theorem
---

## Statement

Let $d$ be a positive squarefree integer.
The imaginary [[quadratic field|7SV4WA92SM]] $\Q(\sqrt{-d})$ has [[class number|KTKK9B1X41]] $1$ if and only if
$$d \in \set{1, 2, 3, 7, 11, 19, 43, 67, 163}.$$

## Remarks

Equivalently, the fundamental discriminants $D < 0$ with class number $1$ are $-3, -4, -7, -8, -11, -19, -43, -67, -163$.
Class number $1$ means that the ring of integers is a principal ideal domain, or, equivalently for rings of integers, a [[unique factorisation domain|0W4X9G6263]].
Gauss's work on [[binary quadratic forms|SBDSYA037Q]] led him to expect this list; the theorem settles the case $h = 1$ of the [[class number problem|KTGAS9DGRX]].
Heegner gave a proof using modular functions and [[complex multiplication|D3HEJTVY7G]], which was at first not accepted.
Baker, with linear forms in logarithms, and Stark, with a method close to Heegner's, later gave complete proofs.

Example: $\Q(\sqrt{-163})$ has class number $1$.
A related fact is that $n^2 + n + 41$ is prime for $n = 0, 1, \ldots, 39$; this works because $163 = 4 \cdot 41 - 1$.
By contrast $\Q(\sqrt{-5})$ has class number $2$, as $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$ shows.

## Explanations

### L1 human

In most rings of algebraic integers, numbers can factor into irreducibles in several different ways.
For imaginary quadratic fields, the theorem gives the complete list of the nine fields where factorisation is unique.
The largest one comes from $\sqrt{-163}$.

### L2 human

The main difficulty is to rule out one possible extra field with a huge discriminant.
Lower bounds for class numbers of the form $h(-d) \to \infty$ were known, but they were not effective, so they could not exclude a single exception.
The theorem is closely related to the near-integer $e^{\pi \sqrt{163}}$, which comes from the $j$-invariant at a point of complex multiplication.
