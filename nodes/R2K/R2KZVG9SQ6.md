---
tag: R2KZVG9SQ6
kind: definition
name: Volterra equations with completely monotone kernels
msc: [45D05, "45E10", 26A48]
defines: MFJSS5HVA0
uses: [SNFYTC1TTA, ZBS1JA62QP]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein%27s_theorem_on_monotone_functions
---

## Definition

A function $k \colon (0, \infty) \to \R$ is *completely monotone* if it is infinitely differentiable and $(-1)^j k^{(j)}(t) \ge 0$ for all integers $j \ge 0$ and all $t > 0$.
Let $k \colon (0, \infty) \to \R$ and let $f$ be a given function on $[0, \infty)$.
Consider the [[Volterra equation of convolution type|SNFYTC1TTA]]
$$x(t) + \int_0^t k(t - s) \, x(s) \, ds = f(t), \quad t \ge 0,$$
and its first-kind analogue $\int_0^t k(t - s) \, x(s) \, ds = f(t)$.
Each is a *Volterra equation with a completely monotone kernel* if:

1. $k$ is completely monotone on $(0, \infty)$;
2. $k$ is integrable on $(0, 1)$, so that it is locally integrable on $[0, \infty)$.

## Remarks

Example: $k(t) = t^{-1/2}$.
Its derivatives are $k^{(j)}(t) = (-1)^j \frac{1 \cdot 3 \cdots (2j - 1)}{2^j} t^{-1/2 - j}$, so $(-1)^j k^{(j)} \ge 0$, and $\int_0^1 t^{-1/2} \, dt = 2$.
So [[Abel's integral equation|G4GWBYTW7B]] is a first-kind equation with a completely monotone kernel.
Non-example: $k(t) = t$ is positive but increasing, so $(-1)^1 k'(t) = -1 < 0$ and clause 1 fails.
Non-example: $k(t) = 1/t$ is completely monotone but not integrable near $0$, so clause 2 fails.
By [[Bernstein's theorem|ZBS1JA62QP]], clause 1 holds exactly when $k(t) = \int_{[0, \infty)} e^{-st} \, d\mu(s)$ for a positive Borel measure $\mu$ for which the integral converges for $t > 0$.
For $k(t) = t^{-1/2}$ the measure is $d\mu(s) = \pi^{-1/2} s^{-1/2} \, ds$.
