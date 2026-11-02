---
tag: RSAK8YHMXF
kind: definition
name: Integrable function
msc: [28A25, 26A42]
defines: X7GTF3D98F
uses: [P15VQS5DJ9, YYNCJSR0PJ, DG76G5Z6XW]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_integral
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]].
Let $f \colon X \to \R$ or $f \colon X \to \C$ be a [[measurable function|YYNCJSR0PJ]].
The function $f$ is *integrable*, or *Lebesgue integrable*, if
$$\int_X \abs{f} \, d\mu < \infty,$$
where the left side is the [[integral of the non-negative function|DG76G5Z6XW]] $\abs{f}$.

## Remarks

Example: on $\R$ with Lebesgue measure, $f(x) = e^{-\abs{x}}$ is measurable since it is continuous.
Its integral is $\int_\R e^{-\abs{x}} \, dx = 2 < \infty$, so $f$ is integrable.

Non-example: $g(x) = \sin(x) / x$ on $[1, \infty)$ with Lebesgue measure is measurable but not integrable.
On each interval $[k\pi, (k+1)\pi]$ the integral of $\abs{g}$ is at least $2 / ((k+1)\pi)$, and these bounds have an infinite sum.
Its improper Riemann integral still converges, so improper integrals and Lebesgue integrals differ here.

A real function $f$ is integrable if and only if both $f^+ = \max(f, 0)$ and $f^- = \max(-f, 0)$ have finite integral.
A function with values in $[-\infty, \infty]$ is called integrable under the same condition, and it is then finite almost everywhere.
The integrable functions form a vector space, often written $\mathcal{L}^1(\mu)$.
