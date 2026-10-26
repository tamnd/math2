---
tag: 0EPW94MJ1P
kind: concept
name: Constrained optimisation
aliases: [constrained-optimization]
msc: [90C30]
uses: [0JPCHTXWG0, 0WFBH1Q3WC]
sources:
  - url: https://en.wikipedia.org/wiki/Constrained_optimization
    locator: General form
  - url: https://en.wikipedia.org/wiki/Constrained_optimization
    locator: Equality constraints
same_as:
  wikidata: Q4477763
  wikipedia: Constrained optimization
---

## Summary

Constrained optimisation looks for the maximum or minimum of an objective function $f$ of several variables over the set of points that satisfy given constraints.
Typical constraints are equations $g_i(x) = c_i$ and inequalities $h_j(x) \ge d_j$.

## Remarks

An example is to maximise $f(x, y) = x y$ on the circle $x^2 + y^2 = 2$. The maximum value is $1$, at $(1, 1)$ and $(-1, -1)$.
For equality constraints, one method solves the constraints for some variables and substitutes them into $f$. Another method uses [[Lagrange multipliers|0VKKP8X6Q6]].
A constrained extremum need not be a critical point of $f$. In the example above, $\nabla f(1, 1) = (1, 1) \ne 0$.

## Explanations

### L1 human

In many problems you cannot choose the variables freely.
For example, you want the largest area for a fixed length of fence.
Constrained optimisation finds the best value only among the choices that obey the rules.
