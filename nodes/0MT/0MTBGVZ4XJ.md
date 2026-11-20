---
tag: 0MTBGVZ4XJ
kind: statement
role: theorem
name: First isomorphism theorem for vector spaces
msc: ["15A04", "16D10"]
topics: [QHKTJ89V6S]
audience: ug1
about: [0BR3FY5Q8M, 0NRYHJPQG2]
uses: [0SVR29SV1V, 02YFME3RGW, 0JB228DCWB, 0RJF668P1T, 0XSJ25Z9M4]
formal:
  - system: lean4
    library: mathlib
    decl: LinearMap.quotKerEquivRange
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem A (modules)
  - book: isbn:9783031410253
    locator: Section 3E
---

## Statement

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].
Then the map
$$\bar T \colon V / \ker T \to \operatorname{im} T, \qquad v + \ker T \mapsto T(v),$$
is well defined, and it is a linear [[isomorphism|0XSJ25Z9M4]].
Here $V / \ker T$ is the [[quotient space|0SVR29SV1V]] by the [[kernel|02YFME3RGW]], and $\operatorname{im} T$ is the [[image|0JB228DCWB]] of $T$.
In particular, if $T$ is surjective, then $V / \ker T \cong W$.

## Remarks

### Why each hypothesis is needed

- The quotient must be by the whole kernel. If we divide by a smaller subspace $U \subsetneq \ker T$, the map $v + U \mapsto T(v)$ is still well defined, but it is not injective. For $T(x, y) = x$ on $\R^2$ and $U = \{0\}$, the map is $T$ itself, which sends $(0, 1)$ to $0$.
- The quotient cannot be by a larger subspace. If $U \supsetneq \ker T$, then the formula $v + U \mapsto T(v)$ is not well defined, since some $u \in U$ has $T(u) \ne 0$.
- The target must be the image. As a map into $W$, the map $\bar T$ is injective, but it is surjective only when $T$ is.
- $T$ must be linear. For a nonlinear map, the fibres $T^{-1}(w)$ need not be cosets of one subspace.

### Consequences

- For finite-dimensional $V$, with the [[dimension of a quotient|0SXDQ6TN00]], it gives the [[rank–nullity theorem|0W4FSW1TVB]]: $\dim V - \dim \ker T = \dim \operatorname{im} T$.
- Every quotient arises this way: $V / U$ is the image of the [[quotient map|0J0SK5FF4M]], whose kernel is $U$.
- Two linear maps out of $V$ with the same kernel have isomorphic images.
- $T$ factors as $T = \iota \circ \bar T \circ \pi$: a surjection $\pi$, an isomorphism $\bar T$, and an inclusion $\iota \colon \operatorname{im} T \to W$.
- The [[second|0APN65D6Y6]] and [[third isomorphism theorems|07RB3EMBWW]] follow by applying this theorem to suitable maps.

### Converse

If $U$ is a subspace of $V$ and the map $v + U \mapsto T(v)$ is a well-defined injective map, then $U = \ker T$.
So the kernel is the only subspace for which the theorem holds.

## History

The isomorphism theorems were formulated for groups by Jordan and Hölder in the nineteenth century, in the study of composition series.
Noether stated them in general form for modules and rings in 1927, and the vector space case became standard after van der Waerden's *Moderne Algebra*.
The analogue for groups is the [[first isomorphism theorem for groups|0CXXJNG5B6]].

## Explanations

### L1 human

A linear map identifies vectors that differ by an element of the kernel.
After we glue these vectors together, the map becomes one to one.
So the quotient by the kernel is a copy of the image.

### L2 human

Let $T \colon \R^3 \to \R^2$ be $T(x, y, z) = (x, y)$.

1. $\ker T$ is the $z$-axis, and $\operatorname{im} T = \R^2$.
2. The cosets of $\ker T$ are the vertical lines $\{(a, b, t) : t \in \R\}$.
3. $\bar T$ sends the vertical line through $(a, b, 0)$ to $(a, b)$.
4. $\bar T$ is well defined, since all points of the line have the same $x$ and $y$.
5. $\bar T$ is injective, since different vertical lines have different $(a, b)$. It is surjective, since every $(a, b)$ is hit.

So $\R^3 / (z\text{-axis}) \cong \R^2$.
The trap is to forget to replace $W$ by $\operatorname{im} T$ when $T$ is not surjective.

### L3 human

In category theory, the theorem says that in the category of vector spaces the coimage $V / \ker T$ and the image of $T$ agree.
This is one of the axioms of an abelian category, so the theorem holds verbatim for modules over any ring and for sheaves of modules.
Combined with the [[universal property of the quotient|0ZERJX6PH6]], it gives the factorization of any linear map as a surjection followed by an injection.
Mathlib states it as `LinearMap.quotKerEquivRange`.
