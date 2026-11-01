---
tag: QCBYAWBYWM
kind: definition
name: Separably generated extension
msc: [12F20, 12F15]
defines: 1Z2BCP64SZ
uses: [0WQ1A8SHTZ, E45PA267S4, 0N019F6RE9, VWBVKT794W, 966GNVGB8A]
sources:
  - url: https://en.wikipedia.org/wiki/Separable_extension
---

## Definition

Let $L/K$ be a [[field extension|0WQ1A8SHTZ]].
A *separating transcendence basis* of $L/K$ is a [[transcendence basis|E45PA267S4]] $B$ of $L/K$ such that $L$ is a [[separable|0N019F6RE9]] algebraic extension of $K(B)$.
The extension $L/K$ is *separably generated* if it has a separating transcendence basis.

## Remarks

An algebraic extension is separably generated if and only if it is separable, since then $B = \emptyset$.
In characteristic $0$ every extension is separably generated.
Every finitely generated extension of a [[perfect field|VWBVKT794W]] is separably generated.
Example: $K(t)/K$ is separably generated, with separating transcendence basis $\set{t}$.
Non-example: let $K = \F_p(t)$ and $L = K(t^{1/p})$; then $L/K$ is algebraic and [[purely inseparable|966GNVGB8A]] of degree $p$, so its only transcendence basis is $\emptyset$ and $L/K$ is not separable.
Not every transcendence basis of a separably generated extension is separating: $\set{t^p}$ is a transcendence basis of $\F_p(t)/\F_p$, but $\F_p(t)/\F_p(t^p)$ is purely inseparable.
