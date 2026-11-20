---
tag: 07RB3EMBWW
kind: statement
role: theorem
name: Third isomorphism theorem for vector spaces
msc: ["15A03", "16D10"]
topics: [QHKTJ89V6S]
audience: ug1
about: [0BR3FY5Q8M]
uses: [0SVR29SV1V, 0EPTJA5QV4, 0XSJ25Z9M4]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule.quotientQuotientEquivQuotient
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem C (modules)
  - url: https://web.williams.edu/Mathematics/it3/texts/quotients.pdf
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$, and let $W \subseteq U$ be [[subspaces|0EPTJA5QV4]] of $V$.
Then $U / W = \{u + W : u \in U\}$ is a subspace of $V / W$, and the map
$$(V / W) / (U / W) \to V / U, \qquad (v + W) + U/W \mapsto v + U,$$
is well defined, and it is a linear [[isomorphism|0XSJ25Z9M4]] of [[quotient spaces|0SVR29SV1V]].

## Remarks

### Why each hypothesis is needed

- $W \subseteq U$ is needed for the map to be well defined. For the $x$-axis $W$ and the $y$-axis $U$ in $\R^2$, the cosets $0 + W$ and $(1, 0) + W$ are equal, but $0 + U \ne (1, 0) + U$.
- $W \subseteq U$ is also needed for $U / W$ to make sense as a subspace of $V / W$. Without it, one uses $(U + W)/W$, which leads back to the [[second isomorphism theorem|0APN65D6Y6]].

### Consequences

- In finite dimension, both sides have dimension $\dim V - \dim U$, by the [[dimension of a quotient|0SXDQ6TN00]].
- The subspaces of $V / W$ are exactly the spaces $U / W$ with $W \subseteq U \subseteq V$, by the [[correspondence theorem|GCHY414Y11]].
- Quotients can be taken in stages: dividing by $W$ and then by the image of $U$ is the same as dividing by $U$ at once.

### Converse

If $W \subseteq U$ and $Y$ is a subspace of $V / W$ with $(V / W)/Y \cong V / U$ through $v + W + Y \mapsto v + U$, then $Y = U / W$.
So the subspace $U / W$ is forced.

## History

The third isomorphism theorem for groups was known to Hölder and to Frobenius in the late nineteenth century.
Noether gave the general form for modules in 1927, and the numbering of the three theorems became standard after van der Waerden's *Moderne Algebra*.

## Explanations

### L1 human

Dividing first by a small subspace and then by a larger one is the same as dividing by the larger one at once.
This works like cancelling in fractions.
The same theorem holds for groups, rings and modules.

### L2 human

Let $W$ be the $z$-axis and $U$ the $yz$-plane in $\R^3$, as in [[the example of a chain of subspaces|BBQGT4RJKX]].

1. $V / W \cong \R^2$ through $(x, y, z) + W \mapsto (x, y)$.
2. Under this isomorphism, $U / W$ becomes the line $\{(0, y)\}$ in $\R^2$.
3. So $(V / W)/(U / W) \cong \R^2 / \{(0, y)\} \cong \R$ through $x$.
4. And $V / U \cong \R$ through $x$ as well. The map of the theorem matches the two.

The trap is to forget the hypothesis $W \subseteq U$.

### L3 human

The [[proof|743PKABTM8]] applies the [[first isomorphism theorem|0MTBGVZ4XJ]] to the surjective map $V / W \to V / U$, $v + W \mapsto v + U$, whose kernel is $U / W$.
In category theory, the theorem is a statement about composing cokernels, and it holds in every abelian category.
Mathlib states it as `Submodule.quotientQuotientEquivQuotient`.
