---
tag: GY3QA6NH0E
kind: concept
name: Unramified morphism of rings
msc: [13B40, 14B25, 13N05]
sources:
  - url: https://en.wikipedia.org/wiki/Unramified_morphism
---

## Summary

An unramified morphism of rings is a map $R \to A$ of commutative rings that makes $A$ a [[finitely generated|AC5TFFQT9M]] $R$-algebra.
Moreover its module of [[Kähler differentials|7HCFARHG7D]] $\Omega_{A/R}$ must be zero.
It generalizes finite separable field extensions and unramified extensions of rings of integers in number theory.
Locally, take a prime $\mathfrak q$ of $A$ and the prime $\mathfrak p$ of $R$ below it.
Then $\mathfrak p$ generates the maximal ideal of $A_{\mathfrak q}$, and the residue field extension is finite and separable.
An unramified map that is also flat and finitely presented is [[étale|FTRW0679E2]].

## Explanations

### L1 human

In number theory, a prime $p$ ramifies in a larger ring of integers when it becomes a square, or a higher power, of a prime upstairs.
In $\Z[i]$, the prime $2$ ramifies, since $2 = -i(1 + i)^2$.
An unramified map is one where nothing like this happens at any prime.
The test is short: the differentials of $A$ over $R$ must all vanish.
For $\Z[i] = \Z[x]/(x^2 + 1)$, the differentials are $\Z[i]/(2i)$, which is nonzero exactly because of the prime $2$.
