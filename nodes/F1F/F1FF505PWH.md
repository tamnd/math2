---
tag: F1FF505PWH
kind: concept
name: Height function
msc: [11G50, 14G40]
sources:
  - url: https://en.wikipedia.org/wiki/Height_function
same_as:
  wikidata: Q65088643
  wikipedia: Height function
---

## Summary

A height function measures the arithmetic complexity of a rational or algebraic point, roughly the number of digits needed to write down its coordinates.
The basic example is the Weil height on projective space; composing it with a morphism gives heights on any projective variety.
The key property, due to Northcott, is that there are only finitely many points of bounded height and bounded degree.
Heights drive finiteness proofs such as [[Mordell's theorem|BZHGKN6Q3K]] and appear in the [[Gross–Zagier theorem|BX558DTV2D]] and the [[Birch and Swinnerton-Dyer conjecture|ZWEFBG40H9]].

## Explanations

### L1 human

The rational numbers $1/2$ and $1000001/2000001$ are close in size, but the second is much more complicated.
A height captures this: the height of a fraction $a/b$ in lowest terms is $\max(\abs{a}, \abs{b})$, so the first has height $2$ and the second has height $2000001$.
There are only finitely many fractions of height at most a given bound, so heights let one turn "infinitely many points" into "points of ever larger complexity".
For points with several coordinates, one takes the largest coordinate after clearing denominators.
On an elliptic curve, a refined height behaves like a quadratic form under the group law, which is the engine of the descent proofs.
