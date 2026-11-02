---
tag: AJHEYJE5XY
kind: concept
name: Eilenberg–MacLane space
msc: [55P20]
sources:
  - url: https://en.wikipedia.org/wiki/Eilenberg–MacLane_space
same_as:
  wikidata: Q5349490
  wikipedia: Eilenberg–MacLane space
---

## Summary

An Eilenberg–MacLane space $K(G, n)$ is a path-connected space whose only nonzero [[homotopy group|P976WYEFMB]] is $G$ in degree $n$.
Such spaces exist for every group $G$ when $n = 1$ and every abelian group $G$ when $n \ge 2$, and they are unique up to weak homotopy equivalence.
They are the building blocks of all spaces in the sense of Postnikov towers.
They represent ordinary cohomology: for an abelian group $G$ and a CW complex $X$, $H^n(X; G)$ is the set of homotopy classes of maps $X \to K(G, n)$.

## Explanations

### L1 human

Homotopy groups measure holes of each dimension in a space.
An Eilenberg–MacLane space has holes of exactly one dimension, described by the group $G$.
The circle is $K(\Z, 1)$: it has a one-dimensional hole, and its higher homotopy groups vanish because its universal cover, the line, is contractible.
Infinite-dimensional complex projective space is $K(\Z, 2)$, and infinite-dimensional real projective space is $K(\Z/2, 1)$.
