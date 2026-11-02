---
tag: YB7GN4EAF7
kind: definition
name: Hellinger distance
msc: [62B10, 60B10]
defines: SM0R5T87TH
uses: [059TJN0NZ1, WEBBT18D4X, 1NTKG64F7N, 0VKD1TP7F3, 3SZESKX3N5]
sources:
  - url: https://en.wikipedia.org/wiki/Hellinger_distance
---

## Definition

Let $P$ and $Q$ be [[probability measures|059TJN0NZ1]] on a measurable space $(\mathcal{X}, \mathcal{F})$.
Let $\lambda$ be a [[σ-finite measure|WEBBT18D4X]] such that $P$ and $Q$ are absolutely continuous with respect to $\lambda$, for example $\lambda = P + Q$.
Let $p = dP/d\lambda$ and $q = dQ/d\lambda$ be the [[Radon–Nikodym derivatives|1NTKG64F7N]].
The *Hellinger distance* between $P$ and $Q$ is the number $H(P, Q) \ge 0$ given by
$$H^2(P, Q) = \frac{1}{2} \int_{\mathcal{X}} \big( \sqrt{p} - \sqrt{q} \big)^2 \, d\lambda.$$

## Remarks

The value does not depend on the choice of $\lambda$.
Expanding the square gives $H^2(P, Q) = 1 - \int \sqrt{p q} \, d\lambda$, so $0 \le H \le 1$.
The map $H$ is a [[metric|0VKD1TP7F3]] on the set of probability measures on $(\mathcal{X}, \mathcal{F})$.
Some authors omit the factor $\frac{1}{2}$, which multiplies $H$ by $\sqrt{2}$.
With the convention above, the [[total variation distance|3SZESKX3N5]] $\delta$ satisfies $H^2(P, Q) \le \delta(P, Q) \le \sqrt{2} \, H(P, Q)$.

Example: on $\set{0, 1}$ with counting measure, let $P$ give mass $\frac{1}{2}$ to each point and let $Q$ be the point mass at $1$.
Then $\int \sqrt{pq} = \sqrt{0 \cdot \tfrac{1}{2}} + \sqrt{1 \cdot \tfrac{1}{2}} = 1/\sqrt{2}$, so $H^2(P, Q) = 1 - 1/\sqrt{2}$.

Non-example: the quantity $\frac{1}{2} \int (p - q)^2 \, d\lambda$, without square roots, is not the Hellinger distance.
It changes with $\lambda$: replacing $\lambda$ by $2\lambda$ halves $p$ and $q$ and divides the quantity by $2$.
