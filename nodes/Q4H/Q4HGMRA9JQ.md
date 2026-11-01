---
tag: Q4HGMRA9JQ
kind: concept
name: Dehn function
msc: [20F65, 20F06, 20F10]
sources:
  - url: https://en.wikipedia.org/wiki/Dehn_function
same_as:
  wikidata: Q4493444
  wikipedia: Dehn function
---

## Summary

The Dehn function of a [[finitely presented group|TJKANTKASZ]] measures how many relators are needed to prove that a word of length $n$ equals the identity.
Up to a standard equivalence it does not depend on the presentation, and it is a [[quasi-isometry|6FKYSH729T]] invariant.
It is a geometric measure of the difficulty of the word problem.
The word problem is solvable exactly when the Dehn function is bounded by a computable function.
A group is [[hyperbolic|JWJ8YPR7EB]] if and only if its Dehn function is linear.

## Explanations

### L1 human

A word in the generators that equals the identity can be reduced to the empty word by inserting relators, one at a time, and cancelling.
The area of the word is the least number of relators needed.
The Dehn function gives the largest area of such a word of length at most $n$.
In $\Z^2 = \langle a, b \mid aba^{-1}b^{-1} \rangle$, the word $a^n b^n a^{-n} b^{-n}$ traces the boundary of an $n \times n$ square and needs $n^2$ relators, one per unit square.
So the Dehn function of $\Z^2$ grows like $n^2$, like the area enclosed by a loop in the plane.
