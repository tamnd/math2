---
tag: VCBWR1WSK0
kind: definition
name: Banach–Mazur distance
msc: [46B20, 52A21, 46B07]
defines: ZJKSYYASPT
uses: [03J5RAKB30, 0B8T10CE7N, 06EKW1AKXF]
sources:
  - url: https://en.wikipedia.org/wiki/Banach%E2%80%93Mazur_compactum
---

## Definition

Let $n \ge 1$, and let $X$ and $Y$ be real [[normed vector spaces|03J5RAKB30]] of the same dimension $n$.
The *Banach–Mazur distance* between $X$ and $Y$ is
$$d(X, Y) = \inf_T \norm{T} \, \norm{T^{-1}}.$$
Here $T$ runs over the [[linear isomorphisms|0B8T10CE7N]] from $X$ to $Y$, and $\norm{\cdot}$ is the [[operator norm|06EKW1AKXF]].

## Remarks

Always $d(X, Y) \ge 1$, $d(X, Y) = d(Y, X)$ and $d(X, Z) \le d(X, Y) \, d(Y, Z)$; so $\log d$ is a pseudometric.
The infimum is attained by compactness, and $d(X, Y) = 1$ if and only if $X$ and $Y$ are isometric.
In terms of the unit balls $B_X$ and $B_Y$, $d(X, Y)$ is the least $\lambda \ge 1$ with $B_X \subseteq T B_Y \subseteq \lambda B_X$ for some linear isomorphism $T \colon \R^n \to \R^n$, after identifying both spaces with $\R^n$.
Example: let $X = \ell_1^2$ and $Y = \ell_\infty^2$, that is, $\R^2$ with the norms $\abs{x_1} + \abs{x_2}$ and $\max(\abs{x_1}, \abs{x_2})$.
The map $T(x_1, x_2) = (x_1 + x_2, x_1 - x_2)$ satisfies $\max(\abs{x_1 + x_2}, \abs{x_1 - x_2}) = \abs{x_1} + \abs{x_2}$, so it is an isometry and $d(X, Y) = 1$.
Non-example: if $\dim X \ne \dim Y$, there is no linear isomorphism, and the distance is not defined.
John's theorem gives $d(X, \ell_2^n) \le \sqrt{n}$ for every $n$-dimensional normed space $X$.
