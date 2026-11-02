---
tag: PXF8731MBK
kind: definition
name: Uniformly convex space
msc: [46B20]
defines: BEAMC5011M
uses: [03J5RAKB30]
sources:
  - url: https://en.wikipedia.org/wiki/Uniformly_convex_space
---

## Definition

Let $X$ be a [[normed vector space|03J5RAKB30]] over $\R$ or $\C$.
The space $X$ is *uniformly convex* if the following holds.
For every $\varepsilon$ with $0 < \varepsilon \le 2$ there is $\delta > 0$ such that for all $x, y \in X$ with $\norm{x} \le 1$, $\norm{y} \le 1$ and $\norm{x - y} \ge \varepsilon$,
$$\left\| \frac{x + y}{2} \right\| \le 1 - \delta.$$

## Remarks

Example: an inner product space is uniformly convex.
By the parallelogram law, for $\norm{x}, \norm{y} \le 1$ and $\norm{x - y} \ge \varepsilon$,
$$\left\| \frac{x + y}{2} \right\|^2 = \frac{\norm{x}^2 + \norm{y}^2}{2} - \left\| \frac{x - y}{2} \right\|^2 \le 1 - \frac{\varepsilon^2}{4},$$
so $\delta = 1 - \sqrt{1 - \varepsilon^2/4}$ works.
Non-example: $\R^2$ with the norm $\norm{(a, b)}_\infty = \max(\abs{a}, \abs{b})$.
For $x = (1, 1)$ and $y = (1, -1)$ one has $\norm{x - y}_\infty = 2$ but $\norm{(x + y)/2}_\infty = \norm{(1, 0)}_\infty = 1$, so no $\delta > 0$ works for $\varepsilon = 2$.
The spaces $\ell^p$ and $L^p$ for $1 < p < \infty$ are uniformly convex by [[Clarkson's inequalities|1V11QM5C07]]; $\ell^1$ and $\ell^\infty$ are not.
Uniform convexity depends on the norm, not only on the topology: $\R^2$ is uniformly convex with the Euclidean norm and not with the norm $\norm{\cdot}_\infty$.
