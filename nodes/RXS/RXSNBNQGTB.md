---
tag: RXSNBNQGTB
kind: concept
name: Twisted K-theory
msc: [19L50, 55N15]
sources:
  - url: https://en.wikipedia.org/wiki/Twisted_K-theory
same_as:
  wikidata: Q3811882
  wikipedia: Twisted K-theory
---

## Summary

Twisted K-theory is a variant of [[complex K-theory|9E4JE4902G]] of a space $X$ that depends on an extra datum, a twist.
Twists are classified by classes in $H^3(X; \Z)$.
With the trivial twist it is ordinary K-theory.
It arises from bundles of [[Fredholm operators|8HWGKWD6ZM]] glued with projective unitary transformations.
It appears in string theory, in the representation theory of loop groups and in the study of continuous-trace C*-algebras.

## Explanations

### L1 human

By the Atiyah–Jänich theorem, a K-theory class on $X$ is a continuous family of Fredholm operators, one for each point of $X$.
In twisted K-theory the operators no longer live in one fixed Hilbert space.
Instead they live in a bundle of Hilbert spaces that is glued with unitary operators that are only defined up to scalar multiples.
Such gluings are classified by a class in the third cohomology group of $X$, and this class is the twist.
For example, on the $3$-sphere the twist is an integer $k$, and for $k \ne 0$ the twisted K-groups are $0$ and $\Z/k$.
