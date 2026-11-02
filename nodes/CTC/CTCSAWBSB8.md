---
tag: CTCSAWBSB8
kind: definition
name: Topological conjugacy
msc: [37C15, 37B02]
defines: HNXXAPQKG3
uses: [0CQHFPGJ45, 0X3WGX95FE, 0QT00PB5G2, 0THBK9V825]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_conjugacy
    locator: Definition
---

## Definition

Let $X$ and $Y$ be [[topological spaces|0CQHFPGJ45]], and let $f \colon X \to X$ and $g \colon Y \to Y$ be [[continuous maps|0X3WGX95FE]].
A *topological conjugacy* from $f$ to $g$ is a [[homeomorphism|0QT00PB5G2]] $h \colon X \to Y$ such that
$$h \circ f = g \circ h,$$
where $\circ$ is [[composition|0THBK9V825]].
The maps $f$ and $g$ are *topologically conjugate* if such an $h$ exists.

For flows $\varphi$ on $X$ and $\psi$ on $Y$, a topological conjugacy is a homeomorphism $h \colon X \to Y$ with $h \circ \varphi_t = \psi_t \circ h$ for all $t \in \R$.

## Remarks

The relation $h \circ f = g \circ h$ gives $h \circ f^n = g^n \circ h$ for all $n \ge 0$, so $h$ maps orbits of $f$ onto orbits of $g$.
In particular $h$ maps fixed points to fixed points and periodic points of minimal period $p$ to periodic points of minimal period $p$.
Topological conjugacy is an equivalence relation on continuous self-maps.

Example: the tent map $T(x) = 1 - \abs{2x - 1}$ and the logistic map $f(x) = 4x(1 - x)$ on $[0, 1]$ are conjugate through $h(x) = \sin^2(\pi x / 2)$.
The map $h$ is an increasing homeomorphism of $[0, 1]$.
One has $f(h(x)) = 4 \sin^2(\pi x/2) \cos^2(\pi x/2) = \sin^2(\pi x)$.
Also $h(T(x)) = \sin^2(\pi x)$ for $x \le 1/2$, and $h(T(x)) = \sin^2(\pi - \pi x) = \sin^2(\pi x)$ for $x \ge 1/2$.

Non-example: $f(x) = x/2$ and $g(x) = -x/2$ on $\R$ are not conjugate.
A conjugacy $h$ would map the only fixed point $0$ to $0$, so it would map $(0, \infty)$ onto $(0, \infty)$ or onto $(-\infty, 0)$.
Since $f$ maps $(0, \infty)$ into itself while $g$ maps each half-line into the other one, $h \circ f = g \circ h$ fails.

For flows, the weaker notion of topological equivalence only asks that $h$ map orbits onto orbits and preserve their direction, not the time parametrisation.
