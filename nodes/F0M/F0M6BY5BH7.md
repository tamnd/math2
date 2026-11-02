---
tag: F0M6BY5BH7
kind: definition
name: Exact couple
msc: [55T05, 18G40]
defines: VXDPP4EJPG
uses: [071DDFVG4J, CBDM280TDF]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_couple
---

## Definition

An *exact couple* consists of two [[abelian groups|071DDFVG4J]] $D$ and $E$ and three homomorphisms
$$i \colon D \to D, \qquad j \colon D \to E, \qquad k \colon E \to D,$$
such that the triangle is [[exact|CBDM280TDF]] at each vertex:

1. $\ker j = \im i$;
2. $\ker k = \im j$;
3. $\ker i = \im k$.

## Remarks

The map $d = j \circ k \colon E \to E$ satisfies $d \circ d = j (k j) k = 0$, by clause 2.
The *derived couple* has $D' = i(D)$ and $E' = \ker d / \im d$, with $i'$ the restriction of $i$, $j'(i(x)) = [j(x)]$ and $k'([e]) = k(e)$; it is again an exact couple.
Iterating gives groups $E^r$ with differentials $d^r$ such that $E^{r+1}$ is the homology of $(E^r, d^r)$, that is, a [[spectral sequence|GG8AYV847V]].
In practice $D$ and $E$ are bigraded, and the bidegrees of $i, j, k$ fix the bidegree of each $d^r$.

Example: let $C$ be a chain complex of free abelian groups and $p$ a prime.
The short exact sequence $0 \to C \xrightarrow{p} C \to C / pC \to 0$ gives a long exact sequence in homology.
It is an exact couple with $D = H_*(C)$, $E = H_*(C/pC)$, $i$ multiplication by $p$, $j$ reduction mod $p$ and $k$ the connecting map.

Non-example: take $D = E = \Z$ with $i = 0$, $j = \id$ and $k = 0$.
Clause 1 holds, since $\ker j = 0 = \im i$, and clause 2 holds, since $\ker k = \Z = \im j$.
Clause 3 fails, since $\ker i = \Z$ while $\im k = 0$.

Exact couples were introduced by William S. Massey.
