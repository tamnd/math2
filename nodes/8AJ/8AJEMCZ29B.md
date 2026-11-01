---
tag: 8AJEMCZ29B
kind: definition
name: Holomorphic map between Riemann surfaces
msc: [30F10, 30F99]
defines: T19P7J53A1
uses: [5K0N8QMV6Q, 0P27W9RW0G, 0DG0Z72CQD]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_surface
---

## Definition

Let $X$ and $Y$ be [[Riemann surfaces|5K0N8QMV6Q]].
A map $f \colon X \to Y$ is *holomorphic* if:

1. $f$ is [[continuous|0P27W9RW0G]], and
2. for every chart $\varphi \colon U \to \C$ of $X$ and every chart $\psi \colon V \to \C$ of $Y$, the map
$$\psi \circ f \circ \varphi^{-1} \colon \varphi(U \cap f^{-1}(V)) \to \C$$
is [[holomorphic|0DG0Z72CQD]].

A holomorphic map is a *biholomorphism* if it is bijective; its inverse is then also holomorphic.

## Remarks

Continuity makes $U \cap f^{-1}(V)$ open, so clause 2 makes sense.
It suffices to check clause 2 for charts from one atlas of $X$ and one atlas of $Y$.
When $X$ and $Y$ are open subsets of $\C$ with the identity chart, this is the usual notion of a holomorphic function.

Example: $f \colon \hat\C \to \hat\C$ with $f(z) = z^2$ for $z \in \C$ and $f(\infty) = \infty$.
In the chart $z$ near finite points it is $z \mapsto z^2$.
Near $\infty$, in the chart $w = 1/z$ on both sides, it reads $w \mapsto 1/(1/w)^2 = w^2$, which is holomorphic.

Non-example: complex conjugation $z \mapsto \bar z$ on $\C$ is continuous, but in the identity chart it is [[not holomorphic|0Z8ATBPM5W]], so clause 2 fails.
