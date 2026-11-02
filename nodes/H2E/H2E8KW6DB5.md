---
tag: H2E8KW6DB5
kind: definition
name: Painlevé property
msc: [34M55, 34M04]
defines: 8EV1G2Y6CC
uses: [0NT64JV96A, 066E7PJCYE, 0ZZ7ZYDR8W, 0M3YQJ81NB]
sources:
  - url: https://en.wikipedia.org/wiki/Painlev%C3%A9_transcendents
---

## Definition

Let $U \subseteq \C$ be a domain, and consider an [[ordinary differential equation|0NT64JV96A]]
$$y^{(n)} = F\left( z, y, y', \ldots, y^{(n-1)} \right),$$
where $F$ is rational in $y, y', \ldots, y^{(n-1)}$ with coefficients holomorphic in $z \in U$.
Consider the singularities of solutions, reached by [[analytic continuation|0M3YQJ81NB]].
A singularity is *fixed* if its position is determined by the equation alone, such as a singular point of the coefficients.
Otherwise it is *movable*: its position depends on the initial conditions.
The equation has the *Painlevé property* if every movable singularity of every solution is a [[pole|066E7PJCYE]].

## Remarks

For the first, second and fourth Painlevé equations, the only fixed singular point is $\infty$, and every solution is a [[meromorphic|0ZZ7ZYDR8W]] function on all of $\C$.
For the other three, solutions can still branch at the fixed singular points, such as $0$, $1$ and $\infty$ for the sixth equation.
Some authors only require that no movable singularity is a branch point.

Example: the Riccati equation $y' = y^2$ has the solutions $y = 0$ and $y = \frac{1}{c - z}$, $c \in \C$.
The only singularity is the simple pole at $z = c$, which moves with $c$, so this movable singularity is a pole.
More generally, every Riccati equation $y' = a(z) + b(z) y + c(z) y^2$ has the Painlevé property.

Non-example: $y' = y^3$ has the solutions $y^2 = \frac{1}{2 (c - z)}$, so $y = \pm \left( 2 (c - z) \right)^{-1/2}$.
The point $z = c$ is a movable branch point and not a pole, so the property fails.

The first Painlevé equation $y'' = 6 y^2 + z$ has the Painlevé property, and its solutions are not expressible by classical functions in general.
