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

Let $F$ be a field, let $V$ and $U$ be vector spaces over $F$, and let $W$ be a subspace of $V$.
Let $\pi \colon V \to V / W$ be the [[quotient map|0J0SK5FF4M]] onto the [[quotient space|0SVR29SV1V]].
Let $T \colon V \to U$ be a [[linear map|0RJF668P1T]] with $W \subseteq \ker T$, where $\ker T$ is the [[kernel|02YFME3RGW]].
Then there is exactly one linear map $\bar T \colon V / W \to U$ with $\bar T \circ \pi = T$.
It is given by $\bar T(v + W) = T(v)$.
Moreover, $\ker \bar T = \ker T / W$ and $\operatorname{im} \bar T = \operatorname{im} T$.

## Remarks

### Why each hypothesis is needed

- $W \subseteq \ker T$ is needed for $\bar T$ to be well defined. For $W = \R(1, 1)$ in $\R^2$ and $T(x, y) = x$, the cosets $(0, 0) + W$ and $(1, 1) + W$ are equal, but $T$ gives $0$ and $1$.
- $T$ must be linear. Otherwise $\bar T$ would not be linear, since $\bar T \circ \pi = T$ and $\pi$ is surjective.
- Conversely, any map of the form $\bar T \circ \pi$ vanishes on $W = \ker \pi$, so the condition $W \subseteq \ker T$ is also necessary for a factorization to exist.

### Consequences

- The map $\bar T \mapsto \bar T \circ \pi$ is an isomorphism from $\mathcal{L}(V / W, U)$ onto the subspace of maps $V \to U$ that vanish on $W$.
- For $W = \ker T$, the map $\bar T$ is injective, which gives the [[first isomorphism theorem|0MTBGVZ4XJ]].
- For $U = F$, the dual $(V / W)^*$ is isomorphic to the [[annihilator|0ASHNYF7AG]] of $W$ in $V^*$.
- The quotient space is determined up to a unique isomorphism by this property.

### Converse

If a space $Q$ with a linear map $p \colon V \to Q$ vanishing on $W$ has the same property, then the induced map $V / W \to Q$ is an isomorphism.

## History

The factorization of homomorphisms through quotients was used by Noether in her work on ideals and modules in the 1920s.
It was stated as a universal property in the language of categories by Mac Lane and others in the 1950s.

## Explanations

### L1 human

A linear map that kills every vector of $W$ cannot tell apart two vectors that differ by an element of $W$.
So it makes sense on the cosets, and it becomes a map from the quotient space.
This property describes the quotient space completely.

### L2 human

Let $T \colon \R^3 \to \R$ be $T(x, y, z) = x + y$ and $W$ the $z$-axis.

1. $T(0, 0, z) = 0$, so $W \subseteq \ker T$.
2. Define $\bar T((x, y, z) + W) = x + y$.
3. Well defined: two representatives of one coset differ by $(0, 0, t)$, which does not change $x + y$.
4. $\ker T$ is the set $x + y = 0$, a plane containing $W$, and $\ker \bar T$ is the line $\ker T / W$ in $\R^3 / W \cong \R^2$.

The trap is to define $\bar T$ by a formula that uses $z$, which would change along a coset.

### L3 human

The quotient map $\pi$ is the cokernel of the inclusion $W \to V$ in the category of vector spaces.
The property says that $V / W$ represents the functor sending $U$ to the linear maps $V \to U$ that vanish on $W$.
The same factorization holds for groups, rings and modules, and in any abelian category.
Mathlib constructs $\bar T$ as `Submodule.liftQ W T h` and proves $\bar T \circ \pi = T$ as `Submodule.liftQ_mkQ`.
