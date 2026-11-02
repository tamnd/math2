---
tag: 231TRBRZSY
kind: definition
name: Measure-preserving transformation
msc: [28D05, 37A05]
defines: 556WBDAHNP
uses: [P15VQS5DJ9, YYNCJSR0PJ]
sources:
  - url: https://en.wikipedia.org/wiki/Measure-preserving_dynamical_system
    locator: Definition
---

## Definition

Let $(X, \mathcal{A}, \mu)$ and $(Y, \mathcal{B}, \nu)$ be [[measure spaces|P15VQS5DJ9]].
A map $T \colon X \to Y$ is *measure-preserving* if two conditions hold.

1. $T$ is [[measurable|YYNCJSR0PJ]]: $T^{-1}(B) \in \mathcal{A}$ for every $B \in \mathcal{B}$.
2. $\mu(T^{-1}(B)) = \nu(B)$ for every $B \in \mathcal{B}$.

## Remarks

Condition 2 says that the [[pushforward measure|3N66TM3TSQ]] $T_* \mu$ equals $\nu$.
When $X = Y$ and $\mu = \nu$, one says that $T$ preserves $\mu$, and $(X, \mathcal{A}, \mu, T)$ is a measure-preserving system.
Example: the doubling map $T(x) = 2x \bmod 1$ on $[0,1)$ with Lebesgue measure $\lambda$.
For $0 \le a < b \le 1$ one has $T^{-1}([a, b)) = [a/2, b/2) \cup [(a+1)/2, (b+1)/2)$, of measure $b - a$.
The intervals form a $\pi$-system that generates the Borel sets, so condition 2 holds for all Borel sets.
Non-example: $T(x) = x^2$ on $[0,1]$ with Lebesgue measure is measurable but $\lambda(T^{-1}([0, 1/4])) = \lambda([0, 1/2]) = 1/2 \ne 1/4$.
