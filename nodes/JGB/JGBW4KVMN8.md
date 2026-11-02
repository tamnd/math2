---
tag: JGBW4KVMN8
kind: definition
name: Homology manifold
msc: [57P05, 55N10]
defines: 6TKGN8K8KT
uses: [0FE2SB8WVJ, 0S1FJ8VEX9, 4BVWH0BN28, QQQ9B1DK4P]
sources:
  - url: https://en.wikipedia.org/wiki/Homology_manifold
---

## Definition

Let $n \ge 0$ be an integer and let $X$ be a [[locally compact|0FE2SB8WVJ]] [[Hausdorff space|0S1FJ8VEX9]].
The space $X$ is a *homology $n$-manifold* if, for every point $x \in X$, the local [[relative homology|4BVWH0BN28]] groups satisfy
$$H_i(X, X \setminus \set{x}; \Z) \cong \begin{cases} \Z & \text{if } i = n, \\ 0 & \text{if } i \neq n. \end{cases}$$

## Remarks

Several variants are in use: some authors also ask that $X$ be finite-dimensional or an absolute neighbourhood retract, or use sheaf-theoretic homology or coefficients in a ring other than $\Z$.

Example: a [[topological $n$-manifold|QQQ9B1DK4P]] $M$ is a homology $n$-manifold.
By excision, $H_i(M, M \setminus \set{x}) \cong H_i(\R^n, \R^n \setminus \set{0})$, and the long exact sequence of the pair gives $H_i(\R^n, \R^n \setminus \set{0}) \cong \tilde{H}_{i-1}(S^{n-1})$, which is $\Z$ for $i = n$ and $0$ otherwise.

Non-example: let $X$ be the wedge of two circles and $x$ the wedge point.
Then $X \setminus \set{x}$ is a disjoint union of two open arcs, and the long exact sequence gives $H_1(X, X \setminus \set{x}) \cong \Z^3$, so $X$ is not a homology $1$-manifold.

The suspension of the Poincaré homology sphere is a homology $4$-manifold that is not a topological manifold.
The reason is that a small neighbourhood of a suspension point, with that point removed, is not simply connected.
