---
tag: XVBF9EJY10
kind: concept
name: Linear-fractional programming
msc: [90C32, 90C05]
specializes: [NQ52QHDMMV]
sources:
  - url: https://en.wikipedia.org/wiki/Linear-fractional_programming
same_as:
  wikidata: Q4168281
  wikipedia: Linear-fractional programming
---

## Summary

Linear-fractional programming is the optimization of a ratio of two affine functions over a polyhedron.
It is the simplest case of [[fractional programming|NQ52QHDMMV]] and generalizes [[linear programming|VNMXB0J2KA]], which is the case of a constant denominator.
When the denominator is positive on a bounded feasible region, the Charnes–Cooper transformation turns the problem into an equivalent linear program.
Such ratios appear as efficiency measures, such as return per unit cost, and in [[data envelopment analysis|Z7SSS8G8G9]].

## Explanations

### L1 human

Often one wants to make a ratio as large as possible, such as profit per hour or output per unit of input.
If both the top and the bottom of the ratio are linear and the allowed plans are given by linear inequalities, the problem is linear-fractional.
A ratio is not linear, but a change of variables that divides by the denominator makes the problem linear.
For instance, the largest value of $(x + 1)/(y + 1)$ with $0 \le x, y \le 1$ is $2$, at $x = 1$, $y = 0$.
