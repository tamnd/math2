---
tag: A2W5SNSC05
kind: definition
name: Backward error analysis
msc: [65G50, 65F35]
defines: CMXHRNWY35
uses: [AB3S6MHJ8X, 0V2WP9B1MF]
sources:
  - url: https://en.wikipedia.org/wiki/Error_analysis_(mathematics)
---

## Definition

Let $X$ and $Y$ be normed spaces with [[norms|0V2WP9B1MF]] $\norm{\cdot}$, and let $f \colon X \to Y$ be a problem.
Let $x \in X$ with $x \ne 0$, and let $\hat y \in Y$ be a computed approximation of $y = f(x)$.

1. The *forward error* of $\hat y$ is $\norm{\hat y - y}$, and its relative forward error is $\norm{\hat y - y}/\norm{y}$ when $y \ne 0$.
2. The *relative backward error* of $\hat y$ is
$$\eta(\hat y) = \inf \set{ \frac{\norm{\Delta x}}{\norm{x}} : f(x + \Delta x) = \hat y },$$
with $\eta(\hat y) = \infty$ when no such $\Delta x$ exists.
3. *Backward error analysis* of an algorithm is a bound on $\eta(\hat y)$ for its computed outputs $\hat y$, usually by a modest multiple of the unit roundoff.

## Remarks

Example: in floating-point arithmetic the computed sum is $\hat s = \mathrm{fl}(a + b) = (a + b)(1 + \delta)$ with $\abs{\delta} \le u$.
It equals the exact sum of $a(1 + \delta)$ and $b(1 + \delta)$.
So for the problem $(a, b) \mapsto a + b$ with the max norm, the relative backward error is at most $u$.
Non-example: a bound on $\norm{\hat y - y}$ alone, with no statement about a perturbed input, is a forward error analysis.
If $f$ is differentiable with relative [[condition number|AB3S6MHJ8X]] $\kappa$ at $x$, then to first order the relative forward error is at most $\kappa \, \eta(\hat y)$.
Componentwise backward errors, which bound each $\abs{\Delta x_i}/\abs{x_i}$ separately, are also common.
