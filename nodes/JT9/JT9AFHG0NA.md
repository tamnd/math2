---
tag: JT9AFHG0NA
kind: concept
name: Riemann–Stieltjes integral
msc: [26A42]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%E2%80%93Stieltjes_integral
same_as:
  wikidata: Q285771
  wikipedia: Riemann–Stieltjes integral
---

## Summary

The Riemann–Stieltjes integral $\int_a^b f \, dg$ integrates a function $f$ against another function $g$, the integrator.
Its sums weight each value of $f$ by the change of $g$ over a subinterval instead of by the length of the subinterval.
With $g(x) = x$ it is the [[Riemann integral|0QM4TXT3DR]].
It handles sums and integrals in one formula.
It is the setting of the Riesz representation of continuous linear functionals on $C[a, b]$, and of expectations written with a [[cumulative distribution function|0MXMS3AE13]].

## Explanations

### L1 human

In an ordinary integral every piece of the $x$-axis counts by its length.
In a Stieltjes integral a piece counts by how much $g$ grows on it, so $g$ decides where the mass sits.
If $g$ jumps by $1$ at the point $c$ and is constant elsewhere, then $\int_a^b f \, dg = f(c)$ for continuous $f$: the integral just reads off a value.
If $g$ is a step function with several jumps, the integral becomes a finite sum.
