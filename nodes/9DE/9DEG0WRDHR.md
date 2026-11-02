---
tag: 9DEG0WRDHR
kind: concept
name: Ehrhart polynomial
msc: [52B20, 11P21, 05A15]
sources:
  - url: https://en.wikipedia.org/wiki/Ehrhart_polynomial
same_as:
  wikidata: Q5348622
  wikipedia: Ehrhart polynomial
---

## Summary

The Ehrhart polynomial of a [[lattice polytope|F39N9NBFPZ]] $P$ counts the integer points in the dilates $tP$ for positive integers $t$.
Ehrhart's theorem says that this count is a polynomial in $t$ of degree $\dim P$.
Its leading coefficient is the volume of $P$ when $P$ is full-dimensional, and its constant term is $1$.
It is a discrete analogue of volume, and it satisfies [[Ehrhart–Macdonald reciprocity|ZDBER9FJ6T]].

## Explanations

### L1 human

Blow up a lattice polygon by a factor $t$ and count the grid points inside it, including those on the boundary.
For the unit square the count is $(t+1)^2$: a $t$ by $t$ square holds $t+1$ points along each side.
For every lattice polytope the count follows a polynomial formula in $t$ like this one.
For a full-dimensional polytope in $\R^n$ and large $t$, the count is close to the volume times $t^n$, as one expects from area.
