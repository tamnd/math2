---
tag: ZFZR65WYBX
kind: definition
name: Quasi-isometry
msc: [20F65, 51F30, 53C23]
defines: 6FKYSH729T
uses: [0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-isometry
    locator: Definition
---

## Definition

Let $(X, d_X)$ and $(Y, d_Y)$ be [[metric spaces|0VKD1TP7F3]], and let $f \colon X \to Y$ be a map, not necessarily continuous.
The map $f$ is a *quasi-isometric embedding* if there are constants $A \ge 1$ and $B \ge 0$ such that
$$\frac{1}{A} d_X(x, x') - B \le d_Y(f(x), f(x')) \le A \, d_X(x, x') + B \quad \text{for all } x, x' \in X.$$
The map $f$ is a *quasi-isometry* if it is a quasi-isometric embedding and its image is $C$-dense for some $C \ge 0$.
This means that every point of $Y$ lies within distance $C$ of $f(X)$.
The spaces $X$ and $Y$ are *quasi-isometric* if there is a quasi-isometry $X \to Y$.

## Remarks

Example: the inclusion $f \colon \Z \to \R$, with the usual distances.
It satisfies the two inequalities with $A = 1$ and $B = 0$, and each real number lies within $C = 1/2$ of an integer.
So $f$ is a quasi-isometry.

Non-example: the map $f \colon \R \to \R$, $f(x) = x^3$.
It fails the upper inequality: $d(f(n), f(0)) = n^3$ is not bounded by $A n + B$ for large $n$.

A map $f \colon X \to Y$ is a quasi-isometry if and only if it is a quasi-isometric embedding and has a quasi-inverse.
This is a quasi-isometric embedding $g \colon Y \to X$ such that $g \circ f$ and $f \circ g$ are at bounded distance from the identity maps.
Being quasi-isometric is an equivalence relation on metric spaces.
Every bounded metric space is quasi-isometric to a point.
