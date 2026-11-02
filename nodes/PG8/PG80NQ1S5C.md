---
tag: PG80NQ1S5C
kind: definition
name: Homotopy group
msc: [55Q05]
defines: P976WYEFMB
uses: [T9DG8DDE75, 9YA6S6HD9V, S1XK3HXHFX]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_group
---

## Definition

Let $(X, x_0)$ be a [[pointed space|T9DG8DDE75]], and let $n \ge 1$ be an integer.
Let $I^n = [0, 1]^n$ be the $n$-cube, with boundary $\partial I^n$.
The *$n$-th homotopy group* $\pi_n(X, x_0)$ is the set of [[homotopy|9YA6S6HD9V]] classes of continuous maps $f \colon I^n \to X$ with $f(\partial I^n) = \set{x_0}$.
Here the homotopies $F \colon I^n \times [0, 1] \to X$ must satisfy $F(s, t) = x_0$ for all $s \in \partial I^n$ and all $t$.
The group operation is $[f] + [g] = [f + g]$, where
$$(f + g)(s_1, s_2, \ldots, s_n) = \begin{cases} f(2 s_1, s_2, \ldots, s_n) & \text{if } s_1 \le \tfrac12, \\ g(2 s_1 - 1, s_2, \ldots, s_n) & \text{if } s_1 \ge \tfrac12. \end{cases}$$

## Remarks

Since $I^n / \partial I^n$ is homeomorphic to $S^n$, the elements of $\pi_n(X, x_0)$ are also the pointed homotopy classes of pointed maps $(S^n, s_0) \to (X, x_0)$.
For $n = 1$ the definition gives the [[fundamental group|S1XK3HXHFX]].
The set $\pi_0(X, x_0)$ is defined as the set of path components of $X$, with the component of $x_0$ as base point; it is not a group in general.

Example: $\pi_n(\R^m, 0)$ is trivial for all $n \ge 1$.
For $f$ as above, $F(s, t) = (1 - t) f(s)$ is a homotopy that keeps $\partial I^n$ at $0$ and ends at the constant map.

Non-example: a map $f \colon I^n \to X$ that does not send all of $\partial I^n$ to $x_0$ does not define an element of $\pi_n(X, x_0)$.
Likewise, free homotopy classes of maps $S^1 \to X$ form in general a different set: they correspond to conjugacy classes of $\pi_1(X, x_0)$ when $X$ is path-connected.
