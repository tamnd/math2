---
tag: 9RWS7TZHXH
kind: concept
name: Subfactor
msc: [46L37]
sources:
  - url: https://en.wikipedia.org/wiki/Subfactor
same_as:
  wikidata: Q7631133
  wikipedia: Subfactor
---

## Summary

A subfactor is an inclusion $N \subseteq M$ of factors, von Neumann algebras with trivial center, that share the same identity.
For factors of type $\mathrm{II}_1$, Vaughan Jones attached to such an inclusion a number $[M:N]$, the index.
It measures the relative size of $M$ over $N$.
The [[Jones index theorem|31N0FH22ZT]] shows that the possible index values are surprisingly restricted.
Subfactor theory connects operator algebras with knot invariants, quantum groups, tensor categories and conformal field theory.

## Explanations

### L1 human

A subfactor is like a field extension or a subgroup, but for operator algebras.
For a subgroup $H$ of a finite group $G$, the index $[G:H]$ counts how many copies of $H$ fit into $G$.
For a subfactor, the index is a real number that plays the same role.
For example, let $N$ be a $\mathrm{II}_1$ factor and look at the $k \times k$ matrices with entries in $N$.
The diagonal matrices with all diagonal entries equal form a copy of $N$ inside them, and the index is $k^2$.
The surprise is that the index need not be an integer.
