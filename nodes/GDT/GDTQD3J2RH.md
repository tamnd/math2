---
tag: GDTQD3J2RH
kind: definition
name: Universal cover
msc: [57M10, 55R05]
defines: Y1YPE6PM52
uses: [3XZRRE165N, S1XK3HXHFX, 0WB6DH499T]
sources:
  - url: https://en.wikipedia.org/wiki/Covering_space
---

## Definition

Let $X$ be a [[path-connected|0WB6DH499T]] topological space.
A *universal cover* of $X$ is a [[covering map|3XZRRE165N]] $p \colon \tilde X \to X$ such that $\tilde X$ is simply connected.
Here $\tilde X$ is simply connected if it is path-connected and its [[fundamental group|S1XK3HXHFX]] $\pi_1(\tilde X, \tilde x)$ is trivial for one, hence every, point $\tilde x \in \tilde X$.

## Remarks

Example: $p \colon \R \to S^1$, $p(t) = (\cos 2\pi t, \sin 2\pi t)$, is a covering map.
Its total space $\R$ is path-connected and contractible, so $\pi_1(\R) = 1$, and $p$ is a universal cover of the circle.
For $n \ge 2$, the quotient map $S^n \to \R P^n$ is a universal cover, because $S^n$ is simply connected.

Non-example: the map $S^1 \to S^1$, $z \mapsto z^2$, on the unit circle in $\C$ is a covering map.
Its total space $S^1$ has fundamental group $\Z$, so it is not a universal cover.

If $X$ is connected, locally path-connected and [[semilocally simply connected|R3SHZX0NZR]], then a universal cover exists.
If $X$ is locally path-connected, two universal covers of $X$ are isomorphic over $X$.
A universal cover is often written $\tilde X \to X$.
