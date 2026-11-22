---
tag: 1GYTT98CC5
kind: statement
role: theorem
name: Short exact sequences of vector spaces split
msc: ["15A03", "18G35"]
topics: [QHKTJ89V6S]
audience: grad
about: [946YAZNYKX]
uses: [8MCYV0P04T, 0RJF668P1T, 02WZB422CE, 0XSJ25Z9M4]
formal:
  - system: lean4
    library: mathlib
    decl: LinearMap.exists_rightInverse_of_surjective
    match: partial
sources:
  - url: https://en.wikipedia.org/wiki/Splitting_lemma
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Exact_sequence
    locator: Splitting
---

## Statement

Over a field, a space built from a subspace and a quotient is always the direct sum of the two pieces.
Let $F$ be a field, and let
$$0 \to U \xrightarrow{f} V \xrightarrow{g} W \to 0$$
be a [[short exact sequence|8MCYV0P04T]] of vector spaces over $F$.
Then there is a [[linear map|0RJF668P1T]] $s \colon W \to V$ with $g \circ s = \operatorname{id}_W$, and for each such $s$ the map
$$U \oplus W \to V, \qquad (u, w) \mapsto f(u) + s(w),$$
from the [[external direct sum|02WZB422CE]] is an [[isomorphism|0XSJ25Z9M4]].
There is also a linear map $r \colon V \to U$ with $r \circ f = \operatorname{id}_U$.

## Remarks

### Why each hypothesis is needed

The scalars must form a field.
For abelian groups, which are modules over the ring $\Z$, the sequence $0 \to \Z \xrightarrow{\cdot 2} \Z \to \Z / 2\Z \to 0$ is exact.
It does not split, because $\Z$ is not isomorphic to $\Z \oplus \Z / 2\Z$: the second group has the element $(0, \bar 1)$ of order $2$, and $\Z$ has none.
The [[proof|H3TPZZP95H]] uses a complement of $\ker g$, and $2\Z$ has no complement in $\Z$.

Exactness in the middle is needed.
Let $f(t) = (t, 0, 0)$ from $\R$ to $\R^3$ and $g(x, y, z) = y$ from $\R^3$ to $\R$.
Then $f$ is injective and $g$ is onto, but $\operatorname{im} f$ is the $x$-axis while $\ker g$ is the $xz$-plane.
The conclusion fails, since $\R \oplus \R$ has dimension $2$ and $\R^3$ has dimension $3$.

The map $g$ must be onto, since $g \circ s = \operatorname{id}_W$ forces every $w = g(s(w))$ to lie in the image of $g$.
In the same way, $r \circ f = \operatorname{id}_U$ forces $f$ to be injective.

### What it gives you

In finite dimension the isomorphism gives $\dim V = \dim U + \dim W$.

Applied to the sequence $0 \to \ker g \to V \to W \to 0$, the theorem says that every onto linear map has a right inverse.
Applied to $0 \to U \to V \to V / f(U) \to 0$, it says that every injective linear map has a left inverse.
For example, $g(x, y) = x + y$ from $\R^2$ to $\R$ has the right inverse $s(t) = (t, 0)$, and also $s'(t) = (0, t)$.

Every additive functor, such as $\operatorname{Hom}(X, -)$, $\operatorname{Hom}(-, X)$ or $X \otimes -$, sends a split exact sequence to a split exact sequence.
So these functors keep short exact sequences of vector spaces exact.
In module language, every vector space is both projective and injective as a module over $F$.

### The converse

For any spaces $U$ and $W$, the sequence $0 \to U \to U \oplus W \to W \to 0$ with $u \mapsto (u, 0)$ and $(u, w) \mapsto w$ is exact and split.
So the theorem says that every short exact sequence of vector spaces is isomorphic to one of this trivial kind.

## History

For modules the general statement is the [[splitting lemma|7ZGQKWYKQS]], which says when a short exact sequence splits.
For vector spaces the content is the [[existence of complementary subspaces|0P9T8WHNMH]], applied to $\ker g$.

## Explanations

### L1 human

Suppose that $V$ contains a copy of $U$, and that collapsing that copy to $0$ leaves $W$.
Then you can find a copy of $W$ inside $V$ as well.
Every vector of $V$ is then a sum of one piece from each copy, in exactly one way.
For example, $\R^3$ is the line through $(1, 1, 1)$ plus the plane $z = 0$.

### L2 human

Take $f(t) = (t, t, t)$ and $g(x, y, z) = (x - y, y - z)$, as in [[the example|EEN9A35R25]].

1. A right inverse is $s(a, b) = (a + b, b, 0)$, since
$$g(a + b, b, 0) = (a + b - b,\ b - 0) = (a, b).$$
2. The isomorphism $\R \oplus \R^2 \to \R^3$ is $(t, (a, b)) \mapsto (t + a + b,\ t + b,\ t)$.
3. Its inverse reads off $t = z$, then $b = y - z$, then $a = x - y$.
   Check: $(z + (x - y) + (y - z),\ z + (y - z),\ z) = (x, y, z)$.

The typical use is to replace $V$ by $U \oplus W$ and to work with the two smaller spaces.
Watch out: $s$ is not unique.
Adding to $s$ any linear map $W \to f(U)$ gives another right inverse, because $g$ kills $f(U)$, and each choice of $s$ matches a choice of complement of $f(U)$.

### L3 human

The [[proof|H3TPZZP95H]] uses the [[existence of complements|0P9T8WHNMH]], which in infinite dimension rests on the axiom of choice through the existence of bases.
In homological algebra the theorem says that $\operatorname{Ext}^1_F(W, U) = 0$ for all vector spaces $U$ and $W$ over a field.
The rings over which every short exact sequence of modules splits are exactly the semisimple rings, and a field is the simplest example.
Over general rings the failure of splitting is what makes [[exact sequences|946YAZNYKX]] carry information beyond dimension.
