---
tag: 0ZERJX6PH6
kind: statement
role: theorem
name: Universal property of the quotient space
msc: ["15A04"]
topics: [QHKTJ89V6S]
audience: ug1
about: [0BR3FY5Q8M]
uses: [0J0SK5FF4M, 0RJF668P1T, 0SVR29SV1V, 02YFME3RGW]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule.liftQ_mkQ
    match: partial
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Properties
  - book: isbn:9783031410253
    locator: Section 3E
---

## Statement

A linear map that sends a subspace to zero passes to the quotient by that subspace, in exactly one way.
Let $F$ be a field, let $V$ and $U$ be vector spaces over $F$, and let $W$ be a subspace of $V$.
Let $\pi \colon V \to V / W$ be the [[quotient map|0J0SK5FF4M]] onto the [[quotient space|0SVR29SV1V]].
Let $T \colon V \to U$ be a [[linear map|0RJF668P1T]] with $W \subseteq \ker T$, where $\ker T$ is the [[kernel|02YFME3RGW]].
Then there is exactly one linear map $\bar T \colon V / W \to U$ with $\bar T \circ \pi = T$, and it is given by
$$\bar T(v + W) = T(v) \qquad (v \in V).$$
In addition, $\ker \bar T = \ker T / W$ and $\operatorname{im} \bar T = \operatorname{im} T$.

## Remarks

### Why each hypothesis is needed

The condition $W \subseteq \ker T$ is what makes the formula for $\bar T$ meaningful.
Take $W = \R(1, 1)$ in $\R^2$ and $T(x, y) = x$.
The cosets $(0, 0) + W$ and $(1, 1) + W$ are equal, but $T$ gives $0$ on one representative and $1$ on the other, so no map $\bar T$ with $\bar T \circ \pi = T$ exists.
The condition is also necessary in general: if $T = S \circ \pi$ for some $S$, then $T(w) = S(w + W) = S(0 + W) = 0$ for every $w \in W$.

The linearity of $T$ is needed for $\bar T$ to be linear.
Since $\pi$ is surjective and linear, $\bar T$ is linear exactly when $\bar T \circ \pi = T$ is linear.

### What it gives you

The theorem is the standard way to define a map on a quotient: write down a linear map on $V$, check that it kills $W$, and pass to $V / W$.
For example, differentiation on polynomials of degree at most $3$ kills the constants, so it gives a map on polynomials modulo constants, as [[differentiation modulo constants|20YC6C97W9]] works out.

When $W = \ker T$, the kernel $\ker \bar T = \ker T / W$ is zero, so $\bar T$ is injective onto $\operatorname{im} T$.
This is the [[first isomorphism theorem|0MTBGVZ4XJ]], $V / \ker T \cong \operatorname{im} T$.

The assignment $S \mapsto S \circ \pi$ is a linear isomorphism from the linear maps $V / W \to U$ onto the linear maps $V \to U$ that vanish on $W$.
For $U = F$, this identifies the dual space $(V / W)^*$ with the [[annihilator|0ASHNYF7AG]] of $W$ in $V^*$.

### The converse: the property determines the quotient

Suppose that a space $Q$ and a linear map $p \colon V \to Q$ that vanishes on $W$ have the same property: every linear map that vanishes on $W$ factors uniquely through $p$.
Then the map $V / W \to Q$ induced by $p$ is an isomorphism.
So the quotient space is determined, up to a unique isomorphism, by its universal property.

## History

The phrase "universal property" belongs to category theory, which Eilenberg and Mac Lane introduced in 1945.
The factorization itself is older and is used throughout the algebra of groups, rings and modules.

## Explanations

### L1 human

A linear map that sends every vector of $W$ to zero cannot tell apart two vectors that differ by an element of $W$.
So it gives the same answer on a whole coset, and it makes sense as a rule on cosets.
That rule is a map out of the quotient space.

### L2 human

Let $T \colon \R^3 \to \R$ be $T(x, y, z) = x + y$, and let $W$ be the $z$-axis.
First check the hypothesis: $T(0, 0, z) = 0 + 0 = 0$, so $W \subseteq \ker T$.
Then define $\bar T\bigl((x, y, z) + W\bigr) = x + y$.
Two representatives of one coset differ by some $(0, 0, t)$, and
$$T(x, y, z + t) = x + y = T(x, y, z),$$
so $\bar T$ is well defined.
The kernel of $T$ is the plane $x + y = 0$, which contains $W$, and $\ker \bar T$ is the line $\ker T / W$ inside $\R^3 / W \cong \R^2$.
The image of $\bar T$ is all of $\R$, the same as the image of $T$.
Watch out: a formula such as $(x, y, z) + W \mapsto x + z$ uses the coordinate $z$, which changes along a coset, so it does not define a map on $\R^3 / W$.

### L3 human

The quotient map $\pi$ is the cokernel of the inclusion $W \to V$ in the category of vector spaces.
The theorem says that $V / W$ represents the functor that sends a space $U$ to the linear maps $V \to U$ that vanish on $W$.
The same factorization holds for quotient groups by normal subgroups, quotient rings by ideals and quotient modules, and in any abelian category.
Mathlib constructs $\bar T$ as `Submodule.liftQ W T h` and proves $\bar T \circ \pi = T$ as `Submodule.liftQ_mkQ`.
