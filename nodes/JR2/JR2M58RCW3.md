---
tag: JR2M58RCW3
kind: statement
role: theorem
name: Â-genus as the index of the Dirac operator
msc: [58J20, 57R20, 53C27]
uses: [QMRAVX14BJ, RSPZ9TCFQ8, DN11FKWN63, 44GBFZ16SG]
about: [QMRAVX14BJ, 44GBFZ16SG]
sources:
  - url: https://en.wikipedia.org/wiki/Genus_of_a_multiplicative_sequence
---

## Statement

Let $M$ be a closed Riemannian manifold of dimension $4k$ with a [[spin structure|RSPZ9TCFQ8]], and let $S = S^+ \oplus S^-$ be its complex spinor bundle.
Let $D^+ \colon C^\infty(M; S^+) \to C^\infty(M; S^-)$ be the [[Dirac operator|QMRAVX14BJ]] restricted to positive spinors.
Let $p_i \in H^{4i}(M; \Q)$ be the [[Pontryagin classes|DN11FKWN63]] of $TM$.
Let $\hat A_k(p_1, \ldots, p_k)$ be the degree $4k$ part of the multiplicative sequence with characteristic power series $\dfrac{\sqrt{z}/2}{\sinh(\sqrt{z}/2)}$.
Then the [[analytic index|44GBFZ16SG]] of $D^+$ is
$$\operatorname{ind} D^+ = \hat A(M) := \langle \hat A_k(p_1, \ldots, p_k), [M] \rangle.$$

## Remarks

The theorem is the case of the Atiyah–Singer index theorem for the spin Dirac operator.
In the cohomological formula, the Chern character of the spinor symbol combined with the Todd class leaves exactly the $\hat A$-class.
The first terms are $\hat A_1 = -\tfrac{1}{24} p_1$ and $\hat A_2 = \tfrac{1}{5760}(-4 p_2 + 7 p_1^2)$.
Consequence: the $\hat A$-genus of a closed spin manifold is an integer, while for general manifolds it is only rational.
The spin hypothesis is necessary: $\C P^2$ is not spin, and $\hat A(\C P^2) = -\tfrac{1}{24} \cdot 3 = -\tfrac18$.
Example: a K3 surface is spin with $p_1 = -48$, so $\hat A = 2$, and the Dirac operator has index $2$.
With the Lichnerowicz formula $D^2 = \nabla^*\nabla + \tfrac{s}{4}$, where $s$ is the scalar curvature, the theorem shows that a closed spin manifold with $\hat A(M) \ne 0$ has no metric of positive scalar curvature.

## Explanations

### L1 human

The $\hat A$-genus is a number computed from the curvature, or the Pontryagin classes, of a manifold.
A priori it is a fraction.
On a spin manifold it counts the harmonic positive spinors minus the harmonic negative spinors, so it is an integer.

### L2 human

On an even-dimensional spin manifold, the K-theory Thom isomorphism shows that every class in $K(T^*M)$ is a difference of symbol classes of Dirac operators twisted by vector bundles.
Twisting by a complex vector bundle $W$ gives $\operatorname{ind} D^+_W = \langle \hat A(TM) \operatorname{ch}(W), [M] \rangle$, where $\operatorname{ch}$ is the Chern character.
So on spin manifolds this special case already contains the general index theorem.
The vanishing of $\hat A(M)$ under positive scalar curvature, due to Lichnerowicz, began the study of obstructions to positive scalar curvature.
