---
tag: GEXSRZ7JEH
kind: definition
name: Caustic
msc: [53D12, 58K05, 78A05]
defines: GMRYG4S3G0
uses: [F45VQ47GPV, H8ACPTMX08, QKPMR9MC9W]
sources:
  - url: https://en.wikipedia.org/wiki/Caustic_(mathematics)
---

## Definition

Let $Q$ be a [[smooth manifold|F45VQ47GPV]] of dimension $n$.
Let $\pi \colon T^*Q \to Q$ be its cotangent bundle with the canonical symplectic form, and let $L \subset T^*Q$ be a [[Lagrangian submanifold|H8ACPTMX08]].
Let $\Sigma_L \subset L$ be the set of [[Lagrangian singularities|QKPMR9MC9W]] of $L$, the points where the differential of $\pi|_L \colon L \to Q$ has rank less than $n$.
The *caustic* of $L$ is the set
$$C_L = \pi(\Sigma_L) \subset Q$$
of critical values of the Lagrangian map $\pi|_L$.

## Remarks

Example: $Q = \R$ and $L = \set{(p^2, p) : p \in \R} \subset T^*\R = \R^2$.
The map $\pi|_L$ is $p \mapsto p^2$, singular only at $p = 0$, so $\Sigma_L = \set{(0, 0)}$ and $C_L = \set{0}$.
Over $q > 0$ lie two points of $L$, and over $q < 0$ none, so the number of preimages jumps at the caustic.

Non-example: if $L$ is the graph of $dS$ for a smooth function $S$ on $Q$, then $\pi|_L$ is a diffeomorphism, $\Sigma_L$ is empty, and the caustic is empty.

In geometric optics, $Q$ is space and $L$ is the set of positions and directions of the rays of a beam.
Then $C_L$ is the envelope of the family of rays, where the rays focus.
If $L$ is given locally by a generating family $F(q, y)$, the caustic is the [[bifurcation set|JV45S0KQE6]] of the family $y \mapsto F(q, y)$ with $q$ as control.
