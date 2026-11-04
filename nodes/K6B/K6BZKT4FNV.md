---
tag: K6BZKT4FNV
kind: proof
name: Proof that a tangent is perpendicular to the radius
msc: [51M04]
proves: 031JV5S54D
uses: [0T7DX8NY1X, 060W5CBZP6, 0MP9BCF6DP, 0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Power_of_a_point
    locator: "Secants theorem, chords theorem: common proof"
---

## Proof

We intersect the line with the circle and solve for the parameter.

1. Let $v$ be a direction vector of the [[line|0MP9BCF6DP]] $\ell$. Since $T \in \ell$, we have $\ell = \set{T + tv : t \in \mathbb{R}}$, and distinct values of $t$ give distinct points because $v \neq 0$.
2. The point $X = T + tv$ lies on the [[circle|060W5CBZP6]] $C$ if and only if $\norm{T - O + tv}^2 = r^2$.
3. Expanding with the [[dot product|0S52TNNTH9]] and using $\norm{T - O} = r$, this is $r^2 + 2t\, v \cdot (T - O) + t^2\norm{v}^2 = r^2$.
4. So $X \in C$ if and only if $t\,(2\, v \cdot (T - O) + t\norm{v}^2) = 0$, that is, $t = 0$ or $t = t_1$ with $t_1 = -\frac{2\, v \cdot (T - O)}{\norm{v}^2}$.
5. By definition, $\ell$ is [[tangent|0T7DX8NY1X]] to $C$ at $T$ if and only if $\ell \cap C = \set{T}$. By steps 1 and 4, this holds if and only if $t_1 = 0$, that is, $v \cdot (T - O) = 0$.
6. Each point of $\ell$ is $X = T + tv$, so $(X - T) \cdot (T - O) = t\, v \cdot (T - O)$. This is zero for all $X \in \ell$ if and only if $v \cdot (T - O) = 0$, taking $t = 1$ for one direction.
7. By steps 5 and 6, $\ell$ is tangent to $C$ at $T$ if and only if $(X - T) \cdot (T - O) = 0$ for each point $X$ of $\ell$.

## Idea

A line through a point of the circle meets the circle again at one more parameter value. That second value is zero exactly when the direction of the line is perpendicular to the radius. So the line touches the circle only at $T$ in exactly this case.
