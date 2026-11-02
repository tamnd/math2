---
tag: YRTFS7NHM8
kind: definition
name: Convex body
msc: [52A20]
defines: 437FSG3419
uses: [0XPR1E85W0, 02AS45T3H9, 0R6EWFKRCF, 0RZH6W98HK]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_body
---

## Definition

Let $n \ge 1$ and consider [[Euclidean space|0XPR1E85W0]] $\R^n$.
A *convex body* in $\R^n$ is a subset $K \subseteq \R^n$ such that:

1. $K$ is [[convex|02AS45T3H9]];
2. $K$ is [[compact|0R6EWFKRCF]];
3. $K$ has nonempty [[interior|0RZH6W98HK]].

## Remarks

Example: the closed unit ball $B = \set{x \in \R^n : \abs{x} \le 1}$.
It is convex by the triangle inequality, compact because it is closed and bounded, and its interior contains the open unit ball, so it is not empty.

Non-example: the closed segment $[0, 1] \times \set{0}$ in $\R^2$ is convex and compact, but its interior in $\R^2$ is empty, so clause 3 fails.

Some authors, for example in the theory of mixed volumes, call every nonempty compact convex set a convex body and drop clause 3.
With that convention, the bodies with nonempty interior are called full-dimensional.
