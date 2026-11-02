---
tag: D38ZP0YX0D
kind: definition
name: Quasi-measure-preserving map
msc: [28D05, 37A40]
defines: F608XX51KA
uses: [P15VQS5DJ9, YYNCJSR0PJ, VQQM4Y550T]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-invariant_measure
---

## Definition

Let $(X, \mathcal{A}, \mu)$ and $(Y, \mathcal{B}, \nu)$ be [[measure spaces|P15VQS5DJ9]].
A map $T \colon X \to Y$ is *quasi-measure-preserving* if two conditions hold.

1. $T$ is [[measurable|YYNCJSR0PJ]]: $T^{-1}(B) \in \mathcal{A}$ for every $B \in \mathcal{B}$.
2. If $B \in \mathcal{B}$ and $\nu(B) = 0$, then $\mu(T^{-1}(B)) = 0$.

## Remarks

Condition 2 says that the pushforward $T_* \mu$ is [[absolutely continuous|P0P21KDV6E]] with respect to $\nu$, that is, preimages of [[null sets|VQQM4Y550T]] are null sets.
Every [[measure-preserving|556WBDAHNP]] map satisfies it.
Example: $T(x) = 2x$ on $\R$ with Lebesgue measure $\lambda$.
For a Borel set $B$ one has $\lambda(T^{-1}(B)) = \lambda(B)/2$, so null sets pull back to null sets, but $T$ is not measure-preserving.
Non-example: the constant map $T(x) = 0$ from $[0,1]$ to $\R$, both with Lebesgue measure, is measurable.
But $\lambda(\set{0}) = 0$ while $\lambda(T^{-1}(\set{0})) = \lambda([0,1]) = 1$, so condition 2 fails.
