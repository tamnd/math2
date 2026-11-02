---
tag: 39MVMBCXG3
kind: concept
name: Strong maximal function
msc: [42B25]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_maximal_function
---

## Summary

The strong maximal function of a function $f$ on $\R^n$ is a supremum of averages of $\abs{f}$.
At a point $x$, it is taken over all rectangles that contain $x$ and have sides parallel to the axes.
Unlike the [[Hardy–Littlewood maximal function|VX1A56P5KQ]], it allows rectangles of any shape, long and thin in some directions.
It is bounded on $L^p(\R^n)$ for $1 < p \le \infty$ but is not of [[weak type|9534R6VMY0]] $(1, 1)$ when $n \ge 2$.
It controls multiparameter averages and is the basic maximal operator of product, or multiparameter, harmonic analysis.

## Explanations

### L1 human

The usual maximal function looks at balls around a point, which have the same size in every direction.
The strong maximal function also looks at boxes that can be very long in one direction and very short in another.
Because there are many more boxes than balls, it can be much larger than the usual maximal function.
Still, it is bounded on $L^p$ for $p > 1$, because in each coordinate direction it is no worse than a one-dimensional maximal function.
For example, take the indicator of the unit square in the plane and the point $(a, 1/2)$ with $a > 1$.
The rectangle $[0, a] \times [0, 1]$ gives the average $1/a$.
For large $a$, balls centred at the point only give averages of order $1/a^2$.
