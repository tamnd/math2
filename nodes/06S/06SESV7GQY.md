---
tag: 06SESV7GQY
kind: statement
role: theorem
name: Continuous functions are Riemann integrable
msc: [26A42]
uses: [0W0TZDRF9C, 017DH8WXTE]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_integral
    locator: Integrability
---

## Statement

Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be continuous.
Then $f$ is Riemann integrable on $[a, b]$.

## Remarks

By the [[Heine–Cantor theorem|0W0TZDRF9C]], $f$ is uniformly continuous. Choose $\delta$ for $\varepsilon/(b - a)$. For a partition of mesh less than $\delta$, $U(f, P) - L(f, P) < \varepsilon$. Then [[Riemann's criterion|017DH8WXTE]] applies.
More generally, a bounded function with finitely many discontinuities is Riemann integrable.

## Explanations

### L1 human

On short pieces of the interval, a continuous function changes very little.
So the upper and lower sums are close for fine partitions.
