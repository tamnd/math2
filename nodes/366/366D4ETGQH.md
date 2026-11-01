---
tag: 366D4ETGQH
kind: object
name: Conway groups
msc: [20D08, 11H56]
uses: [PZ49Z4CBFZ, 0YMYMNQ0QZ, XETV3657DG, 0K1SCPBNKJ, 0DZ93493VN]
sources:
  - url: https://en.wikipedia.org/wiki/Conway_group
same_as:
  wikidata: Q942433
  wikipedia: Conway group
---

## Description

The Conway groups $\mathrm{Co}_1$, $\mathrm{Co}_2$ and $\mathrm{Co}_3$ are three [[sporadic groups|PZ49Z4CBFZ]], found by John Conway from the symmetries of the [[Leech lattice|XETV3657DG]].
Let $\mathrm{Co}_0$ be the [[automorphism group|0K1SCPBNKJ]] of the Leech lattice, that is, the group of linear isometries of $\R^{24}$ that map the lattice onto itself.
Its [[centre|0DZ93493VN]] is $\set{\pm 1}$, and its order is $8315553613086720000$.

1. $\mathrm{Co}_1 = \mathrm{Co}_0 / \set{\pm 1}$, of order $4157776806543360000 = 2^{21} \cdot 3^9 \cdot 5^4 \cdot 7^2 \cdot 11 \cdot 13 \cdot 23$.
2. $\mathrm{Co}_2$ is the stabiliser in $\mathrm{Co}_0$ of a lattice vector of norm $4$, of order $42305421312000 = 2^{18} \cdot 3^6 \cdot 5^3 \cdot 7 \cdot 11 \cdot 23$.
3. $\mathrm{Co}_3$ is the stabiliser in $\mathrm{Co}_0$ of a lattice vector of norm $6$, of order $495766656000 = 2^{10} \cdot 3^7 \cdot 5^3 \cdot 7 \cdot 11 \cdot 23$.

All three are [[simple groups|0YMYMNQ0QZ]].
Here the lattice is scaled so that its shortest nonzero vectors have norm $4$.

## Remarks

The group $\mathrm{Co}_0$ itself is not simple, because of its centre $\set{\pm 1}$.
Several other sporadic groups are subgroups of $\mathrm{Co}_0$, among them the [[Mathieu group|T1KR4KPX8P]] $M_{24}$, the Higman–Sims group and the McLaughlin group.
All three Conway groups are subquotients of the [[Monster group|C9VY20TAPT]].

## Explanations

### L1 human

The Leech lattice is an extremely symmetric arrangement of points in $24$-dimensional space.
Its symmetry group, divided by the symmetry $v \mapsto -v$, is the simple group $\mathrm{Co}_1$.
The groups $\mathrm{Co}_2$ and $\mathrm{Co}_3$ are the symmetries that keep one chosen lattice point fixed, for two kinds of points.
