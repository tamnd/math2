---
tag: YZY11W08SD
kind: concept
name: Koszul complex
msc: [13D02, 13D07]
sources:
  - url: https://en.wikipedia.org/wiki/Koszul_complex
same_as:
  wikidata: Q6433699
  wikipedia: Koszul complex
---

## Summary

The Koszul complex of elements $x_1, \ldots, x_n$ of a commutative ring $R$ is a complex of free modules built from the [[exterior algebra|0MDMZ965VE]] of $R^n$.
Its zeroth homology is $R/(x_1, \ldots, x_n)$, and when the $x_i$ form a [[regular sequence|69R5R2FCS5]] it is a [[free resolution|HK2AA1YSQ2]] of this quotient.
It computes [[depth|M2RADBFW99]], gives the proof of [[Hilbert's syzygy theorem|R0DSZPRG6T]], and is a basic tool throughout commutative algebra.

## Explanations

### L1 human

The Koszul complex is the simplest free complex one can write down from a list of elements.
For one element $x$ it is $0 \to R \xrightarrow{x} R \to 0$.
For two elements $x, y$ it is $0 \to R \to R^2 \to R \to 0$, where the last map sends $(a, b)$ to $ax + by$ and the first map sends $c$ to $(-cy, cx)$.
The composite is zero because $-cyx + cxy = 0$, and this simple cancellation is the heart of the construction.
