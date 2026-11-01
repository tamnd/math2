---
tag: M9Z8VM4K1Z
kind: concept
name: Grünwald–Letnikov derivative
msc: [26A33]
sources:
  - url: https://en.wikipedia.org/wiki/Gr%C3%BCnwald%E2%80%93Letnikov_derivative
same_as:
  wikidata: Q4162531
  wikipedia: Grünwald–Letnikov derivative
---

## Summary

The Grünwald–Letnikov derivative of real order $\alpha$ is a limit of weighted sums of values of the function.
It extends the [[difference quotient|AZBDB5F4M4]] that defines ordinary derivatives.
The weights are generalised [[binomial coefficients|0GBZM0MT0F]] $\binom{\alpha}{k}$ with alternating signs.
For whole orders it gives the usual derivatives, and for smooth enough functions it agrees with the Riemann–Liouville derivative of [[fractional calculus|T73XK15SA2]].
Its discrete form is the basis of many numerical methods for fractional differential equations.

## Explanations

### L1 human

The first derivative is the limit of $(f(x) - f(x - h))/h$, and the second derivative is the limit of $(f(x) - 2f(x - h) + f(x - 2h))/h^2$.
The coefficients $1, -1$ and $1, -2, 1$ are binomial coefficients with alternating signs.
Binomial coefficients $\binom{\alpha}{k}$ make sense for any real $\alpha$, so the same recipe defines a derivative of order $\alpha$.
For non-integer $\alpha$ the sum does not stop, so the derivative at $x$ depends on all earlier values of $f$ back to a starting point.
