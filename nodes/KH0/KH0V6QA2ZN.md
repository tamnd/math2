---
tag: KH0V6QA2ZN
kind: concept
name: Mosco convergence
msc: [49J45, 49J40, 49J53]
specializes: [NW9MM370A5]
sources:
  - url: https://en.wikipedia.org/wiki/Mosco_convergence
same_as:
  wikidata: Q6915414
  wikipedia: Mosco convergence
---

## Summary

Mosco convergence is a convergence of functionals on a normed space that combines the weak and the strong topology.
It asks for the lower bound inequality of [[Γ-convergence|NW9MM370A5]] along weakly convergent sequences and for recovery sequences that converge strongly.
It was introduced by Umberto Mosco to study the stability of variational inequalities when the constraint sets change.
In finite dimension it is the same as Γ-convergence; in general it implies Γ-convergence for both the weak and the norm topology.
The [[definition|RNDKD74V17]] gives the precise conditions.

## Explanations

### L1 human

In an infinite-dimensional space, bounded sequences often have no strongly convergent subsequence, but they have weakly convergent ones.
So a useful lower bound must hold along weakly convergent sequences, while a useful approximation should be as good as possible, that is strong.
Mosco convergence asks for exactly this pair of conditions.
For closed convex sets $K_n$ it says two things.
Weak limits of points of $K_n$ lie in the limit set $K$, and each point of $K$ is a strong limit of points of $K_n$.
For example, the segments $K_n = [0, 1 - 1/n]$ in $\R$ converge in this sense to $[0, 1]$.
