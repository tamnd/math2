---
tag: DCMFQ01QGS
kind: concept
name: Newtonian potential
msc: [31B15, 31B10]
specializes: [JHKSF3XFY2]
sources:
  - url: https://en.wikipedia.org/wiki/Newtonian_potential
same_as:
  wikidata: Q4328383
  wikipedia: Newtonian potential
---

## Summary

The Newtonian potential of a mass distribution $\mu$ in $\R^n$, $n \ge 3$, is the function $U^\mu(x) = \int \abs{x - y}^{2-n} \, d\mu(y)$.
It is the [[potential of the measure|JHKSF3XFY2]] $\mu$ with respect to the [[Newtonian kernel|6TJTWQ5HCR]].
In $\R^3$ it is the gravitational potential of Newton's theory, up to the gravitational constant and a sign.
It is harmonic off the support of $\mu$.
In the sense of distributions it solves Poisson's equation $\Delta U^\mu = -(n-2)\sigma_n \mu$, where $\sigma_n$ is the area of the unit sphere.

## Explanations

### L1 human

Newton's law says that a point mass $m$ at $y$ creates the potential $m / \abs{x - y}$ at the point $x$ of space.
A planet, a star or a cloud of dust is a sum of many small masses.
Its Newtonian potential is the sum, or integral, of all these contributions.
For a uniform ball of mass $M$, the potential outside the ball is the same as that of a point mass $M$ at the centre.
