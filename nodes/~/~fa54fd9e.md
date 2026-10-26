---
tag: ~fa54fd9e
kind: statement
role: theorem
name: Picard's great theorem
aliases: [big-picard-theorem, great-picard-theorem]
msc: [30D35]
uses: [~75d899a4, ~66c83564]
sources:
  - url: https://en.wikipedia.org/wiki/Picard_theorem
    locator: The theorems
---

## Statement

Let $c \in \mathbb{C}$, let $r > 0$, and let $f$ be [[holomorphic|~1a187203]] on the punctured disc $0 < |z - c| < r$.
Assume that $c$ is an [[essential singularity|~75d899a4]] of $f$.
Then for each $\delta$ with $0 < \delta < r$, there is at most one $w_0 \in \mathbb{C}$ with this property: $f$ takes the value $w_0$ only finitely many times on $0 < |z - c| < \delta$.
Thus, on each punctured disc around $c$, $f$ takes each complex value infinitely often, with at most one exception.

## Remarks

The exception can occur: $e^{1/z}$ never takes the value $0$, and it takes each $w \neq 0$ infinitely often near $0$, see [[exp(1/z)|~ead0048f]].
The theorem is much stronger than the [[Casorati–Weierstrass theorem|~66c83564]], which gives only that the values come close to each $w$.
Picard's little theorem is a related result: a nonconstant entire function takes all complex values with at most one exception.

## Explanations

### L1 human

Near an essential singularity, the function does not only come close to each value: it hits almost every value infinitely many times.
At most one value can be missed, as $0$ is missed by $e^{1/z}$.
