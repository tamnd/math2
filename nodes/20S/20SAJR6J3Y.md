---
tag: 20SAJR6J3Y
kind: statement
role: theorem
name: Shell theorem
msc: [31B15]
uses: [DCMFQ01QGS, T2CYAYF0MT, 0HYPR64JM2]
about: [DCMFQ01QGS]
sources:
  - url: https://en.wikipedia.org/wiki/Shell_theorem
same_as:
  wikidata: Q2222575
  wikipedia: Shell theorem
---

## Statement

Let $R > 0$ and $M > 0$.
Let $\mu$ be the measure on $\R^3$ of total mass $M$ spread uniformly over the sphere $S_R = \set{y : \abs{y} = R}$, that is, $\mu = \frac{M}{4\pi R^2} \, dS$ on $S_R$.
Let $U^\mu(x) = \int \frac{d\mu(y)}{\abs{x - y}}$ be its [[Newtonian potential|DCMFQ01QGS]].
Then
$$U^\mu(x) = \frac{M}{\abs{x}} \quad (\abs{x} \ge R), \qquad U^\mu(x) = \frac{M}{R} \quad (\abs{x} \le R).$$
Consequently the gravitational force of the shell on a point mass is $0$ inside the shell.
Outside the shell it equals the force of a point mass $M$ at the centre.

## Remarks

Proof idea: $U^\mu(x)$ is $M$ times the average of the function $y \mapsto 1/\abs{x - y}$ over the sphere $S_R$.
If $\abs{x} > R$, this function is harmonic on a neighbourhood of the closed ball of radius $R$, and the [[mean value property|0HYPR64JM2]] gives the value $1/\abs{x}$ at the centre.
If $\abs{x} < R$, fix $y_0 \in S_R$.
By rotation symmetry, the average of $1/\abs{x - y}$ over $y \in S_R$ equals the average of $1/\abs{x' - y_0}$ over $x'$ in the sphere of radius $\abs{x}$.
That function of $x'$ is harmonic on the ball of radius $R$, so the average is its value $1/\abs{y_0} = 1/R$ at the centre.
The value $\abs{x} = R$ follows by continuity of both formulas, or by [[Gauss's law|T2CYAYF0MT]] applied to spheres about the origin.
Since a ball with radial density is a union of concentric uniform shells, the potential of such a ball of mass $M$ is $M / \abs{x}$ outside the ball as well.

## Explanations

### L1 human

Newton proved that a hollow planet with a uniform crust pulls on outside objects as if all its mass sat at its centre.
Inside the hollow there is no pull at all: the near part of the crust pulls harder, but the far part is larger, and the two effects cancel exactly.
This is why one may treat the Sun and the planets as point masses.

### L2 human

The theorem is the first example of how potential theory turns symmetry into exact formulas.
It says that the potential of the shell is constant inside, so it is harmonic there, and that outside it is a multiple of the Newtonian kernel.
In $\R^n$ with $n \ge 3$ the same argument gives $M \abs{x}^{2-n}$ outside and $M R^{2-n}$ inside, and in the plane the logarithmic potential of a uniform circle behaves in the same way.
