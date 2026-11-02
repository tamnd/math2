---
tag: 6EWEE3F9R8
kind: definition
name: Algebraic torus
msc: [20G15, 14L10]
defines: 66FQFAJNS4
uses: [GA81VVQHEP, GH81SYAPPN]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_torus
---

## Definition

Let $k$ be a field with algebraic closure $\bar{k}$.
Let $\mathbb{G}_m = \operatorname{Spec} k[t, t^{-1}]$ be the multiplicative group.
An *algebraic torus* over $k$ is an [[algebraic group|GH81SYAPPN]] $T$ over $k$ such that $T \times_k \bar{k} \cong \mathbb{G}_{m, \bar{k}}^n$ as algebraic groups for some $n \ge 0$.
The torus is *split* if $T \cong \mathbb{G}_m^n$ already over $k$.

## Remarks

An algebraic torus is a [[linear algebraic group|GA81VVQHEP]], and $n$ is its dimension.
One can replace $\bar{k}$ by a separable closure of $k$ in the definition.

Example: over $k = \R$, let $T$ be the circle $x^2 + y^2 = 1$ with $(x, y)(x', y') = (x x' - y y', x y' + x' y)$.
Over $\C$, the map $(x, y) \mapsto x + iy$ is an isomorphism $T_{\C} \cong \mathbb{G}_{m, \C}$, so $T$ is a torus of dimension $1$.
It is not split, because $T(\R)$ is compact while $\mathbb{G}_m(\R) = \R^{*}$ is not.

Non-example: the additive group $\mathbb{G}_a = \operatorname{Spec} k[x]$ is not a torus.
The ring $\bar{k}[x]$ has only constant units, while $\bar{k}[t, t^{-1}]$ has the unit $t$, so $\mathbb{G}_{a, \bar{k}} \not\cong \mathbb{G}_{m, \bar{k}}$.
