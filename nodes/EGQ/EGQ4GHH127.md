---
tag: EGQ4GHH127
kind: definition
name: Quasi-invariant measure
msc: [28C10, 28D05, 22D40]
defines: FCNQP0A60D
uses: [PR11BZQQPG, 0WCY42EV9V, VQQM4Y550T, 3N66TM3TSQ, P0P21KDV6E, P0DV2TCH1N, 0ACRGYNHSR, WAE4ZGJXJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-invariant_measure
---

## Definition

Let $(X, \Sigma)$ be a measurable space and let $\mu$ be a [[measure|PR11BZQQPG]] on $\Sigma$.
Let $G$ be a group that acts on $X$ by [[group action|0WCY42EV9V]], such that each map $T_g \colon X \to X$, $x \mapsto g \cdot x$, is measurable.
The measure $\mu$ is *quasi-invariant* under $G$ if for every $g \in G$ and every $A \in \Sigma$,
$$\mu(A) = 0 \iff \mu(T_g^{-1}(A)) = 0.$$

## Remarks

Equivalently, for each $g$ the [[pushforward|3N66TM3TSQ]] $(T_g)_* \mu$ and $\mu$ are each [[absolutely continuous|P0P21KDV6E]] with respect to the other.
Every invariant measure is quasi-invariant.

Example: let $G = \R$ act on $X = \R$ by translations, and let $\mu$ be the standard [[Gaussian measure|P0DV2TCH1N]].
Its density is positive everywhere, so $\mu(A) = 0$ exactly when $A$ has Lebesgue measure $0$.
Lebesgue [[null sets|VQQM4Y550T]] are preserved by translations, so $\mu$ is quasi-invariant.

Non-example: under the same action, the [[Dirac measure|0ACRGYNHSR]] $\delta_0$ is not quasi-invariant.
For $g = 1$ and $A = \set{1}$, one has $\delta_0(A) = 0$ but $\delta_0(T_1^{-1}(A)) = \delta_0(\set{0}) = 1$.

By the [[Cameron–Martin theorem|WAE4ZGJXJ7]], Wiener measure is quasi-invariant under translations by the Cameron–Martin space, but not under all translations of the path space.

## Explanations

### L1 human

Moving a set by the group never turns a negligible set into a non-negligible one.
The measure can change in size, but its null sets stay the same.
