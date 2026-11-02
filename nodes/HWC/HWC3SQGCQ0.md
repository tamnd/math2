---
tag: HWC3SQGCQ0
kind: definition
name: Kissing number
msc: [52C17, 05B40, 11H31]
defines: B408FZYXF9
uses: [0XPR1E85W0, 0Q0H13G8ZB, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Kissing_number
---

## Definition

Let $n \ge 1$.
A *kissing configuration* in the [[Euclidean space|0XPR1E85W0]] $\R^n$ is a finite set $X \subset \R^n$ such that:

1. $\abs{x} = 2$ for every $x \in X$;
2. $\abs{x - y} \ge 2$ for all distinct $x, y \in X$, where $\abs{\cdot}$ is the [[Euclidean distance|0NPPGHQNXQ]].

The *kissing number* $\tau(n)$ is the largest size of a kissing configuration in $\R^n$.

## Remarks

The conditions say that the [[closed balls|0Q0H13G8ZB]] of radius $1$ centred at the points of $X$ touch the unit ball at $0$ and have pairwise disjoint interiors.
Example: in $\R^2$, the six points $2(\cos(k\pi/3), \sin(k\pi/3))$ for $k = 0, \dots, 5$ have norm $2$, and neighbours are at distance exactly $2$, so they form a kissing configuration; hence $\tau(2) \ge 6$.
Non-example: seven points of norm $2$ in $\R^2$ cannot form one.
Two of them make an angle less than $60^\circ$ at $0$, and are then at distance less than $2$.
Equivalently, $\tau(n)$ is the largest number of points on the unit sphere $S^{n-1}$ with pairwise angles at least $60^\circ$.
The *lattice kissing number* is the largest size of such a configuration when $X$ is the set of shortest nonzero vectors of a lattice, scaled to length $2$.
