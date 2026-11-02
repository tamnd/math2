---
tag: GE75S5XZ9T
kind: definition
name: Polarity
msc: ["51A10", "51A50"]
defines: 727TZQJ4ZA
uses: [ZT9A6JK8QF, 000AYPA9AJ, 00YC1D652K, 0SQZMXB6GP, 054YEQ0Y8M]
sources:
  - url: https://en.wikipedia.org/wiki/Duality_(projective_geometry)
---

## Definition

Let $V$ be a [[vector space|000AYPA9AJ]] of finite dimension $n + 1 \ge 3$ over a division ring.
Let $\mathcal{L}(V)$ be the set of its [[linear subspaces|00YC1D652K]], which are the subspaces of the [[projective space|ZT9A6JK8QF]] $\mathbb{P}(V)$.
A *correlation* of $\mathbb{P}(V)$ is a bijection $\delta \colon \mathcal{L}(V) \to \mathcal{L}(V)$ such that $U \subseteq W$ if and only if $\delta(W) \subseteq \delta(U)$, for all $U, W \in \mathcal{L}(V)$.
A *polarity* is a correlation $\delta$ with $\delta(\delta(U)) = U$ for all $U \in \mathcal{L}(V)$.

## Remarks

A correlation sends subspaces of dimension $k$ to subspaces of dimension $n + 1 - k$, so it exchanges points and hyperplanes.
For a polarity $\delta$, the hyperplane $\delta(P)$ is the polar of the point $P$, and $P$ is the pole of that hyperplane.

Example: let $F$ be a field, $V = F^{n+1}$ and $\delta(U) = U^\perp = \set{y : x \cdot y = 0 \text{ for all } x \in U}$, with the dot product $x \cdot y = \sum_i x_i y_i$.
If $U \subseteq W$ then $W^\perp \subseteq U^\perp$; since the dot product is a non-degenerate symmetric [[bilinear form|0SQZMXB6GP]], $\dim U^\perp = n + 1 - \dim U$ and $(U^\perp)^\perp = U$.
So $\delta$ is a bijection that reverses inclusion and has $\delta^2 = \id$: it is a polarity.

Non-example: on $F^3$ let $M$ be the matrix with rows $(1, 1, 0)$, $(0, 1, 0)$, $(0, 0, 1)$, and let $\delta(U) = \set{y : x^T M y = 0 \text{ for all } x \in U}$.
This is a correlation, but $\delta(\delta(U)) = M^{-1} M^T U$.
For $U = \langle e_1 \rangle$ one gets $M^T e_1 = (1, 1, 0)$ and $M^{-1} (1, 1, 0) = (0, 1, 0)$, so $\delta^2(\langle e_1 \rangle) = \langle e_2 \rangle \ne \langle e_1 \rangle$, and $\delta$ is not a polarity.

Every correlation of $\mathbb{P}(V)$ comes from a non-degenerate [[sesquilinear form|054YEQ0Y8M]] $f$ by $\delta(U) = \set{y : f(x, y) = 0 \text{ for all } x \in U}$.
It is a polarity exactly when $f$ is reflexive, that is $f(x, y) = 0$ implies $f(y, x) = 0$; up to a scalar, such forms are symmetric, alternating or Hermitian.
