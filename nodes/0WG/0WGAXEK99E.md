---
tag: 0WGAXEK99E
kind: statement
role: proposition
name: A subspace of full dimension is the whole space
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [03GSZ8RTZJ]
uses: [05G2G0P224, 0EPTJA5QV4]
proofs: [345D462T59]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Properties
---

## Statement

In finite dimension, a subspace that is as large as the whole space, measured by dimension, is the whole space.
Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $W$ be a [[linear subspace|00YC1D652K]] of $V$.
If $\dim W = \dim V$, where $\dim$ is the [[dimension|05G2G0P224]], then $W = V$.

## Remarks

### Equality by one inclusion and a count

The proposition turns a proof of equality into a count.
Let $W$ be the subspace of $\mathbb{R}^3$ spanned by $(1, 1, 0)$, $(0, 1, 1)$ and $(1, 0, 1)$.
These three are independent: from $a(1, 1, 0) + b(0, 1, 1) + c(1, 0, 1) = 0$ we get
$$a + c = 0, \qquad a + b = 0, \qquad b + c = 0.$$
Adding the three equations gives $2(a + b + c) = 0$, so $a + b + c = 0$, and then each equation gives one variable: $b = 0$, $c = 0$ and $a = 0$.
So $\dim W = 3 = \dim \mathbb{R}^3$, and the proposition gives $W = \mathbb{R}^3$ without writing a single vector of $\mathbb{R}^3$ as a combination.

More generally, two finite-dimensional subspaces $U \subseteq W$ with $\dim U = \dim W$ are equal: apply the proposition with $W$ as the whole space.

### Why each hypothesis is needed

Finite dimension is needed.
In $F[x]$, the subspace of polynomials with constant term $0$ has the same dimension $\aleph_0$ as $F[x]$, but it does not contain $1$; see [[this example|DVEZQ8SP64]].

The inclusion $W \subseteq V$ is needed, and it is easy to forget when subspaces are compared with each other.
The $x$-axis and the $y$-axis in $\mathbb{R}^2$ both have dimension $1$, but neither contains the other, so they are not equal.

The scalars must form a field.
Over $\mathbb{Z}$, the submodule $2\mathbb{Z}$ of $\mathbb{Z}$ is free of rank $1$, like $\mathbb{Z}$, but it is a proper submodule.

### The converse and the general version

The converse is immediate: if $W = V$, then $\dim W = \dim V$.
The proposition is part 2 of the theorem on the [[dimension of a subspace|0QW084460E]], which also gives $\dim W \le \dim V$ in general.

## Explanations

### L1 human

If a subspace is as big as the whole space, measured by dimension, then it is the whole space.
For example, a subspace of the plane that contains two independent arrows is the whole plane.
There is no room in a finite-dimensional space for a smaller copy of the same size.

### L2 human

Here is a typical use: show that the polynomials $1$, $1 + x$ and $1 + x + x^2$ span the space $P_2$ of real polynomials of degree at most $2$.
Let $W$ be their span, a subspace of $P_2$.
The three polynomials are independent: in $a + b(1 + x) + c(1 + x + x^2) = 0$ the coefficient of $x^2$ gives $c = 0$, then the coefficient of $x$ gives $b = 0$, and then $a = 0$.
So $\dim W = 3 = \dim P_2$, and the proposition gives $W = P_2$.
Watch out: the same count proves nothing in an infinite-dimensional space such as $F[x]$.
