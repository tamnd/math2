---
tag: 0VTQTPQGAV
kind: definition
name: Basis
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
defines: 0KCQ9Y3QKA
uses: [0EVHJFTG9Z, 0BJKVF90Z6]
formal:
  - system: lean4
    library: mathlib
    decl: Module.Basis
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Definition
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-2.xml#L220
    locator: src/section3-2.xml:220
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-5.xml#L516
    locator: src/section3-5.xml:516
  - book: isbn:9783031410253
    locator: Section 2B
---

## Definition

Let $F$ be a field and let $V$ be a vector space over $F$.
A *basis* of $V$ is a family $(b_i)_{i \in I}$ of vectors of $V$ that is [[linearly independent|0EVHJFTG9Z]] and [[spans|0BJKVF90Z6]] $V$.

## Remarks

A family $(b_i)_{i \in I}$ is a basis if and only if each $v \in V$ has exactly one expression $v = \sum_{i \in I} a_i b_i$.
Here $(a_i)_{i \in I}$ is a finitely supported family of scalars; see [[unique coordinates|~89452b4d]].
The scalars $a_i$ are the [[coordinates|04CYQHN6MC]] of $v$ in the basis.
The [[standard basis|~91c029b0]] $e_1, \dots, e_n$ is a basis of $F^n$; the vectors $(1, 1)$ and $(1, -1)$ form another basis of $\R^2$.
The empty family is a basis of the zero space.
[[Every vector space has a basis|00MS9VMQ9Z]], and all bases of a space have the same cardinality.
Mathlib's `Module.Basis ι R M` stores a basis as a linear isomorphism `M ≃ₗ[R] (ι →₀ R)`, which is the unique-coordinates form of the definition.

## Explanations

### L1 human

A basis is a set of directions that is just right: enough to reach every vector, and none of them redundant.
Once we fix a basis, each vector gets a unique list of coordinates.
A vector space has many bases, but all of them have the same number of vectors.
