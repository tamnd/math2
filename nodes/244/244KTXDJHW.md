---
tag: 244KTXDJHW
kind: statement
role: proposition
name: Every complement is isomorphic to the quotient
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
about: [0M83V17KHX, 0BR3FY5Q8M]
uses: [04C3BAHV03, 0SVR29SV1V, 0J0SK5FF4M, 0XSJ25Z9M4]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule.quotientEquivOfIsCompl
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Properties
  - book: isbn:9783031410253
    locator: Section 3E
---

## Statement

A complement of a subspace $U$ is a copy of the quotient by $U$ that sits inside the space.
Let $V$ be a vector space over a field $F$, let $U$ be a subspace of $V$, and let $W$ be a [[complement|04C3BAHV03]] of $U$, so that $V = U \oplus W$.
Let $\pi \colon V \to V / U$ be the [[quotient map|0J0SK5FF4M]] onto the [[quotient space|0SVR29SV1V]].
Then the restriction
$$\pi|_W \colon W \to V / U, \qquad w \mapsto w + U,$$
is an [[isomorphism|0XSJ25Z9M4]].
In particular, any two complements of $U$ are isomorphic.

## Remarks

### Why each hypothesis is needed

The two conditions of a complement match the two halves of "bijective".
The condition $U \cap W = \{0\}$ gives injectivity.
Without it the map can have a kernel: for $W = V$ the sum $U + W$ is $V$, but $\pi|_V = \pi$ has kernel $U$, which is nonzero unless $U = \{0\}$.

The condition $U + W = V$ gives surjectivity.
Without it the image can be too small: for $W = \{0\}$ the intersection is $\{0\}$, but the image of $\pi|_W$ is the zero coset only, which is not $V / U$ unless $U = V$.

### What it gives you

In finite dimension, every complement has the same dimension,
$$\dim W = \dim (V / U) = \dim V - \dim U,$$
by the [[dimension of a quotient space|0SXDQ6TN00]].
For a plane $U$ in $\R^3$ this says that every complement is a line, and for a line in $\R^3$ that every complement is a plane.

The inverse map $V / U \to W$ has a concrete description.
It picks out, in each coset $v + U$, the unique vector of the coset that lies in $W$.
For the $x$-axis $U$ in $\R^2$ and $W = \R(1, 1)$, the coset $(5, 2) + U$ is the horizontal line $y = 2$, and its only point on $W$ is $(2, 2)$.

Since every subspace has a complement, every quotient $V / U$ is isomorphic to a subspace of $V$.
So $V \cong U \oplus V / U$, where the right side is the external direct sum.

### The converse

The converse holds.
If $W$ is a subspace such that $\pi|_W$ is an isomorphism, then injectivity gives $U \cap W = \{0\}$, because the kernel of $\pi|_W$ is $U \cap W$.
Surjectivity gives $U + W = V$, because each $v$ then has some $w \in W$ with $v - w \in U$.
So the complements of $U$ are exactly the subspaces that $\pi$ maps isomorphically onto $V / U$.

### Watch out

The isomorphism $W \cong V / U$ depends on the choice of $W$.
There is no preferred isomorphism between $V / U$ and a subspace of $V$, because there is no preferred complement.
For the $x$-axis in $\R^2$, the complements $\R(0, 1)$ and $\R(1, 1)$ send the coset $y = 2$ to the different vectors $(0, 2)$ and $(2, 2)$.

## History

The statement belongs to the basic theory of quotient spaces, and we do not attribute it to a single author.
In Mathlib it is the linear equivalence `Submodule.quotientEquivOfIsCompl`.

## Explanations

### L1 human

Take the horizontal axis in the plane.
Its cosets are the horizontal lines, one for each height.
A slanted line through the origin crosses each horizontal line exactly once.
So the points of the slanted line label the horizontal lines, one point for each line, and that labeling is the isomorphism.

### L2 human

Let $U$ be the $x$-axis in $\R^2$ and $W = \R(1, 1)$.
The cosets of $U$ are the horizontal lines $y = c$.
The line $y = c$ meets $W$ in the single point $(c, c)$, so $\pi|_W$ sends $(c, c)$ to the line $y = c$, and this is a bijection.
It is linear, since $(c, c) + (d, d) = (c + d, c + d)$ goes to the line $y = c + d$, which is the sum of the cosets $y = c$ and $y = d$.
So both $W$ and $\R^2 / U$ are identified with $\R$ through the height $c$.
The typical use is to compute in $V / U$ by computing in a complement, where the elements are ordinary vectors.

### L3 human

The theorem is a special case of the [[first isomorphism theorem|0MTBGVZ4XJ]]: the map $\pi|_W$ is surjective with kernel $U \cap W = \{0\}$.
In the language of exact sequences, it says that the [[short exact sequence|1GYTT98CC5]] $0 \to U \to V \to V / U \to 0$ splits, with the splitting map $V / U \to V$ given by the inverse of $\pi|_W$ followed by the inclusion of $W$.
For modules over a ring the same proof works whenever a complement exists, but complements need not exist there.
