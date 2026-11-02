---
tag: 1BKVNEHX96
kind: definition
name: Differential inclusion
msc: [34A60, 49J21]
defines: 9ZSMF6NYKM
uses: [03CPD1HGF3, ZT6F4C2YHK, 0NT64JV96A, XNMKX7H4FD]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_inclusion
---

## Definition

Let $I \subseteq \R$ be an interval and let $\Omega \subseteq \R^n$ be an open set.
Let $F$ be a [[multivalued function|03CPD1HGF3]] that assigns to each $(t, x) \in I \times \Omega$ a nonempty subset $F(t, x)$ of $\R^n$.
The *differential inclusion* given by $F$ is the relation
$$x'(t) \in F(t, x(t)).$$
A *solution* on a subinterval $J \subseteq I$ is an [[absolutely continuous|ZT6F4C2YHK]] function $x \colon J \to \Omega$ such that $x'(t) \in F(t, x(t))$ for almost every $t \in J$.

## Remarks

If $F(t, x) = \set{f(t, x)}$ for a function $f$, the solutions are the solutions of the [[ordinary differential equation|0NT64JV96A]] $x' = f(t, x)$ in the sense of Carathéodory.
Example: for $F(t, x) = [-1, 1]$ on $\R \times \R$, the function $x(t) = \abs{t}$ is a solution, since it is absolutely continuous and $x'(t) = \pm 1$ for every $t \ne 0$.
Non-example: $x(t) = 2t$ is not a solution of the same inclusion, because $x'(t) = 2 \notin [-1, 1]$ at every $t$.
An equation with a discontinuous right side, such as $x' = -\sgn x$, is often replaced by the inclusion $x' \in -\operatorname{Sgn}(x)$, where $\operatorname{Sgn}(0) = [-1, 1]$; then $x \equiv 0$ is a solution.
Local existence of solutions holds when the values $F(t, x)$ are nonempty, compact and convex and $F$ satisfies suitable [[upper hemicontinuity|XNMKX7H4FD]] and measurability conditions.
