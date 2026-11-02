---
tag: TEG1ZX1AGJ
kind: statement
role: theorem
name: Hirzebruch signature theorem
msc: [57R20, 55R40]
uses: [F45VQ47GPV, 913WEQERBE, DN11FKWN63, WK8GKRKAVD, 07EZA80NEH, T8BVGPPSZP]
about: [DN11FKWN63, WK8GKRKAVD]
sources:
  - url: https://en.wikipedia.org/wiki/Hirzebruch_signature_theorem
same_as:
  wikidata: Q7512855
  wikipedia: Hirzebruch signature theorem
---

## Statement

Let $M$ be a closed oriented [[smooth manifold|F45VQ47GPV]] of dimension $4k$ with fundamental class $[M]$.
Let $\sigma(M)$ be the [[signature|07EZA80NEH]] of its [[intersection form|WK8GKRKAVD]] on $H^{2k}(M; \R)$, the symmetric bilinear form $(a, b) \mapsto \langle a \smile b, [M] \rangle$.
Let $p_i = p_i(TM) \in H^{4i}(M; \Q)$ be the [[Pontryagin classes|DN11FKWN63]] of the tangent bundle.
Let $L_k(p_1, \ldots, p_k)$ be the degree $4k$ part of the multiplicative sequence of Hirzebruch with characteristic power series $\sqrt{z} / \tanh \sqrt{z}$.
Then
$$\sigma(M) = \langle L_k(p_1, \ldots, p_k), [M] \rangle.$$

## Remarks

The first two polynomials are $L_1 = \tfrac{1}{3} p_1$ and $L_2 = \tfrac{1}{45}(7 p_2 - p_1^2)$.
Idea of the proof: both sides are invariants of oriented [[cobordism|T8BVGPPSZP]], additive under disjoint union and multiplicative under products.
So both sides are ring homomorphisms from the rational oriented cobordism ring to $\Q$.
Thom showed that this ring is a polynomial ring on the classes of the complex projective spaces $\C P^{2i}$.
The power series is chosen so that the right side equals $1 = \sigma(\C P^{2i})$ on each generator, and so the two homomorphisms agree.

Example: for $M = \C P^2$ with generator $h \in H^2$, the total Pontryagin class is $(1 + h^2)^3$, so $p_1 = 3h^2$ and $\langle L_1, [M] \rangle = 1$.
The intersection form is $(1)$, so $\sigma(\C P^2) = 1$, as the theorem says.
For a closed oriented smooth $4$-manifold the theorem gives $p_1[M] = 3 \sigma(M)$.

## Explanations

### L1 human

The signature is a whole number read off from how middle-dimensional cycles in a manifold intersect.
Pontryagin classes measure how the tangent bundle is twisted.
The theorem says that one fixed combination of the Pontryagin numbers always equals the signature.
So a number defined by pure topology is computed by curvature-type data.

### L2 human

The theorem shows that a certain rational combination of Pontryagin numbers is always an integer, which constrains which manifolds can exist.
Milnor used the case $k = 2$ to show that some $7$-manifolds homeomorphic to $S^7$ are not diffeomorphic to it, the first [[exotic spheres|6WYEMXSHD9]].
The theorem is a special case of the Atiyah–Singer index theorem applied to the signature operator.
It is also the model for the [[Hirzebruch–Riemann–Roch theorem|G3X02FKQCR]].
In surgery theory, the signature formula is what makes the simply connected surgery obstruction in dimensions $4k$ computable.
