---
tag: 1Z2BCP64SZ
kind: concept
name: Separably generated extension
msc: [12F20, 12F15]
sources:
  - url: https://en.wikipedia.org/wiki/Separable_extension
---

## Summary

A separably generated extension is a field extension with a [[transcendence basis|E45PA267S4]] over which the whole extension is [[separable|0WCX7NB4N7]] algebraic.
Such a basis is a separating transcendence basis.
It extends the notion of a separable algebraic extension to transcendental extensions.
Every extension in characteristic $0$, and every finitely generated extension of a [[perfect field|VWBVKT794W]], is separably generated.

## Explanations

### L1 human

In characteristic $p$, adding a $p$-th root can give an inseparable extension, where an irreducible polynomial has a repeated root.
For example, over $\F_p(t)$ the polynomial $x^p - t$ is irreducible, but it equals $(x - t^{1/p})^p$ once $t^{1/p}$ is added.
A separably generated extension is one where one can choose free variables so that the rest is reached by separable steps only.
The function field $\F_p(x, y)$ with $y^2 = x^3 + 1$ and $p$ odd is separably generated over $\F_p$, with separating basis $\set{x}$.
