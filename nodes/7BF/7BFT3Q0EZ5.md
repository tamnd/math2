---
tag: 7BFT3Q0EZ5
kind: definition
name: Lorentz factor
msc: [83A05]
defines: 2E9AJVZS6E
uses: []
sources:
  - url: https://en.wikipedia.org/wiki/Lorentz_factor
---

## Definition

Let $c > 0$ be the speed of light.
Let $v$ be a real number with $\abs{v} < c$, the speed of a body relative to an inertial frame.
The *Lorentz factor* of $v$ is
$$\gamma(v) = \frac{1}{\sqrt{1 - v^2 / c^2}}.$$
With $\beta = v / c$ it reads $\gamma = 1 / \sqrt{1 - \beta^2}$.

## Remarks

Example: for $v = 0.6 c$, one has $\beta^2 = 0.36$, $\sqrt{1 - 0.36} = 0.8$ and $\gamma = 1.25$.
Non-example: for $v = c$ the denominator is $0$, so the Lorentz factor is not defined; it tends to $+\infty$ as $\abs{v} \to c$.
Always $\gamma \ge 1$, with equality only at $v = 0$, and $\gamma = 1 + \tfrac{1}{2} \beta^2 + O(\beta^4)$ for small $\beta$.
The useful identity $\gamma^2 (1 - \beta^2) = 1$ is equivalent to $\gamma^2 - (\gamma \beta)^2 = 1$.
