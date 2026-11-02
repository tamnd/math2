---
tag: FWF9D69R3F
kind: definition
name: Casson invariant
msc: [57K31]
defines: 33GY6P5A4T
uses: [HK8NS02NNE, QYEAZTYGPT, ZA405B0Z1S, JKA25KDPQP]
sources:
  - url: https://en.wikipedia.org/wiki/Casson_invariant
---

## Definition

Let $\Sigma$ be an oriented integral [[homology 3-sphere|HK8NS02NNE]], let $K \subset \Sigma$ be a [[knot|QYEAZTYGPT]] and let $n$ be an integer.
Let $\Sigma_{K, 1/n}$ be the result of [[Dehn surgery|ZA405B0Z1S]] on $K$ with coefficient $1/n$; it is again an oriented integral homology $3$-sphere.
Let $\Delta_K(t)$ be the [[Alexander polynomial|JKA25KDPQP]] of $K$, normalised so that $\Delta_K(t^{-1}) = \Delta_K(t)$ and $\Delta_K(1) = 1$.

The *Casson invariant* is the unique function $\lambda$ from oriented integral homology $3$-spheres, up to orientation-preserving homeomorphism, to $\Z$ such that:

1. $\lambda(S^3) = 0$, and
2. for every $\Sigma$, $K$ and $n$ as above,
$$\lambda(\Sigma_{K, 1/(n+1)}) - \lambda(\Sigma_{K, 1/n}) = \tfrac{1}{2} \Delta_K''(1).$$

Casson proved that such a function exists and is unique.

## Remarks

Example: for a trefoil knot $K$ in $S^3$, $\Delta_K(t) = t - 1 + t^{-1}$, so $\Delta_K''(t) = 2 t^{-3}$ and $\tfrac12 \Delta_K''(1) = 1$.
Since $S^3_{K, 1/0} = S^3$, clause 2 with $n = 0$ gives $\lambda(S^3_{K, 1}) = 1$.
For the right-handed trefoil, $S^3_{K, 1}$ is the Poincaré homology sphere with the orientation opposite to that of $\Sigma(2, 3, 5)$, and $\lambda(\Sigma(2, 3, 5)) = -1$.

Further properties: $\lambda(-\Sigma) = -\lambda(\Sigma)$, $\lambda$ is additive under connected sum, and $\lambda(\Sigma)$ is congruent modulo $2$ to the Rokhlin invariant of $\Sigma$.
