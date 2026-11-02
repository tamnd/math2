---
tag: W0RYRVJY5Z
kind: concept
name: Free spectrum of a variety
msc: [08B20]
sources:
  - url: https://en.wikipedia.org/wiki/Variety_(universal_algebra)
---

## Summary

The free spectrum of a [[variety|AJNZJD8442]] $\mathcal{V}$ is a function on the natural numbers.
It sends $n$ to the number of elements of the free algebra of $\mathcal{V}$ on $n$ generators.
It is finite for all $n$ exactly when $\mathcal{V}$ is locally finite.
Its growth rate measures how much freedom the identities of $\mathcal{V}$ leave, and it is used to separate and classify locally finite varieties.

## Explanations

### L1 human

Count how many different expressions in $n$ letters a variety can tell apart.
For Boolean algebras on $n$ letters, every expression is a truth function of $n$ inputs, so there are $2^{2^n}$ of them.
For semilattices, an expression is determined by the set of letters it uses, so there are $2^n - 1$ of them.
For groups, already one letter gives infinitely many elements $x, x^2, x^3, \ldots$, so the free spectrum is infinite.
