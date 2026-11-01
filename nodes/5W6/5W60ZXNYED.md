---
tag: 5W60ZXNYED
kind: definition
name: Stratonovich integral
msc: [60H05]
defines: EE1QZRCFPJ
uses: [4EJB6E2AZK, JA95NH206E, X4DHMZD5JA, 22735FGJV6]
sources:
  - url: https://en.wikipedia.org/wiki/Stratonovich_integral
---

## Definition

Let $X$ and $Y$ be continuous real [[semimartingales|4EJB6E2AZK]] on a filtered probability space, and let $t \ge 0$.
The *Stratonovich integral* of $Y$ with respect to $X$ is
$$\int_0^t Y_s \circ dX_s = \int_0^t Y_s \, dX_s + \frac12 [Y, X]_t.$$
Here $\int_0^t Y_s \, dX_s$ is the [[Itô integral|JA95NH206E]].
The process $[Y, X]$ is the [[quadratic covariation|X4DHMZD5JA]] of $Y$ and $X$.

## Remarks

Equivalently, it is the limit in probability of the sums $\sum_i \tfrac12 (Y_{t_i} + Y_{t_{i+1}})(X_{t_{i+1}} - X_{t_i})$ over partitions $0 = t_0 < \cdots < t_n = t$ whose mesh tends to $0$.
Example: let $B$ be a [[Brownian motion|22735FGJV6]] with $B_0 = 0$.
Then $\int_0^t B_s \, dB_s = \tfrac12 (B_t^2 - t)$ and $[B, B]_t = t$, so $\int_0^t B_s \circ dB_s = \tfrac12 B_t^2$.
Non-example: the left-point sums $\sum_i B_{t_i} (B_{t_{i+1}} - B_{t_i})$ converge to $\tfrac12 (B_t^2 - t)$, not to the Stratonovich integral, because they omit the covariation term.
For $f$ three times continuously differentiable, the chain rule takes the classical form $f(X_t) = f(X_0) + \int_0^t f'(X_s) \circ dX_s$.
The notation $\circ \, dX$, with a small circle, marks the Stratonovich integral.
