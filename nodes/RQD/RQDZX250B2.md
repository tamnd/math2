---
tag: RQDZX250B2
kind: definition
name: Strictly convex space
msc: [46B20]
defines: GDTKW9KPH8
uses: [03J5RAKB30]
sources:
  - url: https://en.wikipedia.org/wiki/Strictly_convex_space
---

## Definition

Let $X$ be a [[normed vector space|03J5RAKB30]] over $\R$ or $\C$.
The space $X$ is *strictly convex* if for all $x, y \in X$ with $\norm{x} = \norm{y} = 1$ and $x \ne y$,
$$\left\| \frac{x + y}{2} \right\| < 1.$$

## Remarks

Equivalent forms: the unit sphere contains no nondegenerate line segment; and $\norm{x + y} = \norm{x} + \norm{y}$ with $x, y \ne 0$ implies $y = c x$ for some real $c > 0$.
Example: $\R^2$ with the Euclidean norm.
If $\norm{x} = \norm{y} = 1$ and $x \ne y$, the parallelogram law gives $\norm{(x + y)/2}^2 = 1 - \norm{(x - y)/2}^2 < 1$.
Non-example: $\R^2$ with $\norm{(a, b)}_1 = \abs{a} + \abs{b}$.
For $x = (1, 0)$ and $y = (0, 1)$ the midpoint $(1/2, 1/2)$ has norm $1$.
Every [[uniformly convex space|BEAMC5011M]] is strictly convex, but not conversely.
For instance, $\ell^1$ with the norm $\norm{x}_1 + \norm{x}_2$ is strictly convex.
Indeed, equality in the triangle inequality forces equality for $\norm{\cdot}_2$.
But this space is not reflexive, so it is not uniformly convex by the [[Milman–Pettis theorem|AJ5RG9XQYZ]].
