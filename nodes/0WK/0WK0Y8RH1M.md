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

However we choose a basis of a vector space, it has the same number of vectors.
Let $F$ be a field and let $V$ be a vector space over $F$.

1. If $V$ has a finite [[basis|0VTQTPQGAV]] with $n$ vectors, then every basis of $V$ is finite and has exactly $n$ vectors.
2. Any two bases of $V$ have the same cardinality.

## Remarks

### Two bases of one plane

Let $W$ be the plane $x + y + z = 0$ in $\mathbb{R}^3$.
One basis is $(1, -1, 0), (0, 1, -1)$, and another is $(1, 0, -1), (1, 1, -2)$.
Each vector lies in $W$, since its entries add to $0$, and in each pair neither vector is a multiple of the other, so each pair is independent.
The first pair spans $W$, since a point with $z = -x - y$ equals $x (1, -1, 0) + (x + y)(0, 1, -1)$.
The second pair then spans $W$ by the [[right-size criterion|096V7H13H9]].
Check one relation by hand:
$$(1, 1, -2) = (1, -1, 0) + 2 (0, 1, -1).$$
The theorem says that no basis of $W$ has one vector or three vectors, whatever vectors we choose.

### Why each hypothesis is needed

The scalars must form a field, or at least a ring in which the count of a basis is fixed.
Let $E$ be the ring of linear maps of a vector space $U$ of countable dimension to itself.
Since $U \cong U \oplus U$, one can show that $E \cong E^2$ as modules over $E$, so the free module $E$ has bases with $1$ and with $2$ elements.
Over a field this cannot happen, and the [[proof by the exchange lemma|WXB40PTZNV]] shows where the field is used: it divides by nonzero coefficients.

Part 2 for infinite bases needs more than algebra.
The [[proof for infinite bases|C6V1B2MC0X]] uses cardinal arithmetic, which rests on the axiom of choice.

### What it gives you

The common size of all bases is the [[dimension|03GSZ8RTZJ]] of $V$, so dimension is a well-defined invariant of the space.
For example, $F^n$ and $F^m$ are not isomorphic for $n \ne m$, because a linear isomorphism carries a basis to a basis.
Two spaces over $F$ are isomorphic exactly when they have the same dimension, as the [[classification by dimension|0VJBSK15SN]] states.

### The converse

The theorem has a natural converse, and it holds.
If $V$ and $V'$ have bases $B$ and $B'$ of the same cardinality, then a bijection $B \to B'$ extends to a linear isomorphism $V \to V'$.
So the size of a basis is all that one needs to know about a vector space, up to isomorphism.

### Generalizations

The proofs work without change over a division ring, where multiplication need not commute.
For a free module over a nonzero commutative ring $R$, all bases also have the same size: reduce modulo a maximal ideal $\mathfrak{m}$, and a basis of the module gives a basis of a vector space over the field $R / \mathfrak{m}$.
In a finite [[matroid|PX31ZNYS3Z]], all bases have the same size, by the exchange axiom.

## History

The exchange lemma that gives the finite case carries the name of Steinitz, who used it in a paper of 1913.
In 1905 Hamel showed that $\mathbb{R}$ has a basis as a vector space over $\mathbb{Q}$, an early example of an infinite basis.

## Explanations

### L1 human

A basis is a set of building blocks: every vector is built from them in exactly one way.
A space has many different bases, but they all have the same number of blocks.
In the plane, every basis has two vectors, and in ordinary space every basis has three.
That shared number is what we call the dimension.

### L2 human

The finite case has two standard proofs, and they show two sides of linear algebra.
The [[proof by the exchange lemma|WXB40PTZNV]] compares the two bases directly: each is independent and each spans, so the [[Steinitz exchange lemma|08ZDRN6H41]] bounds each size by the other.
The [[proof by row reduction|2BVBSVQYMB]] writes $m$ vectors in terms of $n$ spanning vectors, so that a dependence relation is a nonzero solution of a homogeneous system with $m$ unknowns and $n$ equations.
When $m > n$, such a solution exists, and the relation follows.
For example, any three vectors in the plane $W$ above are dependent, because $W$ has a basis of two vectors.
Watch out: the zero space has the empty basis, so its dimension is $0$, not $1$.

### L3 human

For infinite bases the count becomes a cardinal, and the proof is a covering argument: each vector of one basis uses finitely many vectors of the other, and all of them must be used.
The theorem is the reason why the category of vector spaces over a field is so simple: its objects up to isomorphism are classified by one cardinal.
Over rings the question is subtle, and rings in which all bases of each free module have the same size are said to have the invariant basis number property.
The sub-area on linear maps builds on this classification, for example in the [[rank-nullity theorem|0W4FSW1TVB]].
