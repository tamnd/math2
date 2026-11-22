---
tag: 0VJBSK15SN
kind: statement
role: theorem
name: Classification of vector spaces by dimension
msc: ["15A03"]
topics: [9080WQTZ3M]
audience: ug1
about: [0B8T10CE7N, 03GSZ8RTZJ]
uses: [0XSJ25Z9M4, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Isomorphism
  - book: isbn:9783031410253
    locator: Chapter 3
  - book: isbn:9780134860244
    locator: Section 2.4
---

## Statement

Up to isomorphism, a finite-dimensional vector space is determined by one number, its dimension.

Let $F$ be a field and let $V$ and $W$ be finite-dimensional vector spaces over $F$.

1. The spaces $V$ and $W$ are [[isomorphic|0XSJ25Z9M4]] if and only if $\dim V = \dim W$, where $\dim$ is the [[dimension|05G2G0P224]].
2. In particular, if $\dim V = n$, then $V \cong F^n$, and each basis $(b_1, \dots, b_n)$ of $V$ gives the isomorphism $F^n \to V$, $(a_1, \dots, a_n) \mapsto a_1 b_1 + \dots + a_n b_n$.

## Remarks

### Why the hypotheses are needed

Both spaces must be over the same field $F$, and the dimension depends on the field.
The set $\C$ has dimension $1$ as a complex space and dimension $2$ as a real space, so as a real space it is isomorphic to $\R^2$, while as a complex space it is isomorphic to $\C^1$.
Finite dimension is needed for part 1 as stated with natural numbers.
In general the dimension is a cardinal, and the theorem still holds in that form.

### What it gives you

The spaces $M_{2 \times 3}(F)$, $F^6$ and the polynomials of degree at most $5$ are pairwise isomorphic, since each has dimension $6$.
A subspace $U \subseteq V$ with $\dim U = \dim V$ is isomorphic to $V$, and in finite dimension it equals $V$.
To prove a statement about all $n$-dimensional spaces that is kept by isomorphisms, it is enough to prove it for $F^n$.

### The isomorphism is not unique

Part 1 is an equivalence, but the isomorphism of part 2 depends on the basis.
Take $V = \R^2$ with the bases $(e_1, e_2)$ and $(e_1 + e_2, e_2)$.
The first basis sends $(1, 0)$ to $e_1 = (1, 0)$, and the second sends $(1, 0)$ to $e_1 + e_2 = (1, 1)$.
So the two isomorphisms $\R^2 \to V$ differ, and neither is preferred when $V$ is an abstract space.
For this reason the [[isomorphism with the coordinate space|059THXBRBB]] is not canonical.
In the same way, [[an isomorphism of R² with its dual given by a basis|A3CP855PNV]] is not canonical.

### Generalizations

For all vector spaces, $V \cong W$ if and only if $\dim V = \dim W$ as cardinal numbers, with the same proof using bases indexed by sets of the same size.
For modules over a commutative ring, free modules are still classified by their rank.
Most modules have no basis, though, and then no single number classifies them.

## History

Peano defined vector spaces axiomatically in 1888, and the classification follows from his axioms together with the dimension theorem.
Hamel bases, introduced in 1905, extended the notion of basis to infinite dimension.

## Explanations

### L1 human

Up to isomorphism, a finite-dimensional vector space is determined by its dimension.
All three-dimensional real spaces behave like $\R^3$.
Only the names of the vectors differ.

### L2 human

To show that two spaces are isomorphic, compute their dimensions.
The $2 \times 2$ real matrices with trace $0$ have the basis
$$\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}.$$
So this space has dimension $3$, and it is isomorphic to $\R^3$.
Watch out: the isomorphism is not unique, since it depends on the chosen basis.

### L3 human

The theorem says that dimension is a complete invariant of vector spaces over a fixed field.
The isomorphisms $F^n \to V$ correspond one to one with the ordered bases of $V$.
The group $GL_n(F)$ acts on them simply transitively, which is why no basis is preferred.
