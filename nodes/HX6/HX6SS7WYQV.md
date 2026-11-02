---
tag: HX6SS7WYQV
kind: definition
name: Invariant measure
msc: [37A05, 28D05, 37C40]
defines: B232EZ1FMB
uses: [PR11BZQQPG, YYNCJSR0PJ, 556WBDAHNP, 3N66TM3TSQ]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_measure
---

## Definition

Let $(X, \mathcal{A})$ be a measurable space and let $T \colon X \to X$ be a [[measurable map|YYNCJSR0PJ]].
A [[measure|PR11BZQQPG]] $\mu$ on $(X, \mathcal{A})$ is *$T$-invariant* if
$$\mu(T^{-1}(A)) = \mu(A) \quad \text{for every } A \in \mathcal{A}.$$
Let a family of measurable maps be given, such as a flow $(\varphi_t)$ or a group action.
Then $\mu$ is *invariant* if it is invariant under each map of the family.

## Remarks

Equivalently, the [[pushforward measure|3N66TM3TSQ]] $T_* \mu$ equals $\mu$, or $T$ is a [[measure-preserving transformation|556WBDAHNP]] of $(X, \mathcal{A}, \mu)$ to itself.
For an integrable function $g$, invariance gives $\int g \circ T \, d\mu = \int g \, d\mu$.
The invariant probability measures of $T$ form a convex set, whose extreme points are the ergodic ones.

Example: the doubling map $T(x) = 2x \bmod 1$ on $[0, 1)$ and Lebesgue measure $\lambda$.
For an interval $[a, b) \subseteq [0, 1)$, one has $T^{-1}([a, b)) = [a/2, b/2) \cup [(a+1)/2, (b+1)/2)$, of length $b - a$.
Since intervals generate the Borel sets and are closed under intersection, $\lambda$ is $T$-invariant.

Non-example: the map $T(x) = x^2$ on $[0, 1]$ with Lebesgue measure $\lambda$.
One has $T^{-1}([0, 1/4]) = [0, 1/2]$, so $\lambda(T^{-1}([0, 1/4])) = 1/2 \ne 1/4$, and $\lambda$ is not $T$-invariant.
The point masses at $0$ and at $1$ are $T$-invariant, since $0$ and $1$ are fixed points.
