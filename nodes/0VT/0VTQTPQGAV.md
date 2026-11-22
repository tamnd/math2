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

A basis of a vector space is a family of vectors from which every vector can be built, with no vector to spare.
Let $F$ be a field and let $V$ be a vector space over $F$.
A *basis* of $V$ is a family $(b_i)_{i \in I}$ of vectors of $V$ that is [[linearly independent|0EVHJFTG9Z]] and [[spans|0BJKVF90Z6]] $V$.
A basis indexed by $\{1, \dots, n\}$, written as a list $(b_1, \dots, b_n)$, is an *ordered basis*.

## Notation

In Mathlib, `Module.Basis ι F V` is a basis of `V` indexed by the type `ι`.
It is stored as a linear isomorphism `V ≃ₗ[F] (ι →₀ F)` to the finitely supported functions on `ι`, which is the unique-coordinates form of the definition.

## Remarks

Each of the two conditions does one job.
Spanning says that every vector of $V$ is a finite combination $\sum_i a_i b_i$, so nothing is out of reach.
Independence says that the only combination equal to $0$ is the one with all $a_i = 0$, so no vector is redundant.
Together they say that each $v \in V$ is a combination of the $b_i$ in [[exactly one way|E2ZRZGXSNX]], and the coefficients are the [[coordinates|04CYQHN6MC]] of $v$.

For example, $(1, 1), (1, -1)$ is a basis of $\mathbb{R}^2$, since $(a, b) = \tfrac{a + b}{2}(1, 1) + \tfrac{a - b}{2}(1, -1)$ and $c(1, 1) + d(1, -1) = 0$ forces $c = d = 0$.
The family $(1, 0), (0, 1), (1, 1)$ spans $\mathbb{R}^2$ but fails independence, because $(1, 0) + (0, 1) - (1, 1) = 0$.
The family $(1, 0, 0), (0, 1, 0)$ is independent in $\mathbb{R}^3$ but fails spanning, because it misses $(0, 0, 1)$.

The definition uses a family, not a set, so a repeated vector makes it dependent: $(v, v)$ is never a basis.
The empty family is a basis of the zero space $\{0\}$, because it is independent and its span is $\{0\}$.
[[Every vector space has a basis|00MS9VMQ9Z]], and the concept page on the [[basis|0KCQ9Y3QKA]] gives more examples and the main properties.

## Explanations

### L1 human

A basis is a set of directions that is just right: enough to reach every vector, and none of them a mix of the others.
In the plane, "east" and "north" form a basis, and so do "east" and "north-east".
Once we fix a basis, each vector gets a unique list of coordinates.

### L2 human

To test the definition, check the two conditions separately.
For $(2, 1)$ and $(1, 1)$ in $\mathbb{R}^2$, the equation $c(2, 1) + d(1, 1) = (x, y)$ means $2c + d = x$ and $c + d = y$.
Subtracting the two equations forces $c = x - y$, and then $d = 2y - x$, so the pair spans.
Check: $(x - y)(2, 1) + (2y - x)(1, 1) = (2x - 2y + 2y - x, x - y + 2y - x) = (x, y)$.
With $x = y = 0$ the only solution is $c = d = 0$, so the pair is also independent and is a basis.
