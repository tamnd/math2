---
tag: 48BP5HZAAC
kind: definition
name: q-convex manifold
msc: [32F10]
defines: VBHR4R5W7F
uses: [JSGWAN2RJV, 80MTNXWW80, 0R6EWFKRCF, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Andreotti%E2%80%93Grauert_theorem
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]] of complex dimension $n$, and let $q$ be an integer with $1 \le q \le n$.
Let $\varphi \colon X \to \R$ be a [[smooth|0V33BNKZ9S]] function.
It is *strongly $q$-convex* at a point $x$ if its [[Levi form|80MTNXWW80]] at $x$, in local holomorphic coordinates, has at least $n - q + 1$ positive eigenvalues.
The manifold $X$ is *$q$-convex* if there are a smooth function $\varphi \colon X \to \R$ and a [[compact set|0R6EWFKRCF]] $K \subseteq X$ such that:

1. $\varphi$ is an exhaustion: the set $\set{x \in X : \varphi(x) < c}$ is relatively compact in $X$ for every $c \in \R$.
2. $\varphi$ is strongly $q$-convex at every point of $X \setminus K$.

The manifold $X$ is *$q$-complete* if this holds with $K = \emptyset$.

## Remarks

This is the convention of Andreotti and Grauert; some authors shift the index by one.
The number of positive eigenvalues of the Levi form does not depend on the choice of local coordinates.
Example: $\C^n$ is $1$-complete with $\varphi(z) = \abs{z}^2$, whose Levi form $\abs{w}^2$ has $n$ positive eigenvalues.
Non-example: a compact complex manifold of positive dimension is $q$-convex with $K = X$, but it is not $1$-complete.
Indeed a strongly $1$-convex function is strictly plurisubharmonic, so it has no maximum, while every continuous function on a compact manifold has one.
The $1$-complete manifolds are exactly the Stein manifolds, and the $1$-convex manifolds are also called strongly pseudoconvex manifolds.
