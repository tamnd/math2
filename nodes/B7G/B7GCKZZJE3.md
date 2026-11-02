---
tag: B7GCKZZJE3
kind: definition
name: Proper cone
msc: [52A20, 90C25]
defines: Z5T0SEF3XA
uses: [0XPR1E85W0, 6VE4KA12VD, J9HA54ACME, 0ZCK8DQYN1, 0RZH6W98HK]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_cone
---

## Definition

Let $n \ge 1$.
A *proper cone* in $\R^n$ is a [[convex cone|6VE4KA12VD]] $K \subseteq \R^n$ such that:

1. $K$ is nonempty and [[closed|0ZCK8DQYN1]];
2. $K$ has nonempty [[interior|0RZH6W98HK]];
3. $K$ is salient: $K \cap (-K) = \set{0}$, so $K$ contains no line through the origin.

## Remarks

A nonempty closed convex cone contains $0 = \lim_{t \to 0^+} t x$, so a proper cone is a [[pointed cone|J9HA54ACME]].

Example: the nonnegative orthant $\R^n_{\ge 0}$.
It is a closed convex cone, its interior is the set of vectors with all coordinates positive, and if $x$ and $-x$ both have nonnegative coordinates then $x = 0$.

Non-example: the closed half-plane $\set{(x, y) \in \R^2 : y \ge 0}$ satisfies clauses 1 and 2, but it contains $(1, 0)$ and $(-1, 0)$, so clause 3 fails.

A proper cone $K$ gives a partial order on $\R^n$ by $x \preceq_K y$ if $y - x \in K$.
Conventions vary: some sources, Mathlib among them, call any closed pointed cone proper and drop clauses 2 and 3.
