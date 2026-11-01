---
tag: QEY26RT19R
kind: statement
role: theorem
name: Rademacher's theorem
msc: [26B05, 28A15]
uses: [0QNVQ4VD9T, 08EVNYZF42]
about: [0QNVQ4VD9T, 08EVNYZF42]
sources:
  - url: https://en.wikipedia.org/wiki/Rademacher%27s_theorem
same_as:
  wikidata: Q132427
  wikipedia: Rademacher's theorem
---

## Statement

Let $n, m \ge 1$, let $U \subseteq \R^n$ be an open set, and let $f \colon U \to \R^m$ be [[Lipschitz continuous|0QNVQ4VD9T]].
Then $f$ is [[Fréchet differentiable|08EVNYZF42]] at almost every point of $U$ with respect to Lebesgue measure on $\R^n$.

## Remarks

For $n = 1$ the theorem follows from Lebesgue's theorem: a Lipschitz function of one variable is [[absolutely continuous|ZT6F4C2YHK]], hence of bounded variation, hence differentiable almost everywhere.
In general one works with each coordinate of $f$, so one may take $m = 1$.
Applying the case $n = 1$ on lines and Fubini's theorem, the directional derivative of $f$ in each fixed direction exists almost everywhere.
One then shows that almost everywhere it depends linearly on the direction, first for a countable dense set of directions, and the Lipschitz bound turns this into full differentiability.
For example, $f(x) = \norm{x}$ is Lipschitz on $\R^n$ and differentiable everywhere except at $0$.
Continuity alone is not enough: the Weierstrass function is continuous on $\R$ and differentiable nowhere.

## Explanations

### L1 human

A Lipschitz function is one whose graph is never steeper than some fixed slope.
Such a function may have corners, but the theorem says the corners are rare: at almost every point the function has a tangent plane.

### L2 human

The theorem is the starting point of analysis on rough sets and maps.
It lets one use the derivative of a Lipschitz map in integrals, for example in the area and coarea formulas of geometric measure theory.
It also shows that Lipschitz functions belong to the Sobolev space $W^{1,\infty}$ locally, with weak gradient equal to the almost everywhere gradient.
The one-dimensional case is closely tied to [[absolute continuity|ZT6F4C2YHK]] and to [[Lebesgue's theorem on monotone functions|1Y4N1DDQNR]].
