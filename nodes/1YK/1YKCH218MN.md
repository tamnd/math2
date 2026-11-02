---
tag: 1YKCH218MN
kind: statement
role: theorem
name: Local index theorem
msc: [58J20, 58J35, 53C27]
uses: [QMRAVX14BJ, 327NP6S7H5, F4WDYPQ9VP, JR2M58RCW3, 82ZPRD39J7, RSPZ9TCFQ8]
about: [QMRAVX14BJ, F4WDYPQ9VP]
sources:
  - url: https://en.wikipedia.org/wiki/Atiyah–Singer_index_theorem
---

## Statement

Let $M$ be a closed Riemannian manifold of even dimension $n$ with a [[spin structure|RSPZ9TCFQ8]] and spinor bundle $S = S^+ \oplus S^-$.
Let $W$ be a Hermitian vector bundle over $M$ with a unitary connection, and let $D_W$ be the [[Dirac operator|QMRAVX14BJ]] on $S \otimes W$.
Let $k_t(x, y)$ be the [[heat kernel|327NP6S7H5]] of $D_W^2$, and let $\operatorname{str}$ be the supertrace on $(S \otimes W)_x$, the trace on $S^+ \otimes W$ minus the trace on $S^- \otimes W$.
Then, uniformly in $x \in M$,
$$\lim_{t \to 0^+} \operatorname{str} k_t(x, x) \, \mathrm{vol}(x) = \Big[ \hat A(TM, \nabla) \operatorname{ch}(W, \nabla^W) \Big]_{n}(x).$$
Here $\hat A(TM, \nabla)$ and $\operatorname{ch}(W, \nabla^W)$ are the [[Chern–Weil|82ZPRD39J7]] forms of the Levi-Civita connection and of the connection on $W$.
They are normalized to represent the $\hat A$-class and the Chern character, and $[\cdot]_n$ is the component of degree $n$.

## Remarks

The [[McKean–Singer formula|F4WDYPQ9VP]] gives $\operatorname{ind} D_W^+ = \int_M \operatorname{str} k_t(x, x) \, \mathrm{vol}(x)$ for every $t > 0$.
Letting $t \to 0^+$ and using the theorem gives $\operatorname{ind} D_W^+ = \int_M \hat A(TM) \operatorname{ch}(W)$, which is the index theorem for twisted Dirac operators and contains [[the Â-genus formula|JR2M58RCW3]] for $W$ trivial.
The striking point is that the singular terms $t^{-n/2}, \ldots, t^{-1}$ of the asymptotic expansion of the supertrace cancel pointwise, not only after integration.
The cancellation was first proved by Patodi for the de Rham complex and by Gilkey with invariance theory.
Getzler gave a proof by a rescaling of the Clifford variables, and Bismut gave a probabilistic proof.
Example: for $n = 2$ and $W$ trivial, $\hat A$ has no component of degree $2$, so the limit is $0$, matching the vanishing index of the Dirac operator on a closed surface.

## Explanations

### L1 human

The index of a Dirac operator is a global count of solutions.
The local index theorem says that the heat kernel, a local object, already knows the curvature integrand that adds up to this count.
At every point, as time goes to zero, the heat flow reveals the characteristic form of the curvature.

### L2 human

The theorem is a sharpened form of the heat equation proof of the index theorem.
It gives the index density pointwise, which is what one needs on manifolds with boundary, for families, and for the [[Atiyah–Patodi–Singer theorem|GGFAH1M80J]].
Its proof by Getzler rescaling is now the standard route to the index theorem in courses on Dirac operators.
