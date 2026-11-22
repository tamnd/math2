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

A linear map becomes an isomorphism onto its image as soon as we glue together the vectors that it cannot tell apart, that is, as soon as we divide by its kernel.
Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].
Then the map
$$\bar T \colon V / \ker T \to \operatorname{im} T, \qquad v + \ker T \mapsto T(v),$$
is well defined, and it is a linear [[isomorphism|0XSJ25Z9M4]].
Here $V / \ker T$ is the [[quotient space|0SVR29SV1V]] of $V$ by the [[kernel|02YFME3RGW]] of $T$, and $\operatorname{im} T$ is the [[image|0JB228DCWB]] of $T$.
In particular, if $T$ is surjective, then $V / \ker T \cong W$.

## Remarks

### A first case

Take $T \colon \R^3 \to \R^2$ with $T(x, y, z) = (x - y, \, y - z)$.
A vector lies in the kernel when $x - y = 0$ and $y - z = 0$, so the kernel is the line $\R(1, 1, 1)$.
The cosets of the kernel are the lines parallel to $(1, 1, 1)$, and $T$ is constant on each of them.
For example, $(1, 0, 0)$ and $(2, 1, 1)$ differ by $(1, 1, 1)$, and both have the same image:
$$T(1, 0, 0) = (1, 0), \qquad T(2, 1, 1) = (2 - 1, \, 1 - 1) = (1, 0).$$
The map is onto $\R^2$, since $T(1, 0, 0) = (1, 0)$ and $T(1, 1, 0) = (0, 1)$.
So the theorem gives $\R^3 / \R(1, 1, 1) \cong \R^2$: each line parallel to $(1, 1, 1)$ is labeled by one point of the plane.
The example of [[R³ modulo the plane x + y + z = 0|7SNB2G6Q36]] runs the same argument with a plane as the kernel.

### Why each hypothesis is needed

The quotient must be by the whole kernel, no more and no less.
Take $T(x, y) = x$ on $\R^2$, whose kernel is the $y$-axis.
If we divide by the smaller subspace $\{0\}$, the formula $v + \{0\} \mapsto T(v)$ is just $T$, and it is not injective, since it sends $(0, 1)$ to $0$.
If we divide by the larger subspace $\R^2$, there is only one coset, and the formula is not well defined: $0 + \R^2 = (1, 0) + \R^2$, but $T(0, 0) = 0$ and $T(1, 0) = 1$.

The target must be the image.
As a map into $W$, the map $\bar T$ is still injective, but it is onto $W$ only when $T$ is surjective.

The map must be linear.
For $f(x) = x^2$ on $\R$, the set of points with value $4$ is $\{-2, 2\}$, which is not a coset of any subspace of $\R$.

### Rank-nullity as a corollary

Let $V$ be finite-dimensional.
The [[dimension of a quotient space|0SXDQ6TN00]] gives $\dim (V / \ker T) = \dim V - \dim \ker T$.
Isomorphic spaces have the same dimension, by the [[classification by dimension|0VJBSK15SN]], so the theorem gives
$$\dim \operatorname{im} T = \dim V - \dim \ker T.$$
This is the [[rank-nullity theorem|0W4FSW1TVB]], $\dim \ker T + \dim \operatorname{im} T = \dim V$.
In the first case above, $1 + 2 = 3$.

### What else it gives you

Every quotient arises in this way, since $V / U$ is the image of the [[quotient map|0J0SK5FF4M]] $v \mapsto v + U$, whose kernel is $U$.
Two linear maps out of $V$ with the same kernel have isomorphic images.
Each linear map factors as $T = \iota \circ \bar T \circ \pi$, where $\pi \colon V \to V / \ker T$ is the quotient map, $\bar T$ is an isomorphism, and $\iota \colon \operatorname{im} T \to W$ is the inclusion.
The [[second|0APN65D6Y6]] and [[third isomorphism theorems|07RB3EMBWW]] follow when we apply the theorem to well-chosen surjective maps.

### The converse

Let $U$ be a subspace of $V$ such that $v + U \mapsto T(v)$ is a well-defined injective map.
Well defined means that $T$ vanishes on $U$, so $U \subseteq \ker T$.
Injective means that only the zero coset goes to $0$, so $\ker T \subseteq U$.
So $U = \ker T$, and the kernel is the only subspace for which the theorem holds.

### Watch out

The quotient by the kernel is isomorphic to the image, not to the target.
Take $T(x, y) = (x + y, \, 2x + 2y)$ on $\R^2$.
Its kernel is the line $\R(1, -1)$, and its image is the line $\R(1, 2)$, since every value is $(x + y)(1, 2)$.
So $\R^2 / \R(1, -1)$ is isomorphic to a line, not to $\R^2$.
Check: $\dim \R^2 - \dim \ker T = 2 - 1 = 1 = \dim \operatorname{im} T$.

## History

Emmy Noether stated the isomorphism theorems for modules in general form in a paper of 1927.
The same pattern for groups is the [[first isomorphism theorem for groups|0CXXJNG5B6]], and the vector space case is a special case of the module version.

## Explanations

### L1 human

Think of the shadow that a lamp straight overhead casts on the floor.
The map $(x, y, z) \mapsto (x, y)$ sends each point of space to its shadow, and all the points on one vertical line have the same shadow.
The vertical line through $(2, 3, 0)$, for instance, has the shadow $(2, 3)$.
If we treat each vertical line as a single object, then different lines have different shadows, and every point of the floor is a shadow.
So the set of vertical lines is a perfect copy of the floor.

### L2 human

Here is a typical use: identify the quotient of $P_3(\R)$, the polynomials of degree at most $3$, by the constant polynomials.
The trick is to find a surjective linear map whose kernel is the subspace we divide by.
Differentiation $D \colon P_3(\R) \to P_2(\R)$ is linear, and $D p = 0$ exactly when $p$ is constant.
It is surjective, since each $a + bx + cx^2$ is the derivative of
$$ax + \tfrac{b}{2} x^2 + \tfrac{c}{3} x^3.$$
So the theorem gives $P_3(\R) / \{\text{constants}\} \cong P_2(\R)$, through $p + \{\text{constants}\} \mapsto p'$.
Check the dimensions: $4 - 1 = 3$.
The example on [[differentiation modulo constants|20YC6C97W9]] looks at the same map through the universal property.
The lesson is that a quotient is easiest to understand through a map that kills exactly the subspace.

### L3 human

The theorem says that the coimage $V / \ker T$ and the image of $T$ agree.
In an [[abelian category|Y9CZ3MTNF1]] this agreement is one of the axioms, so the statement holds word for word for modules over any ring and for sheaves of modules.
Together with the [[universal property of the quotient|0ZERJX6PH6]], it gives the factorization of every linear map as a surjection followed by an injection.
The rank-nullity theorem is its dimension count, and [[exact sequences|946YAZNYKX]] package the theorem as the statement that $0 \to \ker T \to V \to \operatorname{im} T \to 0$ is exact.
Mathlib states the theorem as `LinearMap.quotKerEquivRange`.
