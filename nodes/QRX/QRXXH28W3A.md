---
tag: QRXXH28W3A
kind: concept
name: Lagrangian duality
msc: [90C46, 49N15]
sources:
  - url: https://en.wikipedia.org/wiki/Duality_(optimization)
same_as:
  wikidata: Q2275559
  wikipedia: Duality (optimization)
---

## Summary

Lagrangian duality attaches to a constrained minimization problem a second problem, the dual, built from its Lagrangian.
The dual maximizes a concave function of the multipliers, and its optimal value is a lower bound for the optimal value of the original problem.
The two values are equal for many convex problems, for example under [[Slater's condition|BSRSKXPJPQ]].
Duality gives certificates of optimality, sensitivity information and algorithms such as [[Lagrangian relaxation|P9HK0R14WX]].

## Explanations

### L1 human

Instead of forbidding a constraint violation, one can charge a price for it.
For each choice of prices one solves an easier problem without constraints, and its value is never above the true optimum.
The dual problem looks for the prices that give the best such bound.
For example, to minimize $x^2$ with $x \ge 1$, charge the price $\lambda$ for $1 - x$.
This gives the bound $\lambda - \lambda^2/4$, which is largest at $\lambda = 2$, where it equals the true minimum $1$.
