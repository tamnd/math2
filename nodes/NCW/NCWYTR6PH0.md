---
tag: NCWYTR6PH0
kind: definition
name: Clarke generalized gradient
msc: [49J52, 26B25]
defines: 20967BXZKA
uses: [06GZ956657, 4A82S5FVRT, 0AW1E6YTJY, 0T3RZQXDYD]
sources:
  - url: https://en.wikipedia.org/wiki/Clarke_generalized_derivative
    locator: Definitions
---

## Definition

Let $X$ be a real [[Banach space|06GZ956657]] with [[continuous dual space|4A82S5FVRT]] $X^*$, and write $\ip{\zeta}{v} = \zeta(v)$.
Let $f \colon X \to \R$ be [[Lipschitz|0AW1E6YTJY]] on a neighbourhood of a point $x \in X$.
The *Clarke generalized directional derivative* of $f$ at $x$ in the direction $v \in X$ is
$$f^\circ(x; v) = \limsup_{y \to x, \ t \downarrow 0} \frac{f(y + t v) - f(y)}{t},$$
a [[limit superior|0T3RZQXDYD]] over $y \in X$ and $t > 0$.
The *Clarke generalized gradient* of $f$ at $x$ is the set
$$\partial_C f(x) = \set{\zeta \in X^* : \ip{\zeta}{v} \le f^\circ(x; v) \text{ for all } v \in X}.$$

## Remarks

If $K$ is a Lipschitz constant of $f$ near $x$, then $\abs{f^\circ(x; v)} \le K \norm{v}$, and $v \mapsto f^\circ(x; v)$ is sublinear.
So $\partial_C f(x)$ is convex, nonempty by the Hahn–Banach theorem, and weak-* compact by the Banach–Alaoglu theorem, since it is weak-* closed and bounded by $K$.
If $f$ is continuously differentiable near $x$, then $\partial_C f(x) = \set{f'(x)}$.
If $f$ is convex, then $\partial_C f(x)$ is the subdifferential of convex analysis.
For $X = \R^n$, Clarke's formula describes it through gradients, which exist almost everywhere by Rademacher's theorem.
It is the convex hull of the limits $\lim_k \nabla f(x_k)$ over sequences $x_k \to x$ at which $f$ is differentiable.
This formula still holds when the $x_k$ must avoid a given set of measure zero.

Example: $f(x) = -\abs{x}$ on $\R$ at $x = 0$.
For $y > 0$ small the difference quotient in direction $v$ is $-v$, and for $y < 0$ small it is $v$, so $f^\circ(0; v) = \abs{v}$.
Hence $\partial_C f(0) = \set{\zeta : \zeta v \le \abs{v} \text{ for all } v} = [-1, 1]$.

Non-example: $f(x) = \sqrt{\abs{x}}$ on $\R$ is not Lipschitz near $0$.
The quotient $(f(t) - f(0))/t = t^{-1/2}$ is unbounded as $t \downarrow 0$, so $f^\circ(0; 1) = +\infty$, and the construction gives no useful information.
