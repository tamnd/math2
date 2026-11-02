---
tag: VGZRSDNEBK
kind: definition
name: Measure with density
msc: [28A25, 28A10]
defines: Y98C5T956Q
uses: [P15VQS5DJ9, YYNCJSR0PJ, DG76G5Z6XW, PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Radon–Nikodym_theorem
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]] and let $f \colon X \to [0, \infty]$ be a [[measurable function|YYNCJSR0PJ]].
The *measure with density* $f$ is the map $f\mu \colon \Sigma \to [0, \infty]$ given by
$$(f\mu)(A) = \int_A f \, d\mu = \int_X f \, \mathbf{1}_A \, d\mu,$$
where the integral is the [[integral of a non-negative function|DG76G5Z6XW]].

## Remarks

The map $f\mu$ is a [[measure|PR11BZQQPG]]: $(f\mu)(\emptyset) = 0$, and countable additivity follows from the monotone convergence theorem applied to $f \mathbf{1}_{A_1 \cup \dots \cup A_n}$.
It is absolutely continuous with respect to $\mu$, since $\mu(A) = 0$ implies $\int_A f \, d\mu = 0$.

Example: on $\R$ with Lebesgue measure and $f = \mathbf{1}_{[0,1]}$, the measure $f\mu$ is Lebesgue measure restricted to $[0, 1]$.
Check: $(f\mu)(A) = \int \mathbf{1}_{A \cap [0,1]} \, dx$, the length of $A \cap [0, 1]$.

Non-example: $f(x) = x$ on $\R$ takes negative values, so it is not an admissible density.
The formula $A \mapsto \int_A x \, dx$ is not even defined for $A = \R$.

For measurable $g \ge 0$, $\int g \, d(f\mu) = \int g f \, d\mu$.
Notation: $f\mu$, $f \cdot \mu$, or $d\nu = f \, d\mu$.
