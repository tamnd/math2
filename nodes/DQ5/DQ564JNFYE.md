---
tag: DQ564JNFYE
kind: definition
name: Function field
msc: [12F20, 14H05]
defines: XKEXQDRTGH
uses: [0QA8CHH8MG, 0WQ1A8SHTZ, D7TR0YWR9H, 4V81611P9N, E45PA267S4]
sources:
  - url: https://en.wikipedia.org/wiki/Function_field_of_an_algebraic_variety
---

## Definition

Let $k$ be a [[field|0QA8CHH8MG]] and let $n \ge 0$ be an integer.
A *function field in $n$ variables over $k$* is a [[field extension|0WQ1A8SHTZ]] $K/k$ with two properties.
First, $K = k(a_1, \dots, a_m)$ for finitely many $a_1, \dots, a_m \in K$.
Second, the [[transcendence degree|D7TR0YWR9H]] of $K/k$ is $n$.

## Remarks

Many authors also ask that $k$ be algebraically closed in $K$, and some ask $n \ge 1$.
Example: the [[field of rational functions|4V81611P9N]] $k(x_1, \dots, x_n)$ is a function field in $n$ variables.
Example: if $k$ has characteristic not $2$, the field $k(x)[y]/(y^2 - x^3 - 1)$ is a function field in one variable, with [[transcendence basis|E45PA267S4]] $\set{x}$; it is the function field of the curve $y^2 = x^3 + 1$.
Non-example: the field $k(x_1, x_2, x_3, \dots)$ in infinitely many variables is not finitely generated over $k$.
For an irreducible variety $V$ over $k$, the field $k(V)$ of rational functions on $V$ is a function field in $\dim V$ variables over $k$.
