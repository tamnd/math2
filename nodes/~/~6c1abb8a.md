---
tag: ~6c1abb8a
kind: definition
name: Basis
msc: [15A03]
defines: ~4af6ac42
uses: [~812da5ad, ~0e6a42f1]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Definition
---

## Definition

Let $F$ be a field and let $V$ be a vector space over $F$.
A *basis* of $V$ is a family $(b_i)_{i \in I}$ of vectors of $V$ that is [[linearly independent|~554c4679]] and [[spans|~5884c460]] $V$.

## Remarks

A family $(b_i)_{i \in I}$ is a basis if and only if each $v \in V$ is equal to $\sum_{i \in I} a_i b_i$ for exactly one finitely supported family of scalars $(a_i)_{i \in I}$.
The scalars $a_i$ are the [[coordinates|~985cbebb]] of $v$ in the basis.
The [[standard basis|~b51d2b98]] $e_1, \dots, e_n$ is a basis of $F^n$; the vectors $(1, 1)$ and $(1, -1)$ form another basis of $\R^2$.
[[Every vector space has a basis|~8b5c7035]], and all bases of a space have the same cardinality.

## Explanations

### L1 human

A basis is a set of directions that is just right: enough to reach every vector, and none of them redundant.
Once we fix a basis, each vector gets a unique list of coordinates.
A vector space has many bases, but all of them have the same number of vectors.
