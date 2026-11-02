---
tag: CH9B4RZPMW
kind: definition
name: Least fixed point
msc: [06A06, 47H10]
defines: DBD64TH52D
uses: [0QV2JS9RJ3, 0AANKKNHS4]
sources:
  - url: https://en.wikipedia.org/wiki/Least_fixed_point
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]] and let $f \colon P \to P$ be a map.
A *fixed point* of $f$ is an element $x \in P$ with $f(x) = x$.
A *least fixed point* of $f$ is a fixed point $x$ of $f$ such that $x \le y$ for every fixed point $y$ of $f$.
In other words, it is the [[least element|0AANKKNHS4]] of the set $\set{x \in P : f(x) = x}$.

## Remarks

A least fixed point is unique when it exists, by antisymmetry of $\le$.
It is written $\operatorname{lfp}(f)$ or $\mu f$.
The *greatest fixed point* is defined dually and written $\operatorname{gfp}(f)$ or $\nu f$.
Example: for $f \colon \R \to \R$, $f(x) = x^2$, the fixed points are the solutions of $x^2 = x$, namely $0$ and $1$.
Since $0 \le 1$, the least fixed point is $0$.
Non-example: for $g \colon \R \to \R$, $g(x) = x$, every real number is a fixed point, and $\R$ has no least element, so $g$ has no least fixed point.
The map $x \mapsto x + 1$ on $\R$ has no fixed point at all.
