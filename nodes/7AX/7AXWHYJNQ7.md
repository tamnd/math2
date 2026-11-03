---
tag: 7AXWHYJNQ7
kind: definition
name: Symmetric cone
msc: [17C36, 52A20, 32M15]
defines: NZMXY4WTZX
uses: [0QVNCJXRY3, 6VE4KA12VD, 1ZDAGGGRP4, 0K1SCPBNKJ, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_cone
---

## Definition

Let $V$ be a finite-dimensional real [[inner product space|0QVNCJXRY3]] with inner product $\ip{\cdot}{\cdot}$.
Let $\Omega \subseteq V$ be a nonempty [[open|02BH3MCBQB]] [[convex cone|6VE4KA12VD]], and let $\bar{\Omega}$ be its closure.
The *open dual cone* of $\Omega$ is
$$\Omega^* = \set{y \in V : \ip{x}{y} > 0 \text{ for all } x \in \bar{\Omega} \setminus \set{0}}.$$
Let $G(\Omega) = \set{g \in GL(V) : g(\Omega) = \Omega}$ be the [[automorphism group|0K1SCPBNKJ]] of $\Omega$.
The cone $\Omega$ is *symmetric* if:

1. $\Omega$ is self-dual: $\Omega^* = \Omega$, a condition built on the [[dual cone|1ZDAGGGRP4]].
2. $\Omega$ is homogeneous: for all $x, y \in \Omega$ there is $g \in G(\Omega)$ with $g(x) = y$.

## Remarks

Example: the positive orthant $\Omega = (0, \infty)^n$ in $\R^n$ with the dot product.
A vector $y$ satisfies $\ip{x}{y} > 0$ for every nonzero $x$ with nonnegative entries exactly when every entry of $y$ is positive, so $\Omega^* = \Omega$.
The diagonal matrix with entries $y_i / x_i > 0$ maps $x \in \Omega$ to $y \in \Omega$ and preserves $\Omega$, so $\Omega$ is homogeneous.

Non-example: the sector $\Omega = \set{(s, t) \in \R^2 : \abs{t} < 2s}$ with the dot product.
It is homogeneous, since a linear map that scales its two boundary rays by independent positive factors preserves it and moves any interior point to any other.
It is not self-dual: its opening angle is $2 \arctan 2 > \pi/2$, while its dual cone has the opening angle $\pi - 2\arctan 2 < \pi/2$.

Other standard examples are the Lorentz cone $\set{(t, x) \in \R \times \R^{n} : t > \norm{x}}$ and the cone of positive definite real symmetric $n \times n$ matrices with the inner product $\ip{A}{B} = \tr(AB)$.
