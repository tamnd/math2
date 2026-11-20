---
tag: 0WK0Y8RH1M
kind: statement
role: theorem
name: Dimension theorem for vector spaces
aliases: [invariance-of-dimension]
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [0KCQ9Y3QKA]
uses: [0VTQTPQGAV]
proofs: [WXB40PTZNV, 2BVBSVQYMB, C6V1B2MC0X]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_theorem_for_vector_spaces
    locator: lead section
  - book: isbn:9783031410253
    locator: Section 2C
  - book: isbn:9780134860244
    locator: Section 1.6
  - book: isbn:9780387728285
    locator: Chapter 1
same_as:
  wikidata: Q3527205
  wikipedia: Dimension theorem for vector spaces
inventory: [21BQ4H2ZAY]
---

## Statement

Let $F$ be a field and let $V$ be a vector space over $F$.

1. If $V$ has a finite [[basis|0VTQTPQGAV]] with $n$ vectors, then every basis of $V$ is finite and has exactly $n$ vectors.
2. Any two bases of $V$ have the same cardinality.

## Remarks

### Why each hypothesis is needed

The scalars must form a field, or at least a ring with the invariant basis number property.
There are nonzero rings $R$ with $R \cong R^2$ as $R$-modules, so the free module $R$ has bases of sizes $1$ and $2$.
An example is the ring of endomorphisms of a vector space of countable dimension.
Part 2 for infinite bases uses the axiom of choice through cardinal arithmetic; without choice, a space may have no basis at all.

### Consequences

The common cardinality is the [[dimension|03GSZ8RTZJ]] of $V$, so dimension is well defined.
Two spaces over $F$ are isomorphic if and only if they have the same dimension; see [[isomorphic iff equal dimension|0VJBSK15SN]].
The space $F^n$ is not isomorphic to $F^m$ for $n \ne m$.

### Converse

Spaces with bases of the same cardinality are isomorphic: a bijection between the bases extends to a linear isomorphism.
So the converse direction, from equal size to isomorphism, also holds.

### Generalizations

The theorem holds for free modules over every nonzero commutative ring, by reduction modulo a maximal ideal.
It holds for vector spaces over division rings, with the same proofs.
In a [[matroid|PX31ZNYS3Z]], all bases have the same size, by the exchange axiom.

## History

Grassmann used the invariance of the number of independent units in 1844, and Steinitz gave the exchange proof in 1913.
The infinite case became meaningful after Hamel built a basis of $\R$ over $\Q$ in 1905, and its proof uses cardinal arithmetic.

## Explanations

### L1 human

However we choose a basis of a space, it always has the same number of vectors.
So "the number of vectors in a basis" is a property of the space itself.
We call this number the dimension.

### L2 human

There are three proofs here.
The [[proof by Steinitz|WXB40PTZNV]] uses the exchange lemma in both directions.
The [[proof by row reduction|2BVBSVQYMB]] turns too many vectors into a homogeneous system with more unknowns than equations.
The [[proof for infinite bases|C6V1B2MC0X]] counts finite supports with cardinal arithmetic.
A trap: the zero space has the empty basis, so its dimension is $0$, not $1$.
