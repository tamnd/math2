---
tag: 1X3EV2TZNN
kind: conjecture
name: Kobayashi conjecture
msc: [32Q45, 14J70]
uses: [HRPAX8V7HA, ZT9A6JK8QF, Y7W36GJDJD]
about: [HRPAX8V7HA]
sources:
  - url: https://en.wikipedia.org/wiki/Kobayashi_metric
history:
  posed_by: "Shoshichi Kobayashi"
  first_stated: "1970"
---

## Statement

Let $n \ge 2$ and let $X \subset \mathbb{P}^{n+1}$ be a very general hypersurface of degree $d$ in complex [[projective space|ZT9A6JK8QF]].
Very general means that the defining polynomial lies outside a countable union of proper algebraic subsets of the space of polynomials of degree $d$.

1. If $d \ge 2n + 1$, then $X$ is [[Kobayashi hyperbolic|HRPAX8V7HA]].
2. If $d \ge 2n + 3$, then the complement $\mathbb{P}^{n+1} \setminus X$ is Kobayashi hyperbolic.

## Remarks

Kobayashi stated these problems in his 1970 book on hyperbolic manifolds.
The hypothesis $n \ge 2$ is needed in part 1 in this form.
For $n = 1$ the bound would be $d \ge 3$, but a smooth plane cubic is an elliptic curve, a complex torus, which is not hyperbolic.
For $n = 1$ the true statement is that smooth plane curves of degree at least $4$ are hyperbolic, since they have genus at least $3$.
Part 1 is known for all $d$ larger than a bound that depends on $n$; Yum-Tong Siu and Damian Brotbek gave proofs.
Later work lowered the bound, which is still far above $2n + 1$ for large $n$.
For $d \le 2n - 1$, every hypersurface of degree $d$ in $\mathbb{P}^{n+1}$ contains a line, so it is not hyperbolic.
Since $X$ is compact, part 1 asks equivalently that $X$ contains no entire curve, that is, that $X$ is [[Brody hyperbolic|Y7W36GJDJD]].

## Explanations

### L1 human

A complex manifold is hyperbolic when it contains no copy of the complex plane, in a strong sense.
The conjecture predicts that a typical hypersurface of large enough degree in projective space is hyperbolic, and so is the complement of such a hypersurface.
The degree needs to be large because hypersurfaces of small degree contain lines, which carry many copies of the plane.
