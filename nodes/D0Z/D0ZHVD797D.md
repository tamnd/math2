---
tag: D0ZHVD797D
kind: concept
name: Localization of a space
msc: [55P60]
sources:
  - url: https://en.wikipedia.org/wiki/Localization_of_a_topological_space
same_as:
  wikidata: Q6664613
  wikipedia: Localization of a topological space
---

## Summary

Localizing a space at a set of primes $P$ is the topological analogue of [[localizing|4C1AE84N5N]] the integers at $P$.
For a simply connected space $X$ it produces a map $X \to X_P$.
This map tensors every [[homotopy group|P976WYEFMB]] and every homology group with $\Z_{(P)}$.
This lets one study a space one prime at a time.
The empty set of primes gives rationalization, the starting point of [[rational homotopy theory|8G9QPMBT7R]].

## Explanations

### L1 human

Homotopy groups of spaces are often full of torsion at many primes, which makes them hard to compute all at once.
Localization keeps only the information at chosen primes and makes all other primes invertible.
For example, the rationalization of an odd-dimensional sphere $S^n$ is the Eilenberg–MacLane space $K(\Q, n)$.
Rationally, an odd sphere has just one homotopy group, $\Q$ in degree $n$, and all the torsion disappears.
