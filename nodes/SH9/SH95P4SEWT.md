---
tag: SH95P4SEWT
kind: definition
name: Relaxed control
msc: [49J15, 49J45, 93C15]
defines: SFMD8RKRSE
uses: [8M31QKB0GW, 059TJN0NZ1, 0R6EWFKRCF, ZPDTVZQN5K, 6TQSVJQDEH, XEX7QZV1BS]
sources:
  - url: https://en.wikipedia.org/wiki/Optimal_control
---

## Definition

Let $U$ be a nonempty [[compact set|0R6EWFKRCF]] in $\R^m$, and let $\mathcal{P}(U)$ be the set of Borel [[probability measures|059TJN0NZ1]] on $U$.
Let $T > 0$.
A *relaxed control* on $[0, T]$ is a family $(\mu_t)_{t \in [0, T]}$ with $\mu_t \in \mathcal{P}(U)$ for every $t$.
It must be measurable in this sense: for every continuous function $h \colon U \to \R$, the map $t \mapsto \int_U h \, d\mu_t$ is Lebesgue measurable on $[0, T]$.
For a [[control system|ZPDTVZQN5K]] $x' = f(t, x, u)$ with $f$ continuous, the trajectory of the relaxed control $(\mu_t)$ solves the relaxed equation
$$x'(t) = \int_U f(t, x(t), v) \, d\mu_t(v).$$

## Remarks

Every ordinary [[admissible control|8M31QKB0GW]] $u \colon [0, T] \to U$ gives the relaxed control $\mu_t = \delta_{u(t)}$, the Dirac measure at $u(t)$.
Its relaxed equation is $x' = f(t, x, u(t))$, the original one.
Example: $U = \set{-1, 1}$ and $\mu_t = \frac12 \delta_{-1} + \frac12 \delta_1$ for all $t$.
It is a relaxed control, since $\int_U h \, d\mu_t = \frac12 (h(-1) + h(1))$ is constant in $t$.
For $f(t, x, u) = u$ its trajectory has $x' = 0$, a velocity that no ordinary control with values in $\set{-1, 1}$ gives.
Non-example: $\mu_t = \delta_{-1} + \delta_1$ is not a relaxed control, since $\mu_t(U) = 2$, so $\mu_t$ is not a probability measure.
The velocities of relaxed controls fill the convex hull of $f(t, x, U)$, so the convexity hypothesis of [[Filippov's existence theorem|XEX7QZV1BS]] holds for the relaxed problem.
A relaxed control is a [[Young measure|6TQSVJQDEH]] on $[0, T]$ with values in $U$.
