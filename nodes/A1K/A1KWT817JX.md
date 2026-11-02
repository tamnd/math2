---
tag: A1KWT817JX
kind: concept
name: Variational capacity
msc: [31C45, 31B15, "46E35"]
sources:
  - url: https://en.wikipedia.org/wiki/Capacity_of_a_set
---

## Summary

Let $K$ be a compact set inside an open set $\Omega \subseteq \R^n$, and let $1 < p < \infty$.
The variational capacity, or $p$-capacity, of $K$ is the least $p$-Dirichlet energy $\int_\Omega \abs{\nabla u}^p \, dx$ of a suitable function $u$.
Here $u$ is smooth, at least $1$ on $K$, and zero near the boundary of $\Omega$.
For $p = 2$ it is the classical [[condenser capacity|NTEFMRR3HR]].
It is the natural measure of size in nonlinear potential theory and for the $p$-Laplace equation.
Sets of $p$-capacity zero are the sets that [[Sobolev functions|M4CEZ5K9HP]] with $p$-integrable gradient cannot see.

## Explanations

### L1 human

Think of $\Omega$ as a large room and $K$ as an object inside it.
A test function must climb from $0$ near the walls to at least $1$ on $K$, and the capacity is the cheapest cost of this climb, measured by $\int \abs{\nabla u}^p$.
A large object close to the walls forces steep slopes and has a large capacity.
A single point in $\R^n$ has $p$-capacity zero when $p \le n$: the climb can be made very cheap by spreading it over many scales.
For $p > n$ even a point has positive $p$-capacity, which matches the fact that such Sobolev functions are continuous.
