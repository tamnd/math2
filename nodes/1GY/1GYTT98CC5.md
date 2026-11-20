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

Let $F$ be a field and let
$$0 \to U \xrightarrow{f} V \xrightarrow{g} W \to 0$$
be a [[short exact sequence|8MCYV0P04T]] of vector spaces over $F$.
Then there is a [[linear map|0RJF668P1T]] $s \colon W \to V$ with $g \circ s = \operatorname{id}_W$, and the map
$$U \oplus W \to V, \qquad (u, w) \mapsto f(u) + s(w),$$
is an [[isomorphism|0XSJ25Z9M4]] from the [[external direct sum|02WZB422CE]].
Equivalently, there is a linear map $r \colon V \to U$ with $r \circ f = \operatorname{id}_U$.

## Remarks

### Why each hypothesis is needed

- $F$ must be a field. For abelian groups, $0 \to \Z \xrightarrow{2} \Z \to \Z / 2\Z \to 0$ is exact, but it does not split, since $\Z$ is not isomorphic to $\Z \oplus \Z / 2\Z$: the latter has an element of order $2$.
- Exactness at $V$ is needed. Let $f(t) = (t, 0, 0)$ from $\R$ to $\R^3$ and $g(x, y, z) = y$ from $\R^3$ to $\R$.
  Then $f$ is injective and $g$ is surjective, but $\R \oplus \R$ is not isomorphic to $\R^3$, since the dimensions differ.
- $g$ must be surjective for a right inverse $s$ to exist, since $g \circ s = \operatorname{id}_W$ forces $g$ to hit all of $W$.

### Consequences

- In finite dimension, $\dim V = \dim U + \dim W$.
- Every surjective linear map has a right inverse, and every injective linear map has a left inverse.
- Every additive functor, such as $\operatorname{Hom}(X, -)$, $\operatorname{Hom}(-, X)$ or $X \otimes -$, sends short exact sequences of vector spaces to short exact sequences.
- Every vector space is projective and injective as a module over $F$.

### Converse

Any sequence $0 \to U \to U \oplus W \to W \to 0$ with the canonical maps is exact and split.
So the theorem says that every short exact sequence is isomorphic to such a trivial one.

## History

The splitting of exact sequences of modules is the subject of the splitting lemma, which became standard in the homological algebra of Cartan and Eilenberg in 1956.
For vector spaces, the result is the existence of complements, known since the early abstract treatments of linear algebra.
The splitting lemma in general form is the [[splitting lemma|7ZGQKWYKQS]].

## Explanations

### L1 human

When $V$ contains a copy of $U$ with quotient $W$, we can pick a copy of $W$ inside $V$ as well.
Then $V$ is the direct sum of the two copies.

### L2 human

For $f(t) = (t, t, t)$ and $g(x, y, z) = (x - y, y - z)$, as in [[the example|EEN9A35R25]]:

1. A right inverse is $s(a, b) = (a + b, b, 0)$, since $g(a + b, b, 0) = (a, b)$.
2. Then $(t, (a, b)) \mapsto (t + a + b, t + b, t)$ is the isomorphism $\R \oplus \R^2 \to \R^3$.
3. Its inverse reads $t = z$, $b = y - z$, $a = x - y$.

The trap is that $s$ is not unique: adding any map $W \to f(U)$ to $s$ gives another right inverse.

### L3 human

The [[proof|H3TPZZP95H]] uses the [[existence of complements|0P9T8WHNMH]], which rests on the axiom of choice in infinite dimension.
In the language of homological algebra, the theorem says $\operatorname{Ext}^1_F(W, U) = 0$ for all vector spaces over a field.
Rings over which every short exact sequence of modules splits are exactly the semisimple rings.
