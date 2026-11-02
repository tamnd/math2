---
tag: W6J4MQ6D5N
kind: definition
name: Quaternion-Kähler manifold
msc: [53C26, 53C29]
defines: NAJBH8GJMM
uses: [7CBT4SM83Y, WHDZ3MK56B, 9SYWRGVTRS, CAZYGE1T4E, 87AWY7NQS0, 41S2EZ0KR3]
sources:
  - url: https://en.wikipedia.org/wiki/Quaternion-K%C3%A4hler_manifold
---

## Definition

Let $n \ge 2$ and let $(M, g)$ be a connected [[Riemannian manifold|7CBT4SM83Y]] of dimension $4n$.
Let $Sp(n) \cdot Sp(1) = (Sp(n) \times Sp(1)) / \set{\pm 1}$, acting on $\mathbb{H}^n = \R^{4n}$ by $v \mapsto a v \bar{b}$ for $a \in Sp(n)$ and unit quaternions $b \in Sp(1)$.
The manifold $M$ is *quaternion-Kähler* if its [[holonomy|WHDZ3MK56B]] group is contained in $Sp(n) \cdot Sp(1) \subseteq SO(4n)$.

Equivalently, there is a rank $3$ subbundle $Q \subseteq \End(TM)$ such that:

1. $Q$ is preserved by the [[Levi-Civita connection|CAZYGE1T4E]];
2. near each point, $Q$ has a local frame $I, J, K$ of [[almost complex structures|9SYWRGVTRS]] that are orthogonal for $g$ and satisfy $IJ = K$.

## Remarks

Example: the quaternionic projective space $\mathbb{H}P^n$ with its standard symmetric metric, whose holonomy is all of $Sp(n) \cdot Sp(1)$.

Non-example: no manifold of dimension $6$ is quaternion-Kähler, since the dimension must be a multiple of $4$.

For $n \ge 2$, a quaternion-Kähler manifold is [[Einstein|41S2EZ0KR3]].
[[Hyperkähler manifolds|87AWY7NQS0]] satisfy the definition, with holonomy in $Sp(n) \subseteq Sp(n) \cdot Sp(1)$; many authors exclude them by asking for nonzero scalar curvature.
In dimension $4$ the holonomy condition is empty, since $Sp(1) \cdot Sp(1) = SO(4)$, so one defines quaternion-Kähler $4$-manifolds instead as self-dual Einstein manifolds.
