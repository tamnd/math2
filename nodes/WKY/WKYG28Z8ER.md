---
tag: WKYG28Z8ER
kind: definition
name: Unirational variety
msc: [14M20, "14E08"]
defines: YF1SE8WJK3
uses: [HV6YBS0YDH, ZT9A6JK8QF, 4D073CCYGV, 2D5SS6WM14]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_variety
    locator: Unirationality
---

## Definition

Let $k$ be a field and let $X$ be an integral [[algebraic variety|HV6YBS0YDH]] over $k$.
The variety $X$ is *unirational* over $k$ if there are an integer $N \ge 1$ and a dominant [[rational map|4D073CCYGV]] $\mathbb{P}^N_k \dashrightarrow X$ from [[projective space|ZT9A6JK8QF]].

## Remarks

Equivalently, the [[function field|2D5SS6WM14]] $k(X)$ embeds over $k$ into a purely transcendental extension $k(t_1, \ldots, t_N)$.
Example: every rational variety is unirational, since a birational map is dominant.
Example: the curve $y^2 = x^3$ in $\mathbb{A}^2$ is unirational.
The map $t \mapsto (t^2, t^3)$ is a dominant morphism from $\mathbb{A}^1$, an open subset of $\mathbb{P}^1$, since $(t^3)^2 = (t^2)^3$ and its image is the whole curve.
Non-example: a smooth projective curve $E$ of genus $1$ over $\C$ is not unirational.
A dominant rational map $\mathbb{P}^N \dashrightarrow E$ restricts to a nonconstant rational map on a general line, and this extends to a nonconstant morphism $f \colon \mathbb{P}^1 \to E$.
The Riemann–Hurwitz formula would then give $-2 = 2g(\mathbb{P}^1) - 2 \ge \deg f \cdot (2g(E) - 2) = 0$, which is false.
