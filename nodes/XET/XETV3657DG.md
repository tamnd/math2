---
tag: XETV3657DG
kind: object
name: Leech lattice
msc: [11H06, 11H31, 11H56]
uses: [WN9V7WSJKF, 0XPR1E85W0, SM1TJSAR75]
sources:
  - url: https://en.wikipedia.org/wiki/Leech_lattice
same_as:
  wikidata: Q2510203
  wikipedia: Leech lattice
---

## Description

The Leech lattice $\Lambda_{24}$ is a [[lattice|WN9V7WSJKF]] in the [[Euclidean space|0XPR1E85W0]] $\R^{24}$, discovered by John Leech.
Up to isometry, it is the unique lattice $L \subset \R^{24}$ with these properties:

1. $L$ is unimodular: it has a basis whose Gram matrix has determinant $1$;
2. $L$ is even: $x \cdot x$ is an even integer for every $x \in L$;
3. $L$ has no vector $x$ with $x \cdot x = 2$.

So its shortest nonzero vectors have norm $x \cdot x = 4$.
There are $196560$ of them.

## Remarks

The Leech lattice can be constructed from the extended binary [[Golay code|SM1TJSAR75]].
Its automorphism group $\mathrm{Co}_0$ has order $8315553613086720000$, and its quotient by $\set{\pm 1}$ is the [[Conway group|366D4ETGQH]] $\mathrm{Co}_1$.
The $196560$ shortest vectors show that the kissing number in dimension $24$ is at least $196560$, and in fact it equals $196560$.
The sphere packing obtained from the Leech lattice is the densest sphere packing in $\R^{24}$; this was proved by Cohn, Kumar, Miller, Radchenko and Viazovska.
Even unimodular lattices exist only in dimensions divisible by $8$.
In dimension $24$ there are $24$ of them up to isometry, and the Leech lattice is the only one without vectors of norm $2$.

## Explanations

### L1 human

A lattice is a regular grid of points, like the integer points in the plane, but it can be tilted and stretched.
The Leech lattice is a very special grid in $24$ dimensions.
If you put equal balls at its points, each ball touches $196560$ others, the most possible in $24$ dimensions, and the packing is the densest possible there.
Its symmetry group is huge and gave rise to several new finite simple groups.
